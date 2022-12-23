---
title: Excel dosyalarının verilerini yönetme.
linktitle: Cells veri
type: docs
weight: 110
url: /tr/net/view-and-edit-excel-data/
description: Bu makale, Aspose.Cells kitaplığıyla Excel dosyalarının verilerinin nasıl görüntüleneceğini ve düzenleneceğini açıklamaktadır.
---
{{% alert color="primary" %}}

 İçinde[Bir Çalışma Sayfasının Cells'ine Erişme](/cells/tr/net/accessing-cells-of-a-worksheet/), bir çalışma sayfasındaki hücrelere erişim için temel yaklaşımları tartıştık. Bu makale, hücrelere farklı veri türleri eklemek için bu yaklaşımlardan birini kullanır.

{{% /alert %}}

## **Cells'e Veri Ekleme**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf bir sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Toplamak. İçindeki her öğe[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyon bir nesneyi temsil eder[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)sınıf.

Aspose.Cells, geliştiricilerin çalışma sayfalarındaki hücrelere şunu çağırarak veri eklemesine olanak tanır:[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıf'[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) yöntem. Aspose.Cells, aşırı yüklenmiş sürümler sağlar.[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) geliştiricilerin hücrelere farklı türde veriler eklemesine olanak tanıyan bir yöntem. Bu aşırı yüklenmiş sürümlerini kullanarak[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)yöntemi ile hücreye Boolean, string, double, integer veya tarih/saat vb. değerler eklemek mümkündür.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AddingDataToCells-1.cs" >}}

## **Verimliliği Artırma**

 Eğer kullanırsan[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)Bir çalışma sayfasına büyük miktarda veri koyma yöntemi olarak, hücrelere önce satırlara sonra sütunlara göre değerler eklemelisiniz. Bu yaklaşım, uygulamalarınızın verimliliğini büyük ölçüde artırır.

## **Cells'den Veri Alınıyor**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) dosyadaki çalışma sayfalarına erişim sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf bir sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Toplamak. İçindeki her öğe[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyon bir nesneyi temsil eder[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)sınıf.

 bu[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)class, geliştiricilerin veri türlerine göre hücrelerden değerler almasına izin veren çeşitli özellikler sağlar. Bu özellikler şunları içerir:

- [**Dize değeri**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue): hücrenin dize değerini döndürür.
- [**Çift Değer**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue): hücrenin çift değerini döndürür.
- [**BoolDeğeri**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/boolvalue): hücrenin boole değerini döndürür.
- [**TarihSaatDeğeri**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/datetimevalue): hücrenin tarih/saat değerini döndürür.
- [**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue): hücrenin kayan değerini döndürür.
- [**İç Değer**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/intvalue)hücrenin tamsayı değerini döndürür.

 Bir alan doldurulmadığında,[**Çift Değer**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue) veya[**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue)bir istisna atar.

 Bir hücrede bulunan veri türü kullanılarak da kontrol edilebilir.[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıf'[**Tip**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) Emlak. Aslında,[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıf'[**Tip**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) mülkiyet esas alınır[**Hücre Değeri Türü**](https://reference.aspose.com/cells/net/aspose.cells/cellvaluetype)önceden tanımlanmış değerleri aşağıda listelenen numaralandırma:

|**Cell Değer Türleri**|**Açıklama**|
|:- |:- |
|Bool|Hücre değerinin Boolean olduğunu belirtir.|
|TarihSaat|Hücre değerinin tarih/saat olduğunu belirtir.|
|Boş|Boş bir hücreyi temsil eder.|
|sayısaldır|Hücre değerinin sayısal olduğunu belirtir.|
|Dize|Hücre değerinin bir dize olduğunu belirtir.|
|Bilinmeyen|Hücre değerinin bilinmediğini belirtir.|

Her bir hücrede bulunan veri Türü ile karşılaştırmak için yukarıda önceden tanımlanmış hücre değeri türlerini de kullanabilirsiniz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-RetrievingDataFromCells-1.cs" >}}

{{% alert color="primary" %}}

Çalışma sayfaları üzerinde çalışırken, kullanıcılar hücrelere farklı türde veriler ekleyebilir. Bu veri türleri, Boolean, tamsayı, kayan nokta, metin veya tarih/saat değerlerini içerebilir. Aspose.Cells ile hücrelerden veri türlerine göre uygun değerleri alabilirsiniz.

{{% /alert %}}

## **ileri konular**
- [Bir Çalışma Sayfasının Cells'ine Erişme](/cells/tr/net/accessing-cells-of-a-worksheet/)
- [Metin Sayısal Verilerini Sayıya Dönüştür](/cells/tr/net/convert-text-numeric-data-to-number/)
- [Ara Toplamlar Oluşturma](/cells/tr/net/creating-subtotals/)
- [Veri Filtreleme](/cells/tr/net/data-filtering/)
- [Veri Sıralama](/cells/tr/net/sort-data-of-excel/)
- [Veri doğrulama](/cells/tr/net/data-validation/)
- [Çalışma Sayfasından Verileri Dışa Aktarma](/cells/tr/net/export-data-from-worksheet/)
- [Veri Bul veya Ara](/cells/tr/net/find-or-search-data/)
- [Biçimlendirmeli ve Biçimlendirmesiz Cell Dize Değerini Alın](/cells/tr/net/get-cell-string-value-with-and-without-formatting/)
- [Cell içine HTML Zengin Metin ekleme](/cells/tr/net/adding-html-rich-text-inside-the-cell/)
- [Köprüleri Excel veya OpenOffice'e Ekleme](/cells/tr/net/insert-hyperlinks-to-excel/)
- [Verileri Çalışma Sayfasına Aktarın](/cells/tr/net/import-data-into-worksheet/)
- [Numaralandırıcılar Nasıl ve Nerede Kullanılır?](/cells/tr/net/how-and-where-to-use-enumerators/)
- [Cell Değerinin Genişliğini ve Yüksekliğini Piksel Birimi Olarak Ölçün](/cells/tr/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Cell Değerlerini Birden Çok Konuda Aynı Anda Okumak](/cells/tr/net/reading-cell-values-in-multiple-threads-simultaneously/)
- [Hücre adı ile satır/sütun dizini arasında dönüştürme](/cells/tr/net/names-and-indices/)
- [Verileri Önce Satıra, Sonra Sütuna Göre Doldurun](/cells/tr/net/populate-data-first-by-row-then-by-column/)
- [Cell Değerinin veya Aralığının Tek Alıntı Ön Ekini Koru](/cells/tr/net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Cell Zengin Metin Bölümlerine Erişin ve Güncelleyin](/cells/tr/net/access-and-update-the-portions-of-rich-text-of-cell/)



