---
title: Excel dosyalarının verilerini yönetme
linktitle: Hücre Verileri
type: docs
weight: 110
url: /tr/python-net/view-and-edit-excel-data/
description: Bu makale, Aspose.Cells for Python via .NET kütüphanesi ile Excel dosyalarının verilerini görüntüleme ve düzenleme işlemlerini açıklar.
keywords: Python Excel Kütüphanesi, Aspose.Cells for Python Excel dosyasının verilerini yönetme, Python Excel dosyasına veri ekleme, Python Excel dosyasından veri alma, Python Veri ekleme verimliliğini nasıl arttırır, Python hücre verilerini yönetme, Python hücre verilerini güncelleme, Python hücre verilerini alma, Python hücre verileri eklemek.
---

{{% alert color="primary" %}}

[Bir Çalışma Sayfasının Hücrelerine Erişim](/cells/tr/python-net/accessing-cells-of-a-worksheet/) konusunda çalışma sayfasındaki hücrelere erişim için temel yaklaşımları tartıştık. Bu makale, bu yaklaşımlardan birini kullanarak hücrelere farklı türde veri eklemeyi açıklar.

{{% /alert %}}

## **Hücrelere Veri Ekleme**

Aspose.Cells for Python via .NET, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) adında bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her bir çalışma sayfasına erişim sağlayan bir [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) koleksiyonuna sahiptir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı bir [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/) koleksiyonu sağlar. [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) sınıfının bir nesnesini temsil eder.

Aspose.Cells for Python via .NET, geliştiricilere çalışma sayfalarındaki hücrelere veri eklemek için [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) sınıfının [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#bool) yöntemini çağırarak olanak tanır. Aspose.Cells for Python via .NET, hücrelere farklı türde veri eklemelerine izin veren [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int) yönteminin aşırı yüklenmiş sürümlerini sağlar. Bu aşırı yüklenmiş [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int) yöntemleri kullanılarak, bir hücreye Mantıksal, dize, ondalık, tamsayı veya tarih/saat vb. değerler eklemek mümkündür.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AddingDataToCells-1.py" >}}

## **Verimliliği Nasıl Arttırılır**

[**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int) yöntemini bir çalışma sayfasına büyük miktarda veri eklemek için kullanıyorsanız, uygulamalarınızın verimliliğini artırmak için öncelikle satır ve sonra sütunlar olarak hücrelere değer eklemelisiniz. Bu yaklaşım, uygulamalarınızın verimliliğini büyük ölçüde artırır.

## **Hücrelerden Veri Almak**

Aspose.Cells for Python via .NET, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) adında bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, dosyadaki çalışma sayfalarına erişim sağlayan bir [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) koleksiyonuna sahiptir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı bir [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/) koleksiyonu sağlar. [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) sınıfının bir nesnesini temsil eder.

[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) sınıfı, geliştiricilere verileri hücrelerden türlerine göre almak için birkaç özellik sağlar. Bu özellikler şunları içerir:

- [**string_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/string_value/): hücrenin dize değerini döndürür.
- [**double_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/double_value/): hücrenin ondalık değerini döndürür.
- [**bool_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/bool_value/): hücrenin mantıksal değerini döndürür.
- [**date_time_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/date_time_value/): hücrenin tarih/saat değerini döndürür.
- [**float_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/float_value/): hücrenin ondalık değerini döndürür.
- [**int_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/int_value/): hücrenin tam sayı değerini döndürür.

Bir alan doldurulmadığında, [**double_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/double_value/) veya [**float_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/float_value/) ile başlayan hücreler bir istisna fırlatır.

Hücrede bulunan veri türü ayrıca [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) sınıfının [**type**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/type/) özelliği kullanılarak kontrol edilebilir. Aslında, [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) sınıfının [**type**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/type/) özelliği, önceden tanımlanmış değerleri listelenen [**CellValueType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellvaluetype) numaralı numaralandırmaya dayanan bir özelliktir:

|**Hücre Değer Türleri**|**Açıklama**|
| :- | :- |
|IS_BOOL|Hücre değerinin Mantıksal olduğunu belirtir.|
|IS_DATE_TIME|Hücre değerinin tarih/saat olduğunu belirtir.|
|IS_NULL|Boş bir hücreyi temsil eder.|
|IS_NUMERIC|Hücre değerinin sayısal olduğunu belirtir.|
|IS_STRING|Hücre değerinin bir dize olduğunu belirtir.|
|IS_ERROR|Hücre değerinin hata değeri olduğunu belirtir.|
|IS_UNKNOWN|Hücre değerinin bilinmeyen olduğunu belirtir.|

Yukarıda tanımlanan hücre değeri tiplerini aynı zamanda her hücrede bulunan veri türüyle karşılaştırmak için de kullanabilirsiniz.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-RetrievingDataFromCells-1.py" >}}

{{% alert color="primary" %}}

Çalışma sayfaları üzerinde çalışırken, kullanıcılar hücrelere farklı veri türleri ekleyebilirler. Bu veri tipleri Boolean, tamsayı, kayan noktalı, metin veya tarih/zaman değerlerini içerebilir. Aspose.Cells for Python via .NET ile hücrelerden veri türlerine göre uygun değerleri alabilirsiniz.

{{% /alert %}}

## **Gelişmiş Konular**
- [Bir Çalışma Sayfasının Hücrelerine Erişme](/cells/tr/python-net/accessing-cells-of-a-worksheet/)
- [Metin Sayı Değerini Sayıya Dönüştürme](/cells/tr/python-net/convert-text-numeric-data-to-number/)
- [Alt Toplamlar Oluşturma](/cells/tr/python-net/creating-subtotals/)
- [Veri Filtreleme](/cells/tr/python-net/data-filtering/)
- [Veri Sıralama](/cells/tr/python-net/sort-data-of-excel/)
- [Veri Doğrulama](/cells/tr/python-net/data-validation/)
- [Biçimlendirmeyle ve biçimlendirme olmadan Hücre Dize Değerini Alın](/cells/tr/python-net/get-cell-string-value-with-format-strategy/)
- [Hücre İçinde HTML Zengin Metin Ekleme](/cells/tr/python-net/adding-html-rich-text-inside-the-cell/)
- [Veri Bulma veya Arama](/cells/tr/python-net/find-or-search-data/)
- [Excel veya OpenOffice'de Hyperlinkler Eklemek](/cells/tr/python-net/insert-hyperlinks-to-excel/)
- [Hücre Değeri Genişliğini ve Yüksekliğini Piksel Birimiyle Ölçme](/cells/tr/python-net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Hücre adı ve satır/sütun indeksi arasında dönüşüm](/cells/tr/python-net/names-and-indices/)
- [Veri İlk Olarak Satır, Sonra Sütun Olarak Doldurma](/cells/tr/python-net/populate-data-first-by-row-then-by-column/)
- [Hücre Değerinin veya Aralığın Ön Eklemesini Koruma](/cells/tr/python-net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Zengin Metnin Kısımlarına Erişme ve Güncelleme](/cells/tr/python-net/access-and-update-the-portions-of-rich-text-of-cell/)
{{< app/cells/assistant language="python-net" >}}
