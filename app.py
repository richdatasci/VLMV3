import os
import argparse
from server import analyze_schematic

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Analyze schematic images using VLM")
    parser.add_argument("image_path", help="Path to the schematic image file")
    parser.add_argument("--question", "-q", 
                       default="Analyze this technical schematic and provide a detailed summary of its components and functionality.",
                       help="Question to ask about the schematic")
    parser.add_argument("--model", "-m", 
                       default="granite3.2-vision:latest",
                       help="VLM model to use (default: granite3.2-vision:latest)")
    
    args = parser.parse_args()

    # Validate image path
    if not os.path.exists(args.image_path):
        print(f"Error: Image file not found at {args.image_path}")
        return

    # Run the analysis
    print(f"\nAnalyzing {args.image_path} with {args.model}...\n")
    result = analyze_schematic(args.image_path, args.question, args.model)
    
    # Print the results
    print("Analysis Results:")
    print("=" * 50)
    print(result)
    print("=" * 50)

if __name__ == "__main__":
    main()
