# CLAUDE.md

This file provides comprehensive guidance to Claude Code (claude.ai/code) when working with this repository. It contains project-specific conventions, standards, and important context.

## 🎯 Project Overview

This is a full-stack web application demonstrating AI-powered capabilities with modern web technologies.

**Tech Stack:**
- **Frontend**: SvelteKit 5 (latest version) with TypeScript
- **Backend**: FastAPI (Python) with async support
- **Styling**: Tailwind CSS for utility-first styling
- **AI Integration**: OpenAI API for text analysis and code generation

**Project Structure:**
```
├── frontend/          # SvelteKit application
│   ├── src/
│   │   ├── routes/   # Page components and routing
│   │   └── lib/      # Shared components and utilities
│   └── package.json  # Frontend dependencies
├── backend/          # FastAPI application
│   ├── main.py      # API endpoints and business logic
│   └── requirements.txt
└── PROJECT_IDEAS.md  # Comprehensive development roadmap
```

## 🚀 Development Guidelines

### TypeScript Standards
- **ALWAYS** use TypeScript for all frontend development
- Enable strict mode in tsconfig.json
- Define explicit types for all function parameters and returns
- Use interfaces for object shapes, types for unions/primitives
- Avoid `any` type - use `unknown` if type is truly unknown

### Variable Naming
- Use **descriptive** variable names that clearly indicate purpose
- Follow conventions:
  - `camelCase` for variables and functions
  - `PascalCase` for components and classes
  - `UPPER_SNAKE_CASE` for constants
  - Prefix booleans with `is`, `has`, `should` (e.g., `isLoading`)

### Frontend (Svelte/SvelteKit)
- **ALWAYS** use Svelte 5 with runes (`$state`, `$derived`, `$effect`)
- Use SvelteKit's latest features and best practices
- Component structure:
  ```svelte
  <script lang="ts">
    // Imports first
    // Type definitions
    // Props declarations
    // State and derived values
    // Functions and handlers
    // Lifecycle/effects
  </script>

  <!-- Template -->

  <style>
    /* Scoped styles if needed */
  </style>
  ```
- Prefer `$state` over stores for component state
- Use `+page.ts` for data loading, not `onMount`

### Styling with Tailwind
- Use Tailwind utility classes as primary styling method
- Follow mobile-first responsive design (`sm:`, `md:`, `lg:`)
- Extract common patterns into components, not @apply
- Use semantic color classes from theme
- Maintain consistent spacing scale

### Backend (Python/FastAPI)
- **ALWAYS** include comprehensive docstrings:
  ```python
  def process_data(input_data: str, options: Dict[str, Any]) -> ProcessedResult:
      """
      Process input data according to specified options.

      Args:
          input_data: Raw string data to be processed
          options: Dictionary containing processing options
              - 'normalize': bool - Whether to normalize the data
              - 'validate': bool - Whether to validate input

      Returns:
          ProcessedResult: Object containing processed data and metadata

      Raises:
          ValidationError: If input data fails validation
          ProcessingError: If processing fails

      Example:
          >>> result = process_data("sample", {"normalize": True})
          >>> print(result.output)
          'SAMPLE'
      """
  ```
- Use type hints for all functions
- Follow PEP 8 style guidelines
- Use Pydantic models for request/response validation
- Implement proper error handling with specific exceptions

### API Design
- Follow RESTful conventions
- Use proper HTTP methods (GET, POST, PUT, DELETE)
- Version APIs from the start (`/api/v1/`)
- Return consistent response formats
- Include proper status codes
- Document all endpoints with OpenAPI

### Testing Requirements
- Write tests for all new features
- Maintain minimum 80% code coverage
- Test structure mirrors source structure
- Use descriptive test names that explain what's being tested
- Include edge cases and error scenarios

### Git Commit Messages
- Use conventional commits format
- Types: feat, fix, docs, style, refactor, test, chore
- Keep subject line under 50 characters
- Add body for complex changes
- Reference issues when applicable

## 🔒 Security Practices

- **NEVER** commit secrets, API keys, or credentials
- Use environment variables for sensitive configuration
- Validate and sanitize all user inputs
- Implement proper authentication before accessing protected routes
- Use HTTPS in production
- Keep dependencies updated

## 📁 File Organization

### Frontend Files
- Pages in `src/routes/`
- Reusable components in `src/lib/components/`
- API clients in `src/lib/api/`
- Type definitions in `src/lib/types/`
- Utilities in `src/lib/utils/`

### Backend Files
- Keep `main.py` focused on route definitions
- Extract business logic to service modules
- Database models in separate module
- Configuration in `config.py`
- Utilities in `utils/` directory

## 🚨 Important Reminders

1. **Check Existing Code First**: Before implementing new features, search for existing patterns and utilities
2. **Don't Reinvent**: Use existing libraries and framework features
3. **Performance Matters**: Consider performance implications, especially for lists and real-time features
4. **Accessibility**: Ensure all UI components are accessible (ARIA labels, keyboard navigation)
5. **Error Handling**: Always handle errors gracefully with user-friendly messages

## 🛠️ Development Workflow

1. **Before Starting**:
   - Read relevant parts of PROJECT_IDEAS.md
   - Check for existing similar implementations
   - Verify no breaking changes to APIs

2. **During Development**:
   - Run linters frequently (`npm run lint`, `ruff`)
   - Test changes locally
   - Check for TypeScript errors
   - Verify responsive design

3. **Before Committing**:
   - Run all tests
   - Check for console errors
   - Verify no hardcoded values
   - Ensure proper error handling

## 📚 Key Libraries and Tools

### Frontend
- **SvelteKit 5**: Full-stack framework
- **TypeScript**: Type safety
- **Tailwind CSS**: Utility-first styling
- **Vite**: Build tool and dev server

### Backend
- **FastAPI**: Modern Python web framework
- **Pydantic**: Data validation
- **OpenAI**: AI integration
- **Uvicorn**: ASGI server

### Development Tools
- **ESLint & Prettier**: Code formatting
- **Black & Ruff**: Python formatting
- **Pre-commit**: Git hooks
- **GitHub Actions**: CI/CD

## 🎨 UI/UX Principles

- **Consistency**: Maintain consistent patterns across the application
- **Feedback**: Provide immediate feedback for user actions
- **Loading States**: Always show loading indicators
- **Error States**: Design helpful error messages
- **Mobile First**: Design for mobile, enhance for desktop

## 🔍 Code Review Checklist

When reviewing or writing code, ensure:
- [ ] TypeScript types are properly defined
- [ ] No `any` types without justification
- [ ] Components follow Svelte 5 patterns
- [ ] Tailwind classes follow conventions
- [ ] Python code has comprehensive docstrings
- [ ] API endpoints have proper validation
- [ ] Error cases are handled
- [ ] Tests are included
- [ ] Performance is considered
- [ ] Security best practices followed

## 📖 Additional Resources

- [PROJECT_IDEAS.md](./PROJECT_IDEAS.md) - Comprehensive feature roadmap
- [SvelteKit Documentation](https://kit.svelte.dev)
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [Tailwind CSS Documentation](https://tailwindcss.com)

---

**Remember**: This is a living document. Update it as conventions evolve and new patterns emerge.
