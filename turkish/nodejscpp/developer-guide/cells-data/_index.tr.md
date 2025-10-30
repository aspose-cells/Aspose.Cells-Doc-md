---
title: Excel dosyalarının verilerini yönetme
linktitle: Hücre Verileri
type: docs
weight: 110
url: /tr/nodejs-cpp/view-and-edit-excel-data/
description: Bu makale, Aspose.Cells kütüphanesi ile Node.js üzerinde Excel dosyalarının verilerini görüntüleme ve düzenleme yöntemlerini anlatmaktadır.
keywords: Aspose.Cells Node.js ile C++, Excel verisi yönetimi, veri ekleme, veriyi alma, Verimliliği Artırma, hücre verisi yönetimi, hücreleri güncelleme, hücreleri alma, hücre verisi ekleme
---

{{% alert color="primary" %}}

[Bir Sayfada Hücrelere Erişim](/cells/tr/nodejs-cpp/accessing-cells-of-a-worksheet/)’da, bir sayfadaki hücrelere erişmek için temel yaklaşımları ele aldık. Bu makale, bu yaklaşımlardan birini kullanarak hücrelere farklı veri türleri ekleme yöntemini anlatmaktadır.

{{% /alert %}}

## **Hücrelere Veri Ekleme**

Aspose.Cells for Node.js via C++, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı ise bir [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) koleksiyonu sağlar. [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) sınıfının bir nesnesini temsil eder.

Aspose.Cells, geliştiricilerin [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) sınıfının [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) metodunu çağırarak hücrelere veri eklemesine olanak tanır. Aspose.Cells, farklı veri türlerini hücrelere eklemeyi sağlayan [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) metodunun aşırı yüklenmiş sürümlerini de sunar. Bu aşırı yüklenmiş metodları kullanarak, hücreye Boolean, dize, double, tam sayı veya tarih/zaman gibi değerler ekleyebilirsiniz.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AddDataToCells.js" >}}


## **Verimliliği Nasıl Arttırılır**

Eğer [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) metodunu kullanarak büyük miktarda veri bir çalışma sayfasına yerleştiriyorsanız, verileri önce satır satır, sonra sütun sütun ekmek uygulamanız, uygulamanızın verimliliğini büyük ölçüde artıracaktır.

## **Hücrelerden Veri Almak**

Aspose.Cells for Node.js via C++, dosyadaki çalışma sayfalarına erişim sağlamak için kullanılan [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, ana dosyadaki çalışma sayfalarına erişime imkan tanıyan bir [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, bir [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) koleksiyonu sunar. [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) sınıfının bir nesnesini temsil eder.

[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) sınıfı, geliştiricilerin hücrelerin değerlerini veri türlerine göre almak için kullanabilecekleri birkaç özellik sağlar. Bu özellikler şunları içerir:

- [**getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--): hücrenin dize değerini döndürür.
- [**getDoubleValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDoubleValue--): hücrenin çift değerini döndürür.
- [**getBoolValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getBoolValue--): hücrenin boolean değerini döndürür.
- [**getDateTimeValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDateTimeValue--): hücrenin tarih/zaman değerini döndürür.
- [**getFloatValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFloatValue--): hücrenin float değerini döndürür.
- [**getIntValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getIntValue--): hücrenin tam sayı değerini döndürür.

Bir alan doldurulmadığında, [**getDoubleValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDoubleValue--) veya [**getFloatValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFloatValue--) ile hücreler istisna fırlatır.

Bir hücrede bulunan verinin tipi, [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) sınıfının [**getType()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getType--) metodu kullanılarak da kontrol edilebilir. Aslında, [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) sınıfının [**getType()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getType--) metodu, aşağıda listelenen önceden tanımlı değerlere sahip [**CellValueType**](https://reference.aspose.com/cells/nodejs-cpp/cellvaluetype) enum'ına dayanmaktadır:

|**Hücre Değer Türleri**|**Açıklama**|
| :- | :- |
|IsBool| Hücre değerinin Boolean olduğunu belirtir.
|IsDateTime| Hücre değerinin tarih/saat olduğunu belirtir.
|IsNull| Boş bir hücreyi temsil eder.
|IsNumeric| Hücre değerinin sayısal olduğunu belirtir.
|IsString| Hücre değerinin bir dize olduğunu belirtir.
|IsUnknown| Hücre değerinin bilinmeyen olduğunu belirtir.

Yukarıda tanımlanan hücre değeri tiplerini aynı zamanda her hücrede bulunan veri türüyle karşılaştırmak için de kullanabilirsiniz.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-RetrieveDataFromCells.js" >}}


{{% alert color="primary" %}}

Çalışma sayfaları üzerinde çalışırken kullanıcılar hücrelere farklı veri türleri ekleyebilir. Bu veri türleri Boolean, tam sayı, ondalıklı sayı, metin veya tarih/zaman değerleri içerebilir. Aspose.Cells ile, hücrelerin veri türlerine göre uygun değerleri alabilirsiniz.

{{% /alert %}}

## **Gelişmiş Konular**
- [Bir Çalışma Sayfasının Hücrelerine Erişme](/cells/tr/nodejs-cpp/accessing-cells-of-a-worksheet/)
- [Metin Sayı Değerini Sayıya Dönüştürme](/cells/tr/nodejs-cpp/convert-text-numeric-data-to-number/)
- [Alt Toplamlar Oluşturma](/cells/tr/nodejs-cpp/creating-subtotals/)
- [Veri Filtreleme](/cells/tr/nodejs-cpp/data-filtering/)
- [Veri Sıralama](/cells/tr/nodejs-cpp/sort-data-of-excel/)
- [Veri Doğrulama](/cells/tr/nodejs-cpp/data-validation/)
- [Veri Bulma veya Arama](/cells/tr/nodejs-cpp/find-or-search-data/)
- [Biçimlendirmeyle ve biçimlendirme olmadan Hücre Dize Değerini Alın](/cells/tr/nodejs-cpp/get-cell-string-value-with-and-without-formatting/)
- [Hücre İçinde HTML Zengin Metin Ekleme](/cells/tr/nodejs-cpp/adding-html-rich-text-inside-the-cell/)
- [Excel veya OpenOffice'de Hyperlinkler Eklemek](/cells/tr/nodejs-cpp/insert-hyperlinks-to-excel/)
- [Numaralandırıcıları Nerede ve Nasıl Kullanılır](/cells/tr/nodejs-cpp/how-and-where-to-use-enumerators/)
- [Hücre Değeri Genişliğini ve Yüksekliğini Piksel Birimiyle Ölçme](/cells/tr/nodejs-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Birden Fazla İş Parçacığında Aynı Anda Hücre Değerleri Okuma](/cells/tr/nodejs-cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [Hücre adı ve satır/sütun indeksi arasında dönüşüm](/cells/tr/nodejs-cpp/names-and-indices/)
- [Veri İlk Olarak Satır, Sonra Sütun Olarak Doldurma](/cells/tr/nodejs-cpp/populate-data-first-by-row-then-by-column/)
- [Hücre Değerinin veya Aralığın Ön Eklemesini Koruma](/cells/tr/nodejs-cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Zengin Metnin Kısımlarına Erişme ve Güncelleme](/cells/tr/nodejs-cpp/access-and-update-the-portions-of-rich-text-of-cell/)
{{< app/cells/assistant language="nodejs-cpp" >}}
