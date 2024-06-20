---
title: PHP de Sayfa Kesmelerini Yönetme
type: docs
weight: 20
url: /tr/java/managing-page-breaks-in-php/
---

## **Aspose.Cells - Sayfa Kesmelerini Yönetme**
### **Sayfa Kesmeleri Eklemek**
**Aspose.Cells Java for PHP** kullanarak sayfa sonları eklemek için, **sayfaati** modülünün **add_page_breaks** yöntemini kullanın. Aşağıda kod örneğini görebilirsiniz.

PHP Kodu

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
### **Tüm Sayfa Kesmelerini Temizleme**
**Aspose.Cells Java for PHP** kullanarak tüm sayfa sonlarını temizlemek için, **sayfaati** modülünün **clear_all_page_breaks** yöntemini çağırın. Aşağıda kod örneğini görebilirsiniz.

PHP Kodu

{{< highlight php >}}

 $workbook->getWorksheets()->get(0)->getHorizontalPageBreaks()->clear();

$workbook->getWorksheets()->get(0)->getVerticalPageBreaks()->clear();

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Clear All Page Breaks.xls");

{{< /highlight >}}
### **Belirli Sayfa Kesmelerini Kaldırma**
**Aspose.Cells Java for PHP** kullanarak belirli sayfa sonunu kaldırmak için, **sayfaati** modülünün **remove_page_break** yöntemini çağırın. Aşağıda kod örneğini görebilirsiniz.

PHP Kodu

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
## **Çalışan Kodu İndir**
Aşağıdaki sosyal kodlama sitelerinden herhangi birinden **Sayfa Kesmelerini Yönetme (Aspose.Cells)** indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/ManagingPageBreaks.php)
