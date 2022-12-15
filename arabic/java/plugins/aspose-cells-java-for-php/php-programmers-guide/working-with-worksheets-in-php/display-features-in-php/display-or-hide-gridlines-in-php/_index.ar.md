---
title: عرض أو إخفاء خطوط الشبكة في Php
type: docs
weight: 10
url: /ar/java/display-or-hide-gridlines-in-php/
---
## **Aspose.Cells - عرض أو إخفاء خطوط الشبكة**
### **إخفاء خطوط الشبكة**
 لإخفاء ورقة العمل باستخدام**Aspose.Cells Java for PHP** ، مكالمة**displayhidegridlines** وحدة.

**كود PHP**

{{< highlight "php" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

//Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Hiding the grid lines of the first worksheet of the Excel file

$worksheet->setGridlinesVisible(false);

//Saving the modified Excel file in default (that is Excel 2000) format

$workbook->save($dataDir . "output.xls");


{{< /highlight >}}
## **تحميل كود الجري**
تحميل**عرض خطوط الشبكة أو إخفاؤها (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideGridlines.php)
