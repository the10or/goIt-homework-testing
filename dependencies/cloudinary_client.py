import cloudinary
import cloudinary.uploader

cloudinary.config(
    cloud_name="doyms7hkc",
    api_key="587271116633288",
    api_secret="VnlCzIudEklXEjB0WEiXiqZWg8s"
)


def upload():
    return cloudinary.uploader
