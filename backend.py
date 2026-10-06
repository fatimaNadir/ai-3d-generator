import os
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from models import GenerationHistory
import time

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Studio Pro - Dynamic Client Edition")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GenerateRequest(BaseModel):
    user_prompt: str

@app.post("/generate")
def generate_content(request: GenerateRequest, db: Session = Depends(get_db)):
    start_time = time.time()
    prompt_lower = request.user_prompt.lower()
    
    # 1. Category Detection & Smart Asset Matching with Real Videos & Images
    if "doctor" in prompt_lower or "clinic" in prompt_lower or "hospital" in prompt_lower:
        category = "Healthcare & Medical"
        video_url = "https://assets.mixkit.co/videos/preview/mixkit-doctor-checking-a-patient-in-a-clinic-42995-large.mp4"
        bg_image = "https://images.unsplash.com/photo-1584515979956-d9f6e5d09982?auto=format&fit=crop&w=800&q=80"
    elif "hotel" in prompt_lower or "cafe" in prompt_lower or "restaurant" in prompt_lower:
        category = "Hospitality & Food"
        video_url = "https://assets.mixkit.co/videos/preview/mixkit-luxury-pool-in-a-hotel-resort-41520-large.mp4"
        bg_image = "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=800&q=80"
    elif "shoe" in prompt_lower or "sneaker" in prompt_lower or "store" in prompt_lower or "shop" in prompt_lower:
        category = "E-Commerce & Retail"
        video_url = "https://assets.mixkit.co/videos/preview/mixkit-stylish-woman-walking-with-shopping-bags-40898-large.mp4"
        bg_image = "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=800&q=80"
    else:
        category = "Custom Business Solution"
        video_url = "https://assets.mixkit.co/videos/preview/mixkit-digital-animation-of-screens-and-lights-31910-large.mp4"
        bg_image = "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80"

    optimized_prompt = f"Professional 3D cinematic animation, high-end web scroll sequence for [{category}]: {request.user_prompt}"
    video_name = f"animation_{category.lower().replace(' ', '_')}_{int(time.time())}.mp4"
    
    # 2. Dynamic Professional Website Code Generation based on Client Prompt
    website_code = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{request.user_prompt} - Professional 3D Web App</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .glass {{ background: rgba(15, 23, 42, 0.85); backdrop-filter: blur(12px); }}
        @keyframes float {{ 0%, 100% {{ transform: translateY(0px); }} 50% {{ transform: translateY(-10px); }} }}
        .floating {{ animation: float 4s ease-in-out infinite; }}
    </style>
</head>
<body class="bg-slate-950 text-slate-100 font-sans selection:bg-sky-500 selection:text-white">

    <!-- Navbar -->
    <nav class="fixed top-0 w-full z-50 glass border-b border-slate-800 px-6 py-4 flex justify-between items-center">
        <div class="text-xl font-extrabold text-sky-400 tracking-wider">⚡ {category.upper()}</div>
        <div class="space-x-6 text-sm hidden md:block">
            <a href="#home" class="hover:text-sky-400 transition">Home</a>
            <a href="#services" class="hover:text-sky-400 transition">3D Animation</a>
            <a href="#contact" class="hover:text-sky-400 transition">Contact</a>
        </div>
        <a href="#contact" class="bg-sky-500 hover:bg-sky-400 text-slate-950 px-4 py-2 rounded-xl font-bold text-sm transition">Book Now</a>
    </nav>

    <!-- Hero Section -->
    <header id="home" class="min-h-screen flex flex-col items-center justify-center text-center px-4 pt-20">
        <span class="bg-sky-500/10 text-sky-400 border border-sky-500/20 px-4 py-1.5 rounded-full text-xs font-semibold mb-6">Category: {category}</span>
        <h1 class="text-4xl md:text-6xl font-black max-w-4xl tracking-tight leading-tight mb-6">
            {request.user_prompt}
        </h1>
        <p class="text-slate-400 text-lg max-w-2xl mb-10">Yeh website aapke diye gaye unique prompt aur category ke mutabiq 3D animations aur custom visuals ke sath tayar ki gayi hai.</p>
        <div class="flex gap-4">
            <a href="#services" class="bg-sky-500 hover:bg-sky-400 text-slate-950 font-bold px-8 py-4 rounded-xl shadow-lg transition">Explore Services</a>
            <a href="{bg_image}" target="_blank" class="border border-slate-700 hover:border-slate-500 px-8 py-4 rounded-xl font-bold transition">View Asset Image</a>
        </div>
    </header>

    <!-- Services / 3D Showcase Section -->
    <section id="services" class="py-24 px-6 max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
        <div>
            <h2 class="text-3xl font-bold text-sky-400 mb-4">Custom AI Visuals & 3D Experience</h2>
            <p class="text-slate-300 leading-relaxed mb-6">Client ki requirement ke mutabiq yeh layout har section mein behtareen user experience aur modern design faraham karta hai.</p>
            <ul class="space-y-3 text-slate-400">
                <li>✅ Tailored for {category}</li>
                <li>✅ High-Resolution AI Generated Imagery</li>
                <li>✅ Optimized Mobile & Desktop Layout</li>
            </ul>
        </div>
        <div class="floating bg-slate-900 p-4 rounded-2xl border border-slate-800 shadow-2xl">
            <img src="{bg_image}" alt="{request.user_prompt}" class="rounded-xl w-full h-80 object-cover">
        </div>
    </section>

    <!-- Footer -->
    <footer id="contact" class="border-t border-slate-800 py-12 text-center text-slate-500 text-sm">
        <p>&copy; 2026 AI Studio Pro. Designed for: "{request.user_prompt}". All rights reserved.</p>
    </footer>

</body>
</html>
    """.strip()
    
    db_item = GenerationHistory(
        user_prompt=request.user_prompt,
        optimized_prompt=optimized_prompt,
        video_file=video_name,
        website_code=website_code
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    
    return {
        "status": "success",
        "id": db_item.id,
        "category": category,
        "optimized_prompt": optimized_prompt,
        "video_file": video_url,
        "ai_image": bg_image,
        "website_code": website_code,
        "execution_time": round(time.time() - start_time, 2)
    }

@app.get("/history")
def get_history(db: Session = Depends(get_db)):
    return db.query(GenerationHistory).order_by(GenerationHistory.id.desc()).all()

@app.get("/", response_class=HTMLResponse)
def serve_frontend():
    file_path = "templates/index.html"
    if not os.path.exists(file_path):
        file_path = "index.html"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Error: index.html nahi mili!</h1>"
