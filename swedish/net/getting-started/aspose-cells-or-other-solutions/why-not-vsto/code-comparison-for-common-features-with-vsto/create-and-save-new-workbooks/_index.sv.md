---
title: Skapa och spara nya arbetsböcker
type: docs
weight: 70
url: /sv/net/create-and-save-new-workbooks/
---
## **Migreringstips:**
\1. Skapa arbetsboksobjekt
\2. Hämta aktuellt arbetsblad.
\3. Infoga lite text i valfri cell.
\4. Spara arbetsboken.
### **VSTO**
Nedan är kodexempel för VSTO

{{< highlight "csharp" >}}

  Excel.Workbook newWorkbook = this.Application.Workbooks.Add();

 Excel.Worksheet worksheet = newWorkbook.ActiveSheet;

 Excel.Range cells = worksheet.Cells;

 cells.set_Item(1,1,"Some Text");

 newWorkbook.Save();

{{< /highlight >}}
### **Aspose.Cells**
Nedan är kodexempel för Aspose.Cells

{{< highlight "csharp" >}}

  Workbook newWorkbook = new Workbook();

 Worksheet worksheet = newWorkbook.Worksheets.Add("New Sheet");

 Cells cells = worksheet.Cells;

 cells[0,0].PutValue("Some Text");

 newWorkbook.Save(fileName);

{{< /highlight >}}
## **Ladda ner**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Create_SaveNewWorkbooks.Aspose.Cells.zip)
