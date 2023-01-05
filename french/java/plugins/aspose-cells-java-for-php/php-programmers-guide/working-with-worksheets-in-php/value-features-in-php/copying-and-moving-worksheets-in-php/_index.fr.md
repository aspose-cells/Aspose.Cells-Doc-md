---
title: Copier et déplacer des feuilles de calcul en PHP
type: docs
weight: 10
url: /fr/java/copying-and-moving-worksheets-in-php/
---
## **Aspose.Cells - Copier et déplacer des feuilles de travail**
### **Copier des feuilles de calcul dans un classeur**
 Pour copier une feuille de calcul à l'aide de**Aspose.Cells for Java en PHP** , téléphoner à**copy_worksheet** méthode de**copier des feuilles de travail** module. Ci-dessous, vous pouvez voir un exemple de code.

**Code PHP**

{{< highlight "php" >}}

 # Create a Worksheets object with reference to the sheets of the Workbook.

$sheets = $workbook->getWorksheets();

\# Copy data to a new sheet from an existing sheet within the Workbook.

$sheets->addCopy("Sheet1");

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Copy Worksheet.xls");


{{< /highlight >}}
### **Déplacer des feuilles de calcul dans un classeur**
 Pour déplacer une feuille de calcul à l'aide de**Aspose.Cells for Java en PHP** , téléphoner à**move_worksheet** méthode de**copier des feuilles de travail** module. Ci-dessous, vous pouvez voir un exemple de code.

**Code PHP**

{{< highlight "php" >}}

 # Get the first worksheet in the book.

$sheet = $workbook->getWorksheets()->get(0);

\# Move the first sheet to the third position in the workbook.

$sheet->moveTo(2);

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Move Worksheet.xls");

{{< /highlight >}}
## **Télécharger le code d'exécution**
Télécharger**Copier et déplacer des feuilles de travail (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/CopyingAndMovingWorksheets.php)
