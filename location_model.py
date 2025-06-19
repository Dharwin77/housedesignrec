import torch
import torch.nn as nn
import numpy as np

class LocationModel(nn.Module):
    def __init__(self):
        super(LocationModel, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(2, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 1),
            nn.Sigmoid()
        )
    
    def forward(self, x):
        return self.fc(x)

def validate_location(location):
    lat, lng = map(float, location.split(','))
    model = LocationModel()
    model.load_state_dict(torch.load('location_model.pth'))  # Pretrained weights
    model.eval()
    
    # Dummy Input Normalization
    input_data = torch.tensor([[lat / 90.0, lng / 180.0]], dtype=torch.float32)
    prediction = model(input_data).item()

    if prediction > 0.5:  # Threshold for suitability
        return True, []
    else:
        # Suggest alternatives
        suggestions = [(lat + 0.1, lng + 0.1), (lat - 0.1, lng - 0.1)]
        return False, suggestions
