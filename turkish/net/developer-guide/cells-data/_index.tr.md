---
title: Excel dosyalarının verilerini yönetme
linktitle: Hücre Verileri
type: docs
weight: 110
url: /tr/net/view-and-edit-excel-data/
description: Bu makale, Aspose.Cells kitaplığı ile Excel dosyalarının verilerini görüntüleme ve düzenleme yöntemlerini açıklar.
keywords: Aspose.Cells C# ile Excel dosyasının verilerini yönetme, Excel dosyasına veri ekleme, Excel dosyasından veri alma, Veri ekleme verimliliğini artırma yöntemleri, hücre verileri yönetme, hücre verilerini güncelleme, hücre verilerini alma, hücre verileri ekleme
---

{{% alert color="primary" %}}

[Bir Çalışma Kitabının Sayfalarına Erişim](/cells/tr/net/accessing-cells-of-a-worksheet/) başlıklı makalede çalışma sayfasındaki hücrelere erişim için temel yaklaşımlardan bahsettik. Bu makale, bu yaklaşımlardan birini kullanarak hücrelere farklı türde veri eklemeyi içerir.

{{% /alert %}}

## **Hücrelere Veri Ekleme**

Aspose.Cells, Microsoft Excel dosyasını temsil eden bir [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı bir [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonu sağlar. [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıfından bir nesneyi temsil eder.

Aspose.Cells, geliştiricilere hücrelere farklı türde veri eklemelerine izin veren bir [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıfının [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) yöntemini çağırarak çalışma sayfalarındaki hücrelere veri eklemelerini sağlar. Aspose.Cells, geliştiricilere hücrelere farklı türde veri eklemelerine izin veren [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) yönteminin aşırı yüklenmiş sürümlerini sağlar. Bu aşırı yüklenmiş [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) yöntemlerini kullanarak, bir mantıksal, dize, çift, tamsayı veya tarih/saat vb. değerleri hücreye eklemek mümkündür.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AddingDataToCells-1.cs" >}}

## **Verimliliği Nasıl Arttırılır**

[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) yöntemini bir çalışma sayfasına büyük miktarda veri eklemek için kullanıyorsanız, uygulamalarınızın verimliliğini artırmak için öncelikle satır ve sonra sütunlar olarak hücrelere değer eklemelisiniz. Bu yaklaşım, uygulamalarınızın verimliliğini büyük ölçüde artırır.

## **Hücrelerden Veri Almak**

Aspose.Cells, Microsoft Excel dosyasını temsil eden bir [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, dosyadaki çalışma sayfalarına erişime izin veren bir [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı bir [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonu sağlar. [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıfından bir nesneyi temsil eder.

[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıfı, geliştiricilere verileri hücrelerden türlerine göre almak için birkaç özellik sağlar. Bu özellikler şunları içerir:

- [**StringValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue): hücrenin dize değerini döndürür.
- [**DoubleValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue): hücrenin ondalık değerini döndürür.
- [**BoolValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/boolvalue): hücrenin mantıksal değerini döndürür.
- [**DateTimeValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/datetimevalue): hücrenin tarih/saat değerini döndürür.
- [**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue): hücrenin ondalık değerini döndürür.
- [**IntValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/intvalue): hücrenin tam sayı değerini döndürür.

Bir alan doldurulmadığında, [**DoubleValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue) veya [**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue) ile başlayan hücreler bir istisna fırlatır.

Hücrede bulunan veri türü ayrıca [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıfının [**Type**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) özelliği kullanılarak kontrol edilebilir. Aslında, [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıfının [**Type**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) özelliği, önceden tanımlanmış değerleri listelenen [**CellValueType**](https://reference.aspose.com/cells/net/aspose.cells/cellvaluetype) numaralı numaralandırmaya dayanan bir özelliktir:

|**Hücre Değer Türleri**|**Açıklama**|
| :- | :- |
|IsBool| Hücre değerinin Boolean olduğunu belirtir.
|IsDateTime| Hücre değerinin tarih/saat olduğunu belirtir.
|IsNull| Boş bir hücreyi temsil eder.
|IsNumeric| Hücre değerinin sayısal olduğunu belirtir.
|IsString| Hücre değerinin bir dize olduğunu belirtir.
|IsUnknown| Hücre değerinin bilinmeyen olduğunu belirtir.

Yukarıda tanımlanan hücre değeri tiplerini aynı zamanda her hücrede bulunan veri türüyle karşılaştırmak için de kullanabilirsiniz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-RetrievingDataFromCells-1.cs" >}}

{{% alert color="primary" %}}

Çalışma sayfalarında çalışırken, kullanıcılar hücrelere farklı veri türleri ekleyebilir. Bu veri tipleri, Boolean, tam sayı, kayan nokta, metin veya tarih/saat değerlerini içerebilir. Aspose.Cells ile, hücrelerden uygun değerleri alabilirsiniz, bunlar veri tiplerine göre.

{{% /alert %}}

## **Gelişmiş Konular**
- [Bir Çalışma Sayfasının Hücrelerine Erişme](/cells/tr/net/accessing-cells-of-a-worksheet/)
- [Metin Sayı Değerini Sayıya Dönüştürme](/cells/tr/net/convert-text-numeric-data-to-number/)
- [Alt Toplamlar Oluşturma](/cells/tr/net/creating-subtotals/)
- [Veri Filtreleme](/cells/tr/net/data-filtering/)
- [Veri Sıralama](/cells/tr/net/sort-data-of-excel/)
- [Veri Doğrulama](/cells/tr/net/data-validation/)
- [Çalışma Sayfasından Veri dışa aktarma](/cells/tr/net/export-data-from-worksheet/)
- [Veri Bulma veya Arama](/cells/tr/net/find-or-search-data/)
- [Biçimlendirmeyle ve biçimlendirme olmadan Hücre Dize Değerini Alın](/cells/tr/net/get-cell-string-value-with-and-without-formatting/)
- [Hücre İçinde HTML Zengin Metin Ekleme](/cells/tr/net/adding-html-rich-text-inside-the-cell/)
- [Excel veya OpenOffice'de Hyperlinkler Eklemek](/cells/tr/net/insert-hyperlinks-to-excel/)
- [Çalışma Sayfasına Veri İçe Aktarma](/cells/tr/net/import-data-into-worksheet/)
- [Numaralandırıcıları Nerede ve Nasıl Kullanılır](/cells/tr/net/how-and-where-to-use-enumerators/)
- [Hücre Değeri Genişliğini ve Yüksekliğini Piksel Birimiyle Ölçme](/cells/tr/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Birden Fazla İş Parçacığında Aynı Anda Hücre Değerleri Okuma](/cells/tr/net/reading-cell-values-in-multiple-threads-simultaneously/)
- [Hücre adı ve satır/sütun indeksi arasında dönüşüm](/cells/tr/net/names-and-indices/)
- [Veri İlk Olarak Satır, Sonra Sütun Olarak Doldurma](/cells/tr/net/populate-data-first-by-row-then-by-column/)
- [Hücre Değerinin veya Aralığın Ön Eklemesini Koruma](/cells/tr/net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Zengin Metnin Kısımlarına Erişme ve Güncelleme](/cells/tr/net/access-and-update-the-portions-of-rich-text-of-cell/)



{{< app/cells/assistant language="csharp" >}}
