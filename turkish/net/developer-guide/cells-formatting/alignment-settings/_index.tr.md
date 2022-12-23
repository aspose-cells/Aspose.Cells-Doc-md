---
title: Hizalama Ayarları
type: docs
weight: 20
url: /tr/net/cells-alignment-settings/
---
## **Hizalama Ayarlarını Yapılandırma**

### **Microsoft Excel'deki hizalama ayarları**

Hücreleri biçimlendirmek için Microsoft Excel'i kullanan herkes, Microsoft Excel'deki hizalama ayarlarına aşina olacaktır.

Yukarıdaki şekilde görebileceğiniz gibi, farklı hizalama seçenekleri vardır:

- Metin hizalama (yatay ve dikey)
- Girinti.
- Oryantasyon.
- Metin kontrolü.
- Metin yönü.

Bu hizalama ayarlarının tümü Aspose.Cells tarafından tam olarak desteklenmektedir ve aşağıda daha ayrıntılı olarak ele alınmıştır.

### **Aspose.Cells'deki hizalama ayarları**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , bu bir Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf bir sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Toplamak. İçindeki her öğe[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyon bir nesneyi temsil eder[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)sınıf.

 Aspose.Cells sağlar[**Stil Al**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) ve[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) için yöntemler[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) bir hücrenin biçimlendirmesini almak ve ayarlamak için kullanılan sınıf. bu[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style)class, hizalama ayarlarını yapılandırmak için yararlı özellikler sağlar.

 kullanarak herhangi bir metin hizalama türünü seçin.[**Metin Hizalama Türü**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype) numaralandırma. Ön tanımlı metin hizalama türleri[**Metin Hizalama Türü**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype)numaralandırma şunlardır:

|**Metin Hizalama Türleri**|**Açıklama**|
|:- |:- |
|Alt kısım|Alt metin hizalamasını temsil eder|
|merkez|Merkez metin hizalamasını temsil eder|
|Merkez Boyunca|Metin hizalaması boyunca merkezi temsil eder|
|dağıtılmış|Dağıtılmış metin hizalamasını temsil eder|
|Doldurmak|Dolgu metni hizalamasını temsil eder|
|Genel|Genel metin hizalamasını temsil eder|
|Savunmak|Yaslanmış metin hizalamasını temsil eder|
|Sol|Sola metin hizalamasını temsil eder|
|Doğru|Doğru metin hizalamasını temsil eder|
|Tepe|Üst metin hizalamasını temsil eder|
|GerekçelendirilmişDüşük|Metni, Arapça metin için ayarlanmış bir kashida uzunluğuyla hizalar.|
|Tayland Dağıtılmış|Tayca metni özellikle dağıtır, çünkü her karakter bir kelime olarak ele alınır.|

{{% alert color="primary" %}}

 Yasla dağıtılmış ayarını şunu kullanarak da uygulayabilirsiniz:[**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/isjustifydistributed) Emlak.

{{% /alert %}}

#### **Yatay hizalama**

 Kullan[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnenin[**Yatay hizalama**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/horizontalalignment)Metni yatay olarak hizalama özelliği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.cs" >}}

#### **Dikey hizalama**

 Yatay hizalamaya benzer şekilde,[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnenin[**Dikey hizalama**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/verticalalignment)Metni dikey olarak hizalama özelliği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.cs" >}}

#### **Girinti**

 Bir hücredeki metnin girinti düzeyini ayarlamak mümkündür.[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnenin[**Girinti Düzeyi**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/indentlevel)Emlak.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Indentation-1.cs" >}}

#### **Oryantasyon**

 ile bir hücredeki metnin yönünü (döndürme) ayarlayın.[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnenin[**Dönüş açısı**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/rotationangle)Emlak.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Orientation-1.cs" >}}

#### **Metin Kontrolü**

Aşağıdaki bölümde, metin kaydırma, sığdırmak için küçültme ve diğer biçimlendirme seçeneklerini ayarlayarak metnin nasıl kontrol edileceği anlatılmaktadır.

##### **Metni Kaydırma**

 Metni bir hücreye kaydırmak okumayı kolaylaştırır: Hücrenin yüksekliği, onu kesmek veya bitişik hücrelere dökmek yerine tüm metne sığacak şekilde ayarlanır. ile metin kaydırmayı açık veya kapalı olarak ayarlayın.[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnenin[**metin sarılmış mı**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)Emlak.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

##### **Sığdırmak İçin Küçültmek**

 Metni bir alana kaydırma seçeneği, metin boyutunu bir hücrenin boyutlarına sığacak şekilde küçültmektir. Bu ayarlanarak yapılır.[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnenin[**metin sarılmış mı**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped) mülkiyet**doğru**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.cs" >}}

##### **Birleştirme Cells**

 Microsoft Excel gibi, Aspose.Cells de birkaç hücrenin tek hücrede birleştirilmesini destekler. Aspose.Cells, bu görev için iki yaklaşım sağlar. Bunun bir yolu,[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonun[**Birleştirmek**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) yöntem. bu[**Birleştirmek**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index)yöntemi, hücreleri birleştirmek için aşağıdaki parametreleri alır:

- İlk satır: Birleştirmenin başlayacağı ilk satır.
- İlk sütun: birleştirmeye başlayacağınız ilk sütun.
- Satır sayısı: birleştirilecek satır sayısı.
- Sütun sayısı: birleştirilecek sütun sayısı.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}

 Diğer yol, önce[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonun[**Yaratma Aralığı**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) birleştirilecek bir hücre aralığı oluşturma yöntemi. bu[**Yaratma Aralığı**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) yöntemi ile aynı parametre kümesini alır.[**Birleştirmek**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) yukarıda tartışılan yöntem ve bir döndürür[**Menzil**](https://reference.aspose.com/cells/net/aspose.cells/range) nesne. bu[**Menzil**](https://reference.aspose.com/cells/net/aspose.cells/range) nesne ayrıca bir[**Birleştirmek**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) belirtilen aralığı birleştiren yöntem[**Menzil**](https://reference.aspose.com/cells/net/aspose.cells/range)nesne.

##### **Metin yönü**

Hücrelerdeki metnin okuma sırasını ayarlamak mümkündür. Okuma sırası, karakterlerin, kelimelerin vb. görüntülendiği görsel sıradır. Örneğin, İngilizce soldan sağa bir dilken, Arapça sağdan sola bir dildir.

 Okuma sırası ile ayarlanır[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnenin[**Metin yönü**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/textdirection) Emlak. Aspose.Cells, önceden tanımlanmış metin yönü türleri sağlar.[**Metin Yönü Türü**](https://reference.aspose.com/cells/net/aspose.cells/textdirectiontype)numaralandırma.

|**Metin Yönü Türleri**|**Açıklama**|
|:- |:- |
|Bağlam|İlk girilen karakterin diliyle tutarlı okuma sırası|
|Soldan sağa|Soldan sağa okuma sırası|
|Sağdan sola|Sağdan sola okuma sırası|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChangeTextDirection-1.cs" >}}

## **ileri konular**
- [Cells Hizalamasını Değiştirin ve Mevcut Biçimlendirmeyi Koruyun](/cells/tr/net/change-cells-alignment-and-keep-existing-formatting/)
- [Satır Sonları ve Metin Sarma](/cells/tr/net/line-breaks-and-text-wrapping/)

