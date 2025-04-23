---
title: Elimina Fogli di lavoro dai Workbooks
type: docs
weight: 100
url: /it/net/delete-worksheets-from-workbooks/
---

Puoi eliminare qualsiasi foglio di lavoro in un workbook. Per eliminare un foglio di lavoro, utilizza l'elemento host del foglio di lavoro o accedi al foglio di lavoro utilizzando la raccolta di fogli del workbook.
## **VSTO**
{{< highlight csharp >}}

  Excel.Workbook myWorkbook= this.Application.Workbooks.Open(fileName);

 myWorkbook.Sheets[2].Delete();

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight csharp >}}

  Workbook myWorkbook = new Workbook(fileName);

 myWorkbook.Worksheets.RemoveAt(1);

 myWorkbook.Save(fileName);

{{< /highlight >}}
## **Scarica**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/DeleteWorksheetsFromWorkbooks.zip)
{{< app/cells/assistant language="csharp" >}}
