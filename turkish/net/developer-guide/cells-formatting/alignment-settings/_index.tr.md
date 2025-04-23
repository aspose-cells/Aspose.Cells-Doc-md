---
title: Uyum Ayarları
description: Aspose.Cells kütüphanesinde, metnin düzeni ve gösterimi ayarlamak için hücre uygunluk ayarlarını kullanabilirsiniz. Yatay hizalama, dikey hizalama ve metin kaydırma gibi ayarları ayarlayarak, metnin hücrelerde nasıl akacağı konusunda daha fazla kontrol sahibi olursunuz. Bu belge, hücre uygunluk ayarlarını nasıl kullanacağınızı hızlıca öğrenmenize ve örnek kodlarıyla adım adım rehberlik etmesine yardımcı olacaktır.
keywords: Aspose.Cells, hücre uygunluk, yatay hizalama, dikey hizalama, metin kaydırma
type: docs
weight: 20
url: /tr/net/cells-alignment-settings/
---

## **Hizalama Ayarlarının Yapılandırılması**

### **Microsoft Excel'deki hizalama ayarları**

Hücreleri biçimlendirmek için Microsoft Excel kullanan herkes, Microsoft Excel'deki hizalama ayarlarına aşinadır.

Yukarıdaki şekilden görebileceğiniz gibi, farklı türde hizalama seçenekleri bulunmaktadır:

- Metin hizalama (yatay ve dikey)
- Girinti
- Yönlendirme
- Metin kontrol
- Metin yönü

Bu tüm hizalama ayarları, Aspose.Cells tarafından tamamen desteklenir ve aşağıda daha detaylı olarak tartışılmaktadır.

### **Aspose.Cells'te hizalama ayarları**

Aspose.Cells, bir Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her bir çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, bir [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonu sağlar. [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıfının bir örneğini temsil eder.

Aspose.Cells, [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) ve [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) metodlarını, [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıfı için bir hücrenin biçimlendirmesini almak ve ayarlamak için kullanır. [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) sınıfı, hizalama ayarlarını yapılandırmak için kullanışlı özellikler sağlar.

[**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype) numarasını kullanarak herhangi bir metin hizalama türünü seçin. [**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype) numarasındaki önceden tanımlanmış metin hizalama türleri:

|**Metin Hizalama Türleri**|**Açıklama**|
| :- | :- |
|Bottom|, alt metin hizalamasını temsil eder
|Center|, merkez metin hizalamasını temsil eder
|CenterAcross|, metin hizalamasını çapraz merkezlemeyi temsil eder
|Distributed|, dağıtılmış metin hizalamasını temsil eder
|Fill|, doldurma metin hizalamasını temsil eder
|General|, genel metin hizalamasını temsil eder
|Justify|, düzgün metin hizalamasını temsil eder
|Left|, sol metin hizalamasını temsil eder
|Right|, sağ metin hizalamasını temsil eder
|Top|, üst metin hizalamasını temsil eder
|JustifiedLow|, Arapça metin için ayarlanmış bir kashida uzunluğuyla metni hizalar.
|ThaiDistributed|, Özellikle Tayland metnini dağıtır, çünkü her karakter bir kelime olarak kabul edilir.

{{% alert color="primary" %}}

Ayrıca [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/isjustifydistributed) özelliğini kullanarak düzgün dağıtılmış ayarını uygulayabilirsiniz.

{{% /alert %}}

#### **Yatay Hizalama**

Metni yatay olarak hizalamak için [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesinin [**HorizontalAlignment**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/horizontalalignment) özelliğini kullanın

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.cs" >}}

#### **Dikey Hizalama**

Yatay hizalama ile benzer şekilde metni dikey olarak hizalamak için [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesinin [**VerticalAlignment**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/verticalalignment) özelliğini kullanın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.cs" >}}

#### **Girinti**

Hücredeki metnin girinti seviyesini [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesinin [**IndentLevel**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/indentlevel) özelliği ile ayarlamak mümkündür.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Indentation-1.cs" >}}

#### **Yönlendirme**

Hücrede metnin yönlendirmesini (döndürme) [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesinin [**RotationAngle**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/rotationangle) özelliği ile ayarlayın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Orientation-1.cs" >}}

#### **Metin Kontrolü**

Aşağıdaki bölüm metin kaydırma, sığdırmayı daraltma ve diğer biçimlendirme seçeneklerini ayarlayarak metni nasıl kontrol edeceğinizi tartışmaktadır.

##### **Metni Kaydırma**

Hücrede metni kaydırmak onu okumayı kolaylaştırır: hücrenin yüksekliği, metni kesmek yerine veya yan hücrelere taşmak yerine tüm metni sığdırmak için ayarlanır. Metin kaydırma özelliğini [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesinin [**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped) özelliği ile açın veya kapatın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

##### **Sığdırmayı Daraltma**

Bir alanın metnini kaydırmak için bir seçenek, metni hücre boyutlarına sığdırmak için metin boyutunu küçültmektir. Bu, **true** olarak [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesinin [**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped) özelliği ile ayarlanır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.cs" >}}

##### **Hücreleri Birleştirme**

Microsoft Excel gibi, Aspose.Cells birkaç hücreyi birleştirme işlemine destek verir. Aspose.Cells bu göreve iki yaklaşım sağlar. Bir yol, [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonunun [**Merge**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) yöntemini çağırmaktır. [**Merge**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) yöntemi hücreleri birleştirmek için aşağıdaki parametreleri alır:

- İlk satır: Birleştirmeye başlamak için ilk satır.
- İlk sütun: Birleştirmeye başlamak için ilk sütun.
- Satır sayısı: Birleştirilecek satır sayısı.
- Sütun sayısı: Birleştirilecek sütun sayısı.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}

Diğer yol, öncelikle [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonunun [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) yöntemini çağırmak ve birleştirilecek hücrelerin aralığını oluşturmaktır. [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) yöntemi yukarıdaki [**Merge**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) yönteminin aynı parametre setini alır ve bir [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) nesnesi döndürür. [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) nesnesi ayrıca [**Merge**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) yöntemi sağlar, bu yöntem [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) nesnesinde belirtilen aralığı birleştirir.

##### **Metin Yönü**

Hücrelerdeki metnin okuma sırasını ayarlamak mümkündür. Okuma sırası, karakterlerin, kelimelerin vb. görüntülendiği görsel sıradır. Örneğin, İngilizce soldan sağa bir dil iken Arapça sağdan sola bir dildir.

Okuma sırası, [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesinin [**TextDirection**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/textdirection) özelliği ile ayarlanır. Aspose.Cells, [**TextDirectionType**](https://reference.aspose.com/cells/net/aspose.cells/textdirectiontype) numaralandırmasında önceden tanımlanmış metin yönü türlerini sağlar.

|**Metin Yönü Türleri**|**Açıklama**|
| :- | :- |
|Context|Girilen ilk karakterin diline uygun okuma sırası|
|LeftToRight|Soldan sağa okuma sırası|
|RightToLeft|Sağdan sola okuma sırası|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChangeTextDirection-1.cs" >}}

## **Gelişmiş Konular**
- [Hücre Düzenini Değiştirme ve Mevcut Biçimlendirmeyi Koruma](/cells/tr/net/change-cells-alignment-and-keep-existing-formatting/)
- [Satır Sonları ve Metin Kaydırma](/cells/tr/net/line-breaks-and-text-wrapping/)

{{< app/cells/assistant language="csharp" >}}
