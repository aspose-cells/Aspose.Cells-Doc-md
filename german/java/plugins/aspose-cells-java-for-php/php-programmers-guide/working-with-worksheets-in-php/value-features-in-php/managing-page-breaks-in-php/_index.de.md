---
title: Seitenumbrüche in PHP verwalten
type: docs
weight: 20
url: /de/java/managing-page-breaks-in-php/
---

## **Aspose.Cells - Seitenumbrüche verwalten**
### **Seitenumbrüche hinzufügen**
Um Seitenumbrüche mit **Aspose.Cells Java für PHP** hinzuzufügen, rufen Sie die Methode **add_page_breaks** des Moduls **pagebreaks** auf. Nachfolgend finden Sie ein Beispiel für den Code.

**PHP-Code**

{{< highlight php >}}

 $worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$h_page_breaks = $worksheet->getHorizontalPageBreaks();

$h_page_breaks->add("Y30");

$v_page_breaks = $worksheet->getVerticalPageBreaks();

$v_page_breaks->add("Y30");

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Add Page Breaks.xls");   

{{< /highlight >}}
### **Alle Seitenumbrüche löschen**
Um alle Seitenumbrüche mit **Aspose.Cells Java für PHP** zu löschen, rufen Sie die Methode **clear_all_page_breaks** des Moduls **pagebreaks** auf. Nachfolgend finden Sie ein Beispiel für den Code.

**PHP-Code**

{{< highlight php >}}

 $workbook->getWorksheets()->get(0)->getHorizontalPageBreaks()->clear();

$workbook->getWorksheets()->get(0)->getVerticalPageBreaks()->clear();

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Clear All Page Breaks.xls");

{{< /highlight >}}
### **Bestimmten Seitenumbruch entfernen**
Um einen bestimmten Seitenumbruch mit **Aspose.Cells Java für PHP** zu entfernen, rufen Sie die Methode **remove_page_break** des Moduls **pagebreaks** auf. Nachfolgend finden Sie ein Beispiel für den Code.

**PHP-Code**

{{< highlight php >}}

 $worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$h_page_breaks = $worksheet->getHorizontalPageBreaks();

$h_page_breaks->removeAt(0);

$v_page_breaks = $worksheet->getVerticalPageBreaks();

$v_page_breaks->removeAt(0);

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Remove Page Break.xls");

{{< /highlight >}}
## **Laufenden Code herunterladen**
**Seitenumbrüche verwalten (Aspose.Cells)** von einer der unten genannten Plattformen für soziale Programmierung herunterladen:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/ManagingPageBreaks.php)
