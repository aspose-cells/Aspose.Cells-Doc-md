---
title: Gestion des propriétés du document en PHP
type: docs
weight: 70
url: /fr/java/managing-document-properties-in-php/
---

## **Aspose.Cells - Ajout de propriétés personnalisées**
Pour ajouter des propriétés de document personnalisées à l'aide de Aspose.Cells Java pour PHP, appelez la méthode **add_custom_property** du module **Document**.

**Code PHP**

{{< highlight php >}}

 //Instantiate a Workbook object by excel file path

$workbook = new Workbook($dataDir . "Book1.xls");

//Retrieve a list of all custom document properties of the Excel file

$customProperties = $workbook->getWorksheets()->getCustomDocumentProperties();

//Accessing a custom document property by using the property index

$customProperty1 = $customProperties->get(3);

//Accessing a custom document property by using the property name

$customProperty2 = $customProperties->get("Owner");


//Adding a custom document property to the Excel file

$publisher = $customProperties->add("Publisher", "Aspose");

//Save the file

$workbook->save($dataDir . "Test_Workbook.xls");

//Removing a custom document property

$customProperties->remove("Publisher");

//Save the file

$workbook->save($dataDir . "Test_Workbook_RemovedProperty.xls");

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Accéder aux propriétés du document (Aspose.Cells)** sur l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ManagingDocumentProperties.php)
