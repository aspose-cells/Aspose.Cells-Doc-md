---
title: Impostazione delle opzioni della pagina in Php
type: docs
weight: 10
url: /it/java/setting-page-options-in-php/
---
## **Aspose.Cells - Impostazione Opzioni Pagina**
### **Orientamento della pagina**
 Per applicare le impostazioni di orientamento della pagina utilizzando**Aspose.Cells Java for PHP** , chiamata**orientamento_pagina** metodo di**impostazione della pagina** modulo.

**Codice PHP**

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
### **Fattore di scala**
 Per applicare il ridimensionamento utilizzando**Aspose.Cells Java for PHP** , chiamata**ridimensionamento** metodo di**impostazione della pagina** modulo.

**Codice PHP**

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
## **Scarica il codice in esecuzione**
Scaricamento**Impostazione opzioni pagina (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/PageSetupFeatures/SettingPageOptions.php)
