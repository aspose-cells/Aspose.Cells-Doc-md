---
title: Former i diagram med C++
linktitle: Former i diagram
description: Lär dig hur du använder Aspose.Cells for C++ för att lägga till kontroller och anpassa diagram i Microsoft Excel. Vår guide kommer att demonstrera hur man manipulerar diagramelement, justerar formatering och förbättrar det övergripande utseendet och användbarheten av dina diagram.
keywords: Aspose.Cells for C++, Diagramkontroller, Diagramanpassning, Microsoft Excel, Diagramelement, Formatering.
type: docs
weight: 70
url: /sv/cpp/controls-in-charts/
---

{{% alert color="primary" %}}

Ibland behöver du infoga ritobjekt som etiketter, textrutor, bilder och så vidare i ett diagram. Aspose.Cells kan lägga till kontroller i ett diagram vid körtid.

{{% /alert %}}

## **Lägga till etikettkontroll i diagrammet**

Etiketter ger ett sätt att ge information till användare om innehållet i ett kalkylarks innehåll.
Aspose.Cells tillåter dig att lägga till och manipulera etiketter även i diagram.

Klass [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) tillhandahåller en metod som heter [**AddLabelInChart**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlabelinchart/), som används för att lägga till en etikettkontroll till ett diagram. Nedan är en lista över parametrarna som används för metoden:

- **överst** – vertikalt avstånd från etiketten till det övre vänstra hörnet i enheter av 1/4000 av diagramområdet.
- **vänster** – det horisontella avståndet från etiketten till det övre vänstra hörnet i enheter av 1/4000 av diagramområdet.
- **höjd** – etikettens höjd, i enheter av 1/4000 av diagramområdet.
- **bredd** – etikettens bredd, i enheter på 1/4000 av diagramområdet.

Metoden returnerar [**Aspose::Cells::Drawing::Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/) objekt. [**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/)-klassen representerar en etikett i diagrammet. Den har några viktiga medlemmar:

- [**Text**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) (egenskap) – anger etikettens rubriksträng.
- [**Fill**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getfill/) (egenskap) – specificerar färgfyllningsegenskaper.

Följande exempel visar hur man lägger till en etikett i diagrammet. Exemplet använder en designerfil (**exp_piechart.xls**) som har ett diagram i den. Vi använder denna fil för att infoga en etikett i diagrammet. Nedan finns den ursprungliga koden för att lägga till en etikett i diagrammet. Följande utdata genereras när koden utförs.

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

## **Lägga till textbox-styrenhet i diagrammet**

Ett sätt att belysa viktig information i en rapport är att använda en textruta. Till exempel, ange text för att belysa företagsnamnet eller för att visa den geografiska regionen med högst försäljning. Klass [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) tillhandahåller en metod som heter [**AddTextBoxInChart**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addtextboxinchart/), som används för att lägga till en textrutekontroll till ett diagram. Följande är parameternlistan för metoden:

- **top** – det vertikala avståndet från den övre vänstra hörnet i enheter om 1/4000 av diagramområdet.
- **vänster** – den vertikala avvikelsen för textrutan från det övre vänstra hörnet i enheter på 1/4000 av diagramområdet.
- **höjd** – textrutans höjd, i enheter om 1/4000 av diagramområdet.
- **bredd** – textrutans bredd, i enheter om 1/4000 av diagramområdet.

Metoden returnerar [**Aspose::Cells::Drawing::TextBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textbox/) objekt. [**TextBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textbox/)-klassen representerar en textruta i diagrammet.

Följande exempel visar hur man lägger till en textruta i ett diagram. Exemplet använder den tidigare designerfilen (**exp_piechart.xls**) som har ett diagram i den. Vi använder denna fil för att infoga en textruta i diagrammet för att visa diagramtiteln. Nedan finns den ursprungliga koden för att lägga till en textruta i diagrammet.

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

## **Lägga till bild i diagrammet**

Aspose.Cells gör det möjligt att infoga bilder i ett diagram. Till exempel, lägg till en bild för att betona eller ge mer mening åt ett diagram eller dess innehåll, eller infoga en varumärkesbildfil.

Klass [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) tillhandahåller en metod som heter [**AddPictureInChart**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addpictureinchart/), som används för att lägga till en bildobjekt till diagrammet. Följande är parameternlistan för metoden:

- **top** – det vertikala avståndet från den övre vänstra hörnet i enheter om 1/4000 av diagramområdet.
- **vänster** – det vertikala avståndet från den övre vänstra hörnet i enheter om 1/4000 av diagramområdet.
- **ström** – en strömobjekt som innehåller bilddata.
- **breddskala** – bildens breddskala, en procentuell värde.
- **höjdskala** – bildens höjdskala, en procentuell värde.

Metoden returnerar ett [**Aspose::Cells::Drawing::Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) objekt. [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/)-klassen representerar ett bildobjekt i diagrammet.

Följande exempel visar hur man lägger till en bild i diagrammet. Exemplet använder den tidigare designerfilen (**exp_piechart.xls**) som har ett diagram i den. Vi använder denna fil för att infoga en bild i diagrammet. Nedan finns den ursprungliga koden för att lägga till en bild i diagrammet.

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

## **Lägger till kryssruta i diagrammet**

Aspose.Cells tillåter dig att infoga kryssrutor i ett diagramblad genom att använda [**MsoDrawingType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msodrawingtype/)-uppräkningen. Följande exempel demonstrerar hur man lägger till en kryssruta i ett diagramblad.

Följande bild visar diagrambladet med kryssrutan i utdatafilen.

![todo:image_alt_text](controls-in-charts_1.jpg)

Den [utdatafilen](101089316.xlsx) som genererats av följande kodsnutt bifogas för din referens.

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

## **Fortsatta ämnen**
- [Lägg till WordArt-vattenstämpel på diagram](/cells/sv/cpp/add-wordart-watermark-to-chart/)
{{< app/cells/assistant language="cpp" >}}
