---
title: Çizimlerde C++ ile Çalışma şekilleri
linktitle: Grafiklerde Şekiller
description: Microsoft Excel de kontroller eklemek ve grafikler özelleştirmek için Aspose.Cells for C++ i kullanmayı öğrenin. Kılavuzumuz, grafik öğelerini manipüle etmeyi, biçimlendirmeyi ayarlamayı ve grafiklerin genel görünümünü ve kullanılabilirliğini artırmayı gösterecek.
keywords: Aspose.Cells for C++, Grafik Kontrolleri, Grafik Özelleştirme, Microsoft Excel, Grafik Öğeleri, Biçimlendirme.
type: docs
weight: 70
url: /tr/cpp/controls-in-charts/
---

{{% alert color="primary" %}}

Bazen bir grafik içine etiketler, metin kutuları, resimler ve benzeri çizim nesneleri eklemeniz gerekebilir. Aspose.Cells, çalışma zamanında bir grafiğe denetim ekleyebilir.

{{% /alert %}}

## **Grafiğe Etiket Denetimi Ekleme**

Etiketler, bir elektronik tablonun içeriği hakkında kullanıcılara bilgi verme aracı sağlar.
Aspose.Cells, etiket eklemenize ve manipüle etmenize olanak tanır, hatta grafiklerin içine bile.

[**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) sınıfı, grafiğe etiket kontrolü eklemek için kullanılan [**AddLabelInChart**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlabelinchart/) adlı bir metoda sahiptir. Aşağıda, kullanılan parametrelerin listesi verilmiştir:

- **üst** – etiketin sol üst köşesinden dikey ofset (1/4000 biriminde grafik alanı).
- **sol** – etiketin sol üst köşesinden yatay ofset (1/4000 biriminde grafik alanı).
- **yükseklik** – etiketin yüksekliği, grafik alanının 1/4000 biriminde.
- **genişlik** – etiketin genişliği, grafik alanının 1/4000 biriminde.

Metod, [**Aspose::Cells::Drawing::Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/) nesnesi döndürür. [**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/) sınıfı, grafikte bir etiket temsil eder. İşte bazı önemli üyeleri:

- [**Text**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) (özellik) – bir etiketin başlık dizesini belirtir.
- [**Fill**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getfill/) (özellik) – doldurma rengi özelliklerini belirtir.

Aşağıdaki örnek, bir etiketin grafiğe nasıl ekleneceğini göstermektedir. Örnek, içinde bir grafik bulunan bir tasarımcı dosyası (**exp_piechart.xls**) kullanır. Bu dosyayı, grafikte bir etiket eklemek için kullanırız. Aşağıda, grafiğe bir etiket eklemek için orijinal kod verilmiştir. Kodu yürüttüğünüzde aşağıdaki çıktı üretilir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"chart.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"chart.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the designer chart in the second sheet
    Worksheet sheet = workbook.GetWorksheets().Get(1);
    Aspose::Cells::Charts::Chart chart = sheet.GetCharts().Get(0);

    // Add a new label to the chart
    Label label = chart.GetShapes().AddLabelInChart(100, 100, 350, 900);

    // Set the caption of the label
    label.SetText(u"A Label In Chart");

    // Set the Placement Type, the way the Label is attached to the cells
    label.SetPlacement(PlacementType::FreeFloating);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Label added to chart successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Grafiğe TextBox Kontrolü Ekleme**

Raporda önemli bilgileri vurgulamanın bir yolu, bir metin kutusu kullanmaktır. Örneğin, şirket adını vurgulamak veya en yüksek satış yapan bölgeyi belirtmek için metin girin. [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) sınıfı, grafiğe metin kutusu eklemek için kullanılan [**AddTextBoxInChart**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addtextboxinchart/) adlı bir metod sağlar. İşte metodun parametreleri:

- **top** – metin kutusunun grafik alanının sol üst köşesinden dikey ofseti, 1/4000 birimde.
- **left** – metin kutusunun grafik alanının sol üst köşesinden dikey ofseti, 1/4000 birimde.
- **height** – metin kutusunun yüksekliği, grafik alanının 1/4000 biriminde.
- **width** – metin kutusunun genişliği, grafik alanının 1/4000 biriminde.

Metod, [**Aspose::Cells::Drawing::TextBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textbox/) nesnesi döndürür. [**TextBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textbox/) sınıfı, grafikte bir metin kutusunu temsil eder.

Aşağıdaki örnek, bir metin kutusunun grafiğe nasıl ekleneceğini gösterir. Örnek, içinde bir grafik bulunan önceki bir tasarımcı dosyası (**exp_piechart.xls**) kullanır. Bu dosyayı, grafiğe metin kutusu eklemek için kullanırız. Aşağıda, grafiğe metin kutusu eklemek için orijinal kod bulunmaktadır.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"chart.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"chart.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the designer chart in the second sheet
    Worksheet sheet = workbook.GetWorksheets().Get(1);
    Aspose::Cells::Charts::Chart chart = sheet.GetCharts().Get(0);

    // Add a new textbox to the chart
    TextBox textbox0 = chart.GetShapes().AddTextBoxInChart(100, 1100, 350, 2550);

    // Fill the text
    textbox0.SetText(u"Sales By Region");

    // Set the font color
    textbox0.GetFont().SetColor(Color::Maroon());

    // Set the font to bold
    textbox0.GetFont().SetIsBold(true);

    // Set the font size
    textbox0.GetFont().SetSize(14);

    // Set font attribute to italic
    textbox0.GetFont().SetIsItalic(true);

    // Get the fill format of the textbox
    FillFormat fillformat = textbox0.GetFill();

    // Get the line format type of the textbox
    LineFormat lineformat = textbox0.GetLine();

    // Set the line weight
    lineformat.SetWeight(2);

    // Set the dash style to solid
    lineformat.SetDashStyle(MsoLineDashStyle::Solid);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Textbox added to chart successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Grafiğe Resim Ekleme**

Aspose.Cells, bir grafiğe resim eklemenize olanak tanır. Örneğin, bir resim ekleyerek bir grafiği vurgulamak veya anlamını artırmak veya bir marka resim dosyası eklemek.

[**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) sınıfı, grafiğe resim nesnesi eklemek için kullanılan [**AddPictureInChart**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addpictureinchart/) adlı bir metod sağlar. İşte metodun parametreleri:

- **top** – resmin, grafik alanının sol üst köşesinden dikey ofseti, 1/4000 birimde.
- **left** – resmin, grafik alanının sol üst köşesinden dikey ofseti, 1/4000 birimde.
- **stream** – resim verisini içeren bir akım nesnesi.
- **widthScale** – resmin genişlik ölçeği, yüzde değeri.
- **heightScale** – resmin yükseklik ölçeği, yüzde değeri.

Metod, bir [**Aspose::Cells::Drawing::Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) nesnesi döndürür. [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) sınıfı, grafikte bir resim nesnesini temsil eder.

Aşağıdaki örnek, bir resmin grafiğe nasıl ekleneceğini gösterir. Örnek, içinde bir grafik bulunan önceki bir tasarımcı dosyası (**exp_piechart.xls**) kullanır. Bu dosyayı, grafiğe bir resim eklemek için kullanırız. Aşağıda, grafiğe resim eklemek için orijinal kod bulunmaktadır.

```c++
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

std::vector<uint8_t> ReadFileData(const U16String& filePath) {
    std::ifstream file(filePath.ToUtf8(), std::ios::binary | std::ios::ate);
    std::streamsize size = file.tellg();
    file.seekg(0, std::ios::beg);

    std::vector<uint8_t> buffer(size);
    if (!file.read(reinterpret_cast<char*>(buffer.data()), size)) {
        throw std::runtime_error("Error reading file");
    }
    return buffer;
}

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"chart.xls");
    std::vector<uint8_t> imageData = ReadFileData(srcDir + u"logo.jpg");

    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Chart chart = sheet.GetCharts().Get(0);
    Vector<uint8_t> data(imageData.data(), static_cast<int32_t>(imageData.size()));
    Picture pic0 = chart.GetShapes().AddPictureInChart(50, 50, data, 40, 40);
    LineFormat lineFormat = pic0.GetLine();

    lineFormat.SetDashStyle(MsoLineDashStyle::Solid);
    lineFormat.SetWeight(4);

    workbook.Save(outDir + u"chart.out.xls");
    std::cout << "Chart modified successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Grafiğe Onay Kutusu Ekleme**

Aspose.Cells, bir [**MsoDrawingType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msodrawingtype/) numarasını kullanarak bir grafik tablosuna onay kutuları eklemenize olanak tanır. Aşağıdaki örnek, bir grafik tablosuna onay kutusu eklemeyi göstermektedir.

Aşağıdaki resim, çıktı dosyasındaki grafik tablosunu içeren onay kutusu göstermektedir.

![todo:image_alt_text](controls-in-charts_1.jpg)

Aşağıdaki kod parçası tarafından oluşturulan [çıktı dosyası](101089316.xlsx), referansınız için ekte bulunmaktadır.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add a chart sheet to the workbook
    int32_t index = workbook.GetWorksheets().Add(SheetType::Chart);

    // Get the newly added chart sheet
    Worksheet sheet = workbook.GetWorksheets().Get(index);

    // Add a floating chart to the sheet
    sheet.GetCharts().AddFloatingChart(ChartType::Column, 0, 0, 1024, 960);

    // Add data series to the chart
    sheet.GetCharts().Get(0).GetNSeries().Add(U16String(u"{1,2,3}"), false);

    // Add a checkbox to the chart
    sheet.GetCharts().Get(0).GetShapes().AddShapeInChart(MsoDrawingType::CheckBox, PlacementType::Move, 400, 400, 1000, 600);

    // Set text for the checkbox
    sheet.GetCharts().Get(0).GetShapes().Get(0).SetText(U16String(u"CheckBox 1"));

    // Save the workbook
    workbook.Save(outDir + u"InsertCheckboxInChartSheet_out.xlsx");

    std::cout << "Checkbox added to chart sheet successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Gelişmiş Konular**
- [Grafiklere WordArt Filigranı Ekleme](/cells/tr/cpp/add-wordart-watermark-to-chart/)
{{< app/cells/assistant language="cpp" >}}
