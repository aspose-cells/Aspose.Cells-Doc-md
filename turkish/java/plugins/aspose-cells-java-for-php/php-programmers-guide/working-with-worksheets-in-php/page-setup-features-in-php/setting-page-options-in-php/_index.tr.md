---
title: Php'de Sayfa Seçeneklerini Ayarlama
type: docs
weight: 10
url: /tr/java/setting-page-options-in-php/
---
## **Aspose.Cells - Ayar Sayfası Seçenekleri**
### **Sayfa yönlendirmesi**
 kullanarak sayfa yönü ayarlarını uygulamak için**Aspose.Cells Java for PHP** , aramak**Sayfa yönlendirmesi** yöntemi**sayfa ayarı** modül.

**PHP Kodu**

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
### **Ölçekleme faktörü**
 kullanarak ölçekleme uygulamak için**Aspose.Cells Java for PHP** , aramak**ölçekleme** yöntemi**sayfa ayarı** modül.

**PHP Kodu**

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
## **Çalışan Kodu İndir**
İndirmek**Ayar Sayfası Seçenekleri (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/PageSetupFeatures/SettingPageOptions.php)
