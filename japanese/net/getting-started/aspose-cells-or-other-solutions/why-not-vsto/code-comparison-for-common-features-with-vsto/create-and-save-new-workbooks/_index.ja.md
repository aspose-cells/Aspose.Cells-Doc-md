---
title: 新しいワークブックを作成して保存する
type: docs
weight: 70
url: /ja/net/create-and-save-new-workbooks/
---

## **移行のヒント:**
1. Workbook オブジェクトを作成する
2. 現在のワークシートを取得する
3. 任意のセルにテキストを挿入する
4. ワークブックを保存する
### **VSTO**
以下は VSTO のコード例です

{{< highlight csharp >}}

  Excel.Workbook newWorkbook = this.Application.Workbooks.Add();

 Excel.Worksheet worksheet = newWorkbook.ActiveSheet;

 Excel.Range cells = worksheet.Cells;

 cells.set_Item(1,1,"Some Text");

 newWorkbook.Save();

{{< /highlight >}}
### **Aspose.Cells**
以下は Aspose.Cells のコード例です

{{< highlight csharp >}}

  Workbook newWorkbook = new Workbook();

 Worksheet worksheet = newWorkbook.Worksheets.Add("New Sheet");

 Cells cells = worksheet.Cells;

 cells[0,0].PutValue("Some Text");

 newWorkbook.Save(fileName);

{{< /highlight >}}
## **ダウンロード**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Create_SaveNewWorkbooks.Aspose.Cells.zip)
{{< app/cells/assistant language="csharp" >}}
