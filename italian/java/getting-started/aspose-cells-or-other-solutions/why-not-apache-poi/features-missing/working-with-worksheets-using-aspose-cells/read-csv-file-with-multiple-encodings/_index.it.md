---
title: Leggi il file CSV con più codifiche
type: docs
weight: 70
url: /it/java/read-csv-file-with-multiple-encodings/
---
## **Aspose.Cells - Leggi file CSV con codifiche multiple**
volte, il tuo file CSV contiene più codifiche (Unicode, ANSI, UTF8, UTF7 ecc.). Aspose.Cells consente di caricare tali file CSV e di convertirli in altri formati, ad esempio PDF o XLSX.

**Java**

{{< highlight "java" >}}

 //Set Multi Encoded Property to True

TxtLoadOptions options = new TxtLoadOptions();

options.setMultiEncoded(true);

//Load the CSV file into Workbook

Workbook workbook = new Workbook(dataDir + "MultiEncoded.csv", options);

//Save it in XLSX format

workbook.save(dataDir + "EncodedNewFile_Out.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
## **Scarica il codice in esecuzione**

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/workbook/ReadingCSVFileWithMultipleEncodings.java)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Lettura del file CSV con codifiche multiple](/cells/it/java/reading-csv-file-with-multiple-encodings).

{{% /alert %}}
