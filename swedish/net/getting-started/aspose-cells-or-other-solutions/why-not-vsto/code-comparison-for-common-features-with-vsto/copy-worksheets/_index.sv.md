---
title: Kopiera arbetsblad
type: docs
weight: 60
url: /sv/net/copy-worksheets/
---
## **Migreringstips:**
\1. Skapa ett arbetsboksobjekt och hämta ett arbetsblad.
\2. Infoga text i arbetsbladet.
\3. Skapa ett nytt kalkylblad och kopiera det till föregående kalkylblad.
### **VSTO**
Fel vid rendering av makrot 'kod': Ogiltigt värde angett för parameter lang
### **Aspose.Cells**
{{< highlight "csharp" >}}

  private static string fileName ="CopyWorksheets.xlsx";

 Workbook newWorkbook = new Workbook();

 Worksheet worksheet = newWorkbook.Worksheets.Add("New Sheet");

 Cells cells = worksheet.Cells;

 cells[0, 0].PutValue("Some Text");

 Worksheet worksheet2 = newWorkbook.Worksheets.Add("MySheet");

 worksheet2.Copy(worksheet);

 newWorkbook.Save(fileName);

{{< /highlight >}}
## **Ladda ner**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/CopyWorksheets.Aspose.Cells.zip)
