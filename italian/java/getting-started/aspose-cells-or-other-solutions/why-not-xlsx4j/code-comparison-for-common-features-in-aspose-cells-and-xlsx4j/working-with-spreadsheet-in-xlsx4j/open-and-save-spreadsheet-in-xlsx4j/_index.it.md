---
title: Apri e salva foglio di calcolo in xlsx4j
type: docs
weight: 40
url: /it/java/open-and-save-spreadsheet-in-xlsx4j/
---
## **Aspose.Cells - Apri e salva foglio elettronico**
Gli sviluppatori utilizzano Aspose.Cells per aprire file per scopi diversi. Ad esempio, apri un file per recuperare i dati da esso o utilizza un file di foglio di calcolo predefinito per designer per velocizzare il processo di sviluppo. Aspose.Cells consente agli sviluppatori di aprire diversi tipi di file sorgente. Questi file di origine possono essere report Microsoft Excel, SpreadsheetML, CSV o file delimitati da tabulazioni.

**Aspose.Cells**consente agli sviluppatori di creare file Excel da zero utilizzando la sua API flessibile. Una volta creati i file Excel, dovrai anche salvare la tua cartella di lavoro (file). Aspose.Cells fornisce una varietà di modi per salvare questi file.

**Giava**

{{< highlight "java" >}}

 //Creating an Workbook object with an Excel file path

Workbook workbook = new Workbook(dataDir + "pivot.xlsm");

//Saving the Excel file

workbook.save(dataDir + "pivot-rtt-Aspose.xlsm");

{{< /highlight >}}
## **xlsx4j - Apri e salva foglio di calcolo**
L'esempio seguente mostra come aprire e salvare fogli di calcolo durante l'utilizzo di xlsx4j.

**Giava**

{{< highlight "java" >}}

 String inputfilepath  = dataDir + "pivot.xlsm";

boolean save = true;

String outputfilepath = dataDir + "pivot-rtt-xlsx4j.xlsm";

// Open a document from the file system

// 1. Load the Package

OpcPackage pkg = OpcPackage.load(new java.io.File(inputfilepath));

// Save it

if (save) {

    SaveToZipFile saver = new SaveToZipFile(pkg);

    saver.save(outputfilepath);

}

{{< /highlight >}}
## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/opensavespreadsheet)
