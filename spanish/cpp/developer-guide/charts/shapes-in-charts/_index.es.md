---
title: Formas en Gráficos con C++
linktitle: Formas en gráficos
description: Aprende cómo usar Aspose.Cells for C++ para agregar controles y personalizar gráficos en Microsoft Excel. Nuestra guía demostrará cómo manipular elementos del gráfico, ajustar el formato y mejorar la apariencia y usabilidad general de tus gráficos.
keywords: Aspose.Cells for C++, Controles de gráficos, Personalización de gráficos, Microsoft Excel, Elementos de gráficos, Formato.
type: docs
weight: 70
url: /es/cpp/controls-in-charts/
---

{{% alert color="primary" %}}

A veces es necesario insertar objetos de dibujo como etiquetas, cuadros de texto, imágenes, etc., en un gráfico. Aspose.Cells puede agregar los controles a un gráfico en tiempo de ejecución.

{{% /alert %}}

## **Agregar control de etiqueta al gráfico**

Las etiquetas proporcionan un medio para proporcionar información a los usuarios sobre el contenido de una hoja de cálculo.
Aspose.Cells le permite agregar y manipular etiquetas incluso en gráficos.

La clase [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) proporciona un método llamado [**AddLabelInChart**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlabelinchart/), usado para agregar un control de etiqueta a un gráfico. A continuación hay una lista de los parámetros utilizados para el método:

- **arriba** – el desplazamiento vertical de la etiqueta desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **izquierda** – el desplazamiento horizontal de la etiqueta desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **altura** – la altura de la etiqueta, en unidades de 1/4000 del área del gráfico.
- **ancho** – el ancho de la etiqueta, en unidades de 1/4000 del área del gráfico.

El método devuelve un objeto [**Aspose::Cells::Drawing::Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/). La clase [**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/) representa una etiqueta en el gráfico. Tiene algunos miembros importantes:

- [**Text**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) (propiedad) – especifica la cadena de texto del encabezado de la etiqueta.
- [**Fill**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getfill/) (propiedad) - especifica los atributos del color de relleno.

Con el siguiente ejemplo se muestra cómo añadir una etiqueta al gráfico. El ejemplo utiliza un archivo del diseñador (**exp_piechart.xls**) que contiene un gráfico. Usamos este archivo para insertar una etiqueta en el gráfico. A continuación se muestra el código original para añadir una etiqueta al gráfico. La siguiente salida se genera al ejecutar el código.

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

## **Añadiendo un Control de Cuadro de Texto al Gráfico**

Una forma de resaltar información importante en un informe es usar un cuadro de texto. Por ejemplo, ingresar texto para resaltar el nombre de la empresa o indicar la región geográfica con mayores ventas. La clase [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) proporciona un método llamado [**AddTextBoxInChart**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addtextboxinchart/), que se usa para agregar un control de cuadro de texto a un gráfico. A continuación, la lista de parámetros utilizados para el método:

- **arriba** - el desplazamiento vertical del cuadro de texto desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **izquierda** - el desplazamiento vertical del cuadro de texto desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **altura** - la altura del cuadro de texto, en unidades de 1/4000 del área del gráfico.
- **ancho** - el ancho del cuadro de texto, en unidades de 1/4000 del área del gráfico.

El método devuelve un objeto [**Aspose::Cells::Drawing::TextBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textbox/). La clase [**TextBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textbox/) representa un cuadro de texto en el gráfico.

El siguiente ejemplo muestra cómo añadir un cuadro de texto a un gráfico. El ejemplo utiliza el archivo del diseñador anterior (**exp_piechart.xls**) que contiene un gráfico. Usamos este archivo para insertar un cuadro de texto en el gráfico para mostrar el título del gráfico. A continuación se muestra el código original para añadir un cuadro de texto al gráfico.

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

## **Añadiendo una Imagen al Gráfico**

Aspose.Cells te permite insertar imágenes en un gráfico. Por ejemplo, agregar una imagen para resaltar o dar más significado a un gráfico o sus contenidos, o insertar un archivo de imagen de marca.

La clase [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) proporciona un método llamado [**AddPictureInChart**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addpictureinchart/), que se usa para agregar un objeto de imagen al gráfico. A continuación, la lista de parámetros utilizados para el método:

- **arriba** - el desplazamiento vertical de la imagen desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **izquierda** - el desplazamiento vertical de la imagen desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **flujo** - un objeto de flujo que contiene los datos de la imagen.
- **escalaAncho** - la escala del ancho de la imagen, un valor porcentual.
- **escalaAlto** - la escala de la altura de la imagen, un valor porcentual.

El método devuelve un objeto [**Aspose::Cells::Drawing::Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/). La clase [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) representa un objeto de imagen en el gráfico.

El siguiente ejemplo muestra cómo agregar una imagen al gráfico. El ejemplo utiliza el archivo de diseñador anterior (**exp_piechart.xls**) que tiene un gráfico en él. Utilizamos este archivo para insertar una imagen en el gráfico. A continuación se muestra el código original para agregar una imagen al gráfico.

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

## **Agregar casilla de verificación en el gráfico**

Aspose.Cells le permite insertar casillas de verificación en una hoja de gráfico utilizando la enumeración [**MsoDrawingType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msodrawingtype/). El siguiente ejemplo demuestra cómo agregar una casilla de verificación a una hoja de gráfico.

La siguiente imagen muestra la hoja de gráfico con la casilla de verificación en el archivo de salida.

![todo:image_alt_text](controls-in-charts_1.jpg)

El [archivo de salida](101089316.xlsx) generado por el siguiente fragmento de código se adjunta para su referencia.

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

## **Temas avanzados**
- [Agregar marca de agua de WordArt al gráfico](/cells/es/cpp/add-wordart-watermark-to-chart/)
