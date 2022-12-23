---
title: Dönüştürmek
type: docs
weight: 30
url: /tr/net/conversion/
---
Aspose.Cells Versiyon dönüşümlerinde çalışmayı etkilemeden esneklik sağlayan benzersiz özellik.
SaveFormat, aşağıdaki tabloda verilen uzantılardaki belgeyi dönüştürebilen bir numaralandırmadır.

|**Üye adı** |**Değer** |**Açıklama** |
|:- |:- |:- |
|CSV |1 | Bir CSV dosyasını temsil eder.|
| Xlsx|6 | Bir xlsx dosyasını temsil eder.|
| Xlsm|7 | Makroları etkinleştiren bir xlsm dosyasını temsil eder.|
| Xltx|8 | Bir xltx dosyasını temsil eder.|
| Xltm|9 | Makroları etkinleştiren bir xltm dosyasını temsil eder.|
|TabDelimited |11 | Sekmeyle ayrılmış bir metin dosyasını temsil eder.|
| html|12 | Bir html dosyasını temsil eder.|
| MHtml|17 | Bir mhtml dosyasını temsil eder.|
|ODS |14 | Bir ods dosyasını temsil eder.|
| Excel97To2003|5 | Bir Excel97-2003 xls dosyasını temsil eder.|
|SpreadsheetML |15 | Bir Excel 2003 xml dosyasını temsil eder.|
| Xlsb|16 | Bir xlsb dosyasını temsil eder.|
| Oto|0 | Dosyayı diske kaydediyorsanız, dosya biçimi formatı dosya adının uzantısına göre değişir.<br>Dosya akışa kaydediliyorsa, dosya formatı xlsx'tir.|
| Bilinmeyen|255 | Tanınmayan biçimi temsil eder, kaydedilemez.|
| Pdf|13 | Bir pdf dosyasını temsil eder.|
|XPS |20 | Bir XPS dosyasını temsil eder.|
|TIFF |21 | Bir TIFF dosyasını temsil eder.|
|SVG |22 | Bir SVG dosyasını temsil eder.|
| fark|30 | Veri Değişim Formatı.|
Aşağıda, xls'den xlsx'e dönüşümü gösteren kod parçacığı bulunmaktadır, bunun tersini de yapabilirsiniz

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook("Sample.xls");

workbook.Save("Converted.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}
## **Örnek Kodu İndir**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Conversion%20between%20Excel%20Formats%20%28Aspose.Cells%29.zip)
