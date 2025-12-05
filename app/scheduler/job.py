from apscheduler.schedulers.background import BackgroundScheduler
from app.services.weather_service import get_and_save_indian_weather_data

def start_scheduler(app):
    scheduler = BackgroundScheduler()
    
    scheduler.add_job(
        lambda: app.loop.create_task(get_and_save_indian_weather_data()), 
        'interval', 
        minutes=30
    )
    
    scheduler.start()
    return scheduler