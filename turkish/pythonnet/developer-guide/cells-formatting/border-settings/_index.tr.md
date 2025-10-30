---
title: Kenar Ayarları
description: Python da Aspose.Cells for Python via .NET kütüphanesini kullanarak hücrelerin sınır stilini ve rengini ayarlamak için. Sınırın genişliği, stili ve rengini ayarlayarak, hücrelerin görünümünü ve görünüşünü daha iyi kontrol edebilirsiniz.
keywords: Aspose.Cells for Python via .NET, Hücre Kenarlık Ayarları, Python Kenarlık Kalınlığı, Kenarlık Stili, Kenarlık Rengi
type: docs
weight: 40
url: /tr/python-net/cells-border-settings/
---

## **Hücrelere Kenarlık Eklemek**

Microsoft Excel, kullanıcılara sınırlar ekleyerek hücreleri biçimlendirmelerine olanak tanır. Sınırın türü nereye eklendiğine bağlıdır. Örneğin, üst sınır, bir hücrenin üst konumuna eklenen sınırdır. Kullanıcılar ayrıca sınırların çizgi stili ve rengini değiştirebilirler.

Aspose.Cells for Python via .NET ile geliştiriciler, kenarlıklar ekleyebilir ve Microsoft Excel'deki gibi görünümünü özelleştirebilir.

### **Hücrelere Kenarlık Eklemek**

Aspose.Cells for Python via .NET, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı, [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonunu sağlar. [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) sınıfının bir nesnesini temsil eder.

Aspose.Cells for Python via .NET, [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) adlı yöntemi [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) sınıfında sağlar. [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) yöntemi, bir hücrenin biçimlendirme stilini ayarlamak için kullanılır. [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) sınıfı, hücrelere kenarlık eklemek için özellikler sağlar.

#### **Bir Hücreye Sınır Ekleme**

Geliştiriciler, [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) nesnesinin [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) koleksiyonunu kullanarak bir hücreye sınır ekleyebilirler. Sınır türü, [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) koleksiyonuna bir dizin olarak iletilir. Tüm sınır türleri, [**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype) numaralandırmasında önceden tanımlanmıştır.

**Sınır numaralandırması**

|**Sınır Türleri**|**Açıklama**|
| :- | :- |
|BOTTOM_BORDER|Alt kenarlık çizgisi|
|DIAGONAL_DOWN|Sol üstten sağ altta çapraz çizgi|
|DIAGONAL_UP|Sol alttan sağ üstte çapraz çizgi|
|LEFT_BORDER|Sol kenarlık çizgisi|
|RIGHT_BORDER|Sağ kenarlık çizgisi|
|TOP_BORDER|Üst kenarlık çizgisi|

The [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) collection stores all borders. Each border in the [**Borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) collection is represented by a [**Border**](https://reference.aspose.com/cells/python-net/aspose.cells/border) object which provides two properties, [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/border/color) and [**line_style**](https://reference.aspose.com/cells/python-net/aspose.cells/border/line_style) to set a border's line color and style respectively.

Bir sınırın çizgi rengini ayarlamak için, renk seçmek için .NET Framework'ün bir parçası olan Renk numaralandırmasını seçin ve onu Sınır nesnesinin Renk özelliğine atayın.

Sınırın çizgi stili, [**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype) numaralandırmasından bir çizgi stili seçilerek ayarlanır.

**HücreSınırTürü numaralandırması**

|**Çizgi Stilleri**|**Açıklama**|
| :- | :- |
|DASH_DOT|İnce noktalı çizgi|
|DASH_DOT_DOT|İnce nokta noktalı çizgi|
|DASHED|Kesik çizgi|
|DOTTED|Noktalı çizgi|
|DOUBLE|İki kat çizgi|
|HAIR|Saç hattı|
|MEDIUM_DASH_DOT|Orta noktalı çizgi|
|MEDIUM_DASH_DOT_DOT|Orta nokta noktalı çizgi|
|MEDIUM_DASHED|Orta kesikli çizgi|
|NONE|Hiç çizgi yok|
|MEDIUM|Orta çizgi|
|SLANTED_DASH_DOT|Eğimli orta noktalı çizgi|
|THICK|Kalın çizgi|
|THIN|İnce çizgi|
Bir çizgi stili seçin ve ardından [**Border**](https://reference.aspose.com/cells/python-net/aspose.cells/border) nesnesinin [**line_style**](https://reference.aspose.com/cells/python-net/aspose.cells/border/line_style) özelliğine atayın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Borders-AddingBordersToCells-1.py" >}}

{{% alert color="primary" %}}

Aynı anda çizgi stili ve rengini ayarlamalısınız. İki çapraz kenar çizgisinin aynı çizgi stiline ve renge sahip olması gerekir.

{{% /alert %}}

#### **Hücre Aralığına Sınırlar Ekleme**

Tek bir hücreden ziyade bir hücre aralığına da sınırlar eklemek mümkündür. Bunu yapmak için öncelikle [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonunun [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range) yöntemini çağırarak bir hücre aralığı oluşturun. Aşağıdaki parametreleri alır:

- İlk Sütun, aralığın ilk sütunu.
- İlk Sütun, aralığın ilk sütunu.
- Satır Sayısı, aralıktaki satır sayısı.
- Sütun Sayısı, aralıktaki sütun sayısı.

[**create_range**](hhttps://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str) yöntemi belirtilen hücre aralığını içeren bir [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) nesnesi döndürür. [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) nesnesi, hücre aralığına sınır eklemek için aşağıdaki parametreleri alır:

- **Sınır Türü**, [**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype) sıralamasından seçilen sınır türü.
- **Çizgi Stili**, [**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype) sıralamasından seçilen sınır çizgi stili.
- **Renk**, Renk sıralamasından seçilen çizgi rengi.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Borders-AddingBorderstoRange-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
