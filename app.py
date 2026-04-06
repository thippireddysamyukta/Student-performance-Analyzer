import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🎓 Student Performance Analyzer")
st.header("📌 Student Details")

student_id = st.text_input("Student ID")
name = st.text_input("Student Name")
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
age = st.number_input("Age", 5, 25)
grade = st.selectbox("Class", ["8", "9", "10", "11", "12"])
section = st.text_input("Section")

st.header("📊 Academic Scores")

math = st.number_input("Math Marks", 0, 100)
science = st.number_input("Science Marks", 0, 100)
english = st.number_input("English Marks", 0, 100)
social = st.number_input("Social Studies Marks", 0, 100)
computer = st.number_input("Computer Marks", 0, 100)
st.header("📅 Attendance")

total_days = st.number_input("Total Working Days", 1, 300)
present_days = st.number_input("Days Present", 0, 300)

attendance = (present_days / total_days) * 100 if total_days > 0 else 0
st.header("📝 Assessments")

assignment = st.number_input("Assignment Score", 0, 100)
quiz = st.number_input("Quiz Score", 0, 100)
mid_exam = st.number_input("Mid Exam Marks", 0, 100)
final_exam = st.number_input("Final Exam Marks", 0, 100)
st.header("🧠 Behavior & Study")

study_hours = st.slider("Study Hours per Day", 0, 10)
participation = st.selectbox("Participation Level", ["Low", "Medium", "High"])
discipline = st.slider("Discipline Rating", 1, 10)
extra_activity = st.selectbox("Extra-Curricular Activity", ["Yes", "No"])
st.header("🏠 Background")

parent_education = st.selectbox("Parent Education", ["School", "Graduate", "Postgraduate"])
internet = st.selectbox("Internet Access", ["Yes", "No"])
income = st.selectbox("Family Income", ["Low", "Medium", "High"])

if st.button("Analyze Performance"):

    avg_marks = (math + science + english + social + computer) / 5
    assessment_avg = (assignment + quiz + mid_exam + final_exam) / 4

    overall_score = (avg_marks * 0.6) + (assessment_avg * 0.3) + (attendance * 0.1)

    # Grade Calculation
    if overall_score >= 90:
        grade = "A+"
    elif overall_score >= 75:
        grade = "A"
    elif overall_score >= 60:
        grade = "B"
    elif overall_score >= 50:
        grade = "C"
    else:
        grade = "Fail"

    suggestions = []

    if study_hours < 2:
        suggestions.append("Increase study hours 📚")
    if attendance < 75:
        suggestions.append("Improve attendance 📅")
    if participation == "Low":
        suggestions.append("Participate more in class 🙋‍♂️")
    if discipline < 5:
        suggestions.append("Maintain better discipline ⚠️")

    st.header("📈 Results")

    st.write(f"👤 Name: {name}")
    st.write(f"📊 Average Marks: {avg_marks:.2f}")
    st.write(f"📅 Attendance: {attendance:.2f}%")
    st.write(f"🏆 Overall Score: {overall_score:.2f}")
    st.write(f"🎯 Grade: {grade}")

    st.subheader("💡 Suggestions")
    if suggestions:
        for s in suggestions:
            st.write("- ", s)
    else:
        st.success("Excellent performance! 🎉")

    subjects = ['Math', 'Science', 'English', 'Social', 'Computer']
    marks = [math, science, english, social, computer]

    fig, ax = plt.subplots()
    ax.bar(subjects, marks)
    ax.set_title("Subject-wise Marks")
    ax.set_ylabel("Marks")

    st.pyplot(fig)