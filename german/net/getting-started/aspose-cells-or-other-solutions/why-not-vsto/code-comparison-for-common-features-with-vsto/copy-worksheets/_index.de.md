---
title: Arbeitsblätter kopieren
type: docs
weight: 60
url: /de/net/copy-worksheets/
---
## **Migrationstipp:**
\1. Workbook-Objekt erstellen und Worksheet abrufen.
\2. Text in Arbeitsblatt einfügen.
\3. Erstellen Sie ein neues Arbeitsblatt und kopieren Sie es in das zuvor erstellte Arbeitsblatt.
### **VSTO**
Fehler beim Rendern des Makros „Code“: Ungültiger Wert für Parameter lang angegeben
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
## **Download**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/CopyWorksheets.Aspose.Cells.zip)
