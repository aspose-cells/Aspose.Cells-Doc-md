---
title: Python da Satırları ve Sütunları Otomatik Sığdırma
type: docs
weight: 20
url: /tr/java/autofit-rows-and-columns-in-python/
description: Java API si aracılığıyla Aspose.Cells for Python ile Satırları ve Sütunları Otomatik Sığdırmayı öğrenin.
keywords: Python için Java aracılığıyla Satırları ve Sütunları Otomatik Sığdırma, Python için Java aracılığıyla Satırları Otomatik Sığdırma, Python için Java aracılığıyla Sütunları Otomatik Sığdırma. 
---

## **Satırları ve Sütunları Otomatik Sığdırmanın Yolu**
### **Satır Otomatik Sığdırma**
Bir satırın genişliğini ve yüksekliğini otomatik ayarlamanın en basit yolu Worksheet sınıfının autoFitRow metodunu çağırmaktır. autoFitRow metodu, (yeniden boyutlandırılacak olan satırın) bir satır indeksi olarak bir parametre alır.

**Python Kodu**

{{< highlight python >}}

 def autofit_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Auto-fitting the 3rd row of the worksheet

worksheet.autoFitRow(2)

\# Auto-fitting the 3rd row of the worksheet based on the contents in a range of

\# cells (from 1st to 9th column) within the row

#worksheet.autoFitRow(2,0,8) # Uncomment this line if you to do AutoFit Row in a Range of Cells. Also, comment line 288.

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Autofit Row.xls")

print "Autofit Row Successfully." 

{{< /highlight >}}
### **Sütun Otomatik Sığdırma**
Bir sütunun genişliğini ve yüksekliğini otomatik boyutlandırmanın en kolay yolu Worksheet sınıfının autoFitColumn metodunu çağırmaktır. autoFitColumn metodu, (yeniden boyutlandırılacak olan sütunun) bir sütun indeksini parametre olarak alır.

**Python Kodu**

{{< highlight python >}}

 def autofit_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Auto-fitting the 4th column of the worksheet

worksheet.autoFitColumn(3)

\# Auto-fitting the 4th column of the worksheet based on the contents in a range of

\# cells (from 1st to 9th row) within the column

#worksheet.autoFitColumn(3,0,8) #Uncomment this line if you to do AutoFit Column in a Range of Cells. Also, comment line 310.

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Autofit Column.xls")

print "Autofit Column Successfully." 

{{< /highlight >}}
## **Çalışan Kodu İndir**
Aşağıda belirtilen sosyal kodlama sitelerinden **Satırları ve Sütunları Otomatik Daraltma (Aspose.Cells)** dosyasını indirebilirsiniz:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
