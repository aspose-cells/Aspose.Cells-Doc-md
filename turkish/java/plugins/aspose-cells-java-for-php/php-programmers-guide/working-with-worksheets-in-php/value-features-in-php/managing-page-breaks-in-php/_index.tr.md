---
title: Php'de Sayfa Sonlarını Yönetme
type: docs
weight: 20
url: /tr/java/managing-page-breaks-in-php/
---
## **Aspose.Cells - Sayfa Sonlarını Yönetme**
### **Sayfa Sonları Ekleme**
 kullanarak sayfa sonları eklemek için**PHP için Aspose.Cells Java** , aramak**add_page_breaks** yöntemi**sayfa sonları** modül. Aşağıda kod örneğini görebilirsiniz.

**PHP Kodu**

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
### **Tüm Sayfa Sonlarını Temizleme**
 kullanarak tüm sayfa sonlarını temizlemek için**PHP için Aspose.Cells Java** , aramak**clear_all_page_breaks** yöntemi**sayfa sonları** modül. Aşağıda kod örneğini görebilirsiniz.

**PHP Kodu**

{{< highlight "php" >}}

 $workbook->getWorksheets()->get(0)->getHorizontalPageBreaks()->clear();

$workbook->getWorksheets()->get(0)->getVerticalPageBreaks()->clear();

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Clear All Page Breaks.xls");

{{< /highlight >}}
### **Belirli Sayfa Sonunu Kaldırma**
 Kullanarak belirli sayfa sonunu kaldırmak için**PHP için Aspose.Cells Java** , aramak**remove_page_break** yöntemi**sayfa sonları** modül. Aşağıda kod örneğini görebilirsiniz.

**PHP Kodu**

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
## **Çalışan Kodu İndir**
İndirmek**Sayfa Sonlarını Yönetme (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/ManagingPageBreaks.php)
