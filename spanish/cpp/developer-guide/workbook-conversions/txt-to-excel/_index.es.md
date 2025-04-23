---
title: Convertir CSV, TSV y TXT a Excel con C++
linktitle: Convertir CSV, TSV y TXT a Excel
type: docs
weight: 30
url: /es/cpp/convert-csv-tsv-and-txt-to-excel/
description: Aprende cómo convertir archivos CSV, TSV y TXT a Excel usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Usando Aspose.Cells for C++, puedes convertir archivos CSV a Excel, OpenOffice, PDF, JSON y muchos otros formatos.

{{% /alert %}}

## **Abriendo Archivos CSV**

Los archivos de valores separados por comas (CSV) contienen registros donde los valores están separados por comas. Los datos se almacenan en forma de tabla donde cada columna está separada por el carácter coma y entrecomillada por el carácter de comillas dobles. Si un valor de campo contiene un carácter de comillas dobles, se escapa con un par de comillas dobles. También puedes usar Microsoft Excel para exportar datos de hojas de cálculo a CSV.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate LoadOptions specified by the LoadFormat
    LoadOptions loadOptions4(LoadFormat::Csv);

    // Create a Workbook object and open the file from its path
    Workbook wbCSV(srcDir + u"Book_CSV.csv", loadOptions4);

    std::cout << "CSV file opened successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Abrir archivos CSV y reemplazar caracteres inválidos**

En Excel, cuando se abre un archivo CSV con caracteres especiales, los caracteres se reemplazan automáticamente. Lo mismo lo hace la API Aspose.Cells, como se muestra en el ejemplo de código a continuación.

```c++
// Fix BOM issue
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String filename = srcDir + u"[20180220142533][ASPOSE_CELLS_TEST].csv";

    TxtLoadOptions options;
    options.SetSeparator(u';');
    options.SetCheckExcelRestriction(false);
    options.SetConvertNumericData(false);
    options.SetConvertDateTimeData(false);

    LoadFilter* filter = new LoadFilter(LoadDataFilterOptions::CellData);
    options.SetLoadFilter(filter);

    Workbook workbook(filename, options);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    std::cout << worksheet.GetName().ToUtf8() << std::endl;
    std::cout << worksheet.GetName().GetLength() << std::endl;
    std::cout << "CSV file opened successfully!" << std::endl;

    delete filter;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Usando el Analizador Preferido**

No siempre es necesario usar la configuración predeterminada del analizador para abrir archivos CSV. A veces, importar un archivo CSV no produce la salida esperada, por ejemplo, cuando el formato de fecha no es el esperado o los campos vacíos se manejan de manera diferente. Para esto, está disponible **TxtLoadOptions.PreferredParsers** para proporcionar tu propio analizador preferido para analizar diferentes tipos de datos según tus requerimientos. El siguiente código de ejemplo demuestra el uso de un analizador preferido.

Se pueden descargar los archivos fuente de muestra y los archivos de salida de las siguientes conexiones para probar esta función.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
	Aspose::Cells::Startup();

	U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
	U16String outDir(u"..\\Data\\02_OutputDirectory\\");

	TxtLoadOptions loadOptions(LoadFormat::Csv);
	loadOptions.SetSeparator(u',');
	loadOptions.SetConvertDateTimeData(true);

	Workbook workbook(srcDir + u"sample.csv", loadOptions);

	Worksheet worksheet = workbook.GetWorksheets().Get(0);
	Cells cells = worksheet.GetCells();

	Cell cell = cells.Get(u"A1");
	std::cout << "A1: " << static_cast<int>(cell.GetType())
		<< " - " << cell.GetDisplayStringValue().ToUtf8() << std::endl;

	cell = cells.Get(u"B1");
	std::cout << "B1: " << static_cast<int>(cell.GetType())
		<< " - " << cell.GetDisplayStringValue().ToUtf8() << std::endl;

	workbook.Save(outDir + u"outputsample.xlsx");

	std::cout << "OpeningCSVFilesWith executed successfully." << std::endl;

	Aspose::Cells::Cleanup();
	return 0;
}
```

### **Abriendo Archivos de Texto con Separador Personalizado**

Los archivos de texto se usan para contener datos de hojas de cálculo sin formato. El archivo es un tipo de archivo de texto sin formato que puede tener algunos delimitadores personalizados.

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

    // Path of input CSV file
    U16String filePath = srcDir + u"Book11.csv";

    // Instantiate Text File's LoadOptions
    TxtLoadOptions txtLoadOptions;

    // Specify the separator
    txtLoadOptions.SetSeparator(u',');

    // Create a Workbook object and open the file from its path
    Workbook wb(filePath, txtLoadOptions);

    // Save file
    wb.Save(outDir + u"output.txt");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Abriendo archivos delimitados por tabulación**

Los archivos de valores separados por tabulación (Texto) contienen datos de hojas de cálculo pero sin formato. Los datos están ordenados en filas y columnas como en tablas y hojas de cálculo. Básicamente, un archivo delimitado por tabulación es un tipo especial de archivo de texto plano con una tabulación entre cada columna.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate LoadOptions specified by the LoadFormat
    LoadOptions loadOptions(LoadFormat::TabDelimited);

    // Create a Workbook object and open the file from its path
    Workbook wbTabDelimited(srcDir + u"Book1TabDelimited.txt", loadOptions);

    std::cout << "Tab delimited file opened successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Apertura de archivos de Valores Separados por Comas y con pestañas (TSV)**

Los archivos de valores separados por tabulación (TSV) contienen datos de hojas de cálculo pero sin formato. Es lo mismo que un archivo delimitado por tabulación donde los datos están ordenados en filas y columnas como en tablas y hojas de cálculo.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate LoadOptions specified by the LoadFormat
    LoadOptions loadOptions(LoadFormat::Tsv);

    // Create a Workbook object and open the file from its path
    Workbook workbook(srcDir + u"SampleTSVFile.tsv", loadOptions);

    // Using the Sheet 1 in Workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing a cell using its name
    Cell cell = worksheet.GetCells().Get(u"C3");

    // Output the cell name and value
    std::cout << "Cell Name: " << cell.GetName().ToUtf8() << " Value: " << cell.GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Temas avanzados**
- [Cargar o Importar archivo CSV con fórmulas](/cells/es/cpp/load-or-import-csv-file-with-formulas/)
- [Lectura de archivo CSV con múltiples codificaciones](/cells/es/cpp/reading-csv-file-with-multiple-encodings/)
