---
title: Creare e salvare nuovi fogli di lavoro
type: docs
weight: 70
url: /it/net/create-and-save-new-workbooks/
---

## **Suggerimenti per la migrazione:**
1. Creare un oggetto Workbook
2. Ottenere il foglio di lavoro corrente.
3. Inserire del testo in una qualsiasi cella.
4. Salvare il foglio di lavoro.
### **VSTO**
Di seguito è riportato un esempio di codice per VSTO

{{< highlight csharp >}}

  Excel.Workbook newWorkbook = this.Application.Workbooks.Add();

 Excel.Worksheet worksheet = newWorkbook.ActiveSheet;

 Excel.Range cells = worksheet.Cells;

 cells.set_Item(1,1,"Some Text");

 newWorkbook.Save();

{{< /highlight >}}
### **Aspose.Cells**
Di seguito è riportato un esempio di codice per Aspose.Cells

{{< highlight csharp >}}

  Workbook newWorkbook = new Workbook();

 Worksheet worksheet = newWorkbook.Worksheets.Add("New Sheet");

 Cells cells = worksheet.Cells;

 cells[0,0].PutValue("Some Text");

 newWorkbook.Save(fileName);

{{< /highlight >}}
## **Scarica**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Create_SaveNewWorkbooks.Aspose.Cells.zip)
{{< app/cells/assistant language="csharp" >}}
