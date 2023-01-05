---
title: Gestión de propiedades de documentos en PHP
type: docs
weight: 70
url: /es/java/managing-document-properties-in-php/
---
## **Aspose.Cells - Adición de propiedades personalizadas**
Para agregar propiedades de documentos personalizados usando Aspose.Cells Java for PHP, llame**agregar_propiedad_personalizada** metodo de la**Documento** módulo.

**Código PHP**

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
## **Descargar código de ejecución**
 Descargar**Acceso a las propiedades del documento (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ManagingDocumentProperties.php)
