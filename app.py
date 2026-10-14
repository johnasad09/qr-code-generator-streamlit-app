import io
import qrcode
import streamlit as st

# App Title and Description
st.title("🔗 Simple QR Code Generator")
st.write(
    "Welcome! Type any website link (URL) below to create your very own QR code."
)

# Memory for the app: keeps the QR code on screen after other clicks
if "qr_bytes" not in st.session_state:
    st.session_state.qr_bytes = None

# A form groups the text box and button together.
# Pressing Enter OR clicking the button submits the form.
with st.form("qr_form"):
    url_input = st.text_input("Enter your URL here:")
    submitted = st.form_submit_button("Generate QR Code")

# This runs only when Enter is pressed or the button is clicked
if submitted:
    url = url_input.strip()  # remove extra spaces

    if url:
        # Generate the QR code
        qr_image = qrcode.make(url)

        # Convert it to PNG bytes
        buffer = io.BytesIO()
        qr_image.save(buffer, format="PNG")
        st.session_state.qr_bytes = buffer.getvalue()
    else:
        st.session_state.qr_bytes = None
        st.warning("Please enter a URL above to generate your QR code.")

# Show the QR code and download button if we have one
if st.session_state.qr_bytes:
    st.image(
        st.session_state.qr_bytes,
        caption="Your Generated QR Code",
        width=300,
    )

    st.download_button(
        label="📥 Download QR Code",
        data=st.session_state.qr_bytes,
        file_name="my_qrcode.png",
        mime="image/png",
    )
