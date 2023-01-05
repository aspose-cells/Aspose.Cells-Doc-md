---
title: 在 PHP 中管理文档属性
type: docs
weight: 70
url: /zh/java/managing-document-properties-in-php/
---
## **Aspose.Cells - 添加自定义属性**
要使用 Aspose.Cells Java for PHP 添加自定义文档属性，请调用**添加自定义属性**的方法**文档**模块。

**PHP代码**

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
## **下载运行代码**
下载**访问文档属性 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ManagingDocumentProperties.php)
