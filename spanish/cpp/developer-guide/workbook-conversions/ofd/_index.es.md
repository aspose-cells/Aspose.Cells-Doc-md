---
title: Conversión de Excel al formato OFD
linktitle: Conversión de Excel al formato OFD
description: Aspose.Cells es una biblioteca de C++ para trabajar con archivos de hojas de cálculo que admite la conversión de libros de Excel al formato OFD (Open Fixed-layout Document). Este artículo muestra cómo crear contenido de Excel y exportarlo como OFD, así como cómo convertir archivos Excel existentes a OFD usando Aspose.Cells.
keywords: Aspose.Cells, biblioteca de C++, hoja de cálculo, Excel a OFD, conversión OFD, SaveFormat.Ofd, documento de diseño fijo, exportación de libros
type: docs
weight: 195
url: /es/cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells admite la conversión de libros de Excel directamente al formato OFD (Open Fixed-layout Document) utilizando el valor de la enumeración `SaveFormat.Ofd`. El documento OFD resultante conserva el diseño visible del libro, el contenido, las celdas combinadas, los anchos de columna, las alturas de fila, las fuentes, los colores, los bordes y los formatos de número. Esto hace que Aspose.Cells sea adecuado para flujos de trabajo de archivo, impresión, presentación regulatoria y presentación ante organismos gubernamentales que requieren una salida de diseño fijo.

{{% /alert %}}
## **Introducción**
OFD (Open Fixed-layout Document) es un estándar nacional chino (GB/T 33190-2016) para representar documentos digitales en un diseño fijo basado en páginas. Desempeña un papel similar al de PDF en casos de uso donde la apariencia visual del documento de origen debe conservarse exactamente como fue creado. OFD se adopta ampliamente para presentaciones ante organismos gubernamentales, presentaciones regulatorias, facturas electrónicas y archivado a largo plazo en la República Popular China.

La conversión de libros de Excel a OFD es un requisito común en escenarios donde el contenido de la hoja de cálculo debe distribuirse como un artefacto de solo lectura con diseño bloqueado en lugar de como una hoja de cálculo editable. Algunos ejemplos incluyen el envío de una factura finalizada a un cliente, el archivado de un informe financiero trimestral o la presentación de una hoja de cálculo de presupuesto a una autoridad regulatoria. Aspose.Cells aborda este requisito a través del valor de la enumeración `SaveFormat.Ofd`, que escribe el libro directamente en OFD sin necesidad de un paso de conversión intermedio. La salida OFD conserva los valores de celda, los rangos combinados, las fuentes, los colores, los bordes, los formatos de número y las opciones de configuración de página establecidas en el libro.

{{% alert color="primary" %}}

La salida OFD generada por Aspose.Cells conserva el diseño visible del libro de origen, incluyendo el contenido de las celdas, las celdas combinadas, los anchos de columna y las alturas de fila. El formato de celda, como las fuentes, los colores, los bordes, la alineación y los formatos de número, también se representa en la salida de diseño fijo. Las opciones de configuración de página establecidas en la hoja de cálculo, como el tamaño del papel, la orientación y el área de impresión, influyen en el diseño del documento OFD resultante.

{{% /alert %}}
## **Creación de un libro de Excel y guardado como OFD**
Aspose.Cells permite construir un libro de forma programática, rellenarlo con datos y luego guardarlo directamente en formato OFD utilizando la enumeración `SaveFormat.Ofd`. El siguiente ejemplo crea una factura desde cero. Añade un logotipo de la empresa, información de encabezado, una sección de facturación, líneas de detalle y totales calculados, y luego exporta el libro a un documento OFD.
### **Creación de una factura con un logotipo**
El ejemplo construye una hoja de cálculo de factura insertando una imagen de logotipo en el área superior izquierda, rellenando el nombre de la empresa y los datos de contacto, añadiendo un título "FACTURA" en celdas combinadas, registrando el número y la fecha de la factura, listando el cliente a facturar, construyendo una tabla de líneas de detalle con columnas de descripción, cantidad, precio unitario y total, y calculando el subtotal, los impuestos y el total general mediante fórmulas de celda. Se aplica formato, como encabezados en negrita, formato de moneda para los precios, bordes y anchos de columna utilizando los objetos `Style` y `Font`. Finalmente, el libro se guarda con la extensión `.ofd` utilizando `SaveFormat.Ofd`.

```cpp
// Aspose.Cells para ejemplo en C++
// Compilar con Aspose.Cells 26.6.0 (o posterior) y un compilador C++17 (o posterior)

#include "Aspose.Cells.h"
#include <string>
#include <ctime>

using namespace Aspose::Cells;

int main()
{
    // Inicializar Aspose.Cells
    Aspose::Cells::Startup();

    // Directorio para recursos y salida
    const char16_t* dataDir = u"C:\\Temp\\";

    // Crear un nuevo libro de trabajo
    Workbook workbook;

    // Obtener la primera hoja de cálculo
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Establecer anchos de columna
    cells.SetColumnWidth(0, 5.0);
    cells.SetColumnWidth(1, 35.0);
    cells.SetColumnWidth(2, 12.0);
    cells.SetColumnWidth(3, 15.0);
    cells.SetColumnWidth(4, 15.0);
    cells.SetColumnWidth(5, 5.0);

    // Insertar el logo de la empresa
    worksheet.GetPictures().Add(1, 1, U16String(dataDir) + u"logo.png");

    // Nombre de la empresa y datos de contacto
    cells.Get(u"B3").PutValue(u"Acme Corporation");
    cells.Get(u"B4").PutValue(u"123 Business Street");
    cells.Get(u"B5").PutValue(u"City, State 12345");
    cells.Get(u"B6").PutValue(u"Phone: (555) 123-4567");

    // Título INVOICE - combinar celdas
    cells.Merge(7, 1, 2, 4);
    Cell titleCell = cells.Get(u"B8");
    titleCell.PutValue(u"INVOICE");

    Style titleStyle = workbook.CreateStyle();
    titleStyle.GetFont().SetIsBold(true);
    titleStyle.GetFont().SetSize(20);
    titleStyle.SetHorizontalAlignment(TextAlignmentType::Center);
    titleCell.SetStyle(titleStyle);

    // Número de factura y fecha
    cells.Get(u"B11").PutValue(u"Invoice Number:");
    cells.Get(u"C11").PutValue(u"INV-2024-001");
    cells.Get(u"B12").PutValue(u"Date:");

    std::time_t t = std::time(nullptr);
    std::tm* now = std::localtime(&t);
    char dateBuffer[11];
    std::strftime(dateBuffer, sizeof(dateBuffer), "%Y-%m-%d", now);
    cells.Get(u"C12").PutValue(U16String(dateBuffer));

    // Sección de facturación
    cells.Get(u"B14").PutValue(u"Bill To:");
    cells.Get(u"B15").PutValue(u"Client Name");
    cells.Get(u"B16").PutValue(u"Client Address");
    cells.Get(u"B17").PutValue(u"Client City, State");

    // Encabezado de líneas de detalle
    Cell headerDesc = cells.Get(u"B19");
    Cell headerQty = cells.Get(u"C19");
    Cell headerPrice = cells.Get(u"D19");
    Cell headerTotal = cells.Get(u"E19");

    headerDesc.PutValue(u"Description");
    headerQty.PutValue(u"Quantity");
    headerPrice.PutValue(u"Unit Price");
    headerTotal.PutValue(u"Total");

    Style headerStyle = workbook.CreateStyle();
    headerStyle.GetFont().SetIsBold(true);
    headerStyle.GetFont().SetColor(Color::White());
    headerStyle.SetForegroundColor(Color{0, 0, 128});
    headerStyle.SetPattern(BackgroundType::Solid);
    headerStyle.SetHorizontalAlignment(TextAlignmentType::Center);
    headerStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    headerStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    headerStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    headerStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);

    headerDesc.SetStyle(headerStyle);
    headerQty.SetStyle(headerStyle);
    headerPrice.SetStyle(headerStyle);
    headerTotal.SetStyle(headerStyle);

    // Estilo de moneda con bordes
    Style currencyStyle = workbook.CreateStyle();
    currencyStyle.SetCustom(u"\"$\"#,##0.00");
    currencyStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);

    // Estilo de borde simple para celdas de descripción/cantidad
    Style borderStyle = workbook.CreateStyle();
    borderStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);

    // Filas de líneas de detalle
    struct LineItem { const char16_t* desc; int qty; double price; };
    LineItem lineItems[] = {
        {u"Product A - Widget", 2, 50.00},
        {u"Product B - Gadget", 3, 75.00},
        {u"Product C - Service", 1, 100.00}
    };

    for (int i = 0; i < 3; i++)
    {
        int row = 20 + i;
        Cell descCell = cells.Get(row, 1);
        Cell qtyCell = cells.Get(row, 2);
        Cell priceCell = cells.Get(row, 3);
        Cell totalCell = cells.Get(row, 4);

        descCell.PutValue(lineItems[i].desc);
        qtyCell.PutValue(lineItems[i].qty);
        priceCell.PutValue(lineItems[i].price);

        std::string formula = "C" + std::to_string(row) + "*D" + std::to_string(row);
        totalCell.SetFormula(U16String(formula.c_str()));

        descCell.SetStyle(borderStyle);
        qtyCell.SetStyle(borderStyle);
        priceCell.SetStyle(currencyStyle);
        totalCell.SetStyle(currencyStyle);
    }

    // Subtotal, impuesto, total general
    cells.Get(u"B24").PutValue(u"Subtotal:");
    Cell subtotalCell = cells.Get(u"E24");
    subtotalCell.SetFormula(u"SUM(E20:E22)");

    cells.Get(u"B25").PutValue(u"Tax (10%):");
    Cell taxCell = cells.Get(u"E25");
    taxCell.SetFormula(u"E24*0.1");

    cells.Get(u"B26").PutValue(u"Grand Total:");
    Cell grandTotalCell = cells.Get(u"E26");
    grandTotalCell.SetFormula(u"E24+E25");

    // Estilo de negrita + moneda para los valores totales
    Style totalStyle = workbook.CreateStyle();
    totalStyle.GetFont().SetIsBold(true);
    totalStyle.SetCustom(u"\"$\"#,##0.00");

    subtotalCell.SetStyle(totalStyle);
    taxCell.SetStyle(totalStyle);
    grandTotalCell.SetStyle(totalStyle);

    // Estilo de negrita para las etiquetas de totales
    Style boldStyle = workbook.CreateStyle();
    boldStyle.GetFont().SetIsBold(true);

    cells.Get(u"B24").SetStyle(boldStyle);
    cells.Get(u"B25").SetStyle(boldStyle);
    cells.Get(u"B26").SetStyle(boldStyle);

    // Guardar el libro de trabajo como un archivo OFD
    workbook.Save(U16String(dataDir) + u"Invoice.ofd", SaveFormat::Ofd);

    // Liberar los recursos de Aspose.Cells
    Aspose::Cells::Cleanup();

    return 0;
}
```
## **Conversión de un archivo Excel existente a OFD**
Aspose.Cells también puede cargar un libro de Excel existente desde el disco y exportarlo directamente al formato OFD. Esto es útil para canalizaciones de conversión por lotes, flujos de trabajo de archivo y escenarios en los que el libro de origen fue producido por otra herramienta y solo necesita ser reemitido como un artefacto de diseño fijo. El siguiente ejemplo carga un libro `.xlsx` existente, lee datos de sus celdas, aplica ajustes opcionales de configuración de página y guarda el resultado como un documento OFD.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <iostream>
#include <ctime>

using namespace Aspose::Cells;

std::string GetCurrentTimestamp() {
    std::time_t t = std::time(nullptr);
    std::tm* now = std::localtime(&t);
    char buffer[20];
    std::strftime(buffer, sizeof(buffer), "%Y-%m-%d %H:%M:%S", now);
    return std::string(buffer);
}

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "C:\\Examples\\";

    // Abrir un libro de Excel existente desde el disco
    Workbook workbook(U16String((dataDir + "SampleBook.xlsx").c_str()));

    // (1) Leer y mostrar valores de celdas seleccionadas para confirmar que el archivo fue cargado
    Worksheet firstSheet = workbook.GetWorksheets().Get(0);
    U16String sheetName = firstSheet.GetName();
    Cell a1 = firstSheet.GetCells().Get(u"A1");
    Cell b1 = firstSheet.GetCells().Get(u"B1");
    Cell c1 = firstSheet.GetCells().Get(u"C1");

    std::cout << "First sheet name: " << sheetName.ToUtf8() << std::endl;
    std::cout << "Cell A1: " << a1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Cell B1: " << b1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Cell C1: " << c1.GetStringValue().ToUtf8() << std::endl;

    // (2) Iterar sobre la colección Worksheets para enumerar las hojas disponibles
    std::cout << "\nAvailable worksheets:" << std::endl;
    WorksheetCollection sheets = workbook.GetWorksheets();
    int sheetCount = sheets.GetCount();
    for (int i = 0; i < sheetCount; ++i) {
        Worksheet ws = sheets.Get(i);
        U16String wsName = ws.GetName();
        std::cout << "  [" << i << "] " << wsName.ToUtf8() << std::endl;
    }

    // (3) Opcionalmente actualizar una celda con marca de tiempo para reflejar la conversión
    std::string timestamp1 = GetCurrentTimestamp();
    firstSheet.GetCells().Get(u"A1").PutValue(U16String(("Converted on: " + timestamp1).c_str()));

    // Agregar una fila de encabezado de resumen en la parte superior del bloque de datos
    firstSheet.GetCells().InsertRow(0);
    firstSheet.GetCells().Get(u"A1").PutValue(u"Conversion Summary");

    std::string timestamp2 = GetCurrentTimestamp();
    firstSheet.GetCells().Get(u"A2").PutValue(U16String(("Generated: " + timestamp2).c_str()));

    // (4) Configurar las propiedades de PageSetup en la hoja de cálculo
    PageSetup pageSetup = firstSheet.GetPageSetup();
    pageSetup.SetOrientation(PageOrientationType::Landscape);
    pageSetup.SetPaperSize(PaperSizeType::PaperA4);
    pageSetup.SetFitToPagesTall(1);
    pageSetup.SetFitToPagesWide(1);

    // (5) Opcionalmente establecer el área de impresión para la salida OFD
    int lastRow = firstSheet.GetCells().GetMaxDataRow();
    int lastCol = firstSheet.GetCells().GetMaxDataColumn();
    U16String lastColLetter = CellsHelper::ColumnIndexToName(lastCol);
    std::string printArea = "A1:" + lastColLetter.ToUtf8() + std::to_string(lastRow + 1);
    firstSheet.GetPageSetup().SetPrintArea(U16String(printArea.c_str()));
    std::cout << "\nPrint area set to: " << printArea << std::endl;

    // (6) Guardar el libro como un archivo OFD
    workbook.Save(U16String((dataDir + "SampleBook.ofd").c_str()), SaveFormat::Ofd);
    std::cout << "\nFile successfully converted to OFD format: " << dataDir << "SampleBook.ofd" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Artículos relacionados**
- [Dividir archivos Excel en varios archivos](/cells/es/cpp/splitting-excel-files-into-multiple-files/)
- [Insertar una imagen en una celda](/cells/es/cpp/inserting-an-image-into-a-cell/)
- [Leer y escribir archivos DBF](/cells/es/cpp/dbf/)
- [Convertir minigráficos a imagen y HTML en Aspose.Cells for C++](/cells/es/cpp/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="cpp" >}}