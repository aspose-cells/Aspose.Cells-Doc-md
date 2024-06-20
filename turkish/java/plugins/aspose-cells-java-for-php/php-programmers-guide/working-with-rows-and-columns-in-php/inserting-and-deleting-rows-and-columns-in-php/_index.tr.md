---
title: PHP de Satırları ve Sütunları Ekleme ve Silme
type: docs
weight: 60
url: /tr/java/inserting-and-deleting-rows-and-columns-in-php/
description: Aspose.Cells for PHP via Java API leri aracılığıyla Satırları ve Sütunları Nasıl Ekleyip Sileceğinizi öğrenin.
keywords: PHP de Satırları ve Sütunları Nasıl Ekler ve Siler, PHP ile Satırları ve Sütunları Ekleme, PHP Satırları ve Sütunları Silme, PHP ile Satırları veya Sütunları Ekleme, PHP ile Satırları veya Sütunları Silme.
---

## **Aspose.Cells - Sıraları/Sütunları Yönetme**
### **Satır Ekleme**
Yeni bir satırın nerede ekleneceğini belirlemek için Cells koleksiyonunun insertRows yöntemini çağırarak herhangi bir konuma bir satır ekleyin. InsertRows yöntemi, eklenen yeni satırın konumu için endeks olarak alır ve eklenmesi gereken satır sayısını ikinci bir argüman olarak alır.

PHP Kodu

{{< highlight php >}}

 public static function insert_row($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Inserting a row into the worksheet at 3rd position

    $worksheet->getCells()->insertRows(2,1);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Insert Row.xls");

    print "Insert Row Successfully." . PHP_EOL;

}  

{{< /highlight >}}
### **Birden Fazla Satır Ekleme**
Çalışma sayfasına birden fazla satır eklemek için Cells koleksiyonunun insertRows yöntemini çağırın. insertRows yöntemi iki parametre alır:

- Satır indeksi, yeni satırların ekleneceği satırın indeksi.
- Satır sayısı, eklenmesi gereken toplam satır sayısı.

PHP Kodu

{{< highlight php >}}

 public static function insert_multiple_rows($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Inserting a row into the worksheet at 3rd position

    $worksheet->getCells()->insertRows(2,10);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Insert Multiple Rows.xls");

    print "Insert Multiple Rows Successfully." . PHP_EOL;

}

{{< /highlight >}}
### **Bir Satırı Silme**
Herhangi bir konumda bir satırı silmek için Cells koleksiyonunun deleteRows yöntemini çağırın. DeleteRows yöntemi iki parametre alır:

- Satır endeksi, satırların silineceği başlangıç satırının endeksi.
- Satır sayısı. Silinmesi gereken toplam satır sayısı.

PHP Kodu

{{< highlight php >}}

 public static function delete_row($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Deleting 3rd row from the worksheet

    $worksheet->getCells()->deleteRows(2,1,true);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Delete Row.xls");

    print "Delete Row Successfully." . PHP_EOL;

}

{{< /highlight >}}
### **Birden Fazla Satırı Silme**
Çalışma sayfasından birden fazla satırı silmek için Cells koleksiyonunun deleteRows yöntemini çağırın. DeleteRows yöntemi iki parametre alır:

- Satır endeksi, satırların silineceği başlangıç satırının endeksi.
- Satır sayısı. Silinmesi gereken toplam satır sayısı.

PHP Kodu

{{< highlight php >}}

 public static function delete_multiple_rows($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Deleting 10 rows from the worksheet starting from 3rd row

    $worksheet->getCells()->deleteRows(2,10,true);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Delete Multiple Rows.xls");

    print "Delete Multiple Rows Successfully." . PHP_EOL;

}

{{< /highlight >}}
### **Bir Sütun Ekleme**
Geliştiriciler, Cells koleksiyonunun insertColumns metodunu çağırarak çalışma sayfasına herhangi bir konuma bir sütun da ekleyebilirler. insertColumns metodu iki parametre alır:

- Sütun endeksi, sütunun ekleneceği sütunun endeksi
- Sütun sayısı, eklenecek toplam sütun sayısı

PHP Kodu

{{< highlight php >}}

 public static function insert_column($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Inserting a column into the worksheet at 2nd position

    $worksheet->getCells()->insertColumns(1,1);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Insert Column.xls");

    print "Insert Column Successfully." . PHP_EOL;

}

{{< /highlight >}}
### **Bir Sütunu Silme**
Herhangi bir konumdan çalışma sayfasından bir sütun silmek için Cells koleksiyonunun deleteColumns metodunu çağırın. deleteColumns metodu aşağıdaki parametreleri alır:

- Sütun dizini, sütunun nereden silineceğinin dizini
- Sütun sayısı, silinmesi gereken toplam sütun sayısı
- Hücreleri kaydır, silme işleminden sonra hücreleri sola kaydırmak için Boolean parametre

PHP Kodu

{{< highlight php >}}

 public static function delete_column($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Deleting a column from the worksheet at 2nd position

    $worksheet->getCells()->deleteColumns(1,1,true);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Delete Column.xls");

    print "Delete Column Successfully." . PHP_EOL;

}  

{{< /highlight >}}
## **Çalışan Kodu İndir**
Aşağıda belirtilen sosyal kodlama sitelerinden **Yönetim Satırları/Sütunları (Aspose.Cells)**'ı indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
