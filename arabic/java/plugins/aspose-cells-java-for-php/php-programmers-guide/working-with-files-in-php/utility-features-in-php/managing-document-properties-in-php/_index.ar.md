---
title: إدارة خصائص المستند في PHP
type: docs
weight: 70
url: /ar/java/managing-document-properties-in-php/
---

## **Aspose.Cells - إضافة خصائص مخصصة**
لإضافة خصائص المستند المخصصة باستخدام Aspose.Cells Java for PHP ، اتصل بطريقة **add_custom_property** من وحدة **Document**.

**كود PHP**

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
## **تحميل رمز التشغيل**
قم بتنزيل **الوصول إلى خصائص الوثيقة (Aspose.Cells)** من أي من المواقع المشفرة المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ManagingDocumentProperties.php)
