---
title: Speichern von Dateien in PHP
type: docs
weight: 20
url: /de/net/saving-files-in-php/
---
## **Aspose.Cells - Excel-Dateien speichern**
### **Öffnung durch Pfad**
Speichern einer Microsoft Excel-Datei durch Referenzieren des Dateipfads

**PHP-Code**

{{< highlight "php" >}}

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
## **Laufcode herunterladen**
 Download**Dateien speichern (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/SavingFiles.php)
