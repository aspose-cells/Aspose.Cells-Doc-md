---
title: Arbeitsmappen erstellen und speichern
type: docs
weight: 70
url: /de/net/create-and-save-new-workbooks/
---

## **Migrationshinweise:**
\1. Arbeitsmappenobjekt erstellen
\2. Aktuelles Arbeitsblatt erhalten.
\3. Einfügen von Text in eine Zelle.
\4. Arbeitsmappe speichern.
### **VSTO**
Nachfolgend finden Sie ein Codebeispiel für VSTO

{{< highlight csharp >}}

  Excel.Workbook newWorkbook = this.Application.Workbooks.Add();

 Excel.Worksheet worksheet = newWorkbook.ActiveSheet;

 Excel.Range cells = worksheet.Cells;

 cells.set_Item(1,1,"Some Text");

 newWorkbook.Save();

{{< /highlight >}}
### **Aspose.Cells**
Nachfolgend finden Sie ein Codebeispiel für Aspose.Cells

{{< highlight csharp >}}

  Workbook newWorkbook = new Workbook();

 Worksheet worksheet = newWorkbook.Worksheets.Add("New Sheet");

 Cells cells = worksheet.Cells;

 cells[0,0].PutValue("Some Text");

 newWorkbook.Save(fileName);

{{< /highlight >}}
## **Herunterladen**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Create_SaveNewWorkbooks.Aspose.Cells.zip)
