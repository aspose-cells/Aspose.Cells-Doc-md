---
title: Imprimir y Vista Previa del Libro de Trabajo con C++
linktitle: Imprimir y vista previa
type: docs
weight: 70
url: /es/cpp/workbook-and-worksheet-print-preview/
description: Aspose.Cells soporta imprimir y vista previa de archivos de Excel sin instalación de Microsoft Excel usando C++.
---

{{% alert color="primary" %}}

Después de crear una hoja de cálculo, a menudo querrá imprimir una copia en papel. Este artículo explica cómo imprimir hojas de cálculo con Aspose.Cells.

{{% /alert %}}

## **Introducción a la impresión**

Microsoft Excel asume que desea imprimir toda el área de la hoja de cálculo a menos que especifique una selección. Para imprimir usando Aspose.Cells, primero importe el espacio de nombres Aspose.Cells.Rendering al programa. Tiene varias clases útiles, por ejemplo, [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) y [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/).


## **Vista previa de impresión**

Puede haber casos en los que se necesite convertir archivos de Excel con millones de páginas a PDF o imágenes. Procesar tales archivos consumirá mucho tiempo y recursos. En tales casos, la función de vista previa de impresión del libro y la hoja de cálculo puede resultar útil. Antes de convertir dichos archivos, el usuario puede verificar el número total de páginas y decidir si se debe convertir o no. Este artículo se centra en el uso de las clases [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) y [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) para averiguar el número total de páginas.

Aspose.Cells proporciona la función de vista previa de impresión. Para esto, la API proporciona las clases [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) y [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/). Para crear la vista previa de impresión de todo el libro de trabajo, cree una instancia de la clase [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) pasando objetos [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) y [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) al constructor. La clase [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) proporciona un método [**GetEvaluatedPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/getevaluatedpagecount/) que devuelve el número de páginas en la vista previa generada. Al igual que la clase [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/), la clase [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) se utiliza para generar una vista previa de impresión para una hoja de cálculo específica. Para crear la vista previa de impresión de una hoja de cálculo, cree una instancia de la clase [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) pasando objetos [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) y [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) al constructor. La clase [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) también ofrece un método [**GetEvaluatedPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/getevaluatedpagecount/) que devuelve el número de páginas en la vista previa generada.

El siguiente fragmento de código demuestra el uso de las clases [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) y [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) utilizando el [archivo de Excel de muestra](94896177.xlsx).

### **Código de muestra**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Create image or print options
    ImageOrPrintOptions imgOptions;

    // Create workbook printing preview
    WorkbookPrintingPreview preview(workbook, imgOptions);
    cout << "Workbook page count: " << preview.GetEvaluatedPageCount() << endl;

    // Create sheet printing preview
    SheetPrintingPreview preview2(workbook.GetWorksheets().Get(0), imgOptions);
    cout << "Worksheet page count: " << preview2.GetEvaluatedPageCount() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

A continuación se muestra la salida generada al ejecutar el código anterior.

### **Salida de la consola**

{{< highlight java >}}

Workbook page count: 1
Worksheet page count: 1

{{< /highlight >}}

## **Temas avanzados**
- [Configuración de fuentes para la representación de hojas de cálculo](/cells/es/cpp/configuring-fonts-for-rendering-spreadsheets/)
- [Convertir hoja de cálculo a imagen - Eliminar espacios alrededor de los datos](/cells/es/cpp/convert-worksheet-to-image-remove-whitespace-around-data/)
- [Conversión de hoja de cálculo a imagen y hoja de cálculo a imagen por página](/cells/es/cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [Conversión de hoja de cálculo a imagen usando opciones de imagen o impresión](/cells/es/cpp/converting-worksheet-to-image-using-imageorprint-options/)
- [Exportar un rango de celdas en una hoja de cálculo a una imagen](/cells/es/cpp/export-range-of-cells-in-a-worksheet-to-image/)
- [Exportar hoja de cálculo o gráfico a imagen con ancho y alto deseados](/cells/es/cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Extraer imágenes de las hojas de cálculo usando opciones de imagen o impresión](/cells/es/cpp/extract-images-from-worksheets-using-imageorprintoptions/)
- [Generar miniatura de la hoja de cálculo](/cells/es/cpp/generate-thumbnail-of-the-worksheet/)
- [Página en Blanco de Salida cuando no hay Nada que Imprimir](/cells/es/cpp/output-blank-page-when-there-is-nothing-to-print/)
- [Configuración de página y opciones de impresión](/cells/es/cpp/page-setup-and-printing-options/)
- [Renderizar secuencia de páginas usando las propiedades PageIndex y PageCount de ImageOrPrintOptions](/cells/es/cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [Renderizar la hoja de cálculo en contexto gráfico](/cells/es/cpp/render-worksheet-to-graphic-context/)
- [Especificar un Conjunto Individual o Privado de Fuentes para la Representación del Libro](/cells/es/cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
{{< app/cells/assistant language="cpp" >}}
