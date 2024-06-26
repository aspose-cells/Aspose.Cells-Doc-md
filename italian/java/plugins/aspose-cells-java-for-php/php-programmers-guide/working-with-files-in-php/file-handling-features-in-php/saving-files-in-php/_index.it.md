---
title: Salvataggio dei File in PHP
type: docs
weight: 20
url: /it/java/saving-files-in-php/
---

## **Aspose.Cells - Salvataggio dei file**
### **Salvataggio file in una determinata posizione**
Se gli sviluppatori devono salvare i propri file usando **Aspose.Cells Java per PHP** in una posizione di archiviazione specifica, possono semplicemente specificare il nome del file (con il relativo percorso di archiviazione completo) e il formato del file desiderato (utilizzando l'enumerazione **FileFormatType**) durante la chiamata al metodo **save** dell'oggetto **Workbook**.

**Codice PHP**

{{< highlight php >}}

 $fileFormatType = new FileFormatType();

//Creating an Workbook object with an Excel file path

$workbook = new Workbook($dataDir . "book.xls");

//Save in default (Excel2003) format

$workbook->save($dataDir . "book.default.out.xls");

//Save in Excel2003 format

$workbook->save($dataDir . "book.out.xls",$fileFormatType->EXCEL_97_TO_2003);

//Save in Excel2007 xlsx format

$workbook->save($dataDir . "book.out.xlsx", $fileFormatType->XLSX);

//Save in SpreadsheetML format

$workbook->save($dataDir . "book.out.xml", $fileFormatType->EXCEL_2003_XML);

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Salvataggio File (Aspose.Cells)** da uno qualsiasi dei siti di codifica sociale menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/SavingFiles.php)
