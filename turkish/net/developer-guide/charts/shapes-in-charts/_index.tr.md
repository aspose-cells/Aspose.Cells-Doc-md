---
title: Grafiklerde Şekiller
description: Microsoft Excel de Aspose.Cells for .NET kullanarak denetim eklemeyi ve grafikleri özelleştirmeyi öğrenin. Rehberimiz, grafik öğelerini manipüle etme, biçimlendirme ayarlarını düzenleme ve grafiklerinizin genel görünümünü ve kullanılabilirliğini artırma konusunda size yol gösterecektir.
keywords: Aspose.Cells for .NET, Grafik Denetimleri, Grafik Özelleştirme, Microsoft Excel, Grafik Öğeleri, Biçimlendirme.
type: docs
weight: 70
url: /tr/net/controls-in-charts/
---

{{% alert color="primary" %}}

Bazen bir grafik içine etiketler, metin kutuları, resimler ve benzeri çizim nesneleri eklemeniz gerekebilir. Aspose.Cells, çalışma zamanında bir grafiğe denetim ekleyebilir.

{{% /alert %}}

## **Grafiğe Etiket Denetimi Ekleme**

Etiketler, bir elektronik tablonun içeriği hakkında kullanıcılara bilgi verme aracı sağlar.
Aspose.Cells, etiket eklemenize ve manipüle etmenize olanak tanır, hatta grafiklerin içine bile.

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıfı, bir [**AddLabelInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabelinchart) yöntemi adında bir yöntem sağlar. Bu yöntem, bir etiket denetimini grafiğe eklemek için kullanılır. Yöntem için kullanılan parametrelerin bir listesi aşağıda verilmiştir:

- **üst** – etiketin sol üst köşesinden dikey ofset (1/4000 biriminde grafik alanı).
- **sol** – etiketin sol üst köşesinden yatay ofset (1/4000 biriminde grafik alanı).
- **yükseklik** – etiketin yüksekliği, grafik alanının 1/4000 biriminde.
- **genişlik** – etiketin genişliği, grafik alanının 1/4000 biriminde.

Yöntem, [**Aspose.Cells.Drawing.Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) nesnesi döndürür. [**Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) sınıfı, grafikteki bir etiketi temsil eder. Bazı önemli üyelere sahiptir:

- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) (özellik) – bir etiketin başlık dizgisini belirtir.
- [**Fill**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fill) (özellik) – doldurma rengi özelliklerini belirtir.

Aşağıdaki örnek, bir etiketin grafiğe nasıl ekleneceğini göstermektedir. Örnek, içinde bir grafik bulunan bir tasarımcı dosyası (**exp_piechart.xls**) kullanır. Bu dosyayı, grafikte bir etiket eklemek için kullanırız. Aşağıda, grafiğe bir etiket eklemek için orijinal kod verilmiştir. Kodu yürüttüğünüzde aşağıdaki çıktı üretilir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingLabelControl-1.cs" >}}

## **Grafiğe TextBox Kontrolü Ekleme**

Bir raporda önemli bilgileri vurgulamanın bir yolu, bir metin kutusu kullanmaktır. Örneğin, şirket adını vurgulamak veya en yüksek satış yapılan coğrafi bölgeyi belirtmek için metin girin. [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıfı, grafiğe bir metin kutusu denetimi eklemek için kullanılan [**AddTextBoxInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addtextboxinchart) adında bir yöntem sağlar. Aşağıdaki parametre listesi, yöntem için kullanılan parametreleri gösterir:

- **top** – metin kutusunun grafik alanının sol üst köşesinden dikey ofseti, 1/4000 birimde.
- **left** – metin kutusunun grafik alanının sol üst köşesinden dikey ofseti, 1/4000 birimde.
- **height** – metin kutusunun yüksekliği, grafik alanının 1/4000 biriminde.
- **width** – metin kutusunun genişliği, grafik alanının 1/4000 biriminde.

Yöntem, bir [**Aspose.Cells.Drawing.TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox) nesnesi döndürür. [**TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox) sınıfı, grafiğe bir metin kutusu temsil eder.

Aşağıdaki örnek, bir metin kutusunun grafiğe nasıl ekleneceğini gösterir. Örnek, içinde bir grafik bulunan önceki bir tasarımcı dosyası (**exp_piechart.xls**) kullanır. Bu dosyayı, grafiğe metin kutusu eklemek için kullanırız. Aşağıda, grafiğe metin kutusu eklemek için orijinal kod bulunmaktadır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.cs" >}}

## **Grafiğe Resim Ekleme**

Aspose.Cells, bir grafiğe resim eklemenize olanak tanır. Örneğin, bir resim ekleyerek bir grafiği vurgulamak veya anlamını artırmak veya bir marka resim dosyası eklemek.

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıfı, grafiğe bir resim nesnesi eklemek için kullanılan [**AddPictureInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpictureinchart) adında bir yöntem sağlar. Aşağıdaki parametre listesi, yöntem için kullanılan parametreleri gösterir:

- **top** – resmin, grafik alanının sol üst köşesinden dikey ofseti, 1/4000 birimde.
- **left** – resmin, grafik alanının sol üst köşesinden dikey ofseti, 1/4000 birimde.
- **stream** – resim verisini içeren bir akım nesnesi.
- **widthScale** – resmin genişlik ölçeği, yüzde değeri.
- **heightScale** – resmin yükseklik ölçeği, yüzde değeri.

Yöntem, bir [**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) nesnesi döndürür. [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) sınıfı, grafiğe bir resim nesnesi temsil eder.

Aşağıdaki örnek, bir resmin grafiğe nasıl ekleneceğini gösterir. Örnek, içinde bir grafik bulunan önceki bir tasarımcı dosyası (**exp_piechart.xls**) kullanır. Bu dosyayı, grafiğe bir resim eklemek için kullanırız. Aşağıda, grafiğe resim eklemek için orijinal kod bulunmaktadır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingPictureToChart-1.cs" >}}

## **Grafiğe Onay Kutusu Ekleme**

Aspose.Cells, bir [**MsoDrawingType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msodrawingtype) numarasını kullanarak bir grafik tablosuna onay kutuları eklemenize olanak tanır. Aşağıdaki örnek, bir grafik tablosuna onay kutusu eklemeyi göstermektedir.

Aşağıdaki resim, çıktı dosyasındaki grafik tablosunu içeren onay kutusu göstermektedir.

![todo:image_alt_text](controls-in-charts_1.jpg)

Aşağıdaki kod parçası tarafından oluşturulan [çıktı dosyası](101089316.xlsx), referansınız için ekte bulunmaktadır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.cs" >}}

## **Gelişmiş Konular**
- [Grafiklere WordArt Filigranı Ekleme](/cells/tr/net/add-wordart-watermark-to-chart/)
{{< app/cells/assistant language="csharp" >}}
