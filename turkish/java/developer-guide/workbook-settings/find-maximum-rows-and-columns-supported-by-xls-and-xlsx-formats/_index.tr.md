---
title: XLS ve XLSX biçimleri tarafından desteklenen Maksimum Satır ve Sütunları Bulun
type: docs
weight: 60
url: /tr/java/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---
## **Olası Kullanım Senaryoları**
Excel biçimleri tarafından desteklenen farklı sayıda satır ve sütun vardır. Örneğin, XLS 65536 satır ve 256 sütunu desteklerken XLSX 1048576 satır ve 16384 sütunu destekler. Belirli bir biçimde kaç satır ve sütunun desteklendiğini bilmek istiyorsanız, şunu kullanabilirsiniz:[Workbook.Settings.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow)ve[Workbook.Settings.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn)özellikler.
## **XLS ve XLSX biçimleri tarafından desteklenen Maksimum Satır ve Sütunları Bulun**
Aşağıdaki örnek kod çalışma kitabını önce XLS sonra XLSX biçiminde oluşturur. Yarattıktan sonra, değerlerini yazdırır[Workbook.Settings.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow)ve[Workbook.Settings.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn)özellikler. Lütfen referansınız için aşağıda verilen kodun konsol çıktısına bakın.
## **Basit kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.java" >}}

Konsol Çıkışı

{{< highlight "java" >}}

 Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
