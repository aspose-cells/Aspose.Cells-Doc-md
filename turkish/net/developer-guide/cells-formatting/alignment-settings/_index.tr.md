---
title: Hizalama Ayarları
description: Aspose.Cells kitaplığında metnin düzenini ve görünümünü ayarlamak için hücre hizalama ayarlarını kullanabilirsiniz. Yatay hizalama, dikey hizalama ve metin kaydırma gibi ayarları düzenleyerek metnin hücrelerde nasıl aktığı üzerinde daha fazla kontrole sahip olursunuz. Bu belge, hücre hizalama ayarları için Aspose.Cells'in nasıl kullanılacağını hızlı bir şekilde kavramanıza yardımcı olacak ayrıntılı adımlar ve örnek kod sağlayacaktır.
keywords: Aspose.Cells, cell alignment, horizontal alignment, vertical alignment, text wrapping
type: docs
weight: 20
url: /tr/net/cells-alignment-settings/
---
##  **Hizalama Ayarlarını Yapılandırma**

###  **Microsoft Excel'deki hizalama ayarları**

Hücreleri biçimlendirmek için Microsoft Excel'i kullanan herkes, Microsoft Excel'deki hizalama ayarlarına aşina olacaktır.

Yukarıdaki şekilde görebileceğiniz gibi, farklı türde hizalama seçenekleri vardır:

- Metin hizalaması (yatay ve dikey)
- Girinti.
- Oryantasyon.
- Metin kontrolü.
- Metin yönü.

Bu hizalama ayarlarının tümü Aspose.Cells tarafından tam olarak desteklenmektedir ve aşağıda daha ayrıntılı olarak ele alınmaktadır.

###  **Aspose.Cells'deki hizalama ayarları**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , bu bir Excel dosyasını temsil eder.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**Çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Excel dosyasındaki her çalışma sayfasına erişime izin veren koleksiyon. Bir çalışma sayfası şu şekilde temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Toplamak. İçindeki her öğe[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyon bir nesneyi temsil eder[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)sınıf.

 Aspose.Cells sağlar[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) Ve[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) için yöntemler[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Bir hücrenin biçimlendirmesini almak ve ayarlamak için kullanılan sınıf.[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)sınıfı, hizalama ayarlarını yapılandırmak için kullanışlı özellikler sağlar.

 kullanarak herhangi bir metin hizalama türünü seçin.[**MetinAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype) numaralandırma. Önceden tanımlanmış metin hizalama türleri[**MetinAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype)numaralandırma şunlardır:

|**Metin Hizalama Türleri**|**Tanım**|
| :- | :- |
|Alt|Alt metin hizalamasını temsil eder|
|Merkez|Orta metin hizalamasını temsil eder|
|MerkezKarşısında|Metin hizalaması boyunca merkezi temsil eder|
|Dağıtılmış|Dağıtılmış metin hizalamasını temsil eder|
|Doldurmak|Dolgu metni hizalamasını temsil eder|
|Genel|Genel metin hizalamasını temsil eder|
|Savunmak|Metin hizalamasını yaslamayı temsil eder|
|Sol|Sola metin hizalamasını temsil eder|
|Sağ|Sağ metin hizalamasını temsil eder|
|Tepe|Üst metin hizalamasını temsil eder|
|HaklıDüşük|Metni Arapça metin için ayarlanmış kashida uzunluğuyla hizalar.|
|Tay Dağıtılmış|Tayca metinleri özellikle dağıtır çünkü her karakter bir kelime olarak ele alınır.|

{{% alert color="primary" %}}

 Dağıtılmış yasla ayarını kullanarak da uygulayabilirsiniz.[**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/isjustifydistributed) mülk.

{{% /alert %}}

####  **Yatay hizalama**

 Kullan[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnenin[**Yatay hizalama**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/horizontalalignment)Metni yatay olarak hizalama özelliği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.cs" >}}

####  **Dikey hizalama**

 Yatay hizalamaya benzer şekilde,[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnenin[**Dikey hizalama**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/verticalalignment)Metni dikey olarak hizalama özelliği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.cs" >}}

####  **Girinti**

 Bir hücredeki metnin girinti düzeyini ayarlamak mümkündür.[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnenin[**Girinti Düzeyi**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/indentlevel)mülk.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Indentation-1.cs" >}}

####  **Oryantasyon**

 Bir hücredeki metnin yönünü (döndürmesini) aşağıdaki düğmeyle ayarlayın:[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnenin[**Dönüş açısı**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/rotationangle)mülk.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Orientation-1.cs" >}}

####  **Metin Kontrolü**

Aşağıdaki bölümde metin sarma, sığacak şekilde küçültme ve diğer biçimlendirme seçeneklerini ayarlayarak metnin nasıl kontrol edileceği anlatılmaktadır.

#####  **Metin Sarma**

 Metni bir hücreye sarmak okumayı kolaylaştırır: hücrenin yüksekliği, metni kesmek veya bitişik hücrelere taşmak yerine tüm metne sığacak şekilde ayarlanır. Metin kaydırmayı açık veya kapalı olarak ayarlayın.[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnenin[**Metin Sarılmış**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)mülk.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

#####  **Sığacak Şekilde Küçülüyor**

 Bir alandaki metni sarmalama seçeneği, metin boyutunu hücrenin boyutlarına sığacak şekilde küçültmektir. Bu, ayarlanarak yapılır.[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnenin[**Metin Sarılmış**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)özelliği *true** olarak değiştirin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.cs" >}}

#####  **Birleştirme Cells**

 Microsoft Excel gibi, Aspose.Cells de birkaç hücrenin tek bir hücrede birleştirilmesini destekler. Aspose.Cells bu göreve iki yaklaşım sunuyor. Bunun bir yolu, telefonu aramaktır.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Koleksiyonun[**Birleştirmek**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) yöntem.[**Birleştirmek**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index)yöntem hücreleri birleştirmek için aşağıdaki parametreleri alır:

- İlk satır: birleştirmenin başlayacağı ilk satır.
- İlk sütun: birleştirmenin başlayacağı ilk sütun.
- Satır sayısı: birleştirilecek satır sayısı.
- Sütun sayısı: birleştirilecek sütun sayısı.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}

Diğer yol ise ilk önce telefonu aramaktır.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Koleksiyonun[**Aralık Oluştur**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) Birleştirilecek hücre aralığını oluşturma yöntemi.[**Aralık Oluştur**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) yöntem, yöntem ile aynı parametre kümesini alır.[**Birleştirmek**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) yukarıda tartışılan yöntem ve bir döndürür[**Menzil**](https://reference.aspose.com/cells/net/aspose.cells/range) nesne.[**Menzil**](https://reference.aspose.com/cells/net/aspose.cells/range) nesne aynı zamanda bir sağlar[**Birleştirmek**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) Belirtilen aralığı birleştiren yöntem[**Menzil**](https://reference.aspose.com/cells/net/aspose.cells/range)nesne.

#####  **Metin yönü**

Hücrelerdeki metnin okunma sırasını ayarlamak mümkündür. Okuma sırası, karakterlerin, kelimelerin vb. görüntülendiği görsel sıradır. Örneğin İngilizce soldan sağa doğru bir dil iken Arapça sağdan sola doğru bir dildir.

 Okuma sırası şu şekilde ayarlanır:[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnenin[**Metin yönü**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/textdirection) mülk. Aspose.Cells, önceden tanımlanmış metin yönü türlerini sağlar.[**Metin Yönü Türü**](https://reference.aspose.com/cells/net/aspose.cells/textdirectiontype)numaralandırma.

|**Metin Yönü Türleri**|**Tanım**|
| :- | :- |
|Bağlam|İlk girilen karakterin diliyle tutarlı okuma sırası|
|Soldan sağa|Soldan sağa okuma sırası|
|Sağdan sola|Sağdan sola okuma sırası|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChangeTextDirection-1.cs" >}}

##  **İleri konular**
- [Cells Hizalamasını Değiştirin ve Mevcut Biçimlendirmeyi Koruyun](/cells/tr/net/change-cells-alignment-and-keep-existing-formatting/)
- [Satır Sonları ve Metin Kaydırma](/cells/tr/net/line-breaks-and-text-wrapping/)

