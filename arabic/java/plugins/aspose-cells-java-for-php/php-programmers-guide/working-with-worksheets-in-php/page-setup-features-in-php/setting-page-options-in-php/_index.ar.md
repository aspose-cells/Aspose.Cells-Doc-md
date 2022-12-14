---
title: تعيين خيارات الصفحة في Php
type: docs
weight: 10
url: /ar/java/setting-page-options-in-php/
---
## **Aspose.Cells - ضبط خيارات الصفحة**
### **اتجاه الصفحة**
 لتطبيق إعدادات اتجاه الصفحة باستخدام**Aspose.Cells Java لـ PHP** ، مكالمة**اتجاه الصفحة** طريقة**اعداد الصفحة** وحدة.

**كود PHP**

{{< highlight "php" >}}

 public static function page_orientation($dataDir=null)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook();

    # Accessing the first worksheet in the Excel file

    $worksheets = $workbook->getWorksheets();

    $sheet_index = $worksheets->add();

    $sheet = $worksheets->get($sheet_index);

    # Setting the orientation to Portrait

    $page_setup = $sheet->getPageSetup();

    $page_orientation_type = new PageOrientationType();

    $page_setup->setOrientation($page_orientation_type->PORTRAIT);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Page Orientation.xls");

    print "Set page orientation, please check the output file." . PHP_EOL;

}

{{< /highlight >}}
### **عامل التحجيم**
 لتطبيق التحجيم باستخدام**Aspose.Cells Java لـ PHP** ، مكالمة**التحجيم** طريقة**اعداد الصفحة** وحدة.

**كود PHP**

{{< highlight "php" >}}

 public static function scaling($dataDir=null)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheets = $workbook->getWorksheets();

    $sheet_index = $worksheets->add();

    $sheet = $worksheets->get($sheet_index);

    # Setting the scaling factor to 100

    $page_setup = $sheet->getPageSetup();

    $page_setup->setZoom(100);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Scaling.xls");

    print "Set scaling, please check the output file." . PHP_EOL;

}


{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
تحميل**ضبط خيارات الصفحة (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/PageSetupFeatures/SettingPageOptions.php)
