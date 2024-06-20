---
title: Arbeitsblätter in PHP schützen
type: docs
weight: 10
url: /de/java/protecting-worksheets-in-php/
---

## **Aspose.Cells - Arbeitsblätter schützen**
Um ein Arbeitsblatt mit **Aspose.Cells Java für PHP** zu schützen, rufen Sie die Methode **protect_worksheet** des Moduls **protection** auf.

**PHP-Code**

{{< highlight php >}}

 //Instantiating a Excel object by excel file path

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
## **Laufenden Code herunterladen**
Laden Sie das **Schützen von Arbeitsblättern (Aspose.Cells)** von einer der unten genannten Social-Coding-Websites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/SecurityFeatures/ProtectingWorksheet.php)
