---
title: Python でスクロール バーを表示または非表示にする
type: docs
weight: 20
url: /ja/java/display-or-hide-scroll-bars-in-python/
---
## **Aspose.Cells - スクロール バーの表示または非表示**
### **行/列ヘッダーの非表示**
を使用して行/列ヘッダーを非表示にするには**Aspose.Cells Java for Python**、 電話**DisplayHideRowColumnHeaders**モジュール。

**Python コード**

{{< highlight "python" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(False)

# Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(False)

# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Scroll bars are now hidden, please check the output document."

{{< /highlight >}}
### **行/列ヘッダーを表示する**
Worksheet クラスの setRowColumnHeadersVisible(true) メソッドを使用して、行と列のヘッダーを表示します。

**Python コード**

{{< highlight "python" >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**Hello World (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
