---
title: ワークシートのコピー
type: docs
weight: 60
url: /ja/net/copy-worksheets/
---

## **移行のヒント：**
1. ワークブックオブジェクトを作成してワークシートを取得します。
2. ワークシートにテキストを挿入します。
3. 新しいワークシートを作成し、以前に作成したワークシートにコピーします。
### **VSTO**
マクロ'code'のエラー表示：パラメータlangに無効な値が指定されています
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
## **ダウンロード**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/CopyWorksheets.Aspose.Cells.zip)
