---
title: Apertura dei File in PHP
type: docs
weight: 10
url: /it/java/opening-files-in-php/
---

## **Aspose.Cells - Modi semplici per aprire file Excel**
### **Apertura attraverso percorso**
Apri semplicemente un file Microsoft Excel facendo riferimento al percorso del file

**Codice PHP**

{{< highlight ruby >}}

 $dataDir = '';

$workbook1 = new Workbook($dataDir . "Book1.xls");

{{< /highlight >}}
### **Apertura tramite flusso**
A volte, il file Excel che si desidera aprire è memorizzato come stream. In tal caso, utilizzare una versione sovraccaricata del metodo Open che prende l'oggetto Stream che contiene il file Excel per aprire il file.

**Codice PHP**

{{< highlight ruby >}}

 $fstream = new FileInputStream($dataDir . "Book2.xls");

//Creating an Workbook object with the stream object

$workbook2 = new Workbook($fstream);

$fstream->close();

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Apertura File (Aspose.Cells)** da uno qualsiasi dei siti di codifica sociale menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
