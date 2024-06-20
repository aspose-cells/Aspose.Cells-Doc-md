---
title: Gestione delle proprietà del documento in PHP
type: docs
weight: 70
url: /it/java/managing-document-properties-in-php/
---

## **Aspose.Cells - Aggiunta di proprietà personalizzate**
Per aggiungere proprietà personalizzate del documento utilizzando Aspose.Cells Java per PHP, chiamare il metodo **add_custom_property** del modulo **Document**.

**Codice PHP**

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
## **Scarica il codice in esecuzione**
Scarica **Accesso alle proprietà del documento (Aspose.Cells)** da uno dei siti di codice sociale di seguito elencati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ManagingDocumentProperties.php)
