---
title: SpreadsheetML - XLSX, XML
type: docs
weight: 10
url: /tr/java/spreadsheetml-xlsx-xml/
---

## **SpreadsheetML Hakkında**
SpreadsheetML, elektronik tablo belgeleri için XML tabanlı formatların bir ailesi için bir isimdir. SpreadsheetML'in birkaç sürümü bulunmaktadır:

1. SpreadsheetML sürüm 2003, Microsoft Word 2003'te tanıtılmıştır. SpreadsheetML, belge formatını açık yapma konusunda Microsoft tarafından atılmış önemli bir adımdır.
1. [Office Open XML](https://en.wikipedia.org/wiki/Office_Open_XML) (OOXML), Microsoft Office 2007 uygulamalarında tanıtılmış yeni XML tabanlı formattır. Office Open XML, birkaç özel XML tabanlı işaretleme dili için bir konteyner formatıdır. SpreadsheetML sürüm 2007, Microsoft Office Excel 2007 tarafından belgelerini depolamak için kullanılan işaretleme dilidir.
1. Microsoft Excel 2010 ve sonraki sürümler, belgeleri güncellenmiş OOXML standardında tanımlanan 2010 sürümünde depolar.
## **Aspose.Cells'te SpreadsheetML**
Mevcut üç "sürüm" ile ilgili olarak SpreadsheetML mevcuttur:

|**SpreadsheetML “Sürüm”**|**Uygun Standart/Özellik**|**Aspose.Cells for Java'de Desteklenir**|
| :- | :- | :- |
|Microsoft Excel 2003|[Microsoft Excel 2003 XML](https://en.wikipedia.org/wiki/Microsoft_Office_XML_formats)|Evet|
|Microsoft Excel 2007|[OOXML ECMA-376](https://www.ecma-international.org/publications-and-standards/standards/ecma-376/)|Evet|
|Microsoft Excel 2010 ve sonraki sürümler|OOXML ISO/IEC DIS 29500|Evet|
OOXML SpreadsheetML belgeleri genellikle XLSX dosyaları olarak gelir, ki bunlar ZIP paketleridir. XLSX'ın yanı sıra Aspose.Cells, SpreadsheetML belgelerini yükleme, kaydetme ve dönüştürme konusunda kapsamlı destek sağlar. Böyle kapsamlı bir uygulama sağlamak mümkündür çünkü Aspose.Cells, Microsoft Excel belgelerinin yapısı göz önünde bulundurularak tasarlanmıştır (ve SpreadsheetML'nin, Microsoft Excel belgelerinin iç temsilini taklit ettiği bilinir).

**Aspose.Cells tarafından oluşturulan ve Microsoft Excel'de açılan bir XLSX belgesi** 

![todo:image_alt_text](spreadsheetml-xlsx-xml_1.png)

**Aspose.Cells tarafından oluşturulan XLSX belgesi Açık Paketleme Sözleşmesi'ni takip eder ve bir ZIP uyumlu uygulamada açılabilir** 

![todo:image_alt_text](spreadsheetml-xlsx-xml_2.png)
## **OOXML açıktır, Neden Aspose.Cells Kullanmalısınız?**
Office Open XML teknolojisinin, Aspose.Cells gibi üçüncü şahıs kütüphanelerine dayanmadan yalnızca XML sınıflarını kullanarak belge işleme ve oluşturma uygulamaları oluşturulmasını mümkün kıldığı doğrudur. Ancak, OOXML belgeleriyle uğraşmak zorunda kaldığınızda XML veya diğer kütüphaneler aracılığıyla çalışmaktan ziyade, Aspose.Cells kullanmanın hala çok faydalı olduğuna şiddetle inanıyoruz.

OOXML belgesi birkaç bin sayfa uzunluğundadır. Açık ve standart olmak, basit olmak anlamına gelmez. OOXML belgelerini doğru bir şekilde işlemek veya oluşturmak için formata iyi bir şekilde hakim olmak gereklidir.

Geçerli belgeleri doğru bir şekilde işlemeyi ve oluşturmayı daha basit hale getirmenin yanı sıra, Aspose.Cells, aşağıdaki önemli özellikleri sağlar: XML veya diğer üçüncü taraf kütüphanelerle doğrudan çalışırken sahip olmayacağınız:

- PDF, HTML, TIFF'e dönüş dahil olmak üzere birçok popüler Excel formatı arasında kaliteli dönüşümler
- Belge parçalarından, tek veya çoklu belgelerden belge oluşturma yeteneği, veri birleştirme otomatik olarak biçimsel biçimlendirme, grafikler ve grafiklerle.
- Array, ArrayList, DataTable, DataColumn, DataGrid, DataView ve DataReader gibi farklı veri kaynaklarından veri alımı veya DataTable ya da Array ile veri doldurma için tek satır kodla veri alma yeteneği
- Hemen hemen tüm standart ve gelişmiş Microsoft Excel Fonksiyonlarını destekleyen güçlü Formül Hesaplama Motoru.

Aşağıdaki örneği düşünün. Bazı hücreler kalın şekilde 'Merhaba Dünya' metnini içerir. Şimdi, çalışsayan bir program yazmanız gerektiğini hayal edin ve bu metni 'Hoşçakal Yeryüzü' ile değiştirmeniz gerektiğini düşünün.
## **Office Open XML Belgesinin bir parçası**
**XML**

{{< highlight csharp >}}

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

Bir Office Open XML belgesinde bile basit bir arama ve değiştirme operasyonunu uygulamak zor olabilir.

**Tavsiyemiz:** açık ve standart olmanın basit olmak anlamına gelmediğini unutmayın ve Aspose.Cells kullanın.
