---
title: Copy Worksheets
type: docs
weight: 60
url: /net/copy-worksheets/
---

## **Migration Tip:**
\1. Create Workbook object and get Worksheet.
\2. Insert text in worksheet.
\3. Create new Worksheet and Copy it to previous before made worksheet.
### **VSTO**
Error rendering macro 'code' : Invalid value specified for parameter lang
### **Aspose.Cells**
{{< highlight csharp >}}

  private static string fileName ="CopyWorksheets.xlsx";

 Workbook newWorkbook = new Workbook();

 Worksheet worksheet = newWorkbook.Worksheets.Add("New Sheet");

 Cells cells = worksheet.Cells;

 cells[0, 0].PutValue("Some Text");

 Worksheet worksheet2 = newWorkbook.Worksheets.Add("MySheet");

 worksheet2.Copy(worksheet);

 newWorkbook.Save(fileName);

{{< /highlight >}}
## **Download**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/CopyWorksheets.Aspose.Cells.zip)
