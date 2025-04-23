---
title: Configurar encabezados y pies de página diferentes para diferentes páginas con C++
linktitle: Configurar diferentes encabezados y pies de página
type: docs
weight: 35
url: /es/cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: Este artículo proporciona código de ejemplo que muestra cómo configurar programáticamente varios encabezados y pies de página en la configuración de página de la hoja de trabajo de Excel usando la biblioteca y API de C++. Puedes establecer los encabezados y pies de página para la primera página, páginas impares y páginas pares.
keywords: establecer encabezado y pie de página en Excel para la primera página c++, establecer encabezado y pie de página en páginas impares c++, establecer encabezado y pie de página en páginas pares c++
---

{{% alert color="primary" %}}

 MS Excel admite la configuración de diferentes encabezados y pies de página para la primera página, páginas impares y pares desde Excel 2007.
Aspose.Cells admite la misma función.

{{% /alert %}}

## **Configuración de diferentes encabezados y pies de página en MS Excel**

**![Configuración de diferentes encabezados y pies de página](difpage.png)**

 1. Haz clic en **Diseño de página > Configuración de impresión > Encabezado/Pie de página**.
 1. Marca **Diferentes páginas impares y pares** o **Primera página diferente**.
1. Ingrese encabezados y pies de página diferentes.

## **Configuración de diferentes encabezados y pies de página con Aspose.Cells**

Aspose.Cells se comporta igual que Excel.
 1. Establece las banderas [PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/ishfdiffoddeven/) y [PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/ishfdifffirst/) 
1. Ingrese encabezados y pies de página diferentes.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook wb;

    // Get the first worksheet's page setup
    PageSetup pageSetup = wb.GetWorksheets().Get(0).GetPageSetup();

    // Set different headers for odd and even pages
    pageSetup.SetIsHFDiffOddEven(true);
    pageSetup.SetHeader(1, u"I am the header of the Odd page.");
    pageSetup.SetEvenHeader(1, u"I am the header of the Even page.");

    // Set a different header for the first page
    pageSetup.SetIsHFDiffFirst(true);
    pageSetup.SetFirstPageHeader(1, u"I am the header of the First page.");

    Aspose::Cells::Cleanup();
}
```
