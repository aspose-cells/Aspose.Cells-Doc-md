---
title: Salvataggio dei File in PHP
type: docs
weight: 20
url: /it/net/saving-files-in-php/
---

## **Aspose.Cells - Salva File Excel**
### **Apertura attraverso percorso**
Salvare un file Microsoft Excel facendo riferimento al percorso del file

**Codice PHP**

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
## **Scarica il codice in esecuzione**
Scarica **Salvataggio File (Aspose.Cells)** da uno qualsiasi dei siti di codifica sociale menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/SavingFiles.php)
