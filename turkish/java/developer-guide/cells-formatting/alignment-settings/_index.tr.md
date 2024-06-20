---
title: Uyum Ayarları
type: docs
weight: 20
url: /tr/java/cells-alignment-settings/
---

## **Hizalama Ayarlarının Yapılandırılması**

## **Microsoft Excel'deki hizalama ayarları**

Hücreleri biçimlendirmek için Microsoft Excel kullanan herkes, Microsoft Excel'deki hizalama ayarlarına aşinadır.

Yukarıdaki şekilden görebileceğiniz gibi, farklı türde hizalama seçenekleri bulunmaktadır:

- Metin hizalama (yatay ve dikey)
- Girinti
- Yönlendirme
- Metin kontrol
- Metin yönü

Bu tüm hizalama ayarları, Aspose.Cells tarafından tamamen desteklenir ve aşağıda daha detaylı olarak tartışılmaktadır.

## **Aspose.Cells'te hizalama ayarları**

Aspose.Cells, [**GetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle) ve [**SetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle) metodlarını, [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıfı için bir hücrenin biçimlendirmesini almak ve ayarlamak için kullanır. [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/style) sınıfı, hizalama ayarlarını yapılandırmak için kullanışlı özellikler sağlar.

[**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype) numarasını kullanarak herhangi bir metin hizalama türünü seçin. [**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype) numarasındaki önceden tanımlanmış metin hizalama türleri:

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

Ayrıca [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsJustifyDistributed) özelliğini kullanarak düzgün dağıtılmış ayarını uygulayabilirsiniz.

{{% /alert %}}

## **Yatay, Dikey Hiza ve Girinti**

Metni yatay hizalamak için [**HorizontalAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/style#horizontalalignment) özelliğini ve metni dikey hizalamak için [**VerticalAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/style#verticalalignment) özelliğini kullanın.
Bir hücrede metnin girinti düzeyini [**IndentLevel**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IndentLevel) özelliği ile ayarlamak mümkündür. 
Ve yalnızca yatay hizalama sol veya sağ olduğunda etkilidir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-1.java" >}}


## **Yönlendirme**

Bir hücrede metnin yönlendirmesini (döndürme) [**RotationAngle**](https://reference.aspose.com/cells/java/com.aspose.cells/style#RotationAngle) özelliği ile ayarlayın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-Orientation-1.java" >}}

## **Metin Kontrolü**

Aşağıdaki bölüm metin kaydırma, sığdırmayı daraltma ve diğer biçimlendirme seçeneklerini ayarlayarak metni nasıl kontrol edeceğinizi tartışmaktadır.

### **Metni Kaydırma**

Bir hücredeki metni kaydırmak metni okumayı kolaylaştırır: hücrenin yüksekliği, metni kesmek yerine veya bitişik hücrelere taşmak yerine tüm metni sığdırmak için ayarlanır. Metin kaydırma özelliği ile metin kaydırma açık veya kapalı olarak ayarlayın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LineBreakTextWrapping-WrapText-1.java" >}}

### **Sığdırmayı Daraltma**

Bir alanda metni kaydırmak için bir seçenek, metni bir hücrenin boyutlarına sığdırmak için metin boyutunu küçültmektir. Bu, [**ShrinkToFit**](https://reference.aspose.com/cells/java/com.aspose.cells/style#ShrinkToFit) özelliğini **true** olarak ayarlayarak yapılır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ShrinkingToFit-1.java" >}}

### **Hücreleri Birleştirme**

Microsoft Excel gibi, Aspose.Cells birçok hücreyi tek bir hücre olarak birleştirmeyi destekler. Aspose.Cells bu görevi yerine getirmek için iki yaklaşım sağlar. Bu görevi yerine getirmenin bir yolu [**Merge**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)) yöntemini çağırmaktır. Yöntem, hücreleri birleştirmek için aşağıdaki parametreleri alır:

- İlk satır: Birleştirmeye başlamak için ilk satır.
- İlk sütun: Birleştirmeye başlamak için ilk sütun.
- Satır sayısı: Birleştirilecek satır sayısı.
- Sütun sayısı: Birleştirilecek sütun sayısı.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "MergingCellsInWorksheet.-1.java" >}}


### **Metin Yönü**

Hücrelerdeki metnin okuma sırasını ayarlamak mümkündür. Okuma sırası, karakterlerin, kelimelerin vb. görüntülendiği görsel sıradır. Örneğin, İngilizce soldan sağa bir dil iken Arapça sağdan sola bir dildir.

Okuma sırası [**TextDirection**](https://reference.aspose.com/cells/java/com.aspose.cells/style#TextDirection) özelliği ile ayarlanır. Aspose.Cells, [**TextDirectionType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextDirection) numaralı numaralandırmada önceden tanımlanmış metin yönü tiplerini sağlar.

|**Metin Yönü Türleri**|**Açıklama**|
| :- | :- |
|Context|Girilen ilk karakterin diline uygun okuma sırası|
|LeftToRight|Soldan sağa okuma sırası|
|RightToLeft|Sağdan sola okuma sırası|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ChangeTextDirection-1.java" >}}

## **Gelişmiş Konular**
- [Hücre Düzenini Değiştirme ve Mevcut Biçimlendirmeyi Koruma](/cells/tr/java/change-cells-alignment-and-keep-existing-formatting/)
- [Satır Sonları ve Metin Kaydırma](/cells/tr/java/line-breaks-and-text-wrapping/)
