---
title: Forme nei Grafici con C++
linktitle: Forme nei grafici
description: Impara come usare Aspose.Cells for C++ per aggiungere controlli e personalizzare i grafici in Microsoft Excel. La nostra guida dimostrerà come manipolare gli elementi del grafico, regolare il formato e migliorare l aspetto e l usabilità generale dei tuoi grafici.
keywords: Aspose.Cells for C++, Controlli grafico, Personalizzazione grafico, Microsoft Excel, Elementi del grafico, Formattazione.
type: docs
weight: 70
url: /it/cpp/controls-in-charts/
---

{{% alert color="primary" %}}

A volte è necessario inserire oggetti disegno come etichette, caselle di testo, immagini e così via in un grafico. Aspose.Cells può aggiungere i controlli a un grafico durante l'esecuzione.

{{% /alert %}}

## **Aggiunta del Controllo Etichetta al Grafico**

Le etichette forniscono un modo per fornire informazioni agli utenti sul contenuto di un foglio di calcolo.
Aspose.Cells consente di aggiungere e manipolare le etichette anche nei grafici.

La classe [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) fornisce un metodo chiamato [**AddLabelInChart**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlabelinchart/), usato per aggiungere un controllo etichetta a un grafico. Di seguito è riportato un elenco dei parametri usati per il metodo:

- **top** – lo spostamento verticale dell'etichetta dall'angolo in alto a sinistra in unità dello 1/4000 dell'area del grafico.
- **sinistra** – lo spostamento verticale dell'etichetta dall'angolo in alto a sinistra in unità dello 1/4000 dell'area del grafico.
- **altezza** – l'altezza dell'etichetta, in unità dello 1/4000 dell'area del grafico.
- **larghezza** – la larghezza dell'etichetta, in unità dello 1/4000 dell'area del grafico.

Il metodo restituisce un oggetto [**Aspose::Cells::Drawing::Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/). La classe [**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/) rappresenta un'etichetta nel grafico. Ha alcuni membri importanti:

- [**Text**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) (proprietà) – specifica la stringa di didascalia di un'etichetta.
- [**Fill**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getfill/) (proprietà) – specifica gli attributi del colore di riempimento.

L'esempio seguente mostra come aggiungere un'etichetta al grafico. L'esempio utilizza un file di progettazione (**exp_piechart.xls**) che ha un grafico al suo interno. Usiamo questo file per inserire un'etichetta nel grafico. Di seguito è riportato il codice originale per aggiungere un'etichetta al grafico. L'output seguente viene generato durante l'esecuzione del codice.

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

## **Aggiunta del controllo TextBox al grafico**

Un modo per evidenziare informazioni importanti in un report è utilizzare una casella di testo. Ad esempio, inserisci del testo per evidenziare il nome dell'azienda o per indicare la regione geografica con le vendite più alte. La classe [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) fornisce un metodo chiamato [**AddTextBoxInChart**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addtextboxinchart/), usato per aggiungere un controllo casella di testo a un grafico. Di seguito l'elenco dei parametri usati per il metodo:

- **top** – lo spostamento verticale della casella di testo dall'angolo in alto a sinistra in unità di 1/4000 dell'area del grafico.
- **left** – lo spostamento verticale della casella di testo dall'angolo in alto a sinistra in unità di 1/4000 dell'area del grafico.
- **height** – l'altezza della casella di testo, in unità di 1/4000 dell'area del grafico.
- **width** – la larghezza della casella di testo, in unità di 1/4000 dell'area del grafico.

Il metodo restituisce un oggetto [**Aspose::Cells::Drawing::TextBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textbox/). La classe [**TextBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textbox/) rappresenta una casella di testo nel grafico.

L'esempio seguente mostra come aggiungere una casella di testo a un grafico. L'esempio utilizza il file di progettazione precedente (**exp_piechart.xls**) che contiene un grafico. Utilizziamo questo file per inserire una casella di testo nel grafico per mostrare il titolo del grafico. Di seguito è riportato il codice originale per aggiungere una casella di testo al grafico.

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

## **Aggiunta di un'immagine al grafico**

Aspose.Cells consente di inserire immagini in un grafico. Ad esempio, aggiungi un'immagine per enfatizzare o dare più significato a un grafico o ai suoi contenuti, o inserisci un file immagine del marchio.

La classe [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) fornisce un metodo chiamato [**AddPictureInChart**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addpictureinchart/), usato per aggiungere un oggetto immagine al grafico. Di seguito l'elenco dei parametri usati per il metodo:

- **top** – lo spostamento verticale dell'immagine dall'angolo in alto a sinistra in unità di 1/4000 dell'area del grafico.
- **left** – lo spostamento verticale dell'immagine dall'angolo in alto a sinistra in unità di 1/4000 dell'area del grafico.
- **stream** – un oggetto stream che contiene i dati dell'immagine.
- **widthScale** – la scala della larghezza dell'immagine, un valore percentuale.
- **heightScale** – la scala dell'altezza dell'immagine, un valore percentuale.

Il metodo restituisce un oggetto [**Aspose::Cells::Drawing::Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/). La classe [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) rappresenta un oggetto immagine nel grafico.

L'esempio seguente mostra come aggiungere un'immagine al grafico. L'esempio utilizza il file di progettazione precedente (**exp_piechart.xls**) che contiene un grafico. Utilizziamo questo file per inserire un'immagine nel grafico. Di seguito è riportato il codice originale per aggiungere un'immagine al grafico.

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

## **Aggiunta di una casella di controllo nel grafico**

Aspose.Cells consente di inserire caselle di controllo in un foglio grafico utilizzando l'enumerazione [**MsoDrawingType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msodrawingtype/). L'esempio seguente illustra come aggiungere una casella di controllo a un foglio grafico.

L'immagine seguente mostra il foglio di lavoro del grafico con la casella di controllo nel file di output.

![todo:image_alt_text](controls-in-charts_1.jpg)

Il [file di output](101089316.xlsx) generato dal frammento di codice seguente è allegato per il tuo riferimento.

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

## **Argomenti avanzati**
- [Aggiungi WordArt Watermark al grafico](/cells/it/cpp/add-wordart-watermark-to-chart/)
