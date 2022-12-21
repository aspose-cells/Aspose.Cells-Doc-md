---
title: Python での改ページの管理
type: docs
weight: 20
url: /ja/java/managing-page-breaks-in-python/
---
## **Aspose.Cells - 改ページの管理**
### **改ページの追加**
を使用して改ページを追加するには**Aspose.Cells Ruby の場合は Java**、 電話**add_page_breaks**方法**改ページ**モジュール。以下にコード例を示します。

**Python コード**

{{< highlight "python" >}}

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
### **すべての改ページのクリア**
を使用してすべての改ページをクリアするには**Aspose.Cells Java for Python**、 電話**clear_all_page_breaks**方法**改ページ**モジュール。以下にコード例を示します。

**Python コード**

{{< highlight "python" >}}



def clear_all_page_breaks(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")


workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Clear All Page Breaks.xls")

print "Clear all page breaks, please check the output file."


{{< /highlight >}}
### **特定の改ページの削除**
を使用して特定の改ページを削除するには**Aspose.Cells Java for Python**、 電話**remove_page_break**方法**改ページ**モジュール。以下にコード例を示します。

**Python コード**

{{< highlight "python" >}}



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
## **実行中のコードをダウンロード**
ダウンロード**改ページの管理 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
