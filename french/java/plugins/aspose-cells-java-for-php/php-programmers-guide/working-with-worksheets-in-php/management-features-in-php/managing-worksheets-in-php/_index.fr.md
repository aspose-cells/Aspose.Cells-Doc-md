---
title: Gestion des feuilles de calcul en Php
type: docs
weight: 10
url: /fr/java/managing-worksheets-in-php/
---

## **Aspose.Cells - Gestion des feuilles de calcul**
### **Ajout de feuilles de calcul à un nouveau fichier Excel**
Pour ajouter une feuille de calcul à un nouveau fichier Excel en utilisant **Aspose.Cells Java for PHP**, il suffit d'appeler la méthode **add_worksheet** du module **ManagingWorksheets**.

**Code PHP**

{{< highlight php >}}

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
### **Suppression des feuilles de calcul en utilisant le nom de la feuille**
Pour supprimer une feuille de calcul par nom de feuille en utilisant **Aspose.Cells Java for PHP**, il suffit d'appeler la méthode **remove_worksheet_by_name** du module **ManagingWorksheets**.

**Code PHP**

{{< highlight php >}}

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
### **Suppression des feuilles de calcul en utilisant l'indice de la feuille**
Pour supprimer une feuille de calcul par index de feuille en utilisant **Aspose.Cells Java for PHP**, il suffit d'appeler la méthode **remove_worksheet_by_index** du module **ManagingWorksheets**.

**Code PHP**

{{< highlight php >}}

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
## **Télécharger le code en cours d'exécution**
Téléchargez **Managing Worksheets (Aspose.Cells)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets)
