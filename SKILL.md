SKILL.md
---
name: fams-scan-pic2excel
title: 东方仙盟扫描件转Excel表格 / famsScanPic2Excel
description: Batch recognize table structures from scanned images and scanned PDFs, restore complete cell layout, and export standard editable Excel files with one-click skill invocation. Optimized for large-volume multi-page document digital entry scenarios.
version: 1.0.0
author: Oriental Xianmeng
tags: document,scan,table,excel,convert
---
Skill Overview
famsScanPic2Excel is a self-developed document structuring skill. It focuses on batch table recognition and restoration for scanned pictures and scanned PDF files. It supports tilt correction, noise reduction and blurry file optimization, perfectly restores cross-page tables and cell structures, and outputs standard editable Excel files efficiently.
Core Capabilities
- Batch parsing for multi-page scanned PDFs and image files
- Built-in scanned image enhancement: tilt correction, noise reduction, blur repair
- Precise table detection, cell segmentation and text recognition
- Automatic cross-page table merging and structure completion
- Standard .xlsx output, fully compatible with mainstream office software
Input Parameters
Parameter Name
Type
Required
Description
filePath
String
Yes
Path of scanned image or scanned PDF file
outputPath
String
No
Excel output path, default same as source file directory
batchMode
Boolean
No
Large file batch processing mode, adapt to thousand-page files, default true
Output
Returns the saved path of the generated editable Excel file and recognition logs, supporting direct preview and download.
Running Rules
- Automatically identify image and PDF file types and match parsing strategies
- Stream processing for large files to prevent memory overflow
- Strictly retain original table layout and data integrity
- Intelligent error correction for low-quality scanned documents