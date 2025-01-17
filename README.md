# Video Hosting Server

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Tux.svg/1280px-Tux.svg.png" alt="Linux Logo" width="100" height="150"/><img src="https://upload.wikimedia.org/wikipedia/commons/8/83/The_GNU_logo.png" alt="GNU Logo" width="100" height="150"/>
<img src="https://static.fsf.org/common/img/logo-new.png" alt="Free Software Logo" width="200" height="60"/><img src="https://www.openmaint.org/images/opensource-logo.png/@@images/image.png" alt="openSOURCE" width="200"/><img src="https://sfconservancy.org/static/img/conservancy-header.8c88caa4010b.svg" alt="Software Freedom Conservancy" width="200" height="100"/><img src="https://upload.wikimedia.org/wikipedia/commons/f/fc/Free_Software_Foundation_Europe%2C_logo.svg" alt="Software Freedom Conservancy" width="200" height="100"/>
V

## Overview
This project is part of an initiative to **prevent electronic waste** by repurposing old servers and computers. By converting your old devices into functional video hosting servers, you can contribute to sustainability while creating a useful tool for your personal or organizational video storage needs.

The application serves as a simple **video hosting server**, where users can store and stream videos from old hardware. The server is built using **Flask** (a lightweight Python web framework), and it hosts videos stored in a specific directory on your Linux machine.

## Features
- Serve videos from any folder on your Linux machine.
- Web interface to list videos and stream them in a browser.
- Responsive design using **Bootstrap 5**.
- Modal video player for smooth viewing experience.
- Open source and free to use.

## Technology Stack
- **Backend**: Python with **Flask**
- **Frontend**: HTML, CSS, JavaScript with **Bootstrap 5**
- **Operating System**: **Linux** (e.g., Ubuntu)
- **Video Hosting**: Serve videos from your own file system

## Project Structure
```
/project-folder
    /templates
        index.html
    /app.py
```

## Installation

### 1. Clone the Repository

First, clone the repository to your local machine:
```bash
git clone https://github.com/your-username/video-hosting-server.git
cd video-hosting-server
```

### 2. Install Dependencies

Make sure you have **Python 3** and **pip** installed on your system. Install the required Python packages:

```bash
pip install flask
```

### 3. Run the Flask App

Once the dependencies are installed, you can run the Flask app:

```bash
python app.py
```

The server will start at `http://127.0.0.1:5000`. You can now access your video hosting server through your browser.

### 4. Customize Video Directory

Modify the `VIDEO_FOLDER` variable in `app.py` to point to your desired directory where the videos are stored. For example:
```python
VIDEO_FOLDER = "/home/{username}/Videos/Hosting"
```

Replace `{username}` with your actual Linux username.

## Contributing

We welcome contributions to improve the project. If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request!

### How to Contribute:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Create a new Pull Request

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [Flask](https://flask.palletsprojects.com/) - The web framework used to build this project.
- [Bootstrap](https://getbootstrap.com/) - For the responsive and modern UI design.
- [FFmpeg](https://ffmpeg.org/) - For video processing (optional for thumbnail generation).
- **FSFE (Free Software Foundation Europe)**: Supporting **Free Software** and open-source projects.



## Support

If you need help with this project or have any questions, feel free to open an issue in the repository or contact the project maintainer.

---

Thank you for contributing to a more sustainable future by reducing electronic waste! 🌍♻️



