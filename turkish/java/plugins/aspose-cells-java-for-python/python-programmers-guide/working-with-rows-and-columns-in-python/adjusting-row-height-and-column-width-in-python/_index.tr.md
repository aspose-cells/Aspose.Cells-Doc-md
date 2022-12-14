---
title: Python'de Satır Yüksekliğini ve Sütun Genişliğini Ayarlama
type: docs
weight: 10
url: /tr/java/adjusting-row-height-and-column-width-in-python/
keywords: create XLSX in Python, create XLS in Python, XLS python, XLSX python, row height python, column width python, Excel pytho
description: Python Excel API'i kullanarak Python'de Excel dosyaları oluşturun. MS Office olmadan Python uygulamalarınızda XLSX veya XLS'de satır yüksekliğini ve sütun genişliğini ayarlayın.
---
## **Python'de Excel Elektronik Tabloları - Satır Yüksekliğini ve Sütun Genişliğini Ayarlama**
### **Satır Yüksekliğini Ayarlama**
Aspose.Cells ile Cells koleksiyonunun setRowHeight yöntemini çağırarak Python'de tek bir satırın yüksekliğini ayarlamak mümkündür. setRowHeight yöntemi aşağıdaki parametreleri alır:

- **Satır dizini**, yüksekliğini değiştirdiğiniz satırın dizini.
- **Satır yüksekliği**, satıra uygulanacak satır yüksekliği.

**Python Kod**

{{< highlight "python" >}}

 def set_row_height(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Setting the height of the second row to 13

cells.setRowHeight(1, 13)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Set Row Height.xls")

print "Set Row Height Successfully." 

{{< /highlight >}}
### **Sütun Genişliğini Ayarlama**
Cells koleksiyonunun setColumnWidth yöntemini çağırarak bir sütunun genişliğini ayarlayın. setColumnWidth yöntemi aşağıdaki parametreleri alır:

- **Sütun dizini**, genişliğini değiştirdiğiniz sütunun dizini.
- **Sütun genişliği**, istenen sütun genişliği.

**Python Kod**

{{< highlight "python" >}}

 def set_column_width(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Setting the width of the second column to 17.5

cells.setColumnWidth(1, 17.5)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Set Column Width.xls")

print "Set Column Width Successfully." 

{{< /highlight >}}
## **Çalışan Kodu İndir**
İndirmek**Satır Yüksekliğini ve Sütun Genişliğini Ayarlama (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
