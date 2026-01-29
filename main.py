from fastapi import FastAPI, Query
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class BMIOutput(BaseModel):
    bmi: float
    message: str
class BMIInput(BaseModel): # The Blueprint for what's coming IN
    weight: float
    height: float

# Create the app
app = FastAPI()

# Create Endpoints
@app.get("/")
# Create the function of the endpoint
def Hi():
    return {'message': 'Hello Pyhton'}

# --- MANDATORY FOR FRONTEND CONNECTION ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with your frontend URL
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers=["*"],
)
# new endpoint 
# @app.get ("/caclulate_bmi", response_model = BMIOutput)
# def caclulate_bmi(
#     weight: float = Query(... , gt=20, lt=200, description="weight in KG"), 
#     height : float = Query(... , gt=1, lt=3, description="height in m")):
#     bmi = weight / (height ** 2)
#     if bmi < 18.5:
#         message = "لديك نقص في الوزن، كُل أكثر "
#     elif 18.5 <= bmi < 25:
#         message = "لديك وزن طبيعي، حافظ عليه."
#     elif 25 <= bmi < 30:
#         message = "لديك زيادة في الوزن، تمرن أكثر"
#     else:
#         message = "أنت تعاني من السمنة، قم بمراجعة طبيب"
#     return BMIOutput(bmi=bmi, message=message)

@app.post ("/calculate_bmi", response_model = BMIOutput)
def caclulate_bmi(data: BMIInput):
    
    bmi = data.weight / (data.height ** 2)
    if bmi < 18.5:
        message = "لديك نقص في الوزن، كُل أكثر "
    elif 18.5 <= bmi < 25:
        message = "لديك وزن طبيعي، حافظ عليه."
    elif 25 <= bmi < 30:
        message = "لديك زيادة في الوزن، تمرن أكثر"
    else:
        message = "أنت تعاني من السمنة، قم بمراجعة طبيب"
    return BMIOutput(bmi=bmi, message=message)