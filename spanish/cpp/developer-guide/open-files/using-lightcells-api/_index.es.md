---
title: Usando LightCells API con C++
linktitle: Utilizando la API de LightCells
type: docs
weight: 160
url: /es/cpp/using-lightcells-api/
description: Aprende cómo usar la LightCells API en C++ para leer y escribir archivos Excel grandes de manera eficiente con un uso mínimo de memoria.
---

{{% alert color="primary" %}} 

A veces necesitas leer y escribir archivos de Excel de Microsoft grandes con una enorme lista de datos o contenido en la hoja de cálculo. La API de LightCells es útil para crear hojas de cálculo de Excel extensas: con ella, necesita menos memoria y obtiene un mejor rendimiento y eficiencia.

{{% /alert %}} 

# Arquitectura Orientada a Eventos
Aspose.Cells proporciona la API de LightCells, diseñada principalmente para manipular los datos de las celdas una por una sin construir un modelo completo de datos (usando la colección de Celdas, etc.) en la memoria. Funciona en modo de eventos.

Para guardar libros de trabajo, proporciona el contenido de la celda una por una al guardar, y el componente lo guarda directamente en el archivo de salida.

Al leer archivos de plantilla, el componente analiza cada celda y proporciona su valor uno por uno.

En ambos procedimientos, se procesa un objeto de Celda y luego se descarta, el objeto de Libro de trabajo no retiene la colección. En este modo, por lo tanto, se ahorra memoria al importar y exportar archivos de Microsoft Excel que tienen un gran conjunto de datos que de otra manera usaría mucha memoria.

Aunque la API de LightCells procesa las celdas de la misma manera para archivos XLSX y XLS (no carga todas las celdas en la memoria sino que procesa una celda y luego la descarta), ahorra memoria de manera más efectiva para archivos XLSX que para archivos XLS debido a los diferentes modelos de datos y estructuras de los dos formatos.

Sin embargo, **para archivos XLS**, para ahorrar más memoria, los desarrolladores pueden especificar una ubicación temporal para guardar los datos temporales generados durante el proceso de Guardar. Comúnmente, **utilizando la API de LightCells para guardar archivos XLSX se puede ahorrar un 50% o más de memoria** que utilizando el método común, **guardando XLS puede ahorrar alrededor del 20-40% de memoria**.

## Escribir un Archivo de Excel Grande
Aspose.Cells proporciona una interfaz, `LightCellsDataProvider`, que debe ser implementada en tu programa. La interfaz representa el proveedor de datos para guardar archivos de hojas de cálculo grandes en modo liviano.

Al guardar un libro de trabajo en este modo, se verifica `StartSheet(int)` al guardar cada hoja en el libro. Para una hoja, si `StartSheet(int)` es verdadero, entonces todos los datos y propiedades de filas y celdas de dicha hoja son proporcionados por esta implementación. En primer lugar, se llama a `NextRow()` para obtener el próximo índice de fila a guardar. Si se devuelve un índice válido (el índice de fila debe estar en orden ascendente para las filas a guardar), entonces se proporciona un objeto `Row` que representa esa fila para que la implementación establezca sus propiedades mediante `StartRow(Row)`.

Para una fila, primero se verifica `NextCell()`. Si se devuelve un índice de columna válido (el índice de columna debe estar en orden ascendente para todas las celdas de una fila a guardar), entonces se proporciona un objeto `Cell` que representa esa celda para que la implementación establezca sus datos y propiedades mediante `StartCell(Cell)`. Después de establecer los datos de la celda, la celda se guarda directamente en el archivo de hoja de cálculo generado y se verifica y procesa la siguiente celda.

### Escribir un archivo Excel grande: ejemplo
Consulte el siguiente código de muestra para ver el funcionamiento de la API LightCells. Agregue, elimine o actualice los segmentos de código según sus necesidades.

El programa crea un archivo enorme con **10,000 (matriz 10000x30) registros** en una hoja y los llena con datos ficticios. Puedes especificar tu propia matriz cambiando las variables `rowsCount` y `colsCount` en el método `Main()`.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class TestDataProvider : public LightCellsDataProvider {
private:
    int _row = -1;
    int _column = -1;
    int maxRows;
    int maxColumns;
    Workbook _workbook;

public:
    TestDataProvider(Workbook workbook, int maxRows, int maxColumns)
        : _workbook(workbook), maxRows(maxRows), maxColumns(maxColumns) {}

    bool IsGatherString() override {
        return false;
    }

    int NextCell() override {
        ++_column;
        if (_column < this->maxColumns)
            return _column;
        else {
            _column = -1;
            return -1;
        }
    }

    int NextRow() override {
        ++_row;
        if (_row < this->maxRows) {
            _column = -1;
            return _row;
        }
        else
            return -1;
    }

    void StartCell(Cell& cell) override {
        cell.PutValue(_row + _column);
        if (_row != 1) {
            cell.SetFormula(u"=Rand() + A2");
        }
    }

    void StartRow(Row& row) override {}

    bool StartSheet(int sheetIndex) override {
        return sheetIndex == 0;
    }
};

void WriteUsingLightCellsAPI() {
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    int rowsCount = 10000;
    int colsCount = 30;

    Workbook workbook;
    OoxmlSaveOptions ooxmlSaveOptions;

    TestDataProvider dataProvider(workbook, rowsCount, colsCount);
    ooxmlSaveOptions.SetLightCellsDataProvider(&dataProvider);

    workbook.Save(outDir + u"output.out.xlsx", ooxmlSaveOptions);

    std::cout << "File saved successfully using LightCells API!" << std::endl;
}

int main() {
    Aspose::Cells::Startup();
    WriteUsingLightCellsAPI();
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Leer Archivos de Excel Grandes
Aspose.Cells proporciona una interfaz, `LightCellsDataHandler`, que debe ser implementada en tu programa. La interfaz representa el proveedor de datos para leer archivos de hojas de cálculo grandes en modo liviano.

Al leer un libro en este modo, se verifica `StartSheet` al leer cada hoja en el libro. Para una hoja, si `StartSheet` devuelve verdadero, entonces todos los datos y propiedades de las celdas en filas y columnas de la hoja son verificados y procesados por esta interfaz. Para cada fila, se llama a `StartRow` para verificar si necesita ser procesada. Si una fila necesita ser procesada, primero se leen sus propiedades y luego el desarrollador puede acceder a sus propiedades con `ProcessRow`. Si las celdas de la fila también necesitan ser procesadas, `ProcessRow` debe devolver verdadero y luego se llama a `StartCell` para cada celda existente en la fila para verificar si una celda necesita ser procesada. Si una celda necesita ser procesada, entonces se llama a `ProcessCell` para procesar la celda mediante esta interfaz.

### Leer archivos Excel grandes: ejemplo
Consulte el siguiente código de muestra para ver el funcionamiento de la API LightCells. Agregue, elimine o actualice los segmentos de código según sus necesidades.

El programa lee un archivo enorme con millones de registros en una hoja de cálculo. Se tarda un poco en leer cada hoja de cálculo en el libro. El código de muestra lee el archivo y recupera el número total de celdas, el recuento de cadenas y el recuento de fórmulas en cada hoja de cálculo.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

class LightCellsDataHandlerVisitCells : public LightCellsDataHandler
{
private:
    int cellCount;
    int formulaCount;
    int stringCount;

public:
    LightCellsDataHandlerVisitCells() : cellCount(0), formulaCount(0), stringCount(0) {}

    int GetCellCount() const { return cellCount; }
    int GetFormulaCount() const { return formulaCount; }
    int GetStringCount() const { return stringCount; }

    bool StartSheet(Worksheet& sheet) override
    {
        std::cout << "Processing sheet[" << sheet.GetName().ToUtf8() << "]" << std::endl;
        return true;
    }

    bool StartRow(int32_t rowIndex) override
    {
        return true;
    }

    bool ProcessRow(Row& row) override
    {
        return true;
    }

    bool StartCell(int32_t columnIndex) override
    {
        return true;
    }

    bool ProcessCell(Cell& cell) override
    {
        cellCount++;
        if (cell.IsFormula())
        {
            formulaCount++;
        }
        else if (cell.GetType() == CellValueType::IsString)
        {
            stringCount++;
        }
        return false;
    }
};

void Run()
{
    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create load options and set the light cells data handler
    LoadOptions opts;
    auto handler = std::make_shared<LightCellsDataHandlerVisitCells>();
    opts.SetLightCellsDataHandler(handler.get());

    // Load the workbook with the specified options
    Workbook wb(srcDir + u"LargeBook1.xlsx", opts);

    // Get the total number of sheets
    int sheetCount = wb.GetWorksheets().GetCount();

    // Output the results
    std::cout << "Total sheets: " << sheetCount << ", cells: " << handler->GetCellCount()
              << ", strings: " << handler->GetStringCount() << ", formulas: " << handler->GetFormulaCount() << std::endl;
}

int main()
{
    Aspose::Cells::Startup();
    Run();
    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
