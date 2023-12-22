---
title: Python'de Satırları ve Sütunları Gizleme ve Gösterme
type: docs
weight: 50
url: /tr/java/hiding-and-showing-rows-and-columns-in-python/
description: Aspose.Cells for Python Via Java API aracılığıyla Satırları ve Sütunları nasıl Gizleyeceğinizi ve Göstereceğinizi öğrenin.
keywords: How to Hide and Show Rows and Columns in Python Via Java, Hide Rows and Columns using Python Via Java, Python Via Java Show Rows and Columns. 
---
##  **Aspose.Cells - Satır ve Sütunların Görünürlüğünü Kontrol Etme**
###  **Satırları ve Sütunları Gizleme**
Geliştiriciler, sırasıyla Cells koleksiyonunun HideRow ve HideColumn yöntemlerini çağırarak bir satırı veya sütunu gizleyebilir. Her iki yöntem de belirli bir satırı veya sütunu gizlemek için satır/sütun dizinini parametre olarak alır.

**Yakut Kodu**

{{< highlight "ruby" >}}

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
###  **Satır ve Sütunlar Nasıl Gösterilir?**
Geliştiriciler, sırasıyla Cells koleksiyonunun UnhideRow ve UnhideColumn yöntemlerini çağırarak herhangi bir gizli satırı veya sütunu gösterebilir. Her iki yöntem de iki parametre alır:

- **Satır sütun dizini**belirli bir satırı veya sütunu göstermek için kullanılan bir satır veya sütunun dizini.
- **Satır yüksekliği veya sütun genişliği**- gösterildikten sonra satır veya sütuna atanan satır yüksekliği veya sütun genişliği.

**Yakut Kodu**

{{< highlight "ruby" >}}

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
##  **Çalışan Kodu İndir**
 İndirmek**Satırların ve Sütunların Görünürlüğünü Kontrol Etme (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
