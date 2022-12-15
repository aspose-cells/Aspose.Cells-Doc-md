---
title: Hizalama Ayarları
type: docs
weight: 20
url: /tr/java/cells-alignment-settings/
---
## **Hizalama Ayarlarını Yapılandırma**

## **Microsoft Excel'deki hizalama ayarları**

Hücreleri biçimlendirmek için Microsoft Excel'i kullanan herkes, Microsoft Excel'deki hizalama ayarlarına aşina olacaktır.

Yukarıdaki şekilde görebileceğiniz gibi, farklı hizalama seçenekleri vardır:

- Metin hizalama (yatay ve dikey)
- Girinti.
- Oryantasyon.
- Metin kontrolü.
- Metin yönü.

Bu hizalama ayarlarının tümü Aspose.Cells tarafından tam olarak desteklenmektedir ve aşağıda daha ayrıntılı olarak ele alınmıştır.

## **Aspose.Cells'deki hizalama ayarları**

 Aspose.Cells sağlar[**Stil Al**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle) ve[**SetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle) için yöntemler[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) bir hücrenin biçimlendirmesini almak ve ayarlamak için kullanılan sınıf. bu[**stil**](https://reference.aspose.com/cells/java/com.aspose.cells/style)class, hizalama ayarlarını yapılandırmak için yararlı özellikler sağlar.

 kullanarak herhangi bir metin hizalama türünü seçin.[**Metin Hizalama Türü**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype) numaralandırma. Ön tanımlı metin hizalama türleri[**Metin Hizalama Türü**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype)numaralandırma şunlardır:

|**Metin Hizalama Türleri**|**Tanım**|
|:- |:- |
|Alt|Alt metin hizalamasını temsil eder|
|merkez|Merkez metin hizalamasını temsil eder|
|Merkez Boyunca|Metin hizalaması boyunca merkezi temsil eder|
|dağıtılmış|Dağıtılmış metin hizalamasını temsil eder|
|Doldurmak|Dolgu metni hizalamasını temsil eder|
|Genel|Genel metin hizalamasını temsil eder|
|Savunmak|Yaslanmış metin hizalamasını temsil eder|
|Ayrıldı|Sola metin hizalamasını temsil eder|
|Doğru|Doğru metin hizalamasını temsil eder|
|Tepe|Üst metin hizalamasını temsil eder|
|GerekçelendirilmişDüşük|Metni, Arapça metin için ayarlanmış bir kashida uzunluğuyla hizalar.|
|Tayland Dağıtılmış|Tayca metni özellikle dağıtır, çünkü her karakter bir kelime olarak ele alınır.|

{{% alert color="primary" %}}

 Yasla dağıtılmış ayarını şunu kullanarak da uygulayabilirsiniz:[**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsJustifyDistributed) Emlak.

{{% /alert %}}

## **Yatay, Dikey Hizalama ve Girinti**

 Kullan[**Yatay hizalama**](https://reference.aspose.com/cells/java/com.aspose.cells/style#horizontalalignment) metni yatay olarak hizalama özelliği ve[**Dikey hizalama**](https://reference.aspose.com/cells/java/com.aspose.cells/style#verticalalignment)Metni dikey olarak hizalama özelliği.
 Bir hücredeki metnin girinti düzeyini ayarlamak mümkündür.[**Girinti Düzeyi**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IndentLevel) Emlak
ve tt yalnızca Yatay hizalama sola veya sağa olduğunda etkilidir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-1.java" >}}


## **Oryantasyon**

 ile bir hücredeki metnin yönünü (döndürme) ayarlayın.[**Dönüş açısı**](https://reference.aspose.com/cells/java/com.aspose.cells/style#RotationAngle)Emlak.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-Orientation-1.java" >}}

## **Metin Kontrolü**

Aşağıdaki bölümde, metin kaydırma, sığdırmak için küçültme ve diğer biçimlendirme seçeneklerini ayarlayarak metnin nasıl kontrol edileceği anlatılmaktadır.

### **Metni Kaydırma**

 Metni bir hücreye kaydırmak okumayı kolaylaştırır: Hücrenin yüksekliği, onu kesmek veya bitişik hücrelere dökmek yerine tüm metne sığacak şekilde ayarlanır. ile metin kaydırmayı açık veya kapalı olarak ayarlayın.[**metin sarılmış mı**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped)Emlak.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LineBreakTextWrapping-WrapText-1.java" >}}

### **Sığdırmak İçin Küçültmek**

 Metni bir alana kaydırma seçeneği, metin boyutunu bir hücrenin boyutlarına sığacak şekilde küçültmektir. Bu ayarlanarak yapılır.[**Sığdırmak için küçültmek**](https://reference.aspose.com/cells/java/com.aspose.cells/style#ShrinkToFit) Emlak. ile**doğru**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ShrinkingToFit-1.java" >}}

### **Birleştirme Cells**

 Microsoft Excel gibi, Aspose.Cells de birkaç hücrenin tek hücrede birleştirilmesini destekler. Aspose.Cells, bu görev için iki yaklaşım sağlar. Bunun bir yolu,[**Birleştirmek**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)) yöntem. Yöntem, hücreleri birleştirmek için aşağıdaki parametreleri alır:

- İlk satır: Birleştirmenin başlayacağı ilk satır.
- İlk sütun: birleştirmeye başlayacağınız ilk sütun.
- Satır sayısı: birleştirilecek satır sayısı.
- Sütun sayısı: birleştirilecek sütun sayısı.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "MergingCellsInWorksheet.-1.java" >}}


### **Metin yönü**

Hücrelerdeki metnin okuma sırasını ayarlamak mümkündür. Okuma sırası, karakterlerin, kelimelerin vb. görüntülendiği görsel sıradır. Örneğin, İngilizce soldan sağa bir dilken, Arapça sağdan sola bir dildir.

 Okuma sırası ile ayarlanır[**Metin yönü**](https://reference.aspose.com/cells/java/com.aspose.cells/style#TextDirection) Emlak. Aspose.Cells, önceden tanımlanmış metin yönü türleri sağlar.[**Metin Yönü Türü**](https://reference.aspose.com/cells/java/com.aspose.cells/TextDirection)numaralandırma.

|**Metin Yönü Türleri**|**Tanım**|
|:- |:- |
|Bağlam|İlk girilen karakterin diliyle tutarlı okuma sırası|
|Soldan sağa|Soldan sağa okuma sırası|
|Sağdan sola|Sağdan sola okuma sırası|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ChangeTextDirection-1.java" >}}

## **ileri konular**
- [Cells Hizalamasını Değiştirin ve Mevcut Biçimlendirmeyi Koruyun](/cells/tr/java/change-cells-alignment-and-keep-existing-formatting/)
- [Satır Sonları ve Metin Sarma](/cells/tr/java/line-breaks-and-text-wrapping/)
