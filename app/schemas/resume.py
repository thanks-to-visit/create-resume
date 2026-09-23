from pydantic import BaseModel, Field


class ContactInfo(BaseModel):
    email: str
    phone: str
    location: str | None = None


class SocialLinks(BaseModel):
    linkedin: str | None = None
    github: str | None = None
    portfolio: str | None = None


class Skills(BaseModel):
    languages: list[str] = Field(default_factory=list)
    frameworks: list[str] = Field(default_factory=list)
    databases: list[str] = Field(default_factory=list)
    tools: list[str] = Field(default_factory=list)


class Experience(BaseModel):
    company: str
    role: str
    location: str | None = None
    start_date: str
    end_date: str | None = None
    description: list[str] = Field(default_factory=list)


class Project(BaseModel):
    name: str
    description: str
    technologies: list[str] = Field(default_factory=list)
    link: str | None = None


class Achievement(BaseModel):
    title: str
    description: str | None = None
    date: str | None = None


class Education(BaseModel):
    institution: str
    degree: str
    field_of_study: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    grade: str | None = None


class ResumeRequest(BaseModel):
    full_name: str
    contact: ContactInfo
    social_links: SocialLinks | None = None
    summary: str
    skills: Skills

    experience: list[Experience] = Field(default_factory=list)
    projects: list[Project] = Field(default_factory=list)
    achievements: list[Achievement] = Field(default_factory=list)
    education: list[Education] = Field(default_factory=list)
