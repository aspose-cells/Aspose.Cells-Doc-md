---
title: Öffnen von Dateien in PHP
type: docs
weight: 10
url: /de/net/opening-files-in-php/
---

## **Aspose.Cells - Öffnen von Excel-Dateien**
### **Öffnen durch Pfad**
Öffnen Sie einfach eine Microsoft Excel-Datei, indem Sie auf den Dateipfad verweisen

**PHP-Code**

{{< highlight php >}}

         $dataDir = '';

        // Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array($dataDir . '/Book1.xls'));

        $worksheets = $ptr->Get($workbook,"Worksheets",array());

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie **Öffnen von Dateien (Aspose.Cells)** von einer der unten genannten Social-Coding-Sites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
