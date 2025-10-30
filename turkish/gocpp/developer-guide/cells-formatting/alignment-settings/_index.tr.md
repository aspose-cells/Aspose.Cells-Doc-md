---
title: Golang ile Hizalama Ayarları (Alignment Settings)
linktitle: Uyum Ayarları
description: Aspose.Cells kütüphanesinde, metnin düzeni ve gösterimi ayarlamak için hücre uygunluk ayarlarını kullanabilirsiniz. Yatay hizalama, dikey hizalama ve metin kaydırma gibi ayarları ayarlayarak, metnin hücrelerde nasıl akacağı konusunda daha fazla kontrol sahibi olursunuz. Bu belge, hücre uygunluk ayarlarını nasıl kullanacağınızı hızlıca öğrenmenize ve örnek kodlarıyla adım adım rehberlik etmesine yardımcı olacaktır.
keywords: Aspose.Cells, hücre uygunluk, yatay hizalama, dikey hizalama, metin kaydırma
type: docs
weight: 20
url: /tr/go-cpp/cells-alignment-settings/
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

Aspose.Cells, bir Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfı, Excel dosyasındaki her bir çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, bir [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) koleksiyonu sağlar. [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfının bir örneğini temsil eder.

Aspose.Cells, [**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/) ve [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) metodlarını, [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) sınıfı için bir hücrenin biçimlendirmesini almak ve ayarlamak için kullanır. [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) sınıfı, hizalama ayarlarını yapılandırmak için kullanışlı özellikler sağlar.

[**TextAlignmentType**](https://reference.aspose.com/cells/go-cpp/textalignmenttype/) numarasını kullanarak herhangi bir metin hizalama türünü seçin. [**TextAlignmentType**](https://reference.aspose.com/cells/go-cpp/textalignmenttype/) numarasındaki önceden tanımlanmış metin hizalama türleri:

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

Ayrıca [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/go-cpp/style/isjustifydistributed/) özelliğini kullanarak düzgün dağıtılmış ayarını uygulayabilirsiniz.

{{% /alert %}}

#### **Yatay Hizalama**

Metni yatay olarak hizalamak için [**Style**](https://reference.aspose.com/cells/go-cpp/style/) nesnesinin [**GetHorizontalAlignment()**](https://reference.aspose.com/cells/go-cpp/style/gethorizontalalignment/) özelliğini kullanın

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings.go" >}}
#### **Dikey Hizalama**

Yatay hizalama ile benzer şekilde metni dikey olarak hizalamak için [**Style**](https://reference.aspose.com/cells/go-cpp/style/) nesnesinin [**GetVerticalAlignment()**](https://reference.aspose.com/cells/go-cpp/style/getverticalalignment/) özelliğini kullanın.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-1.go" >}}
#### **Girinti**

Hücredeki metnin girinti seviyesini [**Style**](https://reference.aspose.com/cells/go-cpp/style/) nesnesinin [**GetIndentLevel()**](https://reference.aspose.com/cells/go-cpp/style/getindentlevel/) özelliği ile ayarlamak mümkündür.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-2.go" >}}
#### **Yönlendirme**

Hücrede metnin yönlendirmesini (döndürme) [**Style**](https://reference.aspose.com/cells/go-cpp/style/) nesnesinin [**GetRotationAngle()**](https://reference.aspose.com/cells/go-cpp/style/getrotationangle/) özelliği ile ayarlayın.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-3.go" >}}
#### **Metin Kontrolü**

Aşağıdaki bölüm metin kaydırma, sığdırmayı daraltma ve diğer biçimlendirme seçeneklerini ayarlayarak metni nasıl kontrol edeceğinizi tartışmaktadır.

##### **Metni Kaydırma**

Hücrede metni kaydırmak onu okumayı kolaylaştırır: hücrenin yüksekliği, metni kesmek yerine veya yan hücrelere taşmak yerine tüm metni sığdırmak için ayarlanır. Metin kaydırma özelliğini [**Style**](https://reference.aspose.com/cells/go-cpp/style/) nesnesinin [**IsTextWrapped**](https://reference.aspose.com/cells/go-cpp/style/istextwrapped/) özelliği ile açın veya kapatın.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-4.go" >}}
##### **Sığdırmayı Daraltma**

Bir alanın metnini kaydırmak için bir seçenek, metni hücre boyutlarına sığdırmak için metin boyutunu küçültmektir. Bu, **true** olarak [**Style**](https://reference.aspose.com/cells/go-cpp/style/) nesnesinin [**IsTextWrapped**](https://reference.aspose.com/cells/go-cpp/style/istextwrapped/) özelliği ile ayarlanır.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-5.go" >}}
##### **Hücreleri Birleştirme**

Microsoft Excel gibi, Aspose.Cells birkaç hücreyi birleştirme işlemine destek verir. Aspose.Cells bu göreve iki yaklaşım sağlar. Bir yol, [**GetCells()**](https://reference.aspose.com/cells/go-cpp/worksheet/getcells/) koleksiyonunun [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) yöntemini çağırmaktır. [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) yöntemi hücreleri birleştirmek için aşağıdaki parametreleri alır:

- İlk satır: Birleştirmeye başlamak için ilk satır.
- İlk sütun: Birleştirmeye başlamak için ilk sütun.
- Satır sayısı: Birleştirilecek satır sayısı.
- Sütun sayısı: Birleştirilecek sütun sayısı.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-6.go" >}}
Diğer yol, öncelikle [**GetCells()**](https://reference.aspose.com/cells/go-cpp/worksheet/getcells/) koleksiyonunun [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) yöntemini çağırmak ve birleştirilecek hücrelerin aralığını oluşturmaktır. [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) yöntemi yukarıdaki [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) yönteminin aynı parametre setini alır ve bir [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) nesnesi döndürür. [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) nesnesi ayrıca [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/) yöntemi sağlar, bu yöntem [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) nesnesinde belirtilen aralığı birleştirir.

##### **Metin Yönü**

Hücrelerdeki metnin okuma sırasını ayarlamak mümkündür. Okuma sırası, karakterlerin, kelimelerin vb. görüntülendiği görsel sıradır. Örneğin, İngilizce soldan sağa bir dil iken Arapça sağdan sola bir dildir.

Okuma sırası, [**Style**](https://reference.aspose.com/cells/go-cpp/style/) nesnesinin [**GetTextDirection()**](https://reference.aspose.com/cells/go-cpp/style/gettextdirection/) özelliği ile ayarlanır. Aspose.Cells, [**TextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/textdirectiontype/) numaralandırmasında önceden tanımlanmış metin yönü türlerini sağlar.

|**Metin Yönü Türleri**|**Açıklama**|
| :- | :- |
|Context|Girilen ilk karakterin diline uygun okuma sırası|
|LeftToRight|Soldan sağa okuma sırası|
|RightToLeft|Sağdan sola okuma sırası|

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-7.go" >}}
## **Gelişmiş Konular**
- [Hücre Düzenini Değiştirme ve Mevcut Biçimlendirmeyi Koruma](/cells/tr/cpp/change-cells-alignment-and-keep-existing-formatting/)
- [Satır Sonları ve Metin Kaydırma](/cells/tr/cpp/line-breaks-and-text-wrapping/)
