---
title: Python da Satır Yüksekliğini ve Sütun Genişliğini Ayarlama
type: docs
weight: 10
url: /tr/java/adjusting-row-height-and-column-width-in-python/
keywords: Python da XLSX oluşturma, Python da XLS oluşturma, Python da XLSX, Python da XLS, Python da satır yüksekliği, python da sütun genişliği, Excel python
description: Python Excel API sini kullanarak Python da Excel dosyaları oluşturun. Uygulamalarınızda MS Office olmadan XLSX veya XLS te satır yüksekliğini ve sütun genişliğini ayarlayın.
---

## **Python'da Excel Elektronik Tablolarda Satır Yüksekliğini ve Sütun Genişliğini Ayarlama**
### **Satır Yüksekliğini Ayarlamak**
Aspose.Cells ile Python'da tek bir satırın yüksekliğini belirlemek, Cells koleksiyonunun setRowHeight yöntemini çağırarak mümkündür. setRowHeight yöntemi aşağıdaki parametreleri alır:

- **Satır dizini**, yüksekliği değiştirdiğiniz satırın dizini.
- **Satır yüksekliği**, satıra uygulanan satır yüksekliği.

**Python Kodu**

{{< highlight python >}}

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
Bir sütunun genişliğini, Hücreler koleksiyonunun setColumnWidth method'unu çağırarak ayarlayın. setColumnWidth method'u aşağıdaki parametreleri alır:

- **Sütun dizini**, genişliği değiştirdiğiniz sütunun dizini.
- **Sütun genişliği**, istenen sütun genişliği.

**Python Kodu**

{{< highlight python >}}

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
Aşağıda belirtilen sosyal kodlama sitelerinden **Satır Yüksekliğini ve Sütun Genişliğini Ayarlama (Aspose.Cells)** dosyasını indirebilirsiniz:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
