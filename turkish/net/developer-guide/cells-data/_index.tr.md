---
title: Excel dosyalarının verilerini yönetme
linktitle: Cells Veri
type: docs
weight: 110
url: /tr/net/view-and-edit-excel-data/
description: Bu makalede, Aspose.Cells kitaplığıyla Excel dosyalarının verilerinin nasıl görüntüleneceği ve düzenleneceği açıklanmaktadır.
keywords: Aspose.Cells C# Manage data of Excel file, add data to Excel file, get data from excel file, How to Improve Efficiency of adding data, manage cells data, update cells data, get cells data, insert cells data
---
{{% alert color="primary" %}}

 İçinde[Bir Çalışma Sayfasının Cells'ine erişme](/cells/tr/net/accessing-cells-of-a-worksheet/)çalışma sayfasındaki hücrelere erişmeye yönelik temel yaklaşımları tartıştık. Bu makalede, hücrelere farklı türde veriler eklemek için bu yaklaşımlardan biri kullanılmaktadır.

{{% /alert %}}

##  **Cells'e Veri Nasıl Eklenir?**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Microsoft Excel dosyasını temsil eder.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**Çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Excel dosyasındaki her çalışma sayfasına erişime izin veren koleksiyon. Bir çalışma sayfası şu şekilde temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Toplamak. İçindeki her öğe[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyon bir nesneyi temsil eder[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)sınıf.

 Aspose.Cells, geliştiricilerin çalışma sayfalarındaki hücrelere veri eklemesine olanak tanır.[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)sınıf'[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) yöntem. Aspose.Cells aşırı yüklenmiş versiyonlarını sağlar[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) Geliştiricilerin hücrelere farklı türde veriler eklemesine olanak tanıyan yöntem. Bu aşırı yüklenmiş sürümlerini kullanarak[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)yöntemiyle hücreye Boolean, string, double, integer veya tarih/saat vb. değerler eklemek mümkündür.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AddingDataToCells-1.cs" >}}

##  **Verimlilik Nasıl Artırılır?**

 Eğer kullanırsan[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)Bir çalışma sayfasına büyük miktarda veri yerleştirme yönteminde, hücrelere değerleri önce satırlar, sonra sütunlar halinde eklemelisiniz. Bu yaklaşım, uygulamalarınızın verimliliğini büyük ölçüde artırır.

##  **Cells'den Veri Nasıl Alınır?**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bu bir Microsoft Excel dosyasını temsil eder.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**Çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) dosyadaki çalışma sayfalarına erişime izin veren koleksiyon. Bir çalışma sayfası şu şekilde temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Toplamak. İçindeki her öğe[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyon bir nesneyi temsil eder[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)sınıf.

[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)class, geliştiricilerin hücrelerden veri türlerine göre değer almasına olanak tanıyan çeşitli özellikler sağlar. Bu özellikler şunları içerir:

- [**Dize değeri**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue): hücrenin dize değerini döndürür.
- [**Çift Değer**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue): hücrenin double değerini döndürür.
- [**BoolDeğeri**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/boolvalue): hücrenin boolean değerini döndürür.
- [**TarihSaatDeğeri**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/datetimevalue): hücrenin tarih/saat değerini döndürür.
- [**Kayan Değer**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue): hücrenin float değerini döndürür.
- [**IntValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/intvalue): hücrenin tamsayı değerini döndürür.

 Bir alan doldurulmadığında hücreler[**Çift Değer**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue) veya[**Kayan Değer**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue)bir istisna atar.

 Bir hücrede bulunan veri türü aynı zamanda kullanılarak da kontrol edilebilir.[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)sınıf'[**Tip**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) mülk. Aslında,[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)sınıf'[**Tip**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) mülkiyet esasına dayanmaktadır[**Hücre Değeri Türü**](https://reference.aspose.com/cells/net/aspose.cells/cellvaluetype)önceden tanımlanmış değerleri aşağıda listelenen numaralandırma:

|**Cell Değer Türleri**|**Tanım**|
| :- | :- |
|IsBool|Hücre değerinin Boolean olduğunu belirtir.|
|IsDateTime|Hücre değerinin tarih/saat olduğunu belirtir.|
|Boş mu|Boş bir hücreyi temsil eder.|
|Sayısaldır|Hücre değerinin sayısal olduğunu belirtir.|
|IsString|Hücre değerinin bir dize olduğunu belirtir.|
|Bilinmeyen|Hücre değerinin bilinmediğini belirtir.|

Ayrıca, her hücrede bulunan veri türüyle karşılaştırmak için yukarıdaki önceden tanımlanmış hücre değeri türlerini de kullanabilirsiniz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-RetrievingDataFromCells-1.cs" >}}

{{% alert color="primary" %}}

Kullanıcılar çalışma sayfaları üzerinde çalışırken hücrelere farklı türde veriler ekleyebilir. Bu veri türleri Boolean, tamsayı, kayan nokta, metin veya tarih/saat değerlerini içerebilir. Aspose.Cells ile hücrelerden veri türlerine göre uygun değerleri alabilirsiniz.

{{% /alert %}}

##  **İleri konular**
- [Bir Çalışma Sayfasının Cells'ine erişme](/cells/tr/net/accessing-cells-of-a-worksheet/)
- [Metin Sayısal Verilerini Sayıya Dönüştür](/cells/tr/net/convert-text-numeric-data-to-number/)
- [Alt Toplamlar Oluşturma](/cells/tr/net/creating-subtotals/)
- [Veri Filtreleme](/cells/tr/net/data-filtering/)
- [Veri Sıralama](/cells/tr/net/sort-data-of-excel/)
- [Veri doğrulama](/cells/tr/net/data-validation/)
- [Verileri Çalışma Sayfasından Dışa Aktarma](/cells/tr/net/export-data-from-worksheet/)
- [Veri Bul veya Ara](/cells/tr/net/find-or-search-data/)
- [Biçimlendirmeli ve Biçimlendirmesiz Cell Dize Değeri Alın](/cells/tr/net/get-cell-string-value-with-and-without-formatting/)
- [Cell'in içine HTML Zengin Metin eklenmesi](/cells/tr/net/adding-html-rich-text-inside-the-cell/)
- [Köprüleri Excel veya OpenOffice'e Ekleme](/cells/tr/net/insert-hyperlinks-to-excel/)
- [Verileri Çalışma Sayfasına Aktar](/cells/tr/net/import-data-into-worksheet/)
- [Numaralandırıcılar Nasıl ve Nerede Kullanılır?](/cells/tr/net/how-and-where-to-use-enumerators/)
- [Cell Değerinin Genişliğini ve Yüksekliğini Piksel Birimi cinsinden ölçün](/cells/tr/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Birden Fazla Konudaki Cell Değerlerini Aynı Anda Okumak](/cells/tr/net/reading-cell-values-in-multiple-threads-simultaneously/)
- [Hücre adı ile satır/sütun dizini arasındaki dönüşüm](/cells/tr/net/names-and-indices/)
- [Verileri Önce Satıra, Sonra Sütuna Göre Doldurun](/cells/tr/net/populate-data-first-by-row-then-by-column/)
- [Cell Değeri veya Aralığının Tek Alıntı Önekini Koru](/cells/tr/net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Cell Zengin Metin Bölümlerine Erişin ve Güncelleyin](/cells/tr/net/access-and-update-the-portions-of-rich-text-of-cell/)



