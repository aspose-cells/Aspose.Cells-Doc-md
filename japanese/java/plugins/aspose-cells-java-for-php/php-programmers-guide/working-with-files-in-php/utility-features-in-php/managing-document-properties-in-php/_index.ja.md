---
title: PHP でのドキュメント プロパティの管理
type: docs
weight: 70
url: /ja/java/managing-document-properties-in-php/
---
## **Aspose.Cells - カスタム プロパティの追加**
Aspose.Cells Java for PHP を使用してカスタム ドキュメント プロパティを追加するには、次のように呼び出します。**add_custom_property**の方法**書類**モジュール。

**PHP コード**

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
## **実行中のコードをダウンロード**
ダウンロード**ドキュメント プロパティへのアクセス (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ManagingDocumentProperties.php)
