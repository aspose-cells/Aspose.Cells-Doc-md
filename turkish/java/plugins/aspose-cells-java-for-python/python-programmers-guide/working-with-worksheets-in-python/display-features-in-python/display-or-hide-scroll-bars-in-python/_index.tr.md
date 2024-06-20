---
title: Python da Kaydırma Çubuklarını Göster veya Gizle.
type: docs
weight: 20
url: /tr/java/display-or-hide-scroll-bars-in-python/
---

## **Aspose.Cells - Kaydırma Çubuklarını Göster veya Gizle**
### **Satır/Sütun Başlıklarını Gizleme**
Python için Aspose.Cells Java kullanarak satır/sütun başlıklarını gizlemek için **DisplayHideRowColumnHeaders** modülünü çağırın.

**Python Kodu**

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
### **Satır/Sütun Başlıklarını Görünür Yapma**
Satır ve sütun başlıklarını görünür yapmak için **Worksheet** sınıfının **setRowColumnHeadersVisible(true)** metodunu kullanın.

**Python Kodu**

{{< highlight python >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **Çalışan Kodu İndir**
Herhangi bir sosyal kodlama sitesinden **Merhaba Dünya (Aspose.Cells)**'ı indirin

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
