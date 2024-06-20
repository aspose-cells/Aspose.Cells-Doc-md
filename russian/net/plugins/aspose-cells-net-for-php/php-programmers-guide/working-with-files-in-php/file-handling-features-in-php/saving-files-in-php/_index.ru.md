---
title: Сохранение файлов в PHP
type: docs
weight: 20
url: /ru/net/saving-files-in-php/
---

## **Aspose.Cells - Сохранение файлов Excel**
### **Открытие через путь**
Сохранение файла Microsoft Excel, указав путь к файлу

**PHP-код**

{{< highlight php >}}

         $dataDir = '';

        // Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array());

        //Your Code goes here for any workbook related operations

        $ptr->Call($workbook,"Save",array($dataDir.'/book1.xls'));

        print "File saved successfully!" . PHP_EOL;

{{< /highlight >}}
## **Скачать работающий код**
Скачать ** Сохранение файлов (Aspose.Cells) ** из любого из перечисленных ниже сайтов социального кодинга:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/SavingFiles.php)
