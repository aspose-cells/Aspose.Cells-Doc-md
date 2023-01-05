---
title: Php'de Sekmeleri Görüntüle veya Gizle
type: docs
weight: 30
url: /tr/java/display-or-hide-tabs-in-php/
---
## **Aspose.Cells - Sekmeleri Görüntüle veya Gizle**
### **Sekmeleri Gizleme**
 kullanarak sekmeleri gizlemek için**Aspose.Cells Java for PHP** , Arama**sekmeleri göster** modül.

**PHP Kodu**

{{< highlight "php" >}}

 //Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the tabs of the Excel file

$workbook->getSettings()->setShowTabs(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir + "output.xls");

{{< /highlight >}}
## **Çalışan Kodu İndir**
İndirmek**Sekmeleri Gizle veya Görüntüle veya Gizle (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideTabs.php)
