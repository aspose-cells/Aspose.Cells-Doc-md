---
title: Gestion des feuilles de travail en PHP
type: docs
weight: 10
url: /fr/java/managing-worksheets-in-php/
---
## **Aspose.Cells - Gestion des feuilles de travail**
### **Ajout de feuilles de calcul à un nouveau fichier Excel**
 Pour ajouter une feuille de calcul à un nouveau fichier Excel à l'aide**Aspose.Cells Java for PHP** , il suffit d'appeler**add_worksheet** méthode de**Gestion des feuilles de travail** module.

**Code PHP**

{{< highlight "php" >}}

 //Instantiating a Workbook object

$workbook = new Workbook();

//Adding a new worksheet to the Workbook object

$worksheets = $workbook->getWorksheets();

$sheetIndex = $worksheets->add();

$worksheet = $worksheets->get($sheetIndex);

//Setting the name of the newly added worksheet

$worksheet->setName("My Worksheet");

//Saving the Excel file

$workbook->save($dataDir . "book.out.xls");

{{< /highlight >}}
### **Suppression de feuilles de calcul à l'aide du nom de la feuille**
 Pour supprimer une feuille de calcul par nom de feuille à l'aide de**Aspose.Cells Java for PHP** , il suffit d'appeler**remove_worksheet_by_name** méthode de**Gestion des feuilles de travail** module.

**Code PHP**

{{< highlight "php" >}}

 //Creating a file stream containing the Excel file to be opened

$fstream = new FileInputStream($dataDir . "book.xls");

//Instantiating a Workbook object with the stream

$workbook = new Workbook($fstream);

//Removing a worksheet using its sheet name

$workbook->getWorksheets()->removeAt("Sheet1");

//Saving the Excel file

$workbook->save($dataDir . "book.out.xls");

//Closing the file stream to free all resources

$fstream->close();

{{< /highlight >}}
### **Suppression de feuilles de calcul à l'aide de l'index des feuilles**
 Pour supprimer une feuille de calcul par index de feuille à l'aide de**Aspose.Cells Java for PHP** , il suffit d'appeler**remove_worksheet_by_index** méthode de**Gestion des feuilles de travail** module.

**Code PHP**

{{< highlight "php" >}}

 //Creating a file stream containing the Excel file to be opened

$fstream=new FileInputStream($dataDir . "book.xls");

//Instantiating a Workbook object with the stream

$workbook = new Workbook($fstream);

//Removing a worksheet using its sheet index

$workbook->getWorksheets()->removeAt(0);

//Saving the Excel file

$workbook->save($dataDir . "book.out.xls");

//Closing the file stream to free all resources

$fstream->close();

{{< /highlight >}}
## **Télécharger le code d'exécution**
Télécharger**Gestion des feuilles de travail (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets)
