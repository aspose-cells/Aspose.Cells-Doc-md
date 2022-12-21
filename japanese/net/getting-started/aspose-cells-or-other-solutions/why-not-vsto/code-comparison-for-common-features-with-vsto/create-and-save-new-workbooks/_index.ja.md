---
title: 新しいワークブックを作成して保存する
type: docs
weight: 70
url: /ja/net/create-and-save-new-workbooks/
---
## **移行のヒント:**
\1. Workbook オブジェクトの作成
\2.現在のワークシートを取得します。
\3.任意のセルにテキストを挿入します。
\4.ワークブックを保存します。
### **VSTO**
以下はVSTOのコード例です

{{< highlight "csharp" >}}

  Excel.Workbook newWorkbook = this.Application.Workbooks.Add();

 Excel.Worksheet worksheet = newWorkbook.ActiveSheet;

 Excel.Range cells = worksheet.Cells;

 cells.set_Item(1,1,"Some Text");

 newWorkbook.Save();

{{< /highlight >}}
### **Aspose.Cells**
以下は、Aspose.Cells のコード例です。

{{< highlight "csharp" >}}

  Workbook newWorkbook = new Workbook();

 Worksheet worksheet = newWorkbook.Worksheets.Add("New Sheet");

 Cells cells = worksheet.Cells;

 cells[0,0].PutValue("Some Text");

 newWorkbook.Save(fileName);

{{< /highlight >}}
## **ダウンロード**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Create_SaveNewWorkbooks.Aspose.Cells.zip)
