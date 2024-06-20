---
title: Открытие файлов в PHP
type: docs
weight: 10
url: /ru/net/opening-files-in-php/
---

## **Aspose.Cells - Открытие файлов Excel**
### **Открытие через путь**
Просто откройте файл Microsoft Excel, указав путь к файлу

**PHP-код**

{{< highlight php >}}

         $dataDir = '';

        // Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array($dataDir . '/Book1.xls'));

        $worksheets = $ptr->Get($workbook,"Worksheets",array());

{{< /highlight >}}
## **Скачать работающий код**
Загрузите ** Открытие файлов (Aspose.Cells) ** из любого из перечисленных ниже сайтов социального кодинга:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
