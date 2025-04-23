---
title: Arbeitsblätter kopieren
type: docs
weight: 60
url: /de/net/copy-worksheets/
---

## **Migrations-Tipp:**
\1. Arbeitsmappenobjekt erstellen und Arbeitsblatt abrufen.
\2. Text im Arbeitsblatt einfügen.
\3. Neues Arbeitsblatt erstellen und es vorher erstelltem Arbeitsblatt kopieren.
### **VSTO**
Fehler beim Rendern des Makros 'code': Ungültiger Wert für den Parameter lang
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
## **Herunterladen**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/CopyWorksheets.Aspose.Cells.zip)
{{< app/cells/assistant language="csharp" >}}
