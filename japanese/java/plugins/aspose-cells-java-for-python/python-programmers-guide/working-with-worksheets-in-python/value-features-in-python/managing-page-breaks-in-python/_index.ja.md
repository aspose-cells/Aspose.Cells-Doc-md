---
title: Pythonでのページ区切りの管理
type: docs
weight: 20
url: /ja/java/managing-page-breaks-in-python/
---

## **Aspose.Cells - ページの区切りを管理する**
### **ページブレークの追加**
**Aspose.Cells Java for Ruby**を使用してページ区切りを追加するには、**pagebreaks**モジュールの**add_page_breaks**メソッドを呼び出します。以下にコード例があります。

**Pythonコード**

{{< highlight python >}}

 def add_page_breaks(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

h_page_breaks = worksheet.getHorizontalPageBreaks()

h_page_breaks.add("Y30")

v_page_breaks = worksheet.getVerticalPageBreaks()

v_page_breaks.add("Y30")

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Add Page Breaks.xls")

print "Add page breaks, please check the output file."


{{< /highlight >}}
### **すべてのページの改ページをクリアする**
**Aspose.Cells Java for Python**を使用してすべてのページ区切りを解除するには、**pagebreaks**モジュールの**clear_all_page_breaks**メソッドを呼び出します。以下にコード例を示します。

**Pythonコード**

{{< highlight python >}}



def clear_all_page_breaks(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")


workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Clear All Page Breaks.xls")

print "Clear all page breaks, please check the output file."


{{< /highlight >}}
### **特定の改ページを削除する**
**Aspose.Cells Java for Python**を使用して特定のページ区切りを削除するには、**pagebreaks**モジュールの**remove_page_break**メソッドを呼び出します。以下にコード例を示します。

**Pythonコード**

{{< highlight python >}}



def remove_page_break(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

h_page_breaks = worksheet.getHorizontalPageBreaks()

h_page_breaks.removeAt(0)

v_page_breaks = worksheet.getVerticalPageBreaks()

v_page_breaks.removeAt(0)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Remove Page Break.xls")

print "Remove page break, please check the output file."


{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のいずれかのソーシャルコーディングサイトから**Managing Page Breaks (Aspose.Cells)**をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
