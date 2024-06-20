---
title: PHP de Satırları ve Sütunları Otomatik Boyutlandırma
type: docs
weight: 20
url: /tr/java/autofit-rows-and-columns-in-php/
---

## **Aspose.Cells - Satırları ve Sütunları Otomatik Daraltma**
### **Satır Otomatik Daraltma**
Bir satırın genişliğini ve yüksekliğini otomatik ayarlamanın en basit yolu Worksheet sınıfının autoFitRow metodunu çağırmaktır. autoFitRow metodu, (yeniden boyutlandırılacak olan satırın) bir satır indeksi olarak bir parametre alır.

PHP Kodu

{{< highlight php >}}

 public static function autofit_row($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Auto-fitting the 3rd row of the worksheet

    $worksheet->autoFitRow(2);

    # Auto-fitting the 3rd row of the worksheet based on the contents in a range of

    # cells (from 1st to 9th column) within the row

    #$worksheet->autoFitRow(2,0,8) # Uncomment this line if you to do AutoFit Row in a Range of Cells. Also, comment line 288.

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Autofit Row.xls");

    print "Autofit Row Successfully." . PHP_EOL;

}

{{< /highlight >}}
### **Sütun Otomatik Daraltma**
Bir sütunun genişliğini ve yüksekliğini otomatik boyutlandırmanın en kolay yolu Worksheet sınıfının autoFitColumn metodunu çağırmaktır. autoFitColumn metodu, (yeniden boyutlandırılacak olan sütunun) bir sütun indeksini parametre olarak alır.

PHP Kodu

{{< highlight php >}}

 public static function autofit_column($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Auto-fitting the 4th column of the worksheet

    $worksheet->autoFitColumn(3);

    # Auto-fitting the 4th column of the worksheet based on the contents in a range of

    # cells (from 1st to 9th row) within the column

    #$worksheet->autoFitColumn(3,0,8) #Uncomment this line if you to do AutoFit Column in a Range of Cells. Also, comment line 310.

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Autofit Column.xls");

    print "Autofit Column Successfully." . PHP_EOL;

}

{{< /highlight >}}
## **Çalışan Kodu İndir**
Aşağıda belirtilen sosyal kodlama sitelerinden **Satırları ve Sütunları Otomatik Daraltma (Aspose.Cells)** dosyasını indirebilirsiniz:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
