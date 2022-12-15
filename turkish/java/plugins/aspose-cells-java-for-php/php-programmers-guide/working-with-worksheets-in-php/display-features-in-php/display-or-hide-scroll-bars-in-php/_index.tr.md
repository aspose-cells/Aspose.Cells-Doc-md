---
title: Php'de Kaydırma Çubuklarını Görüntüleme veya Gizleme
type: docs
weight: 20
url: /tr/java/display-or-hide-scroll-bars-in-php/
---
## **Aspose.Cells - Kaydırma Çubuklarını Görüntüle veya Gizle**
### **Kaydırma Çubuklarını Gizleme**
 kullanarak Kaydırma Çubuklarını gizlemek için**Aspose.Cells Java for PHP** , aramak**kaydırma çubuklarını görüntüle** modül.

**PHP Kodu**

{{< highlight "php" >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the vertical scroll bar of the Excel file

$workbook->getSettings()->setVScrollBarVisible(false);

//Hiding the horizontal scroll bar of the Excel file

$workbook->getSettings()->setHScrollBarVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "output.xls");

{{< /highlight >}}
## **Çalışan Kodu İndir**
İndirmek**Kaydırma Çubuklarını Görüntüle veya Gizle (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideScrollBars.php)
