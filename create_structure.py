import os

# Define the entire folder & file structure
structure = {
    "backend": {
        "app": {
            "__init__.py": "",
            "main.py": "",
            "config.py": "",
            "dependencies.py": "",
            "middleware.py": "",
            "api": {
                "__init__.py": "",
                "v1": {
                    "__init__.py": "",
                    "users.py": "",
                    "resume.py": "",
                    "interview.py": "",
                    "feedback.py": "",
                    "auth.py": "",
                    "analytics.py": "",
                    "health.py": "",
                },
            },
            "services": {
                "__init__.py": "",
                "resume_analyzer.py": "",
                "ml_models.py": "",
                "auth_service.py": "",
                "pdf_processor.py": "",
                "job_matcher.py": "",
                "email_service.py": "",
            },
            "models": {
                "__init__.py": "",
                "user.py": "",
                "resume.py": "",
                "interview.py": "",
                "feedback.py": "",
            },
            "schemas": {
                "__init__.py": "",
                "user.py": "",
                "resume.py": "",
                "interview.py": "",
                "feedback.py": "",
            },
            "db": {
                "__init__.py": "",
                "database.py": "",
                "session.py": "",
                "crud.py": "",
                "migrations": {},
            },
            "utils": {
                "__init__.py": "",
                "logger.py": "",
                "security.py": "",
                "constants.py": "",
                "helpers.py": "",
            },
            "ml": {
                "__init__.py": "",
                "tfidf_model.py": "",
                "naive_bayes.py": "",
                "clustering.py": "",
                "nlp_processor.py": "",
            },
            "cache": {
                "__init__.py": "",
                "redis_cache.py": "",
                "in_memory.py": "",
            },
        },
        "tests": {
            "__init__.py": "",
            "test_auth.py": "",
            "test_resume.py": "",
            "test_interview.py": "",
            "conftest.py": "",
        },
        "requirements.txt": "",
        ".env.example": "",
        "Dockerfile": "",
    },
    "frontend": {
        "streamlit_app": {
            "main.py": "",
            "config.py": "",
            "auth_config.py": "",
            "pages": {
                "1_user_dashboard.py": "",
                "2_resume_analyzer.py": "",
                "3_interview_practice.py": "",
                "4_job_recommendations.py": "",
                "5_learning_resources.py": "",
                "6_feedback.py": "",
                "7_analytics.py": "",
                "8_admin_panel.py": "",
            },
            "components": {
                "__init__.py": "",
                "auth_component.py": "",
                "resume_uploader.py": "",
                "analysis_display.py": "",
                "interview_component.py": "",
                "charts_component.py": "",
                "job_cards.py": "",
                "feedback_form.py": "",
            },
            "utils": {
                "__init__.py": "",
                "api_client.py": "",
                "session_manager.py": "",
                "styling.py": "",
                "validators.py": "",
            },
            "assets": {
                "css": {
                    "styles.css": "",
                },
                "images": {},
                "logos": {},
            },
            "requirements.txt": "",
            ".streamlit": {
                "config.toml": "",
            },
        },
    },
    "shared": {
        "constants.py": "",
        "models.py": "",
        "schemas.py": "",
    },
    "docker-compose.yml": "",
    ".env.example": "",
    "README.md": "",
    "DEPLOYMENT.md": "",
    "ARCHITECTURE.md": "",
    "SETUP_GUIDE.md": "",
    "LICENSE": "",
}


def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w") as f:
                f.write(content)


if __name__ == "__main__":
    base_dir = "RESUMATE-AI-MEGA"
    create_structure(base_dir, structure)
    print(f"✅ Folder structure for '{base_dir}' created successfully!")
