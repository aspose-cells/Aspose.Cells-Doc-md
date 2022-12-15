---
title: Mostra o nascondi le schede in Php
type: docs
weight: 30
url: /it/java/display-or-hide-tabs-in-php/
---
## **Aspose.Cells - Mostra o nascondi schede**
### **Nascondere le schede**
 Per nascondere le schede utilizzando**Aspose.Cells Giava for PHP** , chiamata**displayhidetabs** modulo.

**Codice PHP**

{{< highlight "php" >}}

 //Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the tabs of the Excel file

$workbook->getSettings()->setShowTabs(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir + "output.xls");

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica**Nascondi o mostra o nascondi schede (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideTabs.php)
