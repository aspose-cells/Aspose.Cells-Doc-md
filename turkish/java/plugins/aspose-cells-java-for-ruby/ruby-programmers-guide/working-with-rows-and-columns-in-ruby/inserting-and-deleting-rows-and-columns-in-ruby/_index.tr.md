---
title: Ruby de Sıraları ve Sütunları Ekleme ve Silme
type: docs
weight: 60
url: /tr/java/inserting-and-deleting-rows-and-columns-in-ruby/
---

## **Aspose.Cells - Sıraları/Sütunları Yönetme**
### **Satır Ekleme**
Yeni bir satırın nerede ekleneceğini belirlemek için Cells koleksiyonunun insertRows yöntemini çağırarak herhangi bir konuma bir satır ekleyin. InsertRows yöntemi, eklenen yeni satırın konumu için endeks olarak alır ve eklenmesi gereken satır sayısını ikinci bir argüman olarak alır.

**Ruby Kodu**

{{< highlight ruby >}}

 def insert_row()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Inserting a row into the worksheet at 3rd position

    worksheet.getCells().insertRows(2,1)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Insert Row.xls")

    puts "Insert Row Successfully."

end   

{{< /highlight >}}
### **Birden Fazla Satır Ekleme**
Çalışma sayfasına birden fazla satır eklemek için Cells koleksiyonunun insertRows yöntemini çağırın. insertRows yöntemi iki parametre alır:

- Satır indeksi, yeni satırların ekleneceği satırın indeksi.
- Satır sayısı, eklenmesi gereken toplam satır sayısı.

**Ruby Kodu**

{{< highlight ruby >}}

 def insert_multiple_rows()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Inserting a row into the worksheet at 3rd position

    worksheet.getCells().insertRows(2,10)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Insert Multiple Rows.xls")

    puts "Insert Multiple Rows Successfully."

end

{{< /highlight >}}
### **Bir Satırı Silme**
Herhangi bir konumda bir satırı silmek için Cells koleksiyonunun deleteRows yöntemini çağırın. DeleteRows yöntemi iki parametre alır:

- Satır endeksi, satırların silineceği başlangıç satırının endeksi.
- Satır sayısı. Silinmesi gereken toplam satır sayısı.

**Ruby Kodu**

{{< highlight ruby >}}

 def delete_row()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Deleting 3rd row from the worksheet

    worksheet.getCells().deleteRows(2,1,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Delete Row.xls")

    puts "Delete Row Successfully."

end

{{< /highlight >}}
### **Birden Fazla Satırı Silme**
Çalışma sayfasından birden fazla satırı silmek için Cells koleksiyonunun deleteRows yöntemini çağırın. DeleteRows yöntemi iki parametre alır:

- Satır endeksi, satırların silineceği başlangıç satırının endeksi.
- Satır sayısı. Silinmesi gereken toplam satır sayısı.

**Ruby Kodu**

{{< highlight ruby >}}

 def delete_multiple_rows()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Deleting 10 rows from the worksheet starting from 3rd row

    worksheet.getCells().deleteRows(2,10,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Delete Multiple Rows.xls")

    puts "Delete Multiple Rows Successfully."

end 

{{< /highlight >}}
### **Bir Sütun Ekleme**
Geliştiriciler, Cells koleksiyonunun insertColumns metodunu çağırarak çalışma sayfasına herhangi bir konuma bir sütun da ekleyebilirler. insertColumns metodu iki parametre alır:

- Sütun endeksi, sütunun ekleneceği sütunun endeksi
- Sütun sayısı, eklenecek toplam sütun sayısı

**Ruby Kodu**

{{< highlight ruby >}}

 def insert_column()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Inserting a column into the worksheet at 2nd position

    worksheet.getCells().insertColumns(1,1)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Insert Column.xls")

    puts "Insert Column Successfully."

end  

{{< /highlight >}}
### **Bir Sütunu Silme**
Herhangi bir konumdan çalışma sayfasından bir sütun silmek için Cells koleksiyonunun deleteColumns metodunu çağırın. deleteColumns metodu aşağıdaki parametreleri alır:

- Sütun dizini, sütunun nereden silineceğinin dizini
- Sütun sayısı, silinmesi gereken toplam sütun sayısı
- Hücreleri kaydır, silme işleminden sonra hücreleri sola kaydırmak için Boolean parametre

**Ruby Kodu**

{{< highlight ruby >}}

 def delete_column()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Deleting a column from the worksheet at 2nd position

    worksheet.getCells().deleteColumns(1,1,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Delete Column.xls")

    puts "Delete Column Successfully."

end   

{{< /highlight >}}
## **Çalışan Kodu İndir**
Aşağıda belirtilen sosyal kodlama sitelerinden **Yönetim Satırları/Sütunları (Aspose.Cells)**'ı indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
