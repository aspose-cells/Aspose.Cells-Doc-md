---
title: Configuración de opciones de impresión con C++
linktitle: Configuración de Opciones de Impresión
type: docs
weight: 40
url: /es/cpp/setting-print-options/
description: Este artículo demuestra cómo establecer programáticamente las Opciones de impresión del concepto Configuración de página de la hoja de Excel usando la API y Biblioteca en C++. Puede establecer el área de impresión, los títulos de impresión y el orden de las páginas.
keywords: establecer área de impresión en Excel c++, establecer títulos de impresión en Excel c++, establecer orden de página en Excel c++
---

{{% alert color="primary" %}}

La configuración de página de Microsoft Excel proporciona varias opciones de impresión (también conocidas como opciones de hoja) que permiten a los usuarios controlar cómo se imprimen las páginas de la hoja de cálculo.

{{% /alert %}}

## **Configuración de Opciones de Impresión**

Estas opciones de impresión permiten a los usuarios:

- Seleccionar un área de impresión específica en una hoja de cálculo.
- Títulos de impresión.
- Líneas de cuadrícula de impresión.
- Encabezados de fila/columna de impresión.
- Lograr calidad de borrador.
- Comentarios de impresión.
- Errores de celda de impresión.
- Definir el orden de páginas.

Aspose.Cells soporta todas las opciones de impresión ofrecidas por Microsoft Excel, y los desarrolladores pueden configurar fácilmente estas opciones para las hojas de cálculo usando las propiedades ofrecidas por la clase [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/). Cómo se utilizan estas propiedades se discute a continuación en más detalle.

### **Establecer Área de Impresión**

De forma predeterminada, el área de impresión abarca todas las áreas de la hoja de cálculo que contienen datos. Los desarrolladores pueden establecer un área de impresión específica de la hoja de cálculo.

Para seleccionar un área de impresión específica, utilice la propiedad [**GetPrintArea()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintarea/) de la clase [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/). Asigne un rango de celdas que define el área de impresión a esta propiedad.

```cpp
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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the PageSetup object of the worksheet
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set the print area to the range A1:T35
    pageSetup.SetPrintArea(u"A1:T35");

    // Save the workbook
    workbook.Save(outDir + u"SetPrintArea_out.xls");

    std::cout << "Print area set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Establecer Títulos de Impresión**

Aspose.Cells le permite designar encabezados de fila y columna para repetir en todas las páginas de una hoja de cálculo impresa. Para hacerlo, utilice las propiedades [**GetPrintTitleColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlecolumns/) y [**GetPrintTitleRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlerows/) de la clase [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/).

Las filas o columnas que se repetirán se definen pasando sus números de fila o columna. Por ejemplo, las filas se definen como $1:$2 y las columnas se definen como $A:$B.

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

    // Path of output excel file
    U16String outputFilePath = outDir + u"SetPrintTitle_out.xls";

    // Create a new workbook
    Workbook workbook;

    // Obtain the reference of the PageSetup of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Define column numbers A & B as title columns
    pageSetup.SetPrintTitleColumns(u"$A:$B");

    // Define row numbers 1 & 2 as title rows
    pageSetup.SetPrintTitleRows(u"$1:$2");

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Print titles set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Establecer Otras Opciones de Impresión**

La clase [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) también proporciona varias otras propiedades para establecer opciones de impresión generales de la siguiente manera:

- [**GetPrintGridlines()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintgridlines/): una propiedad booleana que define si se deben imprimir las líneas de cuadricula o no.
- [**GetPrintHeadings()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintheadings/): propiedad booleana que define si imprimir o no los encabezados de fila y columna.
- [**GetBlackAndWhite()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getblackandwhite/): propiedad booleana que define si imprimir la hoja de cálculo en modo blanco y negro o no.
- [**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/): define si mostrar los comentarios de impresión en la hoja de cálculo o al final de la hoja de cálculo.
- [**GetPrintDraft()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintdraft/): una propiedad booleana que define si se debe imprimir la hoja sin gráficos.
- [**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/): define si se deben imprimir los errores de celda como se muestran, en blanco, guion o N/A.

Para establecer las propiedades [**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/) y [**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/), Aspose.Cells también proporciona dos enumeraciones, [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) y [**PrintErrorsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printerrorstype/) que contienen valores predefinidos que se asignarán a las propiedades [**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/) y [**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/) respectivamente.

Los valores predefinidos en la enumeración [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) se enumeran a continuación con sus descripciones.

|**Tipos de Imprimir Comentarios**|**Descripción**|
| :- | :- |
|PrintInPlace| Especifica imprimir comentarios como se muestra en la hoja de cálculo.
|PrintNoComments| Especifica no imprimir comentarios.
|PrintSheetEnd| Especifica imprimir comentarios al final de la hoja de cálculo.

Los valores predefinidos de la enumeración [**PrintErrorsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printerrorstype/) se enumeran a continuación con sus descripciones.

|**Tipos de Imprimir Errores**|**Descripción**|
| :- | :- |
|PrintErrorsBlank| Especifica no imprimir errores.
|PrintErrorsDash| Especifica imprimir errores como "--".
|PrintErrorsDisplayed| Especifica imprimir errores como se muestra.
|PrintErrorsNA| Especifica imprimir errores como "#N/A".

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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the PageSetup object of the worksheet
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set print options
    pageSetup.SetPrintGridlines(true);  // Allow printing gridlines
    pageSetup.SetPrintHeadings(true);   // Allow printing row/column headings
    pageSetup.SetBlackAndWhite(true);   // Allow printing in black & white mode
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);  // Print comments as displayed
    pageSetup.SetPrintDraft(true);      // Print with draft quality
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsNA);  // Print cell errors as N/A

    // Save the workbook
    U16String outputPath = outDir + u"OtherPrintOptions_out.xls";
    workbook.Save(outputPath);

    std::cout << "Workbook saved with print options successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Establecer Orden de Páginas**

La clase [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) proporciona la propiedad [**GetOrder()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getorder/) que se utiliza para ordenar varias páginas de la hoja de cálculo a imprimir. Hay dos posibilidades para ordenar las páginas de la siguiente manera.

- **Hacia abajo y luego hacia la derecha:** imprime todas las páginas hacia abajo antes de imprimir cualquier página hacia la derecha.
- **Hacia la derecha y luego hacia abajo:** imprime las páginas de izquierda a derecha antes de imprimir las páginas por debajo.

Aspose.Cells proporciona una enumeración, [**PrintOrderType**](https://reference.aspose.com/cells/cpp/aspose.cells/printordertype/) que contiene todos los tipos de orden predefinidos.

Los valores predefinidos de la enumeración [**PrintOrderType**](https://reference.aspose.com/cells/cpp/aspose.cells/printordertype/) se enumeran a continuación.

|**Tipos de Orden de Impresión**|**Descripción**|
| :- | :- |
|DownThenOver|Representa el orden de impresión como primero hacia abajo y luego hacia adelante.|
|OverThenDown|Representa el orden de impresión como primero hacia adelante y luego hacia abajo.|

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

    // Create a new workbook
    Workbook workbook;

    // Obtain the reference of the PageSetup of the first worksheet
    PageSetup pageSetup = workbook.GetWorksheets().Get(0).GetPageSetup();

    // Set the printing order of the pages to over then down
    pageSetup.SetOrder(PrintOrderType::OverThenDown);

    // Save the workbook
    workbook.Save(outDir + u"SetPageOrder_out.xls");

    std::cout << "Page order set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
