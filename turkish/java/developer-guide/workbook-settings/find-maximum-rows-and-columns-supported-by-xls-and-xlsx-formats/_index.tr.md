---
title: XLS ve XLSX formatları tarafından desteklenen maksimum satır ve sütun sayısını bulun.
type: docs
weight: 60
url: /tr/java/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **Olası Kullanım Senaryoları**
Excel formatları tarafından desteklenen farklı satır ve sütun sayıları bulunmaktadır. Örneğin, XLS 65536 satır ve 256 sütunu desteklerken, XLSX 1048576 satır ve 16384 sütunu destekler. Verilen formattan kaç satır ve sütunun desteklendiğini öğrenmek isterseniz, [Workbook.Settings.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow) ve [Workbook.Settings.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn) özelliklerini kullanabilirsiniz.
## **XLS ve XLSX formatları tarafından desteklenen maksimum satır ve sütun sayısını bulun.**
Aşağıdaki örnek kod önce XLS ve ardından XLSX formatında bir çalışma kitabı oluşturur. Oluşturduktan sonra, [Workbook.Settings.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow) ve [Workbook.Settings.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn) özelliklerinin değerlerini yazdırır. Referans için aşağıdaki kodun konsol çıktısına bakınız.
## **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.java" >}}

Konsol Çıktısı

{{< highlight java >}}

 Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
