---
title: Verifica si el libro contiene enlaces externos ocultos con C++
linktitle: Verificar si el libro de trabajo contiene enlaces externos ocultos
type: docs
weight: 230
url: /es/cpp/check-if-workbook-contains-hidden-external-links/
description: Aprende cómo detectar enlaces externos ocultos en libros de Excel usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**
A veces, el libro contiene enlaces externos que están ocultos y no se pueden ver en Microsoft Excel. Aspose.Cells recupera todos los enlaces externos, visibles u ocultos. Sin embargo, puedes comprobar la propiedad [ExternalLink.IsVisible](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isvisible/) para verificar si el enlace externo es visible o no.

## **Verificar si la Hoja de Cálculo contiene Enlaces Externos Ocultos**
El siguiente código de ejemplo carga el [archivo de Excel de origen](5115413.xlsx) que contiene enlaces externos ocultos. Estos enlaces no se pueden ver en Microsoft Excel, pero están presentes en el libro. Después de imprimir [ExternalLink.GetDataSource()](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/getdatasource/) y la propiedad [ExternalLink.IsReferred](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isreferred/), también se imprime la propiedad [ExternalLink.IsVisible](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isvisible/). En la salida de la consola a continuación, puedes ver que todos sus enlaces externos no son visibles.

### **Código de muestra**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Loads the workbook which contains hidden external links
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access the external link collection of the workbook
    ExternalLinkCollection links = workbook.GetWorksheets().GetExternalLinks();

    // Print all the external links and check their IsVisible property
    for (int i = 0; i < links.GetCount(); i++)
    {
        ExternalLink link = links.Get(i);
        std::cout << "Data Source: " << link.GetDataSource().ToUtf8() << std::endl;
        std::cout << "Is Visible: " << (link.IsVisible() ? "true" : "false") << std::endl;
        std::cout << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

### **Salida de la consola**
Aquí está la salida de la consola del código de muestra anterior cuando se ejecuta con el [archivo de Excel de muestra proporcionado](5115413.xlsx).

{{< highlight java >}}

Data Source: C:\International\DDB\FAS 133\Swap Rates\GS_1M_3M_1_2_5_¥$_(B)IRSwaps_0400.xls

Is Referred: True

Is Visible: False

Data Source: C:\DIST DAY\MAY TEMPLATES\030601t.xls

Is Referred: True

Is Visible: False

Data Source: C:\AREVIEW\2002 Controllable\Autobrct.xls

Is Referred: True

Is Visible: False

Data Source: C:\CARDSFO\Main Files\Rate Forecast\FY 11\IFR 11 01 (New Model REPORTS 11.08.07).xls

Is Referred: True

Is Visible: False

{{< /highlight >}}
