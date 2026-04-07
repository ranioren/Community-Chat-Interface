import reflex as rx
from app.components.feature_cards import feature_grid
from app.components.chat_interface import chat_interface


def index() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            rx.el.header(
                rx.el.h1(
                    "#LearningCommunity",
                    class_name="text-4xl md:text-5xl font-black text-gray-900 tracking-tight mb-2",
                ),
                rx.el.h2(
                    "#CommunityLearning",
                    class_name="text-xl md:text-2xl font-bold text-blue-600/80 mb-12",
                ),
                class_name="text-center w-full pt-12",
            ),
            rx.el.section(feature_grid(), class_name="w-full mb-8"),
            rx.el.section(chat_interface(), class_name="w-full"),
            class_name="max-w-[700px] mx-auto w-full px-6 py-8 bg-white border border-gray-100 shadow-2xl rounded-[2.5rem] my-12",
        ),
        class_name="min-h-screen bg-gray-50/50 font-['Inter'] selection:bg-blue-100",
    )


app = rx.App(
    theme=rx.theme(appearance="light", accent_color="blue"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap",
            rel="stylesheet",
        ),
        rx.el.style("""
            .custom-scrollbar::-webkit-scrollbar {
                width: 6px;
            }
            .custom-scrollbar::-webkit-scrollbar-track {
                background: transparent;
            }
            .custom-scrollbar::-webkit-scrollbar-thumb {
                background: #e5e7eb;
                border-radius: 10px;
            }
            .custom-scrollbar::-webkit-scrollbar-thumb:hover {
                background: #d1d5db;
            }
        """),
    ],
)
app.add_page(index, route="/")