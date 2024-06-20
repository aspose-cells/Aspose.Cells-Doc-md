---
title: Pythonでスクロールバーを表示または非表示にする
type: docs
weight: 20
url: /ja/java/display-or-hide-scroll-bars-in-python/
---

## **Aspose.Cells - スクロールバーの表示または非表示**
### **行/列ヘッダーを非表示にする**
**Aspose.Cells Java for Python**を使用して行/列見出しを非表示にするには、**DisplayHideRowColumnHeaders**モジュールを呼び出します。

**Pythonコード**

{{< highlight python >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(False)

#Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(False)

#Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Scroll bars are now hidden, please check the output document."

{{< /highlight >}}
### **行/列ヘッダーを表示する**
行列ヘッダーを表示するには、WorksheetクラスのsetRowColumnHeadersVisible(true)メソッドを使用します。

**Pythonコード**

{{< highlight python >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のソーシャルコーディングサイトから**Hello World (Aspose.Cells)**をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
