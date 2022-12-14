---
title: Öppna filer i PHP
type: docs
weight: 10
url: /sv/net/opening-files-in-php/
---
## **Aspose.Cells - Öppna Excel-filer**
### **Öppning genom vägen**
Öppna helt enkelt en Microsoft Excel-fil genom att referera till filens sökväg

**PHP-kod**

{{< highlight "php" >}}

         $dataDir = '';

        // Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array($dataDir . '/Book1.xls'));

        $worksheets = $ptr->Get($workbook,"Worksheets",array());

{{< /highlight >}}
## **Ladda ner Running Code**
 Ladda ner**Öppna filer (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
