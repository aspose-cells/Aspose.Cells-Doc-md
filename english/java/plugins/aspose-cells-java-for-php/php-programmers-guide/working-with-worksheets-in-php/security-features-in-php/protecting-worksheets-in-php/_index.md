---
title: Protecting Worksheets in PHP
type: docs
weight: 10
url: /java/protecting-worksheets-in-php/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Protecting Worksheets**
To protect a worksheet using **Aspose.Cells for Java in PHP**, call the **protect_worksheet** method of the **protection** module.

**PHP Code**

{{< highlight php >}}

 //Instantiating an Excel object by Excel file path

$excel = new Workbook($dataDir . "book1.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $excel->getWorksheets();

$worksheet = $worksheets->get(0);

$protection = $worksheet->getProtection();

//The following 3 methods are only for Excel 2000 and earlier formats

$protection->setAllowEditingContent(false);

$protection->setAllowEditingObject(false);

$protection->setAllowEditingScenario(false);

//Protects the first worksheet with a password "1234"

$protection->setPassword("1234");

//Saving the modified Excel file in default format

$excel->save($dataDir . "output.xls");    

{{< /highlight >}}

## **Download Running Code**
Download **Protecting Worksheets (Aspose.Cells)** from any of the social coding sites listed below:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/SecurityFeatures/ProtectingWorksheet.php)
