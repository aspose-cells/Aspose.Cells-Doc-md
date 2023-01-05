---
title: Dokumenteigenschaften in PHP verwalten
type: docs
weight: 70
url: /de/java/managing-document-properties-in-php/
---
## **Aspose.Cells – Hinzufügen benutzerdefinierter Eigenschaften**
Um benutzerdefinierte Dokumenteigenschaften mit Aspose.Cells Java for PHP hinzuzufügen, rufen Sie an**add_custom_property** Methode der**Dokumentieren** Modul.

**PHP-Code**

{{< highlight "php" >}}

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
## **Laufcode herunterladen**
 Download**Zugriff auf Dokumenteigenschaften (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ManagingDocumentProperties.php)
