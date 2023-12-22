---
title: PHP'de Satır ve Sütun Ekleme ve Silme
type: docs
weight: 60
url: /tr/java/inserting-and-deleting-rows-and-columns-in-php/
description: Aspose.Cells for PHP via Java API'leri aracılığıyla Satırları ve Sütunları nasıl ekleyeceğinizi ve sileceğinizi öğrenin.
keywords: How to Insert and Delete Rows and Columns in PHP, Insert Rows and Columns using PHP, PHP Delete Rows and Columns, Insert Rows or Columns with PHP, Delete Rows or Columns via PHP.
---
##  **Aspose.Cells - Satırları/Sütunları Yönetme**
###  **Satır Ekleme**
Cells koleksiyonunun insertRows yöntemini çağırarak herhangi bir konuma satır ekleyin. InsertRows yöntemi, ilk argüman olarak yeni satırın ekleneceği satırın indeksini, ikinci argüman olarak eklenecek satır sayısını alır.

**PHP Kodu**

{{< highlight "php" >}}

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
###  **Birden Çok Satır Ekleme**
Çalışma sayfasına birden çok satır eklemek için Cells koleksiyonunun insertRows yöntemini çağırın. InsertRows yöntemi iki parametre alır:

- Satır dizini, yeni satırların ekleneceği satırın dizini.
- Satır sayısı, eklenmesi gereken toplam satır sayısı.

**PHP Kodu**

{{< highlight "php" >}}

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
###  **Satır Silme**
Herhangi bir konumdaki bir satırı silmek için Cells koleksiyonunun deleteRows yöntemini çağırın. SilRows yöntemi iki parametre alır:

- Satır dizini, satırların silineceği satırın dizini.
- Satır sayısı, silinmesi gereken toplam satır sayısı.

**PHP Kodu**

{{< highlight "php" >}}

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
###  **Birden Çok Satırı Silme**
Bir çalışma sayfasından birden çok satırı silmek için Cells koleksiyonunun deleteRows yöntemini çağırın. SilRows yöntemi iki parametre alır:

- Satır dizini, satırların silineceği satırın dizini.
- Satır sayısı, silinmesi gereken toplam satır sayısı.

**PHP Kodu**

{{< highlight "php" >}}

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
###  **Sütun Ekleme**
Geliştiriciler ayrıca Cells koleksiyonunun insertColumns yöntemini çağırarak çalışma sayfasına herhangi bir konuma sütun ekleyebilir. insertColumns yöntemi iki parametre alır:

- Sütun dizini, sütunun ekleneceği sütunun dizini
- Sütun sayısı, eklenmesi gereken toplam sütun sayısı

**PHP Kodu**

{{< highlight "php" >}}

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
###  **Sütun Silme**
Herhangi bir konumdaki çalışma sayfasından bir sütunu silmek için Cells koleksiyonunun deleteColumns yöntemini çağırın. deleteColumns yöntemi aşağıdaki parametreleri alır:

- Sütun dizini, sütunun silineceği sütunun dizini.
- Sütun sayısı, silinmesi gereken toplam sütun sayısı.
- Hücreleri kaydır, silme işleminden sonra hücrelerin sola kaydırılıp kaydırılmayacağını belirten Boolean parametresi.

**PHP Kodu**

{{< highlight "php" >}}

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
##  **Çalışan Kodu İndir**
 İndirmek**Satırları/Sütunları Yönetme (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
