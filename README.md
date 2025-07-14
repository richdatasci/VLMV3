# Schematic Analyzer with VLM

This application uses Vision Language Models (VLM) like IBM's Granite or LLaVA to analyze technical schematics and answer questions about them.

## Features

- Analyze schematic images (PNG, JPG, JPEG, WEBP)
- Support for multiple VLM models (Granite, LLaVA)
- Command-line interface for easy integration
- Detailed technical analysis of schematics

## Prerequisites

- Linux system with NVIDIA GPU (recommended)
- Python 3.8 or higher
- Ollama installed
- NVIDIA drivers and CUDA (for GPU acceleration)

## Installation

### 1. Install Ollama

# Download and install Ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
# Add your user to the ollama group
```bash
sudo usermod -aG ollama $USER
```

# Start the Ollama service
```bash
sudo systemctl enable ollama
sudo systemctl start ollama
```
# Verify installation
```bash
ollama --version
```

# Download VLM models
```bash
ollama pull granite3.2-vision:latest  # IBM's specialized vision model
ollama pull llava:latest             # General purpose vision model
```

# Clone this repository (if applicable)
```bash
git clone https://github.com/yourusername/VLMV3.git
cd VLMV3

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Python dependencies
pip install ollama Pillow argparse
```
