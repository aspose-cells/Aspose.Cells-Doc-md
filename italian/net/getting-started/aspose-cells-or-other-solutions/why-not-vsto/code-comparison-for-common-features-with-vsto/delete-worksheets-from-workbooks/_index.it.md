---
title: Elimina i fogli di lavoro dalle cartelle di lavoro
type: docs
weight: 100
url: /it/net/delete-worksheets-from-workbooks/
---
Puoi eliminare qualsiasi foglio di lavoro in una cartella di lavoro. Per eliminare un foglio di lavoro, utilizzare l'elemento host del foglio di lavoro o accedere al foglio di lavoro utilizzando la raccolta di fogli della cartella di lavoro.
## **VSTO**
{{< highlight "csharp" >}}

  Excel.Workbook myWorkbook= this.Application.Workbooks.Open(fileName);

 myWorkbook.Sheets[2].Delete();

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight "csharp" >}}

  Workbook myWorkbook = new Workbook(fileName);

 myWorkbook.Worksheets.RemoveAt(1);

 myWorkbook.Save(fileName);

{{< /highlight >}}
## **Scarica**
- [Git Hub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/DeleteWorksheetsFromWorkbooks.zip)
