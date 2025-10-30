---
title: Golang ile C++ kullanarak Excel dosyalarının verilerini yönetin
linktitle: Hücre Verileri
type: docs
weight: 110
url: /tr/go-cpp/view-and-edit-excel-data/
description: Bu makale, Aspose.Cells kütüphanesi kullanarak C++ ile Excel dosyalarının verilerini nasıl görüntüleyip düzenleyeceğinizi açıklamaktadır.
keywords: Aspose.Cells C++ ile Excel dosyasının verilerini yönetme, Excel dosyasına veri ekleme, Excel dosyasından veri alma, Veri ekleme verimliliğini artırma, hücre verilerini yönetme, hücreleri güncelleme, hücreleri alma, hücreleri ekleme
---

{{% alert color="primary" %}}

[Bir Çalışma Sayfasının Hücrelerine Erişim](/cells/tr/cpp/accessing-cells-of-a-worksheet/) bölümünde, bir çalışma sayfasındaki hücrelere erişim için temel yaklaşımları tartıştık. Bu makale, bu yaklaşımlardan birini kullanarak hücrelere farklı türde veri eklemeyi ele almaktadır.

{{% /alert %}}

## **Hücrelere Veri Ekleme**

Aspose.Cells, Microsoft Excel dosyasını temsil eden bir [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı bir [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonu sağlar. [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfından bir nesneyi temsil eder.

Aspose.Cells, geliştiricilere hücrelere farklı türde veri eklemelerine izin veren bir [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) sınıfının [**PutValue**](https://reference.aspose.com/cells/go-cpp/cell/putvalue/) yöntemini çağırarak çalışma sayfalarındaki hücrelere veri eklemelerini sağlar. Aspose.Cells, geliştiricilere hücrelere farklı türde veri eklemelerine izin veren [**PutValue**](https://reference.aspose.com/cells/go-cpp/cell/putvalue/) yönteminin aşırı yüklenmiş sürümlerini sağlar. Bu aşırı yüklenmiş [**PutValue**](https://reference.aspose.com/cells/go-cpp/cell/putvalue/) yöntemlerini kullanarak, bir mantıksal, dize, çift, tamsayı veya tarih/saat vb. değerleri hücreye eklemek mümkündür.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CellsData.go" >}}
## **Verimliliği Nasıl Arttırılır**

[**PutValue**](https://reference.aspose.com/cells/go-cpp/cell/putvalue_bool/) yöntemini bir çalışma sayfasına büyük miktarda veri eklemek için kullanıyorsanız, uygulamalarınızın verimliliğini artırmak için öncelikle satır ve sonra sütunlar olarak hücrelere değer eklemelisiniz. Bu yaklaşım, uygulamalarınızın verimliliğini büyük ölçüde artırır.

## **Hücrelerden Veri Almak**

Aspose.Cells, Microsoft Excel dosyasını temsil eden bir [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfı, dosyadaki çalışma sayfalarına erişime izin veren bir [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı bir [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonu sağlar. [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfından bir nesneyi temsil eder.

[**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) sınıfı, geliştiricilere verileri hücrelerden türlerine göre almak için birkaç özellik sağlar. Bu özellikler şunları içerir:

- [**StringValue**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/): hücrenin dize değerini döndürür.
- [**DoubleValue**](https://reference.aspose.com/cells/go-cpp/cell/getdoublevalue/): hücrenin ondalık değerini döndürür.
- [**BoolValue**](https://reference.aspose.com/cells/go-cpp/cell/getboolvalue/): hücrenin mantıksal değerini döndürür.
- [**DateTimeValue**](https://reference.aspose.com/cells/go-cpp/cell/getdatetimevalue/): hücrenin tarih/saat değerini döndürür.
- [**FloatValue**](https://reference.aspose.com/cells/go-cpp/cell/getfloatvalue/): hücrenin ondalık değerini döndürür.
- [**IntValue**](https://reference.aspose.com/cells/go-cpp/cell/getintvalue/): hücrenin tam sayı değerini döndürür.

Bir alan doldurulmadığında, [**DoubleValue**](https://reference.aspose.com/cells/go-cpp/cell/getdoublevalue/) veya [**FloatValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/) ile başlayan hücreler bir istisna fırlatır.

Hücrede bulunan veri türü ayrıca [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) sınıfının [**Type**](https://reference.aspose.com/cells/go-cpp/cell/gettype/) özelliği kullanılarak kontrol edilebilir. Aslında, [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) sınıfının [**Type**](https://reference.aspose.com/cells/go-cpp/cell/gettype/) özelliği, önceden tanımlanmış değerleri listelenen [**CellValueType**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/) numaralı numaralandırmaya dayanan bir özelliktir:

|**Hücre Değer Türleri**|**Açıklama**|
| :- | :- |
|IsBool| Hücre değerinin Boolean olduğunu belirtir.
|IsDateTime| Hücre değerinin tarih/saat olduğunu belirtir.
|IsNull| Boş bir hücreyi temsil eder.
|IsNumeric| Hücre değerinin sayısal olduğunu belirtir.
|IsString| Hücre değerinin bir dize olduğunu belirtir.
|IsUnknown| Hücre değerinin bilinmeyen olduğunu belirtir.

Yukarıda tanımlanan hücre değeri tiplerini aynı zamanda her hücrede bulunan veri türüyle karşılaştırmak için de kullanabilirsiniz.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CellsData-1.go" >}}
{{% alert color="primary" %}}

Çalışma sayfalarında çalışırken, kullanıcılar hücrelere farklı veri türleri ekleyebilir. Bu veri tipleri, Boolean, tam sayı, kayan nokta, metin veya tarih/saat değerlerini içerebilir. Aspose.Cells ile, hücrelerden uygun değerleri alabilirsiniz, bunlar veri tiplerine göre.

{{% /alert %}}

## **Gelişmiş Konular**
- [Bir Çalışma Sayfasının Hücrelerine Erişme](/cells/tr/cpp/accessing-cells-of-a-worksheet/)
- [Metin Sayı Değerini Sayıya Dönüştürme](/cells/tr/cpp/convert-text-numeric-data-to-number/)
- [Alt Toplamlar Oluşturma](/cells/tr/cpp/creating-subtotals/)
- [Veri Filtreleme](/cells/tr/cpp/data-filtering/)
- [Veri Sıralama](/cells/tr/cpp/sort-data-of-excel/)
- [Veri Doğrulama](/cells/tr/cpp/data-validation/)
- [Veri Bulma veya Arama](/cells/tr/cpp/find-or-search-data/)
- [Biçimlendirmeyle ve biçimlendirme olmadan Hücre Dize Değerini Alın](/cells/tr/cpp/get-cell-string-value-with-and-without-formatting/)
- [Hücre İçinde HTML Zengin Metin Ekleme](/cells/tr/cpp/adding-html-rich-text-inside-the-cell/)
- [Excel veya OpenOffice'de Hyperlinkler Eklemek](/cells/tr/cpp/insert-hyperlinks-to-excel/)
- [Numaralandırıcıları Nerede ve Nasıl Kullanılır](/cells/tr/cpp/how-and-where-to-use-enumerators/)
- [Hücre Değeri Genişliğini ve Yüksekliğini Piksel Birimiyle Ölçme](/cells/tr/cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Birden Fazla İş Parçacığında Aynı Anda Hücre Değerleri Okuma](/cells/tr/cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [Hücre adı ve satır/sütun indeksi arasında dönüşüm](/cells/tr/cpp/names-and-indices/)
- [Veri İlk Olarak Satır, Sonra Sütun Olarak Doldurma](/cells/tr/cpp/populate-data-first-by-row-then-by-column/)
- [Hücre Değerinin veya Aralığın Ön Eklemesini Koruma](/cells/tr/cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Zengin Metnin Kısımlarına Erişme ve Güncelleme](/cells/tr/cpp/access-and-update-the-portions-of-rich-text-of-cell/)
