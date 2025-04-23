---
title: XLS ve XLSX formatları tarafından desteklenen maksimum satır ve sütun sayısını bulun.
type: docs
weight: 20
url: /tr/net/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **Olası Kullanım Senaryoları**

Excel formatları tarafından desteklenen farklı sayıda satır ve sütun bulunmaktadır. Örneğin, XLS 65536 satır ve 256 sütunu desteklerken, XLSX 1048576 satır ve 16384 sütunu desteklemektedir. Verilen formattaki kaç satır ve sütunun desteklendiğini bilmek isterseniz, [**Workbook.Settings.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow) ve [**Workbook.Settings.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn) özelliklerini kullanabilirsiniz.

## **XLS ve XLSX formatları tarafından desteklenen maksimum satır ve sütun sayısını bulun.**

Aşağıdaki örnek kod, önce XLS ve ardından XLSX formatında çalışbook oluşturur. Oluşturduktan sonra, [**Workbook.Settings.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow) ve [**Workbook.Settings.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn) özelliklerinin değerlerini yazdırır. Referansınız için aşağıdaki kodun konsol çıktısına bakınız.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.cs" >}}

## **Konsol Çıktısı**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
