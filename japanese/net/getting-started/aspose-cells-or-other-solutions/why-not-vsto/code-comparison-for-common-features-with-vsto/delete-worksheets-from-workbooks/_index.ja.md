---
title: ワークブックからワークシートを削除する
type: docs
weight: 100
url: /ja/net/delete-worksheets-from-workbooks/
---
ワークブック内の任意のワークシートを削除できます。ワークシートを削除するには、ワークシート ホスト項目を使用するか、ブックのシート コレクションを使用してワークシートにアクセスします。
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
## **ダウンロード**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/DeleteWorksheetsFromWorkbooks.zip)
