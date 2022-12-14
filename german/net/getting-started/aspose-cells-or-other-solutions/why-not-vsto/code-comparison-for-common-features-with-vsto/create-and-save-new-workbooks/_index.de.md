---
title: Erstellen und speichern Sie neue Arbeitsmappen
type: docs
weight: 70
url: /de/net/create-and-save-new-workbooks/
---
## **Migrationstipps:**
\1. Workbook-Objekt erstellen
\2. Holen Sie sich das aktuelle Arbeitsblatt.
\3. Fügen Sie Text in eine beliebige Zelle ein.
\4. Speichern Sie die Arbeitsmappe.
### **VSTO**
Nachfolgend finden Sie ein Codebeispiel für VSTO

{{< highlight "csharp" >}}

  Excel.Workbook newWorkbook = this.Application.Workbooks.Add();

 Excel.Worksheet worksheet = newWorkbook.ActiveSheet;

 Excel.Range cells = worksheet.Cells;

 cells.set_Item(1,1,"Some Text");

 newWorkbook.Save();

{{< /highlight >}}
### **Aspose.Cells**
Unten ist ein Codebeispiel für Aspose.Cells

{{< highlight "csharp" >}}

  Workbook newWorkbook = new Workbook();

 Worksheet worksheet = newWorkbook.Worksheets.Add("New Sheet");

 Cells cells = worksheet.Cells;

 cells[0,0].PutValue("Some Text");

 newWorkbook.Save(fileName);

{{< /highlight >}}
## **Download**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Create_SaveNewWorkbooks.Aspose.Cells.zip)
