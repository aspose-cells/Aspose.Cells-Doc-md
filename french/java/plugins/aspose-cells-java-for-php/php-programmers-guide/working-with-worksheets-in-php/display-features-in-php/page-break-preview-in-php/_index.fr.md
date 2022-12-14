---
title: Aperçu des sauts de page en PHP
type: docs
weight: 60
url: /fr/java/page-break-preview-in-php/
---
## **Aspose.Cells - Aperçu des sauts de page**
 Pour définir la feuille de calcul sur l'aperçu des sauts de page à l'aide de**Aspose.Cells Java pour PHP** , invoquez simplement**Aperçu du saut de page** module.

**Code PHP**

{{< highlight "php" >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Adding a new worksheet to the Workbook object

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Displaying the worksheet in page break preview

$worksheet->setPageBreakPreview(true);

//Saving the modified Excel file in default format

$workbook->save($dataDir . "output.xls");

{{< /highlight >}}
## **Télécharger le code d'exécution**
Télécharger**Aperçu des sauts de page (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/PageBreakPreview.php)
