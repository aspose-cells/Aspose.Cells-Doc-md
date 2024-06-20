---
title: Kenar Ayarları
description: Aspose.Cells kitaplığını C#’da hücrelerin sınır stilini ve rengini ayarlamak için nasıl kullanabilirsiniz. Sınırın genişliği, stili ve rengini ayarlayarak, hücrelerin görünümü ve görünümü üzerinde daha fazla kontrol sağlarsınız.
keywords: Aspose.Cells, Hücre Sınır Ayarları, C#, Sınır Genişliği, Sınır Stili, Sınır Rengi
type: docs
weight: 40
url: /tr/net/cells-border-settings/
---

## **Hücrelere Kenarlık Eklemek**

Microsoft Excel, kullanıcılara sınırlar ekleyerek hücreleri biçimlendirmelerine olanak tanır. Sınırın türü nereye eklendiğine bağlıdır. Örneğin, üst sınır, bir hücrenin üst konumuna eklenen sınırdır. Kullanıcılar ayrıca sınırların çizgi stili ve rengini değiştirebilirler.

Aspose.Cells ile geliştiriciler, sınırlar ekleyebilir ve bunları Microsoft Excel'de olduğu gibi esnek bir şekilde özelleştirebilirler.

### **Hücrelere Kenarlık Eklemek**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her bir çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonunu içerir. Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonunu sağlar. [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonunda her öğe, [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıfının bir nesnesini temsil eder.

Aspose.Cells, [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıfında [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) metodunu sağlar. [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) metodu, bir hücrenin biçimlendirme stili ayarlamak için kullanılır. [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) sınıfı, hücrelere sınırlar eklemek için özellikler sağlar.

#### **Bir Hücreye Sınır Ekleme**

Geliştiriciler, [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesinin [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) koleksiyonunu kullanarak bir hücreye sınır ekleyebilirler. Sınır türü, [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) koleksiyonuna bir dizin olarak iletilir. Tüm sınır türleri, [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) numaralandırmasında önceden tanımlanmıştır.

**Sınır numaralandırması**

|**Sınır Türleri**|**Açıklama**|
| :- | :- |
|BottomBorder|Alt sınır çizgisi|
|DiagonalDown|Sol üstten sağ alt köşeye çapraz çizgi|
|DiagonalUp|Sol alttan sağ üste çapraz çizgi|
|LeftBorder|Sol sınır çizgisi|
|RightBorder|Sağ sınır çizgisi|
|TopBorder|Üst sınır çizgisi|

The [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection stores all borders. Each border in the [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection is represented by a [**Border**](https://reference.aspose.com/cells/net/aspose.cells/border) object which provides two properties, [**Color**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color) and [**LineStyle**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) to set a border's line color and style respectively.

Bir sınırın çizgi rengini ayarlamak için, renk seçmek için .NET Framework'ün bir parçası olan Renk numaralandırmasını seçin ve onu Sınır nesnesinin Renk özelliğine atayın.

Sınırın çizgi stili, [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype) numaralandırmasından bir çizgi stili seçilerek ayarlanır.

**HücreSınırTürü numaralandırması**

|**Çizgi Stilleri**|**Açıklama**|
| :- | :- |
|DashDot|İnce tireli kesikli çizgi|
|DashDotDot|İnce tireli kesik noktalı çizgi|
|Dashed|Kesikli çizgi|
|Dotted|Noktalı çizgi|
|Double|Çift çizgi|
|Hair|Saç inceliğinde çizgi|
|MediumDashDot|Orta tireli kesikli çizgi|
|MediumDashDotDot|Orta tireli kesik noktalı çizgi|
|MediumDashed|Orta kesikli çizgi|
|None|No Line|
|Medium|Orta Çizgi|
|SlantedDashDot|Eğik orta kesikli çizgi|
|Thick|Kalın çizgi|
|Thin|İnce çizgi|
Bir çizgi stili seçin ve ardından [**Border**](https://reference.aspose.com/cells/net/aspose.cells/border) nesnesinin [**LineStyle**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) özelliğine atayın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

Aynı anda çizgi stili ve rengini ayarlamalısınız. İki çapraz kenar çizgisinin aynı çizgi stiline ve renge sahip olması gerekir.

{{% /alert %}}

#### **Hücre Aralığına Sınırlar Ekleme**

Tek bir hücreden ziyade bir hücre aralığına da sınırlar eklemek mümkündür. Bunu yapmak için öncelikle [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonunun [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) yöntemini çağırarak bir hücre aralığı oluşturun. Aşağıdaki parametreleri alır:

- İlk Sütun, aralığın ilk sütunu.
- İlk Sütun, aralığın ilk sütunu.
- Satır Sayısı, aralıktaki satır sayısı.
- Sütun Sayısı, aralıktaki sütun sayısı.

[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) yöntemi belirtilen hücre aralığını içeren bir [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) nesnesi döndürür. [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) nesnesi, hücre aralığına sınır eklemek için aşağıdaki parametreleri alır:

- **Sınır Türü**, [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) sıralamasından seçilen sınır türü.
- **Çizgi Stili**, [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype) sıralamasından seçilen sınır çizgi stili.
- **Renk**, Renk sıralamasından seçilen çizgi rengi.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}
