##Managing Document Properties in PHP
## **Aspose.Cells - Adding Custom Properties**
To add custom document properties using Aspose.Cells Java for PHP, call **add_custom_property** method of the **Document** module.
**PHP Code**
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
## **Download Running Code**
Download **Accessing Document Properties (Aspose.Cells)** from any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ManagingDocumentProperties.php)
