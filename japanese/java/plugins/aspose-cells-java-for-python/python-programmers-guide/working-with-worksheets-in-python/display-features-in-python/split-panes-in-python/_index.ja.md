---
title: Pythonでウィンドウを分割
type: docs
weight: 70
url: /ja/java/split-panes-in-python/
---

## **Aspose.Cells - 分割ウィンドウ**
**Aspose.Cells Java for Python**を使用してウィンドウを分割するには、**SplitPanes**モジュールを呼び出すだけです。

**Pythonコード**

{{< highlight java >}}

 saveFormat = self.SaveFormat;

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Set the active cell

workbook.getWorksheets().get(0).setActiveCell("A20");

#Split the worksheet window

workbook.getWorksheets().get(0).split();

#Save the excel file

workbook.save(self.dataDir + "book.out.xls", saveFormat.EXCEL_97_TO_2003);

#Print Message

print "Panes split successfully."

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のソーシャルコーディングサイトから**Split Panes (Aspose.Cells)**をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
