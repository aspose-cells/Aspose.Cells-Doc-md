---
title: Crea e salva nuove cartelle di lavoro
type: docs
weight: 70
url: /it/net/create-and-save-new-workbooks/
---
## **Suggerimenti per la migrazione:**
\1. Crea oggetto cartella di lavoro
\2. Ottieni il foglio di lavoro corrente.
\3. Inserisci del testo in qualsiasi cella.
\4. Salva la cartella di lavoro.
### **VSTO**
Di seguito è riportato un esempio di codice per VSTO

{{< highlight "csharp" >}}

  Excel.Workbook newWorkbook = this.Application.Workbooks.Add();

 Excel.Worksheet worksheet = newWorkbook.ActiveSheet;

 Excel.Range cells = worksheet.Cells;

 cells.set_Item(1,1,"Some Text");

 newWorkbook.Save();

{{< /highlight >}}
### **Aspose.Cells**
Di seguito è riportato un esempio di codice per Aspose.Cells

{{< highlight "csharp" >}}

  Workbook newWorkbook = new Workbook();

 Worksheet worksheet = newWorkbook.Worksheets.Add("New Sheet");

 Cells cells = worksheet.Cells;

 cells[0,0].PutValue("Some Text");

 newWorkbook.Save(fileName);

{{< /highlight >}}
## **Scaricamento**
- [Git Hub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Create_SaveNewWorkbooks.Aspose.Cells.zip)
