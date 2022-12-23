---
title: Kenarlık Ayarları
type: docs
weight: 40
url: /tr/net/cells-border-settings/
---
## **Cells'e Kenarlık Ekleme**

Microsoft Excel, kullanıcıların kenarlık ekleyerek hücreleri biçimlendirmesine olanak tanır. Kenarlığın türü, nereye eklendiğine bağlıdır. Örneğin, bir üst kenarlık bir hücrenin en üst konumuna eklenir. Kullanıcılar ayrıca kenarlıkların çizgi stilini ve rengini değiştirebilir.

Aspose.Cells ile geliştiriciler, Microsoft Excel'de olduğu gibi aynı esnek şekilde kenarlıklar ekleyebilir ve görünüşlerini özelleştirebilir.

### **Cells'e Kenarlık Ekleme**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Toplamak. İçindeki her öğe[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyon bir nesneyi temsil eder[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)sınıf.

 Aspose.Cells şunları sağlar:[**Stil Al**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index)yöntemi[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)sınıf. bu[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index)Yöntem, bir hücrenin biçimlendirme stilini ayarlamak için kullanılır. bu[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style)class, hücrelere kenarlık eklemek için özellikler sağlar.

#### **Cell'e Kenarlık Ekleme**

Geliştiriciler, kullanarak bir hücreye kenarlıklar ekleyebilir[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnenin[**Kenarlıklar**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) Toplamak. Kenarlık türü, bir dizin olarak iletilir.[**Kenarlıklar**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) Toplamak. Tüm kenarlık türleri,[**Kenarlık Türü**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) numaralandırma.

**Sınır numaralandırma**

|**Kenarlık Türleri**|**Açıklama**|
|:- |:- |
|Alt sınır|Bir alt sınır çizgisi|
|Çapraz Aşağı|Sol üstten sağ alta çapraz bir çizgi|
|çapraz Yukarı|Sol alttan sağ üste çapraz bir çizgi|
|Sol Sınır|Bir sol sınır çizgisi|
|Sağ Sınır|Sağ sınır çizgisi|
|Üst Sınır|Bir üst sınır çizgisi|

bu[**Kenarlıklar**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)koleksiyon tüm sınırları saklar. Her sınırda[**Kenarlıklar**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) koleksiyon bir ile temsil edilir[**Sınır**](https://reference.aspose.com/cells/net/aspose.cells/border) iki özellik sağlayan nesne,[**Renk**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color) ve[**Çizgi Stili**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle)Sırasıyla bir kenarlığın çizgi rengini ve stilini ayarlamak için.

Kenarlığın çizgi rengini ayarlamak için, Renk numaralandırmasını (.NET Çerçevesinin bir parçası) kullanarak bir renk seçin ve bunu Kenarlık nesnesinin Renk özelliğine atayın.

 Kenarlığın çizgi stili, menüden bir çizgi stili seçilerek ayarlanır.[**Hücre Sınır Türü**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)numaralandırma.

**CellBorderType numaralandırma**

|**Çizgi Stilleri**|**Açıklama**|
|:- |:- |
|Çizgi nokta|İnce çizgi noktalı çizgi|
|DashDotDot|İnce çizgi noktalı çizgi|
|kesikli|Kesik çizgi|
|Noktalı|Noktalı çizgi|
|Çift|Çift çizgi|
|Saç|Saç çizgisi|
|Orta Çizgi Nokta|Orta kesik noktalı çizgi|
|Orta Çizgi Nokta Nokta|Orta çizgi noktalı çizgi|
|Orta Kesikli|Orta kesik çizgi|
|Hiçbiri|çizgi yok|
|Orta|orta çizgi|
|Eğimli Çizgi Nokta|Eğimli orta kesikli noktalı çizgi|
|Kalın|Kalın çizgi|
|İnce|İnce çizgi|
Çizgi stillerinden birini seçin ve ardından bunu[**Sınır**](https://reference.aspose.com/cells/net/aspose.cells/border) nesnenin[**Çizgi Stili**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) Emlak.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

Hem çizgi stilini hem de rengi aynı anda ayarlamalısınız. İki diyagonal bordür çizgisi aynı çizgi stiline ve rengine sahip olmalıdır.

{{% /alert %}}

#### **Cells Aralığına Kenarlık Ekleme**

Tek bir hücre yerine bir dizi hücreye kenarlık eklemek de mümkündür. Bunu yapmak için, önce, çağırarak bir hücre aralığı oluşturun.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonun[**Yaratma Aralığı**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) yöntem. Aşağıdaki parametreleri alır:

- İlk Satır, aralığın ilk satırı.
- İlk Sütun, aralığın ilk sütununu temsil eder.
- Satır Sayısı, aralıktaki satır sayısı.
- Sütun Sayısı, aralıktaki sütun sayısı.

 bu[**Yaratma Aralığı**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) yöntem bir döndürür[**Menzil**](https://reference.aspose.com/cells/net/aspose.cells/range) belirtilen hücre aralığını içeren nesne. bu[**Menzil**](https://reference.aspose.com/cells/net/aspose.cells/range) nesne sağlar[**SetOutlineSınır**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) hücre aralığına kenarlık eklemek için aşağıdaki parametreleri alan yöntem:

- **Kenarlık Türü** , kenarlık türü,[**Kenarlık Türü**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)numaralandırma.
- **Çizgi Stili** , sınır çizgisi stili,[**Hücre Sınır Türü**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)numaralandırma.
- **Renk**, Renk numaralandırmasından seçilen çizgi rengi.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}

## **Renkler ve Palet**

Palet, bir görüntü oluştururken kullanılabilecek renk sayısıdır. Bir sunumda standartlaştırılmış bir paletin kullanılması, kullanıcının tutarlı bir görünüm oluşturmasına olanak tanır. Her Microsoft Excel (97-2003) dosyası, bir grafikteki hücrelere, yazı tiplerine, kılavuz çizgilerine, grafik nesnelerine, dolgulara ve çizgilere uygulanabilen 56 renk paletine sahiptir.

Aspose.Cells ile paletin mevcut renklerinin yanı sıra özel renklerin de kullanılması mümkündür. Özel bir renk kullanmadan önce palete ekleyin.

Bu konuda palete özel renklerin nasıl ekleneceği anlatılmaktadır.

### **Palete Özel Renkler Ekleme**

Aspose.Cells, Microsoft Excel'in 56 renk paletini destekler. Palette tanımlanmayan özel bir renk kullanmak için rengi palete ekleyin.

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir sağlar[**Paleti Değiştir**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) paleti değiştirmek üzere özel bir renk eklemek için aşağıdaki parametreleri alan yöntem:

- Özel Renk, eklenecek özel renk.
- Dizin, özel rengin değiştireceği paletteki rengin dizini. 0-55 arasında olmalıdır.

Aşağıdaki örnek, bir yazı tipine uygulamadan önce palete özel bir renk (Orkide) ekler.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

Palet sadece 56 renk içerir. Palete özel bir renk eklediğinizde, palet değiştirilir ve önceki renkle biçimlendirilmiş dosyadaki herhangi bir öğe değiştirilir. Bu yüzden paleti değiştirirken lütfen çok dikkatli olun. Ayrıca, bu yalnızca XLS (Excel 97 - 2003) dosya biçimindeki sınırlamadır, çünkü XLSX veya diğer gelişmiş MS Excel (2007/2010 veya 2013) dosya biçimleri için böyle bir sınırlama yoktur.

{{% /alert %}}


