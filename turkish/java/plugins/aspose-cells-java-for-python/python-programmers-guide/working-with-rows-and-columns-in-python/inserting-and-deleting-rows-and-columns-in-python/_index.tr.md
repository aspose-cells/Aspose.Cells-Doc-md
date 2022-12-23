---
title: Python'de Satır ve Sütun Ekleme ve Silme
type: docs
weight: 60
url: /tr/java/inserting-and-deleting-rows-and-columns-in-python/
keywords: create XLSX in Python, create XLS in Python, XLS python, XLSX python, XLT python, XLTX python, insert row python, insert column python, Excel pytho
description: Python'de Excel elektronik tabloları oluşturmak için Python Excel API'i kullanın. MS Office olmadan Python uygulamalarınızda XLSX veya XLS'den satır ekleyin veya silin.
---
## **Python'de Excel Elektronik Tabloları Oluşturun - Satırları/Sütunları Yönetme**
### **Satır Ekleme**
Cells koleksiyonunun insertRows yöntemini çağırarak herhangi bir konuma satır ekleyin. insertRows yöntemi, ilk argüman olarak yeni satırın ekleneceği satırın indeksini, ikinci argüman olarak eklenecek satır sayısını alır. Aşağıdaki adımlar:

- XLS veya XLSX çalışma kitabını yükle
- Çalışma sayfasına erişin
- satırı ekle
- XLS veya XLSX çalışma kitabı olarak kaydedin

**Python Kod**

{{< highlight "python" >}}

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
### **Birden Çok Satır Ekleme**
Çalışma sayfasına birden çok satır eklemek için Cells koleksiyonunun insertRows yöntemini çağırın. InsertRows yöntemi iki parametre alır:

- Satır dizini, yeni satırların ekleneceği satırın dizini.
- Satır sayısı, eklenmesi gereken toplam satır sayısı.

**Python Kod**

{{< highlight "python" >}}

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
### **Satır Silme**
Herhangi bir konumdaki bir satırı silmek için Cells koleksiyonunun deleteRows yöntemini çağırın. DeleteRows yöntemi iki parametre alır:

- Satır dizini, satırların silineceği satırın dizini.
- Satır sayısı, silinmesi gereken toplam satır sayısı.

**Python Kod**

{{< highlight "python" >}}

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
### **Birden Çok Satırı Silme**
Bir çalışma sayfasından birden çok satırı silmek için Cells koleksiyonunun deleteRows yöntemini çağırın. DeleteRows yöntemi iki parametre alır:

- Satır dizini, satırların silineceği satırın dizini.
- Satır sayısı, silinmesi gereken toplam satır sayısı.

**Python Kod**

{{< highlight "python" >}}

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
### **Sütun Ekleme**
Geliştiriciler ayrıca Cells koleksiyonunun insertColumns yöntemini çağırarak çalışma sayfasına herhangi bir konumda bir sütun ekleyebilir. insertColumns yöntemi iki parametre alır:

- Sütun dizini, sütunun ekleneceği sütunun dizini
- Sütun sayısı, eklenmesi gereken toplam sütun sayısı

**Python Kod**

{{< highlight "python" >}}

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
### **Sütun Silme**
Herhangi bir konumdaki çalışma sayfasından bir sütunu silmek için Cells koleksiyonunun deleteColumns yöntemini çağırın. deleteColumns yöntemi aşağıdaki parametreleri alır:

- Sütun dizini, sütunun silineceği sütunun dizini.
- Sütun sayısı, silinmesi gereken toplam sütun sayısı.
- Hücreleri kaydır, silme işleminden sonra hücrelerin sola kaydırılıp kaydırılmayacağını gösteren Boolean parametresi.

**Python Kod**

{{< highlight "python" >}}

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
 İndirmek**Satırları/Sütunları Yönetme (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
