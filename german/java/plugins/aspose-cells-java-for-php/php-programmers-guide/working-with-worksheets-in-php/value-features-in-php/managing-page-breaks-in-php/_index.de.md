---
title: Verwalten von Seitenumbrüchen in Php
type: docs
weight: 20
url: /de/java/managing-page-breaks-in-php/
---
## **Aspose.Cells – Verwalten von Seitenumbrüchen**
### **Seitenumbrüche hinzufügen**
 So fügen Sie Seitenumbrüche hinzu mit**Aspose.Cells Java for PHP** , Anruf**add_page_breaks** Methode von**Seitenumbrüche** Modul. Unten sehen Sie ein Codebeispiel.

**PHP-Code**

{{< highlight "php" >}}

 $worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$h_page_breaks = $worksheet->getHorizontalPageBreaks();

$h_page_breaks->add("Y30");

$v_page_breaks = $worksheet->getVerticalPageBreaks();

$v_page_breaks->add("Y30");

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Add Page Breaks.xls");   

{{< /highlight >}}
### **Löschen aller Seitenumbrüche**
 Um alle Seitenumbrüche zu löschen, verwenden Sie**Aspose.Cells Java for PHP** , Anruf**clear_all_page_breaks** Methode von**Seitenumbrüche** Modul. Unten sehen Sie ein Codebeispiel.

**PHP-Code**

{{< highlight "php" >}}

 $workbook->getWorksheets()->get(0)->getHorizontalPageBreaks()->clear();

$workbook->getWorksheets()->get(0)->getVerticalPageBreaks()->clear();

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Clear All Page Breaks.xls");

{{< /highlight >}}
### **Entfernen eines bestimmten Seitenumbruchs**
 So entfernen Sie einen bestimmten Seitenumbruch mit**Aspose.Cells Java for PHP** , Anruf**remove_page_break** Methode von**Seitenumbrüche** Modul. Unten sehen Sie ein Codebeispiel.

**PHP-Code**

{{< highlight "php" >}}

 $worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$h_page_breaks = $worksheet->getHorizontalPageBreaks();

$h_page_breaks->removeAt(0);

$v_page_breaks = $worksheet->getVerticalPageBreaks();

$v_page_breaks->removeAt(0);

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Remove Page Break.xls");

{{< /highlight >}}
## **Laufcode herunterladen**
Download**Seitenumbrüche verwalten (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/ManagingPageBreaks.php)
