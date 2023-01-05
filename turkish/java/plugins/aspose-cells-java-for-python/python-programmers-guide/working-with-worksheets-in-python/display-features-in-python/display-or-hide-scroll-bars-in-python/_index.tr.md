---
title: Python'de Kaydırma Çubuklarını Görüntüleyin veya Gizle
type: docs
weight: 20
url: /tr/java/display-or-hide-scroll-bars-in-python/
---
## **Aspose.Cells - Kaydırma Çubuklarını Görüntüle veya Gizle**
### **Satır/Sütun Başlıklarını Gizleme**
 kullanarak satır/sütun başlıklarını gizlemek için**Aspose.Cells Java for Python** , Arama**DisplayHideRowColumnHeaders** modül.

**Python Kod**

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
### **Satır/Sütun Başlıklarını Görünür Hale Getirme**
Worksheet sınıfının setRowColumnHeadersVisible(true) yöntemini kullanarak satır ve sütun başlıklarını görünür yapın.

**Python Kod**

{{< highlight "python" >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **Çalışan Kodu İndir**
 İndirmek**Hello World (Aspose.Cells)** aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
