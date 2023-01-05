---
title: Python'de Sayfa Sonlarını Yönetme
type: docs
weight: 20
url: /tr/java/managing-page-breaks-in-python/
---
## **Aspose.Cells - Sayfa Sonlarını Yönetme**
### **Sayfa Sonları Ekleme**
 kullanarak sayfa sonları eklemek için**Yakut için Aspose.Cells Java** , Arama**add_page_breaks** yöntemi**sayfa sonları** modül. Aşağıda kod örneğini görebilirsiniz.

**Python Kod**

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
### **Tüm Sayfa Sonlarını Temizleme**
 kullanarak tüm sayfa sonlarını temizlemek için**Aspose.Cells Java for Python** , Arama**clear_all_page_breaks** yöntemi**sayfa sonları** modül. Aşağıda kod örneğini görebilirsiniz.

**Python Kod**

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
### **Belirli Sayfa Sonunu Kaldırma**
 Kullanarak belirli sayfa sonunu kaldırmak için**Aspose.Cells Java for Python** , Arama**remove_page_break** yöntemi**sayfa sonları** modül. Aşağıda kod örneğini görebilirsiniz.

**Python Kod**

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
## **Çalışan Kodu İndir**
 İndirmek**Sayfa Sonlarını Yönetme (Aspose.Cells)** aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
