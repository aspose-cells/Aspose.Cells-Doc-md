---
title: Anzeigen oder Ausblenden von Registerkarten in Php
type: docs
weight: 30
url: /de/java/display-or-hide-tabs-in-php/
---

## **Aspose.Cells - Anzeigen oder Ausblenden von Registerkarten**
### **Registerkarten ausblenden**
Um Registerkarten in **Aspose.Cells Java für PHP** auszublenden, rufen Sie das Modul **displayhidetabs** auf.

**PHP-Code**

{{< highlight php >}}

 //Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the tabs of the Excel file

$workbook->getSettings()->setShowTabs(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir + "output.xls");

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie **Registerkarten ausblenden oder anzeigen oder ausblenden (Aspose.Cells)** von einer der unten aufgeführten Social-Coding-Sites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideTabs.php)
