---
title: 删除工作簿中的工作表
type: docs
weight: 100
url: /zh/net/delete-worksheets-from-workbooks/
---

您可以删除工作簿中的任何工作表。要删除工作表，请使用工作表宿主项或通过工作簿的sheets集合访问工作表。
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
## **下载**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/DeleteWorksheetsFromWorkbooks.zip)
