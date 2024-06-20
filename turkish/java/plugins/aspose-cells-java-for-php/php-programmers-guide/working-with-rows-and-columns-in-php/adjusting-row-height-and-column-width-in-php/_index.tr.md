---
title: PHP de Sıra Yüksekliğini ve Sütun Genişliğini Ayarlama
type: docs
weight: 10
url: /tr/java/adjusting-row-height-and-column-width-in-php/
---

## **Aspose.Cells - Satır Yüksekliğini ve Sütun Genişliğini Ayarlama**
### **Satır Yüksekliğini Ayarlamak**
Tek bir satırın yüksekliğini belirlemek için  Cells koleksiyonunun setRowHeight metodunu çağırarak yapılabilir. setRowHeight metodu şu parametreleri alır:

- **Satır dizini**, yüksekliği değiştirdiğiniz satırın dizini.
- **Satır yüksekliği**, satıra uygulanan satır yüksekliği.

PHP Kodu

{{< highlight php >}}

 public static function set_row_height($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    $cells = $worksheet->getCells();

    # Setting the height of the second row to 13

    $cells->setRowHeight(1, 13);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Set Row Height.xls");

    print "Set Row Height Successfully." . PHP_EOL;

}

{{< /highlight >}}
### **Sütun Genişliğini Ayarlama**
Bir sütunun genişliğini, Hücreler koleksiyonunun setColumnWidth method'unu çağırarak ayarlayın. setColumnWidth method'u aşağıdaki parametreleri alır:

- **Sütun dizini**, genişliği değiştirdiğiniz sütunun dizini.
- **Sütun genişliği**, istenen sütun genişliği.

PHP Kodu

{{< highlight php >}}

 public static function set_column_width($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    $cells = $worksheet->getCells();

    # Setting the width of the second column to 17.5

    $cells->setColumnWidth(1, 17.5);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Set Column Width.xls");

    print "Set Column Width Successfully." . PHP_EOL;

}

{{< /highlight >}}
## **Çalışan Kodu İndir**
Aşağıda belirtilen sosyal kodlama sitelerinden **Satır Yüksekliğini ve Sütun Genişliğini Ayarlama (Aspose.Cells)** dosyasını indirebilirsiniz:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
