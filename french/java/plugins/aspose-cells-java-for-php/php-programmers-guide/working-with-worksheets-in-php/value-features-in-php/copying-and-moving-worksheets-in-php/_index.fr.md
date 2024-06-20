---
title: Copier et déplacer des feuilles de calcul en Php
type: docs
weight: 10
url: /fr/java/copying-and-moving-worksheets-in-php/
---

## **Aspose.Cells - Copier et déplacer des feuilles de calcul**
### **Copier des feuilles de calcul dans un classeur**
Pour copier une feuille de calcul avec **Aspose.Cells for Java en PHP**, appelez la méthode **copy_worksheet** du module **copyworksheets**. Vous pouvez voir ci-dessous un exemple de code.

**Code PHP**

{{< highlight php >}}

 # Create a Worksheets object with reference to the sheets of the Workbook.

$sheets = $workbook->getWorksheets();

\# Copy data to a new sheet from an existing sheet within the Workbook.

$sheets->addCopy("Sheet1");

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Copy Worksheet.xls");


{{< /highlight >}}
### **Déplacer des feuilles de calcul au sein d'un classeur**
Pour déplacer une feuille de calcul avec **Aspose.Cells for Java en PHP**, appelez la méthode **move_worksheet** du module **copyworksheets**. Vous pouvez voir ci-dessous un exemple de code.

**Code PHP**

{{< highlight php >}}

 # Get the first worksheet in the book.

$sheet = $workbook->getWorksheets()->get(0);

\# Move the first sheet to the third position in the workbook.

$sheet->moveTo(2);

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Move Worksheet.xls");

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Copier et déplacer des feuilles de calcul (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/CopyingAndMovingWorksheets.php)
