---
title: Pythonでウィンドウを固定する
type: docs
weight: 40
url: /ja/java/freeze-panes-in-python/
---

## **Aspose.Cells - ペインを固定する**
**Aspose.Cells Java for Python**を使用してスプレッドシートドキュメントのウィンドウを固定するには、**FreezePanes**モジュールを呼び出すだけです。

**Pythonコード**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Applying freeze panes settings

worksheet.freezePanes(3,2,3,2)

#Saving the modified Excel file in default format

workbook.save(self.dataDir + "book.out.xls")

#Print Message

print "Panes freeze successfull."

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のソーシャルコーディングサイトから**Hello World (Aspose.Cells)**をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
