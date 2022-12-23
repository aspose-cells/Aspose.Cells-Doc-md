---
title: Apertura di file in PHP
type: docs
weight: 10
url: /it/java/opening-files-in-php/
---
## **Aspose.Cells - Semplici modi per aprire file Excel**
### **Apertura attraverso il percorso**
Basta aprire un file Excel Microsoft facendo riferimento al percorso del file

**Codice PHP**

{{< highlight "ruby" >}}

 $dataDir = '';

$workbook1 = new Workbook($dataDir . "Book1.xls");

{{< /highlight >}}
### **Apertura tramite Stream**
A volte, il file Excel che desideri aprire viene archiviato come flusso. In tal caso, utilizzare una versione di overload del metodo Open che accetta l'oggetto Stream che contiene il file Excel per aprire il file.

**Codice PHP**

{{< highlight "ruby" >}}

 $fstream = new FileInputStream($dataDir . "Book2.xls");

//Creating an Workbook object with the stream object

$workbook2 = new Workbook($fstream);

$fstream->close();

{{< /highlight >}}
## **Scarica il codice in esecuzione**
 Scaricamento**Apertura File (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
