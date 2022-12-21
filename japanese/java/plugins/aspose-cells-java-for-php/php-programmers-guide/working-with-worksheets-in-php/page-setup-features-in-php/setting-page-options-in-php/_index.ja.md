---
title: PHP でのページ オプションの設定
type: docs
weight: 10
url: /ja/java/setting-page-options-in-php/
---
## **Aspose.Cells - ページ オプションの設定**
### **ページの向き**
を使用してページの向きの設定を適用するには**Aspose.Cells Java for PHP**、 電話**page_orientation**方法**ページ設定**モジュール。

**PHPコード**

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
### **スケーリング係数**
を使用してスケーリングを適用するには**Aspose.Cells Java for PHP**、 電話**スケーリング**方法**ページ設定**モジュール。

**PHPコード**

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
## **実行中のコードをダウンロード**
ダウンロード**ページオプションの設定 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/PageSetupFeatures/SettingPageOptions.php)
