---
title: Copia fogli di lavoro
type: docs
weight: 60
url: /it/net/copy-worksheets/
---
## **Suggerimento per la migrazione:**
\1. Crea un oggetto Cartella di lavoro e ottieni Foglio di lavoro.
\2. Inserisci il testo nel foglio di lavoro.
\3. Crea un nuovo foglio di lavoro e copialo nel foglio di lavoro precedente.
### **VSTO**
Errore durante il rendering della macro 'codice': valore non valido specificato per il parametro lang
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
## **Scaricamento**
- [Git Hub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/CopyWorksheets.Aspose.Cells.zip)
