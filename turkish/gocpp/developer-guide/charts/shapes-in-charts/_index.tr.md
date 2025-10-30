---
title: Golang ile C++ kullanarak Grafiklerde Şekiller
linktitle: Grafiklerde Şekiller
description: Microsoft Excel de kontroller eklemek ve grafikler özelleştirmek için Aspose.Cells for C++ i kullanmayı öğrenin. Kılavuzumuz, grafik öğelerini manipüle etmeyi, biçimlendirmeyi ayarlamayı ve grafiklerin genel görünümünü ve kullanılabilirliğini artırmayı gösterecek.
keywords: Aspose.Cells for C++, Grafik Kontrolleri, Grafik Özelleştirme, Microsoft Excel, Grafik Öğeleri, Biçimlendirme.
type: docs
weight: 70
url: /tr/go-cpp/controls-in-charts/
---

{{% alert color="primary" %}}

Bazen bir grafik içine etiketler, metin kutuları, resimler ve benzeri çizim nesneleri eklemeniz gerekebilir. Aspose.Cells, çalışma zamanında bir grafiğe denetim ekleyebilir.

{{% /alert %}}

## **Grafiğe Etiket Denetimi Ekleme**

Etiketler, bir elektronik tablonun içeriği hakkında kullanıcılara bilgi verme aracı sağlar.
Aspose.Cells, etiket eklemenize ve manipüle etmenize olanak tanır, hatta grafiklerin içine bile.

[**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/go-cpp/shapecollection/) sınıfı, grafiğe etiket kontrolü eklemek için kullanılan [**AddLabelInChart**](https://reference.aspose.com/cells/go-cpp/shapecollection/addlabelinchart/) adlı bir metoda sahiptir. Aşağıda, kullanılan parametrelerin listesi verilmiştir:

- **üst** – etiketin sol üst köşesinden dikey ofset (1/4000 biriminde grafik alanı).
- **sol** – etiketin sol üst köşesinden yatay ofset (1/4000 biriminde grafik alanı).
- **yükseklik** – etiketin yüksekliği, grafik alanının 1/4000 biriminde.
- **genişlik** – etiketin genişliği, grafik alanının 1/4000 biriminde.

Metod, [**Aspose::Cells::Drawing::Label**](https://reference.aspose.com/cells/go-cpp/label/) nesnesi döndürür. [**Label**](https://reference.aspose.com/cells/go-cpp/label/) sınıfı, grafikte bir etiket temsil eder. İşte bazı önemli üyeleri:

- [**Text**](https://reference.aspose.com/cells/go-cpp/shape/gettext/) (özellik) – bir etiketin başlık dizesini belirtir.
- [**Fill**](https://reference.aspose.com/cells/go-cpp/shape/getfill/) (özellik) – doldurma rengi özelliklerini belirtir.

Aşağıdaki örnek, bir etiketin grafiğe nasıl ekleneceğini göstermektedir. Örnek, içinde bir grafik bulunan bir tasarımcı dosyası (**exp_piechart.xls**) kullanır. Bu dosyayı, grafikte bir etiket eklemek için kullanırız. Aşağıda, grafiğe bir etiket eklemek için orijinal kod verilmiştir. Kodu yürüttüğünüzde aşağıdaki çıktı üretilir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts.go" >}}
## **Grafiğe TextBox Kontrolü Ekleme**

Raporda önemli bilgileri vurgulamanın bir yolu, bir metin kutusu kullanmaktır. Örneğin, şirket adını vurgulamak veya en yüksek satış yapan bölgeyi belirtmek için metin girin. [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/go-cpp/shapecollection/) sınıfı, grafiğe metin kutusu eklemek için kullanılan [**AddTextBoxInChart**](https://reference.aspose.com/cells/go-cpp/shapecollection/addtextboxinchart/) adlı bir metod sağlar. İşte metodun parametreleri:

- **top** – metin kutusunun grafik alanının sol üst köşesinden dikey ofseti, 1/4000 birimde.
- **left** – metin kutusunun grafik alanının sol üst köşesinden dikey ofseti, 1/4000 birimde.
- **height** – metin kutusunun yüksekliği, grafik alanının 1/4000 biriminde.
- **width** – metin kutusunun genişliği, grafik alanının 1/4000 biriminde.

Metod, [**Aspose::Cells::Drawing::TextBox**](https://reference.aspose.com/cells/go-cpp/textbox/) nesnesi döndürür. [**TextBox**](https://reference.aspose.com/cells/go-cpp/textbox/) sınıfı, grafikte bir metin kutusunu temsil eder.

Aşağıdaki örnek, bir metin kutusunun grafiğe nasıl ekleneceğini gösterir. Örnek, içinde bir grafik bulunan önceki bir tasarımcı dosyası (**exp_piechart.xls**) kullanır. Bu dosyayı, grafiğe metin kutusu eklemek için kullanırız. Aşağıda, grafiğe metin kutusu eklemek için orijinal kod bulunmaktadır.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts-1.go" >}}
## **Grafiğe Resim Ekleme**

Aspose.Cells, bir grafiğe resim eklemenize olanak tanır. Örneğin, bir resim ekleyerek bir grafiği vurgulamak veya anlamını artırmak veya bir marka resim dosyası eklemek.

[**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/go-cpp/shapecollection/) sınıfı, grafiğe resim nesnesi eklemek için kullanılan [**AddPictureInChart**](https://reference.aspose.com/cells/go-cpp/shapecollection/addpictureinchart/) adlı bir metod sağlar. İşte metodun parametreleri:

- **top** – resmin, grafik alanının sol üst köşesinden dikey ofseti, 1/4000 birimde.
- **left** – resmin, grafik alanının sol üst köşesinden dikey ofseti, 1/4000 birimde.
- **stream** – resim verisini içeren bir akım nesnesi.
- **widthScale** – resmin genişlik ölçeği, yüzde değeri.
- **heightScale** – resmin yükseklik ölçeği, yüzde değeri.

Metod, bir [**Aspose::Cells::Drawing::Picture**](https://reference.aspose.com/cells/go-cpp/picture/) nesnesi döndürür. [**Picture**](https://reference.aspose.com/cells/go-cpp/picture/) sınıfı, grafikte bir resim nesnesini temsil eder.

Aşağıdaki örnek, bir resmin grafiğe nasıl ekleneceğini gösterir. Örnek, içinde bir grafik bulunan önceki bir tasarımcı dosyası (**exp_piechart.xls**) kullanır. Bu dosyayı, grafiğe bir resim eklemek için kullanırız. Aşağıda, grafiğe resim eklemek için orijinal kod bulunmaktadır.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts-2.go" >}}
## **Grafiğe Onay Kutusu Ekleme**

Aspose.Cells, bir [**MsoDrawingType**](https://reference.aspose.com/cells/go-cpp/msodrawingtype/) numarasını kullanarak bir grafik tablosuna onay kutuları eklemenize olanak tanır. Aşağıdaki örnek, bir grafik tablosuna onay kutusu eklemeyi göstermektedir.

Aşağıdaki resim, çıktı dosyasındaki grafik tablosunu içeren onay kutusu göstermektedir.

![todo:image_alt_text](controls-in-charts_1.jpg)

Aşağıdaki kod parçası tarafından oluşturulan [çıktı dosyası](101089316.xlsx), referansınız için ekte bulunmaktadır.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts-3.go" >}}
## **Gelişmiş Konular**
- [Grafiklere WordArt Filigranı Ekleme](/cells/tr/cpp/add-wordart-watermark-to-chart/)
