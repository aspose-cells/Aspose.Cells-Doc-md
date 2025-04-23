---
title: Node.js ile C++ kullanarak Grafikte biçimlendirme ve öğelerinde şekiller
linktitle: Grafiklerde Şekiller
description: Aspose.Cells for Node.js via C++ kullanarak Microsoft Excel de grafiklere kontrol ekleme ve özelleştirme öğrenin. Bu kılavuz, grafik öğelerini nasıl manipüle edeceğinizi, biçimlendirmeyi ayarlayacağınızı ve genel görünüm ile kullanılabilirliği artıracağınızı gösterir.
keywords: Aspose.Cells for Node.js via C++, Grafik Kontrolleri, Grafik Özelleştirme, Microsoft Excel, Grafik Öğeleri, Biçimlendirme.
type: docs
weight: 70
url: /tr/nodejs-cpp/controls-in-charts/
---

{{% alert color="primary" %}}
Bazen bir grafik içine etiketler, metin kutuları, resimler ve benzeri çizim nesneleri eklemeniz gerekebilir. Aspose.Cells, çalışma zamanında bir grafiğe denetim ekleyebilir.
{{% /alert %}}

## **Grafiğe Etiket Denetimi Ekleme**

Etiketler, bir elektronik tablonun içeriği hakkında kullanıcılara bilgi vermenin bir yolunu sağlar. Aspose.Cells, etiketleri hatta grafiklere bile eklemenize ve bunları manipüle etmenize olanak sağlar.

[**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) sınıfı, bir [**addLabelInChart(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLabelInChart-number-number-number-number-) yöntemi adında bir yöntem sağlar. Bu yöntem, bir etiket denetimini grafiğe eklemek için kullanılır. Yöntem için kullanılan parametrelerin bir listesi aşağıda verilmiştir:

- **üst** – etiketin sol üst köşesinden dikey ofset (1/4000 biriminde grafik alanı).
- **sol** – etiketin sol üst köşesinden yatay ofset (1/4000 biriminde grafik alanı).
- **yükseklik** – etiketin yüksekliği, grafik alanının 1/4000 biriminde.
- **genişlik** – etiketin genişliği, grafik alanının 1/4000 biriminde.

Yöntem, [**Label**](https://reference.aspose.com/cells/nodejs-cpp/label/) nesnesi döndürür. [**Label**](https://reference.aspose.com/cells/nodejs-cpp/label/) sınıfı, grafikteki bir etiketi temsil eder. Bazı önemli üyelere sahiptir:

- [**getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--) (özellik) – bir etiketin başlık dizgisini belirtir.
- [**getFill()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getFill--) (özellik) – doldurma rengi özelliklerini belirtir.

Aşağıdaki örnek, bir etiketin grafiğe nasıl ekleneceğini göstermektedir. Örnek, içinde bir grafik bulunan bir tasarımcı dosyası (**exp_piechart.xls**) kullanır. Bu dosyayı, grafikte bir etiket eklemek için kullanırız. Aşağıda, grafiğe bir etiket eklemek için orijinal kod verilmiştir. Kodu yürüttüğünüzde aşağıdaki çıktı üretilir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart.xls"));

// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(1);
const chart = sheet.getCharts().get(0);

// Add a new label to the chart.
const label = chart.getShapes().addLabelInChart(100, 100, 350, 900);

// Set the caption of the label.
label.setText("A Label In Chart");

// Set the Placement Type, the way the Label is attached to the cells.
label.setPlacement(AsposeCells.PlacementType.FreeFloating);

// Save the excel file.
workbook.save(path.join(dataDir, "chart.out.xls"));
```

## **Grafiğe TextBox Kontrolü Ekleme**

Bir raporda önemli bilgileri vurgulamanın bir yolu, bir metin kutusu kullanmaktır. Örneğin, şirket adını vurgulamak veya en yüksek satış yapılan coğrafi bölgeyi belirtmek için metin girin. [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) sınıfı, grafiğe bir metin kutusu denetimi eklemek için kullanılan [**addTextBoxInChart(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addTextBoxInChart-number-number-number-number-) adında bir yöntem sağlar. Aşağıdaki parametre listesi, yöntem için kullanılan parametreleri gösterir:

- **top** – metin kutusunun grafik alanının sol üst köşesinden dikey ofseti, 1/4000 birimde.
- **left** – metin kutusunun grafik alanının sol üst köşesinden dikey ofseti, 1/4000 birimde.
- **height** – metin kutusunun yüksekliği, grafik alanının 1/4000 biriminde.
- **width** – metin kutusunun genişliği, grafik alanının 1/4000 biriminde.

Yöntem, bir [**TextBox**](https://reference.aspose.com/cells/nodejs-cpp/textbox/) nesnesi döndürür. [**TextBox**](https://reference.aspose.com/cells/nodejs-cpp/textbox/) sınıfı, grafiğe bir metin kutusu temsil eder.

Aşağıdaki örnek, bir metin kutusunun grafiğe nasıl ekleneceğini gösterir. Örnek, içinde bir grafik bulunan önceki bir tasarımcı dosyası (**exp_piechart.xls**) kullanır. Bu dosyayı, grafiğe metin kutusu eklemek için kullanırız. Aşağıda, grafiğe metin kutusu eklemek için orijinal kod bulunmaktadır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart.xls"));

// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(1);
const chart = sheet.getCharts().get(0);

// Add a new textbox to the chart.
const textbox0 = chart.getShapes().addTextBoxInChart(100, 1100, 350, 2550);

// Fill the text.
textbox0.setText("Sales By Region");

// Get the textbox text frame.
// const textframe0 = textbox0.getTextFrame();

// Set the textbox to adjust it according to its contents.
// textframe0.setAutoSize(true);

// Set the font color.
textbox0.getFont().setColor(AsposeCells.Color.Maroon);

// Set the font to bold.
textbox0.getFont().setIsBold(true);

// Set the font size.
textbox0.getFont().setSize(14);

// Set font attribute to italic.
textbox0.getFont().setIsItalic(true);

// Get the fill format of the textbox.
const fillformat = textbox0.getFill();

// Get the line format type of the textbox.
const lineformat = textbox0.getLine();

// Set the line weight.
lineformat.setWeight(2);

// Set the dash style to solid.
lineformat.setDashStyle(AsposeCells.MsoLineDashStyle.Solid);

// Save the excel file.
workbook.save(path.join(dataDir, "chart.out.xls"));
```

## **Grafiğe Resim Ekleme**

Aspose.Cells, bir grafiğe resim eklemenize olanak tanır. Örneğin, bir resim ekleyerek bir grafiği vurgulamak veya anlamını artırmak veya bir marka resim dosyası eklemek.

[**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) sınıfı, grafiğe bir resim nesnesi eklemek için kullanılan [**addPictureInChart(number, number, Uint8Array, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPictureInChart-number-number-uint8array-number-number-) adında bir yöntem sağlar. Aşağıdaki parametre listesi, yöntem için kullanılan parametreleri gösterir:

- **top** – resmin, grafik alanının sol üst köşesinden dikey ofseti, 1/4000 birimde.
- **left** – resmin, grafik alanının sol üst köşesinden dikey ofseti, 1/4000 birimde.
- **stream** – resim verisini içeren bir akım nesnesi.
- **widthScale** – resmin genişlik ölçeği, yüzde değeri.
- **heightScale** – resmin yükseklik ölçeği, yüzde değeri.

Yöntem, bir [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/) nesnesi döndürür. [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/) sınıfı, grafiğe bir resim nesnesi temsil eder.

Aşağıdaki örnek, bir resmin grafiğe nasıl ekleneceğini gösterir. Örnek, içinde bir grafik bulunan önceki bir tasarımcı dosyası (**exp_piechart.xls**) kullanır. Bu dosyayı, grafiğe bir resim eklemek için kullanırız. Aşağıda, grafiğe resim eklemek için orijinal kod bulunmaktadır.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart_shapes.xls"));

// Get an image file to the stream.
const stream = fs.readFileSync(path.join(dataDir, "logo.jpg"));

// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(0);
const chart = sheet.getCharts().get(0);

// Add a new picture to the chart.
const pic0 = chart.getShapes().addPictureInChart(50, 50, stream, 40, 40);

// Get the lineformat type of the picture.
const lineformat = pic0.getLine();          

// Set the dash style.
lineformat.setDashStyle(AsposeCells.MsoLineDashStyle.Solid);

// Set the line weight.
lineformat.setWeight(4);    

// Save the excel file.
workbook.save(path.join(dataDir, "chart.out.xls"));
```

## **Grafiğe Onay Kutusu Ekleme**

Aspose.Cells, bir [**MsoDrawingType**](https://reference.aspose.com/cells/nodejs-cpp/msodrawingtype/) numarasını kullanarak bir grafik tablosuna onay kutuları eklemenize olanak tanır. Aşağıdaki örnek, bir grafik tablosuna onay kutusu eklemeyi göstermektedir.

Aşağıdaki resim, çıktı dosyasındaki grafik tablosunu içeren onay kutusu göstermektedir.

![todo:image_alt_text](controls-in-charts_1.jpg)

Aşağıdaki kod parçası tarafından oluşturulan [çıktı dosyası](101089316.xlsx), referansınız için ekte bulunmaktadır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a chart to the worksheet
const index = workbook.getWorksheets().add(AsposeCells.SheetType.Chart);

const sheet = workbook.getWorksheets().get(index);
sheet.getCharts().addFloatingChart(AsposeCells.ChartType.Column, 0, 0, 1024, 960);
sheet.getCharts().get(0).getNSeries().add("{1,2,3}", false);

// Add checkbox to the chart.
sheet.getCharts().get(0).getShapes().addShapeInChart(AsposeCells.MsoDrawingType.CheckBox, AsposeCells.PlacementType.Move, 400, 400, 1000, 600);
sheet.getCharts().get(0).getShapes().get(0).setText("CheckBox 1");

// Save the excel file.
workbook.save(outputDir +"InsertCheckboxInChartSheet_out.xlsx");
```

## **Gelişmiş Konular**
- [Grafiklere WordArt Filigranı Ekleme](/cells/tr/nodejs-cpp/add-wordart-watermark-to-chart/)

