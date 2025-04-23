---
title: Copia Fogli di lavoro
type: docs
weight: 60
url: /it/net/copy-worksheets/
---

## **Suggerimento per la migrazione:**
1. Creare l'oggetto Workbook e ottenere il foglio di lavoro.
2. Inserire del testo nel foglio di lavoro.
3. Creare un nuovo foglio di lavoro e copiarlo nel foglio di lavoro precedentemente creato.
### **VSTO**
Errore durante il rendering del macro 'code': valore non valido specificato per il parametro lang
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
## **Scarica**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/CopyWorksheets.Aspose.Cells.zip)
{{< app/cells/assistant language="csharp" >}}
