---
title: Python da Satır ve Sütun Ekleme ve Silme
type: docs
weight: 60
url: /tr/java/inserting-and-deleting-rows-and-columns-in-python/
keywords: "Python da XLSX oluşturma, Python da XLS oluşturma, Python da XLSX, Python da XLS, Python da XLT, Python da XLTX, Python da satır ekleme, Python da sütun ekleme, Python da Excel"
description: Python Excel API kullanarak Python da Excel elektronik tabloları oluşturun. Python uygulamalarınızda XLSX veya XLS ten satır ekleyin veya silin, MS Office olmadan.
---

## **Python'da Excel Elektronik Tabloları Oluşturma - Satırları/Sütunları Yönetme**
### **Satır Ekleme**
Yeni bir satırı Cells koleksiyonunun insertRows yöntemini çağırarak herhangi bir konuma ekleyin. InsertRows yöntemi, yeni satırın ekleneceği satırın dizinini ilk argüman olarak ve eklenmesi gereken satır sayısını ikinci argüman olarak alır. Aşağıdaki adımlar vardır:

- XLS veya XLSX çalışma kitabını yükle
- Çalışsayfayı erişin
- Satır ekleme
- XLS veya XLSX çalışma kitabı olarak kaydet

**Python Kodu**

{{< highlight python >}}

 def insert_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + "Book1.xls")

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Inserting a row into the worksheet at 3rd position

worksheet.getCells().insertRows(2,1)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Insert Row.xls")

print "Insert Row Successfully." 

{{< /highlight >}}
### **Birden Fazla Satır Ekleme**
Çalışma sayfasına birden fazla satır eklemek için Cells koleksiyonunun insertRows yöntemini çağırın. insertRows yöntemi iki parametre alır:

- Satır indeksi, yeni satırların ekleneceği satırın indeksi.
- Satır sayısı, eklenmesi gereken toplam satır sayısı.

**Python Kodu**

{{< highlight python >}}

 def insert_multiple_rows(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Inserting a row into the worksheet at 3rd position

worksheet.getCells().insertRows(2,10)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Insert Multiple Rows.xls")

print "Insert Multiple Rows Successfully." 


{{< /highlight >}}
### **Bir Satırı Silme**
Herhangi bir konumda bir satırı silmek için Cells koleksiyonunun deleteRows yöntemini çağırın. DeleteRows yöntemi iki parametre alır:

- Satır endeksi, satırların silineceği başlangıç satırının endeksi.
- Satır sayısı. Silinmesi gereken toplam satır sayısı.

**Python Kodu**

{{< highlight python >}}

 def delete_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Deleting 3rd row from the worksheet

worksheet.getCells().deleteRows(2,1,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Delete Row.xls")

print "Delete Row Successfully." 

{{< /highlight >}}
### **Birden Fazla Satırı Silme**
Çalışma sayfasından birden fazla satırı silmek için Cells koleksiyonunun deleteRows yöntemini çağırın. DeleteRows yöntemi iki parametre alır:

- Satır endeksi, satırların silineceği başlangıç satırının endeksi.
- Satır sayısı. Silinmesi gereken toplam satır sayısı.

**Python Kodu**

{{< highlight python >}}

 def delete_multiple_rows(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Deleting 10 rows from the worksheet starting from 3rd row

worksheet.getCells().deleteRows(2,10,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Delete Multiple Rows.xls")

print "Delete Multiple Rows Successfully." 


{{< /highlight >}}
### **Bir Sütun Ekleme**
Geliştiriciler, Cells koleksiyonunun insertColumns metodunu çağırarak çalışma sayfasına herhangi bir konuma bir sütun da ekleyebilirler. insertColumns metodu iki parametre alır:

- Sütun endeksi, sütunun ekleneceği sütunun endeksi
- Sütun sayısı, eklenecek toplam sütun sayısı

**Python Kodu**

{{< highlight python >}}

 def insert_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Inserting a column into the worksheet at 2nd position

worksheet.getCells().insertColumns(1,1)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Insert Column.xls")

print "Insert Column Successfully." 


{{< /highlight >}}
### **Bir Sütunu Silme**
Herhangi bir konumdan çalışma sayfasından bir sütun silmek için Cells koleksiyonunun deleteColumns metodunu çağırın. deleteColumns metodu aşağıdaki parametreleri alır:

- Sütun dizini, sütunun nereden silineceğinin dizini
- Sütun sayısı, silinmesi gereken toplam sütun sayısı
- Hücreleri kaydır, silme işleminden sonra hücreleri sola kaydırmak için Boolean parametre

**Python Kodu**

{{< highlight python >}}

 def delete_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Deleting a column from the worksheet at 2nd position

worksheet.getCells().deleteColumns(1,1,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Delete Column.xls")

print "Delete Column Successfully." 


{{< /highlight >}}
## **Çalışan Kodu İndir**
Aşağıda belirtilen sosyal kodlama sitelerinden **Yönetim Satırları/Sütunları (Aspose.Cells)**'ı indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
