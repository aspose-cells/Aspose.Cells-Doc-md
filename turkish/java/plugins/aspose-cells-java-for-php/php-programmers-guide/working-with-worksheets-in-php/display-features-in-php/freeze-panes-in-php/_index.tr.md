---
title: Php de Pencereleri Sabitle
type: docs
weight: 40
url: /tr/java/freeze-panes-in-php/
---

## **Aspose.Cells - Panoları Sabitleme**
**Aspose.Cells Java for PHP** kullanarak Elektronik Tablo Belgesinde Pencereleri Sabitlemek için **FreezePanes** modülünü sadece çağırın.

PHP Kodu

{{< highlight php >}}

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
Herhangi bir sosyal kodlama sitesinden **Aspose.Cells** ile Panoları Sabitleme'yi indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/FreezePanes.php)
