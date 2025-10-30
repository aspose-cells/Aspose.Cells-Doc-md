---
title: Características de configuración de página con C++
linktitle: Funciones de configuración de página
type: docs
weight: 60
url: /es/cpp/page-setup-features/
description: Aprende cómo configurar las características de configuración de página en archivos de Excel usando Aspose.Cells con C++.
---

## **Funciones de configuración de página**

Aspose.Cells proporciona un conjunto completo de características para configurar las opciones de configuración de página para archivos de Excel. Estas características te permiten controlar varios aspectos del diseño de la página, como márgenes, orientación, tamaño del papel y más.

### **Establecer márgenes de página**

Puedes establecer los márgenes de la página para una hoja de cálculo usando la clase `PageSetup`. El siguiente ejemplo demuestra cómo establecer los márgenes superior, inferior, izquierdo y derecho:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPageMargins() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set page margins
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetTopMargin(1.0);
    pageSetup.SetBottomMargin(1.0);
    pageSetup.SetLeftMargin(0.75);
    pageSetup.SetRightMargin(0.75);

    // Save the workbook
    workbook.Save("PageMargins.xlsx");
}
```

### **Establecer orientación de página**

Puedes establecer la orientación de la página a retrato o paisaje usando la clase `PageSetup`. El siguiente ejemplo demuestra cómo establecer la orientación de la página a paisaje:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPageOrientation() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetOrientation(PageOrientationType::Landscape);
    workbook.Save("PageOrientation.xlsx");
}
```

### **Establecer tamaño de papel**

Puedes establecer el tamaño de papel para impresión usando la clase `PageSetup`. El siguiente ejemplo demuestra cómo establecer el tamaño de papel a A4:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPaperSize() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPaperSize(PaperSizeType::PaperA4);
    workbook.Save("PaperSize.xlsx");
}
```

### **Establecer área de impresión**

Puedes definir un rango específico de celdas para imprimir usando la clase `PageSetup`. El siguiente ejemplo demuestra cómo establecer el área de impresión:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintArea() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print area
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintArea("A1:D10");

    // Save the workbook
    workbook.Save("PrintArea.xlsx");
}
```

### **Configurar Saltos de Página**

Puedes insertar saltos de página en una hoja de cálculo para controlar dónde terminan las páginas y comienzan las nuevas. El siguiente ejemplo muestra cómo insertar un salto de página horizontal:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPageBreaks() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a horizontal page break at row 10
    worksheet.GetHorizontalPageBreaks().Add("A10");

    // Save the workbook
    workbook.Save("PageBreaks.xlsx");
}
```

### **Configurar Encabezado y Pie de Página**

Puedes personalizar el encabezado y pie de página de una hoja de cálculo usando la clase `PageSetup`. El siguiente ejemplo muestra cómo establecer un encabezado y pie de página personalizados:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetHeaderFooter() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set custom header and footer
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetHeader(0, "&CHeader Text");
    pageSetup.SetFooter(0, "&CFooter Text");

    // Save the workbook
    workbook.Save("HeaderFooter.xlsx");
}
```

### **Configurar Títulos de Impresión**

Puedes especificar filas o columnas que se repitan en la parte superior o izquierda de cada página impresa usando la clase `PageSetup`. El siguiente ejemplo muestra cómo establecer títulos de impresión:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintTitles() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print titles
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintTitleRows("$1:$1");
    pageSetup.SetPrintTitleColumns("$A:$A");

    // Save the workbook
    workbook.Save("PrintTitles.xlsx");
}
```

### **Configurar Calidad de Impresión**

Puedes establecer la calidad de impresión para una hoja de cálculo usando la clase `PageSetup`. El siguiente ejemplo muestra cómo configurar la calidad de impresión:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintQuality() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print quality
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintQuality(600);

    // Save the workbook
    workbook.Save("PrintQuality.xlsx");
}
```

### **Configurar Orden de Impresión**

Puedes establecer el orden de impresión para una hoja de cálculo usando la clase `PageSetup`. El siguiente ejemplo muestra cómo establecer el orden de impresión en "Sobre, luego Abajo":

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintOrder() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetOrder(PrintOrderType::OverThenDown);
    workbook.Save("PrintOrder.xlsx");
}
```

### **Configurar Líneas de Cuadrícula de Impresión**

Puedes controlar si las líneas de cuadrícula se imprimen usando la clase `PageSetup`. El siguiente ejemplo demuestra cómo habilitar la impresión de líneas de cuadrícula:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintGridlines() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Enable printing of gridlines
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintGridlines(true);

    // Save the workbook
    workbook.Save("PrintGridlines.xlsx");
}
```

### **Configurar Encabezados de Impresión**

Puedes controlar si los encabezados de filas y columnas se imprimen usando la clase `PageSetup`. El siguiente ejemplo muestra cómo habilitar la impresión de encabezados:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintHeadings() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Enable printing of headings
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintHeadings(true);

    // Save the workbook
    workbook.Save("PrintHeadings.xlsx");
}
```

### **Configurar Impresión en Blanco y Negro**

Puedes controlar si la hoja de cálculo se imprime en blanco y negro usando la clase `PageSetup`. El siguiente ejemplo demuestra cómo habilitar la impresión en blanco y negro:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintBlackAndWhite() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Enable black and white printing
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetBlackAndWhite(true);

    // Save the workbook
    workbook.Save("PrintBlackAndWhite.xlsx");
}
```

### **Configurar Impresión de Borrador**

Puedes controlar si la hoja de cálculo se imprime en modo borrador usando la clase `PageSetup`. El siguiente ejemplo muestra cómo habilitar la impresión en modo borrador:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintDraft() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintDraft(true);
    workbook.Save("PrintDraft.xlsx");
}
```

### **Configurar Comentarios de Impresión**

Puedes controlar si los comentarios se imprimen usando la clase `PageSetup`. El siguiente ejemplo muestra cómo habilitar la impresión de comentarios:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintComments() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);
    workbook.Save("PrintComments.xlsx");
}
```

### **Configurar Errores de Impresión**

Puedes controlar cómo se imprimen los errores usando la clase `PageSetup`. El siguiente ejemplo muestra cómo establecer la opción de impresión de errores:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintErrors() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsBlank);
    workbook.Save("PrintErrors.xlsx");
}
```

### **Configurar Área de Impresión para que quepa en Páginas**

Puedes controlar si el área de impresión se escala para ajustarse a un número específico de páginas usando la clase `PageSetup`. El siguiente ejemplo muestra cómo ajustar el área de impresión para que quepa en una página de ancho por una de alto:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintAreaFitToPages() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print area to fit to one page wide and one page tall
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetFitToPagesWide(1);
    pageSetup.SetFitToPagesTall(1);

    // Save the workbook
    workbook.Save("PrintAreaFitToPages.xlsx");
}
```

### **Configurar Escala de Impresión**

Puedes establecer la escala de impresión para una hoja de cálculo usando la clase `PageSetup`. El siguiente ejemplo muestra cómo establecer la escala de impresión al 50%:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintScale() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print scale to 50%
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetZoom(50);

    // Save the workbook
    workbook.Save("PrintScale.xlsx");
}
```

### **Configurar Centrado de Impresión Horizontal y Vertical**

Puedes controlar si la hoja de cálculo está centrada horizontal y verticalmente en la página impresa usando la clase `PageSetup`. El siguiente ejemplo muestra cómo centrar la hoja de cálculo horizontal y verticalmente:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintCenterHorizontallyAndVertically() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Center the worksheet horizontally and vertically
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetCenterHorizontally(true);
    pageSetup.SetCenterVertically(true);

    // Save the workbook
    workbook.Save("PrintCenterHorizontallyAndVertically.xlsx");
}
```

### **Configurar Número de la Primera Página de Impresión**

Puedes establecer el número de la primera página para impresión usando la clase `PageSetup`. El siguiente ejemplo muestra cómo establecer el número de la primera página:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintFirstPageNumber() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the first page number
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetFirstPageNumber(2);

    // Save the workbook
    workbook.Save("PrintFirstPageNumber.xlsx");
}
```

### **Configurar número de página de impresión**

Puedes controlar si se imprime el número de página usando la clase `PageSetup`. El siguiente ejemplo muestra cómo habilitar la impresión del número de página:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintPrintPageNumber() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetHeader(0, "&P");
    workbook.Save("PrintPageNumber.xlsx");
}
```

### **Configurar orden de impresión de páginas**

Puedes establecer el orden en que se imprimen las páginas usando la clase `PageSetup`. El siguiente ejemplo muestra cómo establecer el orden de las páginas en "Abajo, luego Horizontal":

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintPageOrder() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the page order to "Down, then Over"
    PageSetup
{{< app/cells/assistant language="cpp" >}}
