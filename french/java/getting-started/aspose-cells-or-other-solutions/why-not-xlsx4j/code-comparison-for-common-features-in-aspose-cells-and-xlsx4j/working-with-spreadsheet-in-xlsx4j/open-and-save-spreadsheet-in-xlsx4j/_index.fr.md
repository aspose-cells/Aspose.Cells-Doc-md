---
title: Ouvrir et enregistrer la feuille de calcul en xlsx4j
type: docs
weight: 40
url: /fr/java/open-and-save-spreadsheet-in-xlsx4j/
---
## **Aspose.Cells - Ouvrir et enregistrer la feuille de calcul**
Les développeurs utilisent Aspose.Cells pour ouvrir des fichiers à des fins différentes. Par exemple, ouvrez un fichier pour en extraire des données ou utilisez une feuille de calcul de concepteur prédéfinie pour accélérer votre processus de développement. Aspose.Cells permet aux développeurs d'ouvrir différents types de fichiers source. Ces fichiers source peuvent être des rapports Excel Microsoft, des fichiers SpreadsheetML, CSV ou délimités par des tabulations.

**Aspose.Cells**permet aux développeurs de créer des fichiers Excel à partir de zéro à l'aide de son API flexible. Une fois que vous avez créé des fichiers Excel, vous devez également enregistrer votre classeur (fichier). Aspose.Cells fournit une variété de façons d'enregistrer ces fichiers.

**Java**

{{< highlight "java" >}}

 //Creating an Workbook object with an Excel file path

Workbook workbook = new Workbook(dataDir + "pivot.xlsm");

//Saving the Excel file

workbook.save(dataDir + "pivot-rtt-Aspose.xlsm");

{{< /highlight >}}
## **xlsx4j - Ouvrir et enregistrer la feuille de calcul**
L'exemple ci-dessous montre comment ouvrir et enregistrer des feuilles de calcul tout en utilisant xlsx4j.

**Java**

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
## **Télécharger le code d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Télécharger l'exemple de code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/opensavespreadsheet)
