---  
title: Lock Cells to Protect Them with Python.NET  
linktitle: Lock Cells to Protect Them  
type: docs  
weight: 130  
url: /python-net/how-to-lock-cells-to-protect-them/  
description: Learn how to lock specific cells and protect worksheets in Excel files using Aspose.Cells for Python via .NET.  
keywords: Python lock cells, protect worksheets, cell protection in Excel with Python, Aspose.Cells Python tutorial  
ai_search_scope: cells_pythonnet  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask" 
---  

## **Possible Usage Scenarios**  
Locking cells to protect them is a common practice in spreadsheet applications, such as Microsoft Excel or Google Sheets, for several important reasons:  

1. **Preventing Accidental Changes**: Locking cells can prevent users from accidentally modifying important data or formulas.  
2. **Maintain Data Integrity**: Ensure critical data remains consistent and accurate.  
3. **Controlled Access**: Manage editing permissions in collaborative environments.  
4. **Protecting Formulas**: Safeguard crucial calculations from alteration.  
5. **Enforcing Business Rules**: Comply with data‑protection requirements.  
6. **Guiding Users**: Provide clear editable areas in complex spreadsheets.  

## **How to Lock Cells to Protect Them in Excel**  
Here's how you can lock cells in Microsoft Excel:  

1. **Select the cells to lock**: Choose cells, or skip to lock the entire sheet.  
2. **Open the Format Cells dialog**: Right‑click ► **Format Cells** or press **Ctrl+1**.  
   <br>  
   <img src="1.png" width=60% />  
3. **Lock the cells**: Go to the **Protection** tab ► check **Locked** ► click **OK**.  
4. **Protect the worksheet**: **Review** tab ► **Protect Sheet** ► set password/permissions ► click **OK**.  
   <br>  
   <img src="2.png" width=60% />  

## **How to Lock Cells to Protect Them Using Python**  

Aspose.Cells for Python via .NET enables programmatic cell protection. Follow these steps:  

1. Load [sample file](sample.xlsx)  
2. Unlock all cells (the default locked state is not enforced until protection)  
3. Lock specific cells  
4. Protect the worksheet to enforce locking  

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("sample.xlsx")
worksheet = workbook.worksheets[0]

# Unlock all cells first
style = ac.Style()
style.is_locked = False
style_flag = ac.StyleFlag()
style_flag.locked = True
worksheet.cells.apply_style(style, style_flag)

# Lock specific cells
worksheet.cells["A1"].get_style().is_locked = True
worksheet.cells["B2"].get_style().is_locked = True

# Enable worksheet protection
worksheet.protect(ac.ProtectionType.ALL)

# Save protected workbook
workbook.save("output.xlsx")
```  

## **Output Result**  
This implementation locks the specified cells (A1 and B2) while keeping others editable. Worksheet protection enforces these settings.  

<br>  
<img src="3.png" width=60% />  

```python
from aspose.cells import Workbook, ProtectionType, StyleFlag

# Load the Excel file
workbook = Workbook("sample.xlsx")

# Access the first worksheet
sheet = workbook.worksheets[0]

# Unlock all cells first
unlock_style = workbook.create_style()
unlock_style.is_locked = False

style_flag = StyleFlag()
style_flag.locked = True
sheet.cells.apply_style(unlock_style, style_flag)

# Lock specific cells (A1 and B2)
lock_style = workbook.create_style()
lock_style.is_locked = True

sheet.cells.get("A1").set_style(lock_style)
sheet.cells.get("B2").set_style(lock_style)

# Protect the worksheet to enforce locking
sheet.protect(ProtectionType.ALL)

# Save the modified workbook
workbook.save("output_locked.xlsx")
```  
{{< app/cells/assistant language="python-net" >}}
