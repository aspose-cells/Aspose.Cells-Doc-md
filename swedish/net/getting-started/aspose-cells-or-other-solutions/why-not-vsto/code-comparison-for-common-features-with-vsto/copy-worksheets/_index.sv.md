---
title: Kopiera kalkylblad
type: docs
weight: 60
url: /sv/net/copy-worksheets/
---

## **Migrations tips:**
\1. Skapa arbetsboksobjekt och hämta kalkylblad.
\2. Infoga text i kalkylbladet.
\3. Skapa nytt kalkylblad och kopiera det till det tidigare gjorda kalkylbladet.
### **VSTO**
Fel vid rendering av makro 'kod': Ogiltigt värde angavs för parametern språk
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
## **Nerladdning**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/CopyWorksheets.Aspose.Cells.zip)
