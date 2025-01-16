import streamlit as st
import pandas as pd
import random
import io

def display_Test_Date_2_panel():
    #header image
    st.image("https://i.imgur.com/L5T4Y9R.jpeg", use_container_width=True)
    st.markdown("---")

    st.title("Test Date 2 Page")

    def process_data(df, date_column, date_input):
        try:
            df[date_column] = pd.to_datetime(df[date_column])
            filtered_df = df[df[date_column].dt.date == date_input]
            
            # Only keep First Name, Last Name, and Date selected for testing
            filtered_df = filtered_df[['First Name', 'Last Name', 'Application Number', date_column]]
            
            return filtered_df
        except Exception as e:
            st.error(f"Error processing data: {e}")
            return None

    def assign_groups(df, num_groups):
        try:
            df = df.sample(frac=1, random_state=42).reset_index(drop=True)  # Shuffle data
            group_labels = [f"Group {i+1}" for i in range(num_groups)]
            df['Group'] = [group_labels[i % num_groups] for i in range(len(df))]
            return df
        except Exception as e:
            st.error(f"Error assigning groups: {e}")
            return None

    def assign_teachers(df, teachers_rooms):
        try:
            groups = df['Group'].unique()
            assignments = {group: None for group in groups}
            teacher_room_pairs = [tr.split(" - ") for tr in teachers_rooms.split("\n") if " - " in tr]

            for group, (teacher, room) in zip(groups, teacher_room_pairs):
                assignments[group] = {'Teacher': teacher, 'Room': room}

            # Assign remainders to "King"
            for group in groups[len(teacher_room_pairs):]:
                assignments[group] = {'Teacher': 'King', 'Room': 'N/A'}

            df['Teacher'] = df['Group'].map(lambda g: assignments[g]['Teacher'])
            df['Room'] = df['Group'].map(lambda g: assignments[g]['Room'])
            return df
        except Exception as e:
            st.error(f"Error assigning teachers and rooms: {e}")
            return None

    def create_csv(df):
        # Convert the dataframe to CSV format
        csv = df.to_csv(index=False)
        return csv

    # Check if the master data exists in session_state
    if "raw_file" in st.session_state and st.session_state["raw_file"] is not None:
        try:
            master_df = pd.read_csv(io.BytesIO(st.session_state["raw_file"]))
            
            date_column = None
            if "Date selected for testing" in master_df.columns:
                date_column = "Date selected for testing"
            else:
                st.write("no date column found")

            date_input = st.date_input("Select Date to Filter:")

            if date_column and date_input:
                filtered_df = process_data(master_df.copy(), date_column, date_input)

                if filtered_df is not None:
                    st.write(f"Filtered Data for {date_input}:")
                    st.dataframe(filtered_df)

                    if not filtered_df.empty:
                        # Group assignment
                        num_groups = st.number_input("Enter number of groups:", min_value=1, max_value=500, value=5)
                        grouped_df = assign_groups(filtered_df.copy(), num_groups)

                        if grouped_df is not None:
                            st.write("Grouped Data:")
                            st.dataframe(grouped_df)

                            # Teacher and room assignment
                            teachers_rooms = st.text_area(
                                "Enter teachers and rooms (format: Teacher Name - Room Number, one per line):"
                            )

                            if teachers_rooms:
                                assigned_df = assign_teachers(grouped_df.copy(), teachers_rooms)

                                if assigned_df is not None:
                                    st.write("Final Group Assignments:")
                                    st.dataframe(assigned_df)

                                    # Download Final Group Assignments as CSV
                                    csv_all = create_csv(assigned_df)
                                    st.download_button(
                                        label="Download Final Group Assignments as CSV",
                                        data=csv_all,
                                        file_name="final_group_assignments.csv",
                                        mime="text/csv"
                                    )

                                    # Filter by Teacher
                                    teacher_filter = st.text_input("Filter by Teacher Name:")
                                    if teacher_filter:
                                        filtered_by_teacher = assigned_df[assigned_df['Teacher'].str.contains(teacher_filter, case=False, na=False)]
                                        st.write(f"Filtered Data for Teacher: {teacher_filter}")
                                        st.dataframe(filtered_by_teacher)

                                        # Download Filtered Data by Teacher as CSV
                                        csv_filtered = create_csv(filtered_by_teacher)
                                        st.download_button(
                                            label=f"Download Filtered Data for Teacher ({teacher_filter}) as CSV",
                                            data=csv_filtered,
                                            file_name=f"filtered_by_teacher_{teacher_filter}.csv",
                                            mime="text/csv"
                                        )


        except Exception as e:
            st.error(f"Error processing the data: {e}")
    else:
        st.warning("No master data found. Please upload data on the Master Data Upload page.")