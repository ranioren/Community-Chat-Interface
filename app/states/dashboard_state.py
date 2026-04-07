import reflex as rx
from typing import TypedDict, Literal
from faker import Faker

fake = Faker()


class StatCard(TypedDict):
    title: str
    value: str
    icon: str
    change: str
    is_up: bool


class Activity(TypedDict):
    description: str
    time: str


class Course(TypedDict):
    id: str
    title: str
    description: str
    status: Literal["Active", "Draft", "Archived"]
    students: int
    progress: int
    last_updated: str


class DashboardState(rx.State):
    active_section: str = "Dashboard"
    user_name: str = "Alex Johnson"
    user_email: str = "alex.j@learningcommunity.edu"
    user_bio: str = (
        "Passionate educator focusing on computer science and data literacy."
    )
    stats: list[StatCard] = [
        {
            "title": "Total Students",
            "value": "1,247",
            "icon": "users",
            "change": "+12%",
            "is_up": True,
        },
        {
            "title": "Active Courses",
            "value": "8",
            "icon": "book-open",
            "change": "+2",
            "is_up": True,
        },
        {
            "title": "Completion Rate",
            "value": "87%",
            "icon": "check-circle",
            "change": "-3%",
            "is_up": False,
        },
        {
            "title": "Revenue",
            "value": "$12,450",
            "icon": "dollar-sign",
            "change": "+18%",
            "is_up": True,
        },
    ]
    activities: list[Activity] = [
        {"description": "New enrollment in Python Basics", "time": "2 mins ago"},
        {"description": "Assignment submitted by Sarah M.", "time": "15 mins ago"},
        {"description": "Course 'Web Dev 101' updated", "time": "1 hour ago"},
        {"description": "New review: 5 stars on Data Science", "time": "3 hours ago"},
        {"description": "System backup completed", "time": "5 hours ago"},
    ]
    courses: list[Course] = [
        {
            "id": "1",
            "title": "Python Basics",
            "description": "Master the fundamentals of Python programming from scratch.",
            "status": "Active",
            "students": 450,
            "progress": 85,
            "last_updated": "2023-11-20",
        },
        {
            "id": "2",
            "title": "Web Development 101",
            "description": "HTML, CSS, and basic JS for modern web applications.",
            "status": "Active",
            "students": 320,
            "progress": 70,
            "last_updated": "2023-11-18",
        },
        {
            "id": "3",
            "title": "Data Science Fundamentals",
            "description": "Learn data analysis with Pandas and visualization.",
            "status": "Active",
            "students": 210,
            "progress": 45,
            "last_updated": "2023-11-15",
        },
        {
            "id": "4",
            "title": "JavaScript Mastery",
            "description": "Deep dive into ES6+, async, and closures.",
            "status": "Draft",
            "students": 0,
            "progress": 0,
            "last_updated": "2023-11-10",
        },
        {
            "id": "5",
            "title": "Machine Learning Intro",
            "description": "Linear regression, classification, and neural nets.",
            "status": "Archived",
            "students": 67,
            "progress": 100,
            "last_updated": "2023-10-05",
        },
        {
            "id": "6",
            "title": "UI/UX Design",
            "description": "User-centric design principles and Figma workflows.",
            "status": "Active",
            "students": 154,
            "progress": 30,
            "last_updated": "2023-11-22",
        },
    ]
    email_notifications: bool = True
    push_notifications: bool = False
    course_updates: bool = True
    student_messages: bool = True

    @rx.event
    def navigate_to(self, section: str):
        self.active_section = section
        if section == "Dashboard":
            return rx.redirect("/dashboard")
        elif section == "Your Courses":
            return rx.redirect("/courses")
        elif section == "Settings":
            return rx.redirect("/settings")
        elif section == "Logout":
            self.active_section = "Dashboard"
            return rx.redirect("/")