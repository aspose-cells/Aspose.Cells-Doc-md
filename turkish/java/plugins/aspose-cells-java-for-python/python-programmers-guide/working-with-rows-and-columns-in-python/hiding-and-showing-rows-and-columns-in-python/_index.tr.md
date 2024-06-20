---
title: Python da Satır ve Sütunları Gizleme ve Gösterme
type: docs
weight: 50
url: /tr/java/hiding-and-showing-rows-and-columns-in-python/
description: Java API aracılığıyla Aspose.Cells for Python ile Satır ve Sütun Gizleme ve Gösterme öğrenin.
keywords: Python Via Java da Satır ve Sütunları Gizleme ve Gösterme, Python Via Java ile Satır ve Sütun Gizleme, Python Via Java Satır ve Sütunları Gösterme. 
---

## **Aspose.Cells - Sıraların ve Sütunların Görünürlüğünü Kontrol Etmek**
### **Satır ve Sütunları Gizleme**
Geliştiriciler, sırasıyla hücrelerin koleksiyonunun HideRow ve HideColumn yöntemlerini çağırarak bir satırı veya sütunu gizleyebilirler. Her iki yöntem de belirli bir satırı veya sütunu gizlemek için satır/sütun endeksini bir parametre olarak alır.

**Ruby Kodu**

{{< highlight ruby >}}

 def hide_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Hiding the 3rd row of the worksheet

cells.hideRow(2)

\# Hiding the 2nd column of the worksheet

cells.hideColumn(1)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Hide Rows And Columns.xls")

print "Hide Rows And Columns Successfully." 

{{< /highlight >}}
### **Satır ve Sütunları Gösterme**
Geliştiriciler, sırasıyla hücrelerin koleksiyonunun UnhideRow ve UnhideColumn yöntemlerini çağırarak gizlenmiş herhangi bir satırı veya sütunu gösterebilirler. Her iki yöntem de iki parametre alır:

- **Satır veya sütun endeksi** - belirli satırı veya sütunu göstermek için kullanılan satırın veya sütunun endeksi.
- **Satır yüksekliği veya sütun genişliği** - gösterildikten sonra satıra veya sütuna atanan satır yüksekliği veya sütun genişliği.

**Ruby Kodu**

{{< highlight ruby >}}

 def unhide_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Unhiding the 3rd row and setting its height to 13.5

cells.unhideRow(2,13.5)

\# Unhiding the 2nd column and setting its width to 8.5

cells.unhideColumn(1,8.5)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Unhide Rows And Columns.xls")

print "Unhide Rows And Columns Successfully." 

{{< /highlight >}}
## **Çalışan Kodu İndir**
Aşağıda belirtilen herhangi bir sosyal kodlama sitesinden **Sıraların ve Sütunların Görünürlüğünü Kontrol Etme (Aspose.Cells)** :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
