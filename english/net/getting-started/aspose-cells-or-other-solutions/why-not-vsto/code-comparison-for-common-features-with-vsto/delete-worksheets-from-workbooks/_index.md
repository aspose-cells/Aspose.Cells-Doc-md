---
title: Delete Worksheets from Workbooks
type: docs
weight: 100
url: /net/delete-worksheets-from-workbooks/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

You can delete any worksheet in a workbook. To delete a worksheet, use the worksheet host item or access the worksheet by using the sheets collection of the workbook.
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
## **Download**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/DeleteWorksheetsFromWorkbooks.zip)
{{< app/cells/assistant language="csharp" >}}
