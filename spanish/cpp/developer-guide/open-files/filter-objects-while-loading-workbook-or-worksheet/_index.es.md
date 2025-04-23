---
title: Filtrar objetos mientras se carga un libro de Excel o hoja de cálculo con C++
linktitle: Filtrar objetos al cargar el libro o la hoja de trabajo
type: docs
weight: 330
url: /es/cpp/filter-objects-while-loading-workbook-or-worksheet/
description: Aprenda cómo filtrar objetos como gráficos, formas y formato condicional al cargar libros de Excel o hojas de cálculo usando el Aspose.Cells for C++.
---

## **Escenarios de uso posibles**
Por favor, use la propiedad [LoadOptions.GetLoadFilter()](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) al filtrar datos del libro de Excel. Pero si desea filtrar datos de hojas de cálculo individuales, deberá anular el método [LoadFilter.StartSheet](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/startsheet/). Proporcione el valor apropiado de la enumeración [LoadDataFilterOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) al crear o trabajar con [LoadFilter](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/).

La enumeración [LoadDataFilterOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) tiene los siguientes valores posibles.

- Todo
- Configuraciones del libro
- Celda en blanco
- Celda booleana
- Datos de celda
- Error de celda
- Numérico de celda
- Cadena de celda
- Valor de celda
- Chart
- Formato condicional
- Validación de datos
- Nombres definidos
- Propiedades del documento
- Fórmula
- Hipervínculos
- Área fusionada
- Tabla Dinámica
- Configuración
- Forma
- Datos de Hoja
- Configuraciones de Hoja
- Estructura
- Estilo
- Tabla
- VBA
- MapaXml

## **Objetos de Filtro al cargar el Libro**
El siguiente código de ejemplo ilustra cómo filtrar gráficos del libro. Por favor, revise el [archivo de Excel de ejemplo](5115258.xlsx) utilizado en este código y el [PDF de salida](5115257.pdf) generado por él. Como se puede ver en el PDF de salida, todos los gráficos han sido filtrados fuera del libro.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Filter charts from the workbook
    LoadOptions lOptions;
    lOptions.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::Chart));

    // Load the workbook with the above filter
    U16String inputFilePath = srcDir + u"sampleFilterCharts.xlsx";
    Workbook workbook(inputFilePath, lOptions);

    // Save worksheet to a single PDF page
    PdfSaveOptions pOptions;
    pOptions.SetOnePagePerSheet(true);

    // Save the workbook in PDF format
    U16String outputFilePath = outDir + u"sampleFilterCharts.pdf";
    workbook.Save(outputFilePath, pOptions);

    std::cout << "Workbook saved successfully with filtered charts!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Objetos de Filtro al cargar la Hoja de Trabajo**
El siguiente código de ejemplo carga el [archivo de Excel fuente](5115255.xlsx) y filtra los siguientes datos de sus hojas de trabajo usando un filtro personalizado.

- Filtra los gráficos de la hoja de trabajo llamada SinGráficos.
- Filtra las formas de la hoja de trabajo llamada SinFormas.
- Filtra el formato condicional de la hoja de trabajo llamada SinFormatoCondicional.

Una vez que carga el [archivo de Excel fuente](5115255.xlsx) con un filtro personalizado, toma las imágenes de todas las hojas una por una. Aquí están las imágenes de salida para su referencia. Como se puede ver, la primera imagen no tiene gráficos, la segunda imagen no tiene formas y la tercera imagen no tiene formato condicional.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomLoadFilter : public LoadFilter
{
public:
    void StartSheet(Worksheet& sheet) override
    {
        U16String sheetName = sheet.GetName();

        if (sheetName == u"NoCharts")
        {
            // Load everything and filter charts
            SetLoadDataFilterOptions(static_cast<LoadDataFilterOptions>(static_cast<int>(LoadDataFilterOptions::All) & ~static_cast<int>(LoadDataFilterOptions::Chart)));
        }

        if (sheetName == u"NoShapes")
        {
            // Load everything and filter shapes
            SetLoadDataFilterOptions(static_cast<LoadDataFilterOptions>(static_cast<int>(LoadDataFilterOptions::All) & ~static_cast<int>(LoadDataFilterOptions::Drawing)));
        }

        if (sheetName == u"NoConditionalFormatting")
        {
            // Load everything and filter conditional formatting
            SetLoadDataFilterOptions(static_cast<LoadDataFilterOptions>(static_cast<int>(LoadDataFilterOptions::All) & ~static_cast<int>(LoadDataFilterOptions::ConditionalFormatting)));
        }
    }
};

// Add main function to serve as entry point
int main() {
    Aspose::Cells::Startup();
    Aspose::Cells::Cleanup();
    return 0;

}
```

Así es como se usa la clase CustomLoadFilter según los nombres de las hojas de cálculo.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomLoadFilter : public LoadFilter
{
public:
    CustomLoadFilter() : LoadFilter(LoadDataFilterOptions::All) {}
};

int main()
{
    Aspose::Cells::Startup();

    // Source directory
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Filter worksheets using CustomLoadFilter class
    LoadOptions loadOpts;
    CustomLoadFilter customLoadFilter;
    loadOpts.SetLoadFilter(&customLoadFilter);

    // Load the workbook with filter defined in CustomLoadFilter class
    Workbook workbook(srcDir + u"sampleCustomFilteringPerWorksheet.xlsx", loadOpts);

    // Take the image of all worksheets one by one
    WorksheetCollection sheets = workbook.GetWorksheets();
    for (int i = 0; i < sheets.GetCount(); i++)
    {
        // Access worksheet at index i
        Worksheet worksheet = sheets.Get(i);

        // Create an instance of ImageOrPrintOptions
        // Render entire worksheet to image
        ImageOrPrintOptions imageOpts;
        imageOpts.SetOnePagePerSheet(true);
        imageOpts.SetImageType(Aspose::Cells::Drawing::ImageType::Png);

        // Convert worksheet to image
        SheetRender render(worksheet, imageOpts);
        render.ToImage(0, outDir + u"outputCustomFilteringPerWorksheet_" + worksheet.GetName() + u".png");
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
