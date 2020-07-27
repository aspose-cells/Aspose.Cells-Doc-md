+++
title = "Setting Page Options in Php" 
description = "" 
weight = 24859 
+++

Aspose.Cells for Java : Setting Page Options in Php  

# Aspose.Cells for Java : Setting Page Options in Php


## Aspose.Cells - Setting Page Options

##### Page Orientation

To apply page orientation settings using **Aspose.Cells Java for PHP**, call **page\_orientation** method of **pagesetup** module.

**PHP Code**

{{< code lang="cs" >}}
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
{{< /code >}}

##### Scaling Factor

To apply scaling using **Aspose.Cells Java for PHP**, call **scaling** method of **pagesetup** module.

**PHP Code**

{{< code lang="cs" >}}
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

{{< /code >}}

## Download Running Code

Download **Setting Page Options (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/PageSetupFeatures/SettingPageOptions.php)

