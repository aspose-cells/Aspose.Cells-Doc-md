---
title: Python da Sayfa Sonlarını Yönetme
type: docs
weight: 20
url: /tr/java/managing-page-breaks-in-python/
---

## **Aspose.Cells - Sayfa Kesmelerini Yönetme**
### **Sayfa Kesmeleri Eklemek**
Ruby için  **Aspose.Cells Java** kullanarak sayfa kesmeleri eklemek için, **pagebreaks** modülünün **add_page_breaks** yöntemini çağırın. Aşağıda örnek kodu görebilirsiniz.

**Python Kodu**

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
### **Tüm Sayfa Kesmelerini Temizleme**
**Python için Aspose.Cells Java** kullanarak tüm sayfa kırıklarını temizlemek için **sayfa_kırıkları** modülünün **tüm_sayfa_kırıklarını_temizle** metodunu çağırın. Aşağıda kod örneğini görebilirsiniz.

**Python Kodu**

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
### **Belirli Sayfa Kesmelerini Kaldırma**
**Python için Aspose.Cells Java** kullanarak belirli sayfa kırığını kaldırmak için **sayfa_kırıkları** modülünün **sayfa_kırığını_kaldır**  metodunu çağırın. Aşağıda kod örneğini görebilirsiniz.

**Python Kodu**

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
## **Çalışan Kodu İndir**
Herhangi bir sosyal kodlama sitesinden **Aspose.Cells** ile Sayfa Sonlarını Yönetmeyi İndirin

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
