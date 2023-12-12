import streamlit as st

def main():
    st.title("Streamlit with Right Sidebar")

    st.markdown(
        """
        <div style="display: flex;">
            <div style="flex: 1;">
                <h2>Sidebar</h2>
                <p style="overflow-wrap: break-word;">This is the sidebar content area.</p>
            </div>
            <div style="flex: 0.5; background-color: orange; padding: 5px;">
                <h2>Main Content</h2>
                <p style="overflow-wrap: break-word;">This is the main content area.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
