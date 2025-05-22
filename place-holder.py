import streamlit as st

st.markdown(
    """
    <style>
    .centered-placeholder {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 24px;
        color: gray;
        user-select: none;
    }
    </style>
    <div class="centered-placeholder">Placeholder</div>
    """,
    unsafe_allow_html=True,
)
