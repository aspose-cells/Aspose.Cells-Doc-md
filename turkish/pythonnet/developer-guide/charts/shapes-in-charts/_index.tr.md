---
title: Grafiklerde Şekiller
description: Aspose.Cells for Python via .NET kullanarak Microsoft Excel de kontroller eklemeyi ve grafikleri özelleştirmeyi öğrenin. Kılavuzumuz, grafik öğelerini nasıl manipüle edeceğinizi, biçimlendirmeyi ayarlayacağınızı ve grafiklerinizin genel görünümünü ve kullanılabilirliğini artırmayı gösterecek.
keywords: Aspose.Cells for Python via .NET, Grafik Kontrolleri, Grafik Özelleştirme, Microsoft Excel, Grafik Öğeleri, Biçimlendirme.
type: docs
weight: 70
url: /tr/python-net/controls-in-charts/
---

{{% alert color="primary" %}}

Bazen grafiğe etiketler, metin kutuları, resimler gibi çizim nesneleri eklemeniz gerekir. Aspose.Cells for Python via .NET, çalışma zamanında grafiğe kontroller ekleyebilir.

{{% /alert %}}

## **Grafiğe Etiket Denetimi Ekleme**

Etiketler, bir elektronik tablonun içeriği hakkında kullanıcılara bilgi verme aracı sağlar.
Aspose.Cells for Python via .NET, grafiğe ve etiketlere eklemeye ve düzenlemeye imkan sağlar.

[**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) sınıfı, bir [**add_label_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_label_in_chart) yöntemi adında bir yöntem sağlar. Bu yöntem, bir etiket denetimini grafiğe eklemek için kullanılır. Yöntem için kullanılan parametrelerin bir listesi aşağıda verilmiştir:

- **üst** – etiketin sol üst köşesinden dikey ofset (1/4000 biriminde grafik alanı).
- **sol** – etiketin sol üst köşesinden yatay ofset (1/4000 biriminde grafik alanı).
- **yükseklik** – etiketin yüksekliği, grafik alanının 1/4000 biriminde.
- **genişlik** – etiketin genişliği, grafik alanının 1/4000 biriminde.

Yöntem, [**aspose.cells.drawing.Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label) nesnesi döndürür. [**Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label) sınıfı, grafikteki bir etiketi temsil eder. Bazı önemli üyelere sahiptir:

- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) (özellik) – bir etiketin başlık dizgisini belirtir.
- [**fill**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill) (özellik) – doldurma rengi özelliklerini belirtir.

Aşağıdaki örnek, bir etiketin grafiğe nasıl ekleneceğini göstermektedir. Örnek, içinde bir grafik bulunan bir tasarımcı dosyası (**exp_piechart.xls**) kullanır. Bu dosyayı, grafikte bir etiket eklemek için kullanırız. Aşağıda, grafiğe bir etiket eklemek için orijinal kod verilmiştir. Kodu yürüttüğünüzde aşağıdaki çıktı üretilir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingLabelControl-1.py" >}}

## **Grafiğe TextBox Kontrolü Ekleme**

Bir raporda önemli bilgileri vurgulamanın bir yolu, bir metin kutusu kullanmaktır. Örneğin, şirket adını vurgulamak veya en yüksek satış yapılan coğrafi bölgeyi belirtmek için metin girin. [**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) sınıfı, grafiğe bir metin kutusu denetimi eklemek için kullanılan [**add_text_box_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_text_box_in_chart) adında bir yöntem sağlar. Aşağıdaki parametre listesi, yöntem için kullanılan parametreleri gösterir:

- **top** – metin kutusunun grafik alanının sol üst köşesinden dikey ofseti, 1/4000 birimde.
- **left** – metin kutusunun grafik alanının sol üst köşesinden dikey ofseti, 1/4000 birimde.
- **height** – metin kutusunun yüksekliği, grafik alanının 1/4000 biriminde.
- **width** – metin kutusunun genişliği, grafik alanının 1/4000 biriminde.

Yöntem, bir [**aspose.cells.drawing.TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox) nesnesi döndürür. [**TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox) sınıfı, grafiğe bir metin kutusu temsil eder.

Aşağıdaki örnek, bir metin kutusunun grafiğe nasıl ekleneceğini gösterir. Örnek, içinde bir grafik bulunan önceki bir tasarımcı dosyası (**exp_piechart.xls**) kullanır. Bu dosyayı, grafiğe metin kutusu eklemek için kullanırız. Aşağıda, grafiğe metin kutusu eklemek için orijinal kod bulunmaktadır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.py" >}}

## **Grafiğe Resim Ekleme**

Aspose.Cells for Python via .NET, grafiğe resim eklemenize olanak tanır; örneğin, bir resim ekleyerek grafiği veya içeriğine vurgu yapabilir veya daha anlamlı hale getirebilirsiniz, veya marka resmi dosyası ekleyebilirsiniz.

[**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) sınıfı, grafiğe bir resim nesnesi eklemek için kullanılan [**add_picture_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture_in_chart) adında bir yöntem sağlar. Aşağıdaki parametre listesi, yöntem için kullanılan parametreleri gösterir:

- **top** – resmin, grafik alanının sol üst köşesinden dikey ofseti, 1/4000 birimde.
- **left** – resmin, grafik alanının sol üst köşesinden dikey ofseti, 1/4000 birimde.
- **stream** – resim verisini içeren bir akım nesnesi.
- **widthScale** – resmin genişlik ölçeği, yüzde değeri.
- **heightScale** – resmin yükseklik ölçeği, yüzde değeri.

Yöntem, bir [**aspose.cells.drawing.Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) nesnesi döndürür. [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) sınıfı, grafiğe bir resim nesnesi temsil eder.

Aşağıdaki örnek, bir resmin grafiğe nasıl ekleneceğini gösterir. Örnek, içinde bir grafik bulunan önceki bir tasarımcı dosyası (**exp_piechart.xls**) kullanır. Bu dosyayı, grafiğe bir resim eklemek için kullanırız. Aşağıda, grafiğe resim eklemek için orijinal kod bulunmaktadır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingPictureToChart-1.py" >}}

## **Grafiğe Onay Kutusu Ekleme**

Aspose.Cells for Python via .NET, [**MsoDrawingType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msodrawingtype) sıralaması kullanarak bir grafik sayfasına onay kutuları eklemenize olanak sağlar. Aşağıdaki örnek, bir grafik sayfasına onay kutusu eklemeyi göstermektedir.

Aşağıdaki resim, çıktı dosyasındaki grafik tablosunu içeren onay kutusu göstermektedir.

![todo:image_alt_text](controls-in-charts_1.jpg)

Aşağıdaki kod parçası tarafından oluşturulan [çıktı dosyası](101089316.xlsx), referansınız için ekte bulunmaktadır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.py" >}}

## **Gelişmiş Konular**
- [Grafiklere WordArt Filigranı Ekleme](/cells/tr/python-net/add-wordart-watermark-to-chart/)
