---
title: Php'de Bölmeleri Dondur
type: docs
weight: 40
url: /tr/java/freeze-panes-in-php/
---
## **Aspose.Cells - Bölmeleri Dondur**
 Kullanarak Elektronik Tablo Belgesindeki Bölmeleri Dondurmak için**Aspose.Cells Java for PHP** , sadece çağırmak**Donma bölmeleri** modül.

**PHP Kodu**

{{< highlight "php" >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Applying freeze panes settings

$worksheet->freezePanes(3,2,3,2);

//Saving the modified Excel file in default format

$workbook->save($dataDir . "book.out.xls");

{{< /highlight >}}
## **Çalışan Kodu İndir**
İndirmek**Bölmeleri Dondur (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/FreezePanes.php)
