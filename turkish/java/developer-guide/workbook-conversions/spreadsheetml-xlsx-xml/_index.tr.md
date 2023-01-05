---
title: SpreadsheetML - XLSX, XML
type: docs
weight: 10
url: /tr/java/spreadsheetml-xlsx-xml/
---
## **SpreadsheetML hakkında**
SpreadsheetML, elektronik tablo belgeleri için XML tabanlı bir biçim ailesinin adıdır. SpreadsheetML'in birkaç versiyonu vardır:

1. SpreadsheetML sürüm 2003, Microsoft Word 2003'te tanıtıldı. SpreadsheetML, Microsoft tarafından belge biçimini açmaya yönelik önemli bir adımdı.
1. [Office Açık XML'i](https://en.wikipedia.org/wiki/Office_Open_XML) (OOXML), Microsoft Office 2007 uygulamalarında tanıtılan yeni XML tabanlı biçimdir. Office Açık XML, birkaç özel XML tabanlı biçimlendirme dili için bir kap biçimidir. SpreadsheetML sürüm 2007, Microsoft Office Excel 2007 tarafından belgelerini depolamak için kullanılan biçimlendirme dilidir.
1. Microsoft Excel 2010 ve sonraki sürümler, belgeleri güncel OOXML standardında tanımlandığı şekilde SpreadsheetML sürüm 2010'da depolar.
## **SpreadsheetML içinde Aspose.Cells**
SpreadsheetML'in üç "versiyonu" mevcuttur:

|**SpreadsheetML "Sürüm"**|**Geçerli Standart/Şartname**|**Aspose.Cells for Java'de desteklenir**|
|:- |:- |:- |
|Microsoft excel 2003|[Microsoft Excel 2003 XML'i](https://en.wikipedia.org/wiki/Microsoft_Office_XML_formats)|Evet|
|Microsoft excel 2007|[OOXML ECMA-376](https://www.ecma-international.org/publications-and-standards/standards/ecma-376/)|Evet|
|Microsoft Excel 2010 ve sonraki sürümler|OOXML ISO/IEC DIS 29500|Evet|
OOXML SpreadsheetML belgeleri genellikle ZIP paketleri olan XLSX dosyaları olarak gelir. XLSX'e ek olarak. Aspose.Cells, SpreadsheetML belgelerinin yüklenmesi, kaydedilmesi ve dönüştürülmesi için kapsamlı destek sağlar. Aspose.Cells, Microsoft Excel belgelerinin yapısı düşünülerek tasarlandığından (ve SpreadsheetML'in, Microsoft Excel belgelerinin dahili temsilini taklit ettiği bilinmektedir) bu tür her şeyi kapsayan bir uygulama mümkündür.

**Aspose.Cells tarafından oluşturulan ve Microsoft Excel'de açılan bir XLSX belgesi** 

![yapılacaklar:resim_alternatif_metin](spreadsheetml-xlsx-xml_1.png)

**Aspose.Cells tarafından oluşturulan XLSX belgesi, Açık Paketleme Kuralına uygundur ve ZIP özellikli bir uygulamada açılabilir.** 

![yapılacaklar:resim_alternatif_metin](spreadsheetml-xlsx-xml_2.png)
## **OOXML Açık, Neden Aspose.Cells Kullanılmalı?**
Office Açık XML teknolojisinin, Aspose.Cells gibi üçüncü taraf kitaplıklara güvenmeden yalnızca XML sınıflarını kullanarak belge işleme ve oluşturma uygulamaları oluşturmayı mümkün kıldığı doğrudur. XML veya diğer kitaplıklar aracılığıyla çalışmak yerine OOXML belgeleriyle ilgilenmek için.

OOXML belirtimi birkaç bin sayfa uzunluğundadır. Açık ve standart olmak, basit olmak anlamına gelmez. OOXML belgelerini doğru bir şekilde işlemek veya oluşturmak için, formatı iyi öğrenmeye yatırım yapılmalıdır.

Aspose.Cells, geçerli belgeleri doğru bir şekilde işlemeyi ve oluşturmayı kolaylaştırmanın yanı sıra, OOXML dosyalarıyla doğrudan XML veya diğer üçüncü taraf kitaplıkları aracılığıyla çalışırken sahip olamayacağınız aşağıdaki önemli özellikleri sağlar:

- PDF, HTML, TIFF'e dönüştürme ve yazdırma dahil olmak üzere birçok popüler Excel biçimi arasında kaliteli dönüştürmeler.
- Verileri biçimsel biçimlendirme, çizelgeler ve grafiklerle otomatik olarak birleştirirken parçalardan, bir veya daha fazla belgeden belgeler oluşturma yeteneği.
- Array, ArrayList, DataTable, DataColumn, DataGrid, DataView ve DataReader dahil olmak üzere farklı veri kaynaklarından veri içe aktarma veya bir DataTable veya Array'i tek bir kod satırıyla doldurmak için verileri dışa aktarma gibi üst düzey işlevler.
- Neredeyse tüm standart ve gelişmiş Microsoft Excel İşlevlerini destekleyen Sağlam Formül Hesaplama Motoru.

Aşağıdaki örneği ele alalım. Bazı hücreler kalın harflerle “Hello World” metnini içerir. Şimdi, çalışma sayfasındaki tüm "Hello World" ifadelerini arayan ve onları "Dünyaya Elveda" ile değiştiren bir program yazmanız gerektiğini hayal edin.
## **Office Açık XML Belgesinin bir parçası**
**xml**

{{< highlight "csharp" >}}

 <?xml version="1.0" encoding="UTF-8" standalone="yes" ?>

\- <worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">

  <dimension ref="A1:M184" />

\- <sheetViews>

\- <sheetView tabSelected="1" workbookViewId="0">

  <selection activeCell="H27" sqref="H27" />

  </sheetView>

  </sheetViews>

  <sheetFormatPr defaultRowHeight="15" />

\- <sheetData>

\- <row r="1" spans="1:7">

\- <c r="A1" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="11" spans="1:7">

\- <c r="D11" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="15" spans="1:7">

\- <c r="G15" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="21" spans="2:7">

\- <c r="G21" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="25" spans="2:7">

\- <c r="F25" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="31" spans="2:7">

\- <c r="B31" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="34" spans="6:13">

\- <c r="M34" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="38" spans="6:13">

\- <c r="F38" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="117" spans="8:8">

\- <c r="H117" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="184" spans="8:8">

\- <c r="H184" s="1" t="s">

  <v>0</v>

  </c>

  </row>

  </sheetData>

  <pageMargins left="0.7" right="0.7" top="0.75" bottom="0.75" header="0.3" footer="0.3" />

</worksheet>



{{< /highlight >}}

Bir Office Açık XML belgesinde basit bir bul ve değiştir işlemini uygulamak bile zordur.

**Bizim tavsiyemiz:** açık ve standardın basit anlamına gelmediğini unutmayın ve Aspose.Cells'i kullanın.
