---
title: Ajuster les options de page en Php
type: docs
weight: 10
url: /ar/java/setting-page-options-in-php/
---

## **Aspose.Cells - ضبط خيارات الصفحة**
### **اتجاه الصفحة**
Pour appliquer les paramètres d'orientation de page en utilisant **Aspose.Cells Java pour PHP**, appelez simplement la méthode **page_orientation** du module **pagesetup**.

**كود PHP**

{{< highlight php >}}

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
### **عامل التحليل**
Pour appliquer la mise à l'échelle en utilisant **Aspose.Cells Java pour PHP**, appelez simplement la méthode **scaling** du module **pagesetup**.

**كود PHP**

{{< highlight php >}}

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
## **تحميل رمز التشغيل**
قم بتنزيل  **ضبط خيارات الصفحة (Aspose.Cells)**  من أي من مواقع التعاون البرمجي الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/PageSetupFeatures/SettingPageOptions.php)
