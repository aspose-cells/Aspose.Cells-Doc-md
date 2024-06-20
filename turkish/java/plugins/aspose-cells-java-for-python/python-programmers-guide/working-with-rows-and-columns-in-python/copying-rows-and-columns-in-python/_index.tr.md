---
title: Python da Satırları ve Sütunları Kopyalama
type: docs
weight: 30
url: /tr/java/copying-rows-and-columns-in-python/
---

## **Aspose.Cells - Satır ve Sütunları Kopyalama**
### **Satırları Kopyalama**
Aspose.Cells, Cells sınıfının copyRow yöntemini sağlar. Bu yöntem, kaynak satırdan hedef satıra formüller, değerler, yorumlar, hücre biçimleri, gizli hücreler, resimler ve diğer çizim nesneleri dahil olmak üzere tüm veri türlerini kopyalar.

copyRow yöntemi aşağıdaki parametreleri alır:

- kaynak Cells nesnesi,
- kaynak satır dizini, ve
- hedef satır dizini.

**Python Kodu**

{{< highlight java >}}

 def copy_rows(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Copy the second row with data, formattings, images and drawing objects

\# to the 12th row in the worksheet.

worksheet.getCells().copyRow(worksheet.getCells(),1,11)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Copy Rows.xls")

print "Copy Rows Successfully." 

{{< /highlight >}}
### **Sütunları Kopyalama**
Aspose.Cells, Cells sınıfının copyColumn yöntemini sağlar; bu yöntem, formüllerle güncellenmiş referanslar ve değerler, yorumlar, hücre biçimleri, gizli hücreler, resimler ve diğer çizim nesneleri dahil olmak üzere tüm veri türlerini kopyalar.

copyColumn yöntemi aşağıdaki parametreleri alır:

- kaynak Cells nesnesi,
- kaynak sütun indeksi ve
- hedef sütun indeksi.

**Python Kodu**

{{< highlight ruby >}}



def copy_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook()

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Put some data into header rows (A1:A4)

i = 0

while i < 5:

worksheet.getCells().get(i, 0).setValue("Header Row #i")





\# Put some detail data (A5:A999)

i = 5

while i < 1000:

worksheet.getCells().get(i, 0).setValue("Detail Row #i")


\# Create another Workbook.

workbook1 = Workbook()

\# Get the first worksheet in the book.

worksheet1 = workbook1.getWorksheets().get(0)

\# Copy the first column from the first worksheet of the first workbook into

\# the first worksheet of the second workbook.

worksheet1.getCells().copyColumn(worksheet.getCells(),0,2)

\# Autofit the column.

worksheet1.autoFitColumn(2)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Copy Columns.xls")

print "Copy Columns Successfully." 

{{< /highlight >}}
## **Çalışan Kodu İndir**
Herhangi aşağıda belirtilen sosyal kodlama sitelerinden **Copying Rows and Columns (Aspose.Cells)**'ı indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
