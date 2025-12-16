from transformers import AutoProcessor, AutoModel
import torch

print("Step 4: Florence load test start")

model_name = "microsoft/Florence-2-large"

print("Loading processor...")
processor = AutoProcessor.from_pretrained(
    model_name,
    trust_remote_code=True
)

print("Loading model (CPU)...")
model = AutoModel.from_pretrained(
    model_name,
    trust_remote_code=True
)

print("Florence processor + model loaded successfully ✅")
