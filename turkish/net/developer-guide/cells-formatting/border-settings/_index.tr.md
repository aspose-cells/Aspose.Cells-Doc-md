---
title: Kenarlık Ayarları
description: Hücrelerin kenarlık stilini ve rengini ayarlamak için C#'deki Aspose.Cells kitaplığı nasıl kullanılır? Kenarlığın genişliğini, stilini ve rengini ayarlayarak hücrelerin nasıl görüneceği ve görüneceği üzerinde daha fazla kontrole sahip olursunuz.
keywords: Aspose.Cells, Cell Border Settings, C#, Border Width, Border Style, Border Color
type: docs
weight: 40
url: /tr/net/cells-border-settings/
---
##  **Cells'e Kenarlık Ekleme**

Microsoft Excel, kullanıcıların hücreleri kenarlıklar ekleyerek biçimlendirmesine olanak tanır. Kenarlığın türü nereye eklendiğine bağlıdır. Örneğin üst kenarlık, hücrenin en üst konumuna eklenen kenarlıktır. Kullanıcılar ayrıca kenarlıkların çizgi stilini ve rengini de değiştirebilir.

Aspose.Cells ile geliştiriciler, Microsoft Excel'dekiyle aynı esnek yöntemle kenarlıklar ekleyebilir ve görünümlerini özelleştirebilir.

###  **Cells'e Kenarlık Ekleme**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bu bir Microsoft Excel dosyasını temsil eder.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**Çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Excel dosyasındaki her çalışma sayfasına erişime izin veren koleksiyon. Bir çalışma sayfası şu şekilde temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf şunları sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Toplamak. İçindeki her öğe[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyon bir nesneyi temsil eder[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)sınıf.

 Aspose.Cells şunları sağlar[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index)yöntemdeki[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)sınıf.[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index)yöntemi bir hücrenin biçimlendirme stilini ayarlamak için kullanılır.[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)sınıf, hücrelere kenarlık eklemek için özellikler sağlar.

####  **Cell'e Kenarlık Ekleme**

Geliştiriciler, kullanarak bir hücreye kenarlıklar ekleyebilirler.[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnenin[**Kenarlıklar**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) Toplamak. Kenarlık türü bir dizin olarak iletilir.[**Kenarlıklar**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) Toplamak. Tüm kenarlık türleri önceden tanımlanmıştır.[**Kenarlık Türü**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) numaralandırma.

**Sınır numaralandırması**

|**Kenar Çeşitleri**|**Tanım**|
| :- | :- |
|Alt sınır|Bir alt sınır çizgisi|
|ÇaprazAşağı|Sol üstten sağ alta çapraz bir çizgi|
|ÇaprazYukarı|Sol alttan sağ üste çapraz bir çizgi|
|Sol Kenarlık|Sol sınır çizgisi|
|Sağ Kenarlık|Sağ sınır çizgisi|
|Üst Kenarlık|Bir üst sınır çizgisi|

[**Kenarlıklar**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)koleksiyon tüm sınırları saklar. Her sınırda[**Kenarlıklar**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) koleksiyon bir ile temsil edilir[**Sınır**](https://reference.aspose.com/cells/net/aspose.cells/border) iki özellik sağlayan nesne,[**Renk**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color) Ve[**Çizgi Stili**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle)sırasıyla bir kenarlığın çizgi rengini ve stilini ayarlamak için.

Kenarlığın çizgi rengini ayarlamak için Renk numaralandırmasını (.NET Çerçevesinin parçası) kullanarak bir renk seçin ve bunu Kenarlık nesnesinin Renk özelliğine atayın.

 Kenarlığın çizgi stili, menüden bir çizgi stili seçilerek ayarlanır.[**Hücre Kenarlığı Türü**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)numaralandırma.

**CellBorderType numaralandırması**

|**Çizgi Stilleri**|**Tanım**|
| :- | :- |
|Çizgi nokta|İnce çizgi noktalı çizgi|
|Çizgi NoktaNokta|İnce çizgi-nokta-noktalı çizgi|
|Kesikli|Kesik çizgi|
|Noktalı|Noktalı çizgi|
|Çift|Çift çizgi|
|Saç|Saç çizgisi|
|Orta ÇizgiNokta|Orta çizgi noktalı çizgi|
|Orta ÇizgiNoktaNokta|Orta çizgi-nokta-noktalı çizgi|
|Orta Kesikli|Orta kesikli çizgi|
|Hiçbiri|Çizgi yok|
|Orta|Orta çizgi|
|Eğimli ÇizgiNokta|Eğimli orta çizgi noktalı çizgi|
|Kalın|Kalın çizgi|
|İnce|İnce çizgi|
Çizgi stillerinden birini seçin ve ardından onu[**Sınır**](https://reference.aspose.com/cells/net/aspose.cells/border) nesnenin[**Çizgi Stili**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) mülk.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

Hem çizgi stilini hem de rengini aynı anda ayarlamalısınız. İki çapraz kenar çizgisi aynı çizgi stiline ve rengine sahip olmalıdır.

{{% /alert %}}

####  **Cells Aralığına Kenarlık Ekleme**

 Tek bir hücre yerine bir dizi hücreye kenarlık eklemek de mümkündür. Bunu yapmak için öncelikle, çağrı yaparak bir hücre aralığı oluşturun.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Koleksiyonun[**Aralık Oluştur**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) yöntem. Aşağıdaki parametreleri alır:

- İlk Satır, aralığın ilk satırı.
- İlk Sütun, aralığın ilk sütununu temsil eder.
- Satır Sayısı, aralıktaki satır sayısı.
- Sütun Sayısı, aralıktaki sütun sayısı.

[**Aralık Oluştur**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) yöntem bir döndürür[**Menzil**](https://reference.aspose.com/cells/net/aspose.cells/range) Belirtilen hücre aralığını içeren nesne.[**Menzil**](https://reference.aspose.com/cells/net/aspose.cells/range) nesne sağlar[**Anahat Kenarlığını Ayarla**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) Hücre aralığına kenarlık eklemek için aşağıdaki parametreleri alan yöntem:

-  *Kenarlık Türü**, kenarlık türü,[**Kenarlık Türü**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)numaralandırma.
-  *Çizgi Stili**, kenar çizgisi stilidir;[**Hücre Kenarlığı Türü**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)numaralandırma.
- *Renk**, Renk numaralandırmasından seçilen çizgi rengi.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}
