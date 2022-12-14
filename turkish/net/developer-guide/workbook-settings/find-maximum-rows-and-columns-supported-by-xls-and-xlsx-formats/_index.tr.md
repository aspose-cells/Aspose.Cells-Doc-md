---
title: XLS ve XLSX biçimleri tarafından desteklenen Maksimum Satır ve Sütunları Bulun
type: docs
weight: 20
url: /tr/net/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---
## **Olası Kullanım Senaryoları**

Excel biçimleri tarafından desteklenen farklı sayıda satır ve sütun vardır. Örneğin, XLS 65536 satır ve 256 sütunu desteklerken XLSX 1048576 satır ve 16384 sütunu destekler. Belirli bir biçimde kaç satır ve sütunun desteklendiğini bilmek istiyorsanız, şunu kullanabilirsiniz:[**Workbook.Settings.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow) ve[**Workbook.Settings.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn)özellikleri.

## **XLS ve XLSX biçimleri tarafından desteklenen Maksimum Satır ve Sütunları Bulun**

Aşağıdaki örnek kod, çalışma kitabını önce XLS'de, sonra XLSX biçiminde oluşturur. Yarattıktan sonra, değerlerini yazdırır[**Workbook.Settings.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow) ve[**Workbook.Settings.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn)özellikleri. Lütfen referansınız için aşağıda verilen kodun konsol çıktısına bakın.

## **Basit kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.cs" >}}

## **Konsol Çıkışı**

{{< highlight "java" >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
