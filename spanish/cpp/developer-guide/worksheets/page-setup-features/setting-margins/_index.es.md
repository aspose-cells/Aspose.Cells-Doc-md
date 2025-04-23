---
title: Configurar márgenes con C++
linktitle: Configurando Márgenes
type: docs
weight: 20
url: /es/cpp/setting-margins/
description: Aprende a establecer los márgenes de una hoja de cálculo de Excel usando C++. Esta guía cubre la configuración de márgenes de página, centrar contenido y configurar márgenes de encabezado y pie de página de forma programática con Aspose.Cells for C++.
keywords: establecer margen de hoja de cálculo de Excel al centro c++, establecer margen de encabezado y pie de página c++
---

{{% alert color="primary" %}}

Aspose.Cells soporta completamente las opciones de configuración de página de Microsoft Excel. Los desarrolladores pueden necesitar configurar ajustes de configuración de página para hojas de cálculo para controlar el proceso de impresión. Este tema discute cómo usar Aspose.Cells para configurar márgenes de página.

{{% /alert %}}

## **Configurando Márgenes**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene la colección [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

La clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) proporciona la propiedad [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) que se utiliza para configurar las opciones de configuración de página de una hoja de cálculo. El atributo [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) es un objeto de la clase [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) que permite a los desarrolladores establecer diferentes opciones de diseño de página para una hoja impresa. La clase [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) ofrece varias propiedades y métodos utilizados para configurar las opciones de configuración de página.

### **Márgenes de Página**

Establece márgenes de página (izquierda, derecha, superior, inferior) utilizando los miembros de la clase [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/). A continuación se enumeran algunos de los métodos que se usan para especificar los márgenes de página:

- [**GetLeftMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getleftmargin/)
- [**GetRightMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getrightmargin/)
- [**GetTopMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/gettopmargin/)
- [**GetBottomMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getbottommargin/)

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

    // Create a workbook object
    Workbook workbook;

    // Get the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first (default) worksheet
    Worksheet worksheet = worksheets.Get(0);

    // Get the pagesetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set bottom, left, right, and top page margins
    pageSetup.SetBottomMargin(2);
    pageSetup.SetLeftMargin(1);
    pageSetup.SetRightMargin(1);
    pageSetup.SetTopMargin(3);

    // Save the Workbook
    workbook.Save(outDir + u"SetMargins_out.xls");

    std::cout << "Margins set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Centrar en la Página**

Es posible centrar algo en una página horizontal y verticalmente. Para esto, hay algunos miembros útiles de la clase [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/), [**GetCenterHorizontally()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcenterhorizontally/) y [**GetCenterVertically()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcentervertically/).

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

    // Create a workbook object
    Workbook workbook;

    // Get the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first (default) worksheet
    Worksheet worksheet = worksheets.Get(0);

    // Get the pagesetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Specify Center on page Horizontally and Vertically
    pageSetup.SetCenterHorizontally(true);
    pageSetup.SetCenterVertically(true);

    // Save the Workbook
    workbook.Save(outDir + u"CenterOnPage_out.xls");

    std::cout << "Workbook saved successfully with centered page setup!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Márgenes de Encabezado y Pie de Página**

Establece márgenes de encabezado y pie de página con los miembros de la clase [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) como [**GetHeaderMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getheadermargin/) y [**GetFooterMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfootermargin/).

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

    // Create a workbook object
    Workbook workbook;

    // Get the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first (default) worksheet
    Worksheet worksheet = worksheets.Get(0);

    // Get the pagesetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Specify Header / Footer margins
    pageSetup.SetHeaderMargin(2);
    pageSetup.SetFooterMargin(2);

    // Save the Workbook
    workbook.Save(outDir + u"CenterOnPage_out.xls");

    std::cout << "Workbook saved successfully with centered header and footer margins!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
