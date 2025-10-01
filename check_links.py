#!/usr/bin/env python3
"""
Script to check all links in README.md
"""

import os
import sys

def check_file_exists(filepath):
    """Check if file exists and return status"""
    if os.path.exists(filepath):
        return "✅"
    else:
        return "❌"

def main():
    print("🔍 Checking all links in README.md...")
    print("=" * 50)
    
    # Files referenced in README
    files_to_check = [
        "arxiv_preprint_enhanced.md",
        "docs/Statistical_Report.md",
        "docs/Validation_Report.md", 
        "docs/PRESS_RELEASE.md",
        "docs/SOCIAL_MEDIA_POSTS.md",
        "docs/DISSEMINATION_PLAN.md",
        "figures/Figure1_Distributions.png",
        "figures/Figure2_Correlations.png",
        "figures/Figure3_3D_Tracts.png",
        "figures/Figure4_Network.png",
        "figures/Figure5_Dataset_Comparison.png",
        "figures/Figure6_Validation.png",
        "figures/Figure7_Fractal_Analysis.png",
        "figures/Figure8_Roadmap.png",
        "figures/Figure9_Comparison_Table.png",
        "figures/ROC_Analysis.png",
        "scripts/optical_connectome_pipeline.py",
        "scripts/create_publication_figures.py",
        "scripts/enhanced_statistics.py",
        "data/ds006181_fixed_metrics.csv",
        "data/multi_dataset_optical_metrics.csv",
        "requirements.txt",
        "CITATION.cff"
    ]
    
    all_good = True
    
    for filepath in files_to_check:
        status = check_file_exists(filepath)
        print(f"{status} {filepath}")
        if status == "❌":
            all_good = False
    
    print("=" * 50)
    if all_good:
        print("🎉 All files exist! README links will work correctly.")
    else:
        print("⚠️  Some files are missing. Please create them before uploading.")
    
    return 0 if all_good else 1

if __name__ == "__main__":
    sys.exit(main())
