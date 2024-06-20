---
title: إخفاء أو عرض ورقة عمل في PHP
type: docs
weight: 50
url: /ar/java/hide-or-unhide-a-worksheet-in-php/
---

## **Aspose.Cells - إخفاء أو إظهار ورقة عمل**
### **إخفاء ورقة عمل**
لإخفاء ورقة العمل باستخدام Aspose.Cells Java لـ PHP ، اُستدعي وحدة **hideunhideworksheet**.

**كود PHP**

{{< highlight php >}}

 //Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Hiding the first worksheet of the Excel file

$worksheet->setVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "output.xls");


{{< /highlight >}}
## **تحميل رمز التشغيل**
تنزيل **إخفاء أو إظهار ورقة عمل (Aspose.Cells)** من أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/HideUnhideWorksheet.php)
