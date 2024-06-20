---
title: Php de Sekmeleri Göster veya Gizle
type: docs
weight: 30
url: /tr/java/display-or-hide-tabs-in-php/
---

## **Aspose.Cells - Sekmeleri Göster veya Gizle**
### **Sekmeleri Gizleme**
Aspose.Cells Java for PHP kullanarak sekmeleri gizlemek için **displayhidetabs** modülünü çağırın.

PHP Kodu

{{< highlight php >}}

 //Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the tabs of the Excel file

$workbook->getSettings()->setShowTabs(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir + "output.xls");

{{< /highlight >}}
## **Çalışan Kodu İndir**
Herhangi bir sosyal kodlama sitesinden **Aspose.Cells** ile Sekmeleri Gizle veya Göster'i indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideTabs.php)
