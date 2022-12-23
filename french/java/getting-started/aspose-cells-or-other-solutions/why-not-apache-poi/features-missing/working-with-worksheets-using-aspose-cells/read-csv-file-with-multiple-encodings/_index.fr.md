---
title: Lire le fichier CSV avec plusieurs encodages
type: docs
weight: 70
url: /fr/java/read-csv-file-with-multiple-encodings/
---
## **Aspose.Cells - Lire le fichier CSV avec plusieurs encodages**
Parfois, votre fichier CSV contient plusieurs encodages (Unicode, ANSI, UTF8, UTF7, etc.). Aspose.Cells vous permet de charger ces fichiers CSV et de les convertir dans d'autres formats, par exemple PDF ou XLSX.

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
## **Télécharger le code d'exécution**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger l'exemple de code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/workbook/ReadingCSVFileWithMultipleEncodings.java)

{{% alert color="primary" %}} 

 Pour plus de détails, visitez[Lecture du fichier CSV avec plusieurs encodages](/cells/fr/java/reading-csv-file-with-multiple-encodings).

{{% /alert %}}
