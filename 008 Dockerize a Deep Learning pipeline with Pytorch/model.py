import torch
from torchvision.models import ResNet18_Weights, resnet18

print("PyTorch version:", torch.__version__)

# Load a pre-trained ResNet18 model.
model = resnet18(weights=ResNet18_Weights.IMAGENET1K_V1)
model.eval()  # Set to evaluation mode

print(" ResNet18 model loaded successfully!")
print(f"Model is running on: {next(model.parameters()).device}")

# Optional: Run a dummy inference
print("\nRunning dummy inference...")
# Create a dummy image (random noise)
dummy_image = torch.randn(1, 3, 224, 224)
with torch.no_grad():
    output = model(dummy_image)
    predicted_class = output.argmax(dim=1).item()

print(f"Dummy inference completed! Predicted class index: {predicted_class}")
print("PyTorch deep learning pipeline is ready!")
