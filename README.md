# Claude Code Project

A modern full-stack web application built with SvelteKit 5 and FastAPI, featuring AI-powered capabilities through OpenAI integration. This project demonstrates best practices in reactive frontend development with a high-performance Python backend.

## 🌟 Key Features

- **AI-Powered Features**: Text analysis and code generation using OpenAI API
- **Modern Frontend**: SvelteKit 5 with TypeScript and Svelte runes
- **Fast Backend**: FastAPI with async Python and automatic API documentation
- **Beautiful UI**: Tailwind CSS with responsive design
- **Type Safety**: Full TypeScript support with strict typing
- **Developer Experience**: Hot reload, linting, and pre-commit hooks
- **Production Ready**: CI/CD pipelines, testing setup, and deployment configs

## 🎯 Live Demo Features

- **Text Analyzer**: AI-powered sentiment analysis, summarization, and keyword extraction
- **Code Generator**: Generate code snippets in multiple languages with explanations
- **RESTful API**: Full CRUD operations with validation
- **Real-time Status**: Live AI service availability monitoring

## 📋 Prerequisites

- Node.js 18+ and npm
- Python 3.8+
- Git
- OpenAI API key (for AI features)

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/KlausWeigele/claude-code-project.git
cd claude-code-project
```

### 2. Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

### 3. Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env.local
```

### 4. Start Development Servers

**Backend** (in one terminal):
```bash
cd backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
uvicorn main:app --reload
```
- API: `http://localhost:8000`
- Docs: `http://localhost:8000/docs`

**Frontend** (in another terminal):
```bash
cd frontend
npm run dev
```
- App: `http://localhost:5173`

## 🏗️ Project Structure

```
claude-code-project/
├── frontend/               # SvelteKit application
│   ├── src/
│   │   ├── routes/        # Page components and routing
│   │   ├── lib/           # Shared components and utilities
│   │   │   ├── api.ts     # API client
│   │   │   └── components/ # Reusable components
│   │   └── app.css        # Global styles with Tailwind
│   ├── static/            # Static assets
│   └── package.json       # Node dependencies
├── backend/               # FastAPI application
│   ├── main.py           # API routes and business logic
│   ├── requirements.txt   # Python dependencies
│   └── .env.example      # Environment variables template
├── .github/              # GitHub Actions workflows
│   ├── workflows/
│   │   ├── ci.yml        # Continuous Integration
│   │   └── deploy.yml    # Deployment pipeline
│   └── dependabot.yml    # Dependency updates
├── PROJECT_IDEAS.md      # Comprehensive development roadmap
├── CLAUDE.md            # AI assistant guidelines
├── LICENSE              # MIT License
└── README.md           # This file
```

## 🛠️ Development

### Frontend Commands
```bash
npm run dev        # Start dev server with hot reload
npm run build      # Build for production
npm run preview    # Preview production build
npm run check      # TypeScript type checking
npm run lint       # Lint code with ESLint
npm run format     # Format code with Prettier
```

### Backend Commands
```bash
uvicorn main:app --reload  # Start with auto-reload
python -m pytest           # Run tests (when implemented)
ruff check .              # Lint Python code
black .                   # Format Python code
```

### Code Quality
- **Pre-commit hooks**: Automatically format and lint code
- **TypeScript**: Strict mode enabled for type safety
- **Python**: Type hints and comprehensive docstrings
- **Testing**: Jest/Vitest for frontend, pytest for backend

## 🔧 Environment Variables

### Backend (.env)
```env
# Required
OPENAI_API_KEY=your-openai-api-key

# Optional
HOST=0.0.0.0
PORT=8000
ENVIRONMENT=development
```

### Frontend (.env.local)
```env
PUBLIC_API_URL=http://localhost:8000
PUBLIC_APP_URL=http://localhost:5173
```

## 📦 Key Technologies

### Frontend
- **SvelteKit 5**: Full-stack framework with SSR/SSG
- **TypeScript**: Type-safe development
- **Tailwind CSS**: Utility-first styling
- **Vite**: Lightning-fast build tool

### Backend
- **FastAPI**: Modern async Python framework
- **Pydantic**: Data validation and serialization
- **OpenAI**: AI/ML capabilities
- **Uvicorn**: ASGI server

### DevOps
- **GitHub Actions**: CI/CD pipelines
- **Pre-commit**: Code quality hooks
- **Dependabot**: Automated dependency updates

## 🚢 Deployment

### Frontend Deployment (Vercel/Netlify)
```bash
cd frontend
npm run build
# Deploy the 'build' directory
```

### Backend Deployment (Railway/Render)
```bash
cd backend
# Ensure requirements.txt is up to date
pip freeze > requirements.txt
# Deploy with your platform's CLI or git push
```

## 🤝 Contributing

We welcome contributions! Please see our development guidelines in [CLAUDE.md](CLAUDE.md).

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Follow coding standards in CLAUDE.md
4. Commit your changes (`git commit -m 'feat: add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

### Commit Convention
We use [Conventional Commits](https://www.conventionalcommits.org/):
- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation changes
- `style:` Code style changes
- `refactor:` Code refactoring
- `test:` Test additions/changes
- `chore:` Maintenance tasks

## 📈 Roadmap

See [PROJECT_IDEAS.md](PROJECT_IDEAS.md) for a comprehensive list of planned features including:
- User authentication system
- Database integration
- Real-time WebSocket support
- Payment processing
- Mobile app development
- And 19 more exciting features!

## 🔒 Security

- Never commit `.env` files
- Keep dependencies updated
- Use environment variables for secrets
- Follow security best practices in [CLAUDE.md](CLAUDE.md)

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with [SvelteKit](https://kit.svelte.dev/)
- Powered by [FastAPI](https://fastapi.tiangolo.com/)
- Styled with [Tailwind CSS](https://tailwindcss.com/)
- AI features by [OpenAI](https://openai.com/)
- Developed with [Claude Code](https://claude.ai/code)

---

**Need help?** Check the [documentation](http://localhost:8000/docs) or open an issue on GitHub.
