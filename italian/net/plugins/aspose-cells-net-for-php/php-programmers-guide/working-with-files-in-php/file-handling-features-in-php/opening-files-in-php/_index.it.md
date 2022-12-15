---
title: Apertura di file in PHP
type: docs
weight: 10
url: /it/net/opening-files-in-php/
---
## **Aspose.Cells - Apri File Excel**
### **Apertura attraverso il percorso**
Basta aprire un file Microsoft Excel facendo riferimento al percorso del file

**Codice PHP**

{{< highlight "php" >}}

         $dataDir = '';

        // Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array($dataDir . '/Book1.xls'));

        $worksheets = $ptr->Get($workbook,"Worksheets",array());

{{< /highlight >}}
## **Scarica il codice in esecuzione**
 Scarica**Apertura File (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
