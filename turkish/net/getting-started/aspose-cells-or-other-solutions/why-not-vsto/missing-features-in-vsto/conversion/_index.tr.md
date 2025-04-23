---
title: Dönüşüm
type: docs
weight: 30
url: /tr/net/conversion/
---

Aspose.Cells'in esneklik sağlayan benzersiz bir özelliği, çalışmayı etkilemeden sürüm dönüşümlerinde esneklik sağlar.
SaveFormat, aşağıdaki tabloda verilen uzantılarda belgeyi dönüştürebilen bir numaralama içerir.

|**Üye Adı** |**Değer** |**Açıklama** |
| :- | :- | :- |
|CSV |1 |Bir CSV dosyasını temsil eder. |
|Xlsx |6 |Bir xlsx dosyasını temsil eder. |
|Xlsm |7 |Makroları etkinleştiren bir xlsm dosyasını temsil eder. |
|Xltx |8 |Bir xltx dosyasını temsil eder. |
|Xltm |9 |Makroları etkinleştiren bir xltm dosyasını temsil eder. |
|TabDelimited |11 |Bir sekme ile ayrılmış metin dosyasını temsil eder. |
|Html |12 |Bir html dosyasını temsil eder. |
|MHtml |17 |Bir mhtml dosyasını temsil eder. |
|ODS |14 |Bir ods dosyasını temsil eder. |
|Excel97To2003 |5 |Bir Excel97-2003 xls dosyasını temsil eder. |
|SpreadsheetML |15 |Bir Excel 2003 xml dosyasını temsil eder. |
|Xlsb |16 |Bir xlsb dosyasını temsil eder. |
|Auto |0 |Dosyayı diske kaydederken, dosya biçimi dosya adının uzantısına uygun olur. <br>Dosyayı akışa kaydederken, dosya biçimi xlsx'ye uygun olur. |
|Unknown |255 |Tanınmayan formatı temsil eder, kaydedilemez. |
|Pdf |13 |Bir Pdf dosyasını temsil eder. |
|XPS |20 |Bir XPS dosyasını temsil eder. |
|TIFF |21 |Bir TIFF dosyasını temsil eder. |
|SVG |22 |Bir SVG dosyasını temsil eder. |
|Dif |30 |Veri Değişim Biçimi. |
Aşağıda xls'ten xlsx'e dönüşümü gösteren kod parçacığı bulunmaktadır, bunun tersini de yapabilirsiniz

{{< highlight csharp >}}

 Workbook workbook = new Workbook("Sample.xls");

workbook.Save("Converted.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}
## **Örnek Kod İndir**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Conversion%20between%20Excel%20Formats%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
