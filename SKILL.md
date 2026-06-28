SKILL.md
---
name: fams-scan-pic2excel
title: 东方仙盟扫描件转Excel表格 / famsScanPic2Excel
description: Self-developed office structuring skill, batch identifies tables from scanned images, supports batch processing of mass scanned files, one-click export of standard editable Excel files.
version: 1.0.0
author: Oriental Xianmeng
tags: scan,table,excel,ocr,office,convert
---
Skill Introduction
famsScanPic2Excel is an exclusive self-developed skill by Oriental Xianmeng. It is dedicated to batch identification and structured restoration of tables in scanned pictures, supports multi-format scanned file recognition and large-volume batch processing, and quickly generates standardized and editable Excel documents through skill one-click invocation.
Core Capabilities
- Batch identify JPG/PNG/BMP/TIFF scanned image files
- Automatic file validity detection and invalid file filtering
- Mass file batch processing, stable adaptation to multi-page file scenarios
- Standard .xlsx file export, compatible with all office software
- Standard skill call interface, support one-click invocation in Claw chat box
Project Structure
Complete official skill package structure:
famsScanPic2Excel/
├── SKILL.md
├── README.md
├── README.en.md
├── requirements.txt
└── src/
    ├── check_images.py
    └── scan_to_excel.py
- check_images.py: Image pre-detection script, dynamically read paths, detect image format, size and file integrity
- scan_to_excel.py: Core conversion script, batch process scanned folders and export Excel files
Environment Dependencies
All dependencies are uniformly configured in requirements.txt
One-click installation command:
pip install -r requirements.txt
Input Parameters
Parameter Name
Type
Required
Description
filePath
String
Yes
Local folder path of scanned images to be processed
outputPath
String
No
Export path of the final Excel file, default is the source directory
batchMode
Boolean
No
Large file batch processing mode, default true
Skill Invocation
Claw Chat Box Command
Basic call:
/fams-scan-pic2excel filePath="你的扫描文件夹路径"
Advanced custom call:
/fams-scan-pic2excel filePath="你的扫描文件夹路径" outputPath="输出文件.xlsx" batchMode=true
Running Rules
- All paths are dynamically passed in, no hard-coded fixed paths
- Automatically filter valid picture formats and eliminate abnormal files
- Stream processing to avoid memory overflow of large files
- Output standard xlsx format file with complete and usable data
Applicable Scenarios
Batch digital entry of financial statements, paper ledgers, archival forms, and scanned archived documents.