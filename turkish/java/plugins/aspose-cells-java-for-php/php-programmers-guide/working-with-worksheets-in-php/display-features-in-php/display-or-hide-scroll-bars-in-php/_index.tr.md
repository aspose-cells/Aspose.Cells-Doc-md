---
title: Php de Kaydırma Çubuklarını Göster veya Gizle
type: docs
weight: 20
url: /tr/java/display-or-hide-scroll-bars-in-php/
---

## **Aspose.Cells - Kaydırma Çubuklarını Göster veya Gizle**
### **Kaydırma çubuklarını gizleme**
Aspose.Cells Java for PHP kullanarak kaydırma çubuklarını gizlemek için **displayhidescrollbars** modülünü çağırın.

PHP Kodu

{{< highlight php >}}

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
**Aspose.Cells** ile **Kaydırma Çubuklarını Göster veya Gizle**'yı aşağıda belirtilen sosyal kodlama sitelerinden herhangi birinden indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideScrollBars.php)
