# Claude Code Project

A modern full-stack web application built with SvelteKit 5 and FastAPI, combining the best of reactive frontend development with a high-performance Python backend.

## 🚀 Features

- **Frontend**: SvelteKit 5 with TypeScript
- **Backend**: FastAPI with Python
- **Styling**: Tailwind CSS
- **Type Safety**: TypeScript throughout
- **Hot Reload**: Development server with instant updates
- **API Documentation**: Auto-generated OpenAPI/Swagger docs

## 📋 Prerequisites

- Node.js 18+ and npm
- Python 3.8+
- Git

## 🛠️ Installation

### Clone the repository
```bash
git clone https://github.com/KlausWeigele/claude-code-project.git
cd claude-code-project
```

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Frontend Setup
```bash
cd frontend
npm install
```

## 🏃‍♂️ Running the Application

### Start the Backend
```bash
cd backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
uvicorn main:app --reload
```
The API will be available at `http://localhost:8000`
API documentation at `http://localhost:8000/docs`

### Start the Frontend
```bash
cd frontend
npm run dev
```
The frontend will be available at `http://localhost:5173`

## 🏗️ Project Structure

```
claude-code-project/
├── backend/
│   ├── main.py          # FastAPI application
│   ├── requirements.txt  # Python dependencies
│   └── venv/            # Python virtual environment
├── frontend/
│   ├── src/
│   │   ├── routes/      # SvelteKit pages
│   │   ├── lib/         # Shared components and utilities
│   │   └── app.css      # Global styles
│   ├── static/          # Static assets
│   └── package.json     # Node dependencies
└── README.md
```

## 🧪 Development

### Frontend Development
- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run check` - Type checking
- `npm run lint` - Lint code

### Backend Development
- `uvicorn main:app --reload` - Start with auto-reload
- FastAPI automatic API documentation
- Type hints for better code quality

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with [SvelteKit](https://kit.svelte.dev/)
- Powered by [FastAPI](https://fastapi.tiangolo.com/)
- Styled with [Tailwind CSS](https://tailwindcss.com/)
- Developed with [Claude Code](https://claude.ai/code)