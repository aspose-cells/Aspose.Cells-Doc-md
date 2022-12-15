---
title: Registerkarten in Php anzeigen oder ausblenden
type: docs
weight: 30
url: /de/java/display-or-hide-tabs-in-php/
---
## **Aspose.Cells – Registerkarten anzeigen oder ausblenden**
### **Registerkarten ausblenden**
 Tabs ausblenden mit**Aspose.Cells Java for PHP** , Anruf**Tabs ausblenden** Modul.

**PHP-Code**

{{< highlight "php" >}}

 //Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the tabs of the Excel file

$workbook->getSettings()->setShowTabs(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir + "output.xls");

{{< /highlight >}}
## **Laufcode herunterladen**
Download**Registerkarten ausblenden oder anzeigen oder ausblenden (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideTabs.php)
