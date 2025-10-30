---
title: Encontrar el nombre del elemento raíz del mapa XML con C++
linktitle: Encuentre el nombre del elemento raíz de XML Map
type: docs
weight: 30
url: /es/cpp/find-the-root-element-name-of-xml-map/
description: Aprenda cómo encontrar el nombre del elemento raíz de un mapa XML usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Puede encontrar el *Nombre del elemento raíz del mapa XML* utilizando Aspose.Cells con la propiedad [**XmlMap.GetRootElementName()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmap/getrootelementname/). La siguiente captura de pantalla muestra el nombre del elemento raíz del mapa XML en Microsoft Excel.

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **Código de muestra**

El siguiente código de ejemplo carga el [archivo de Excel de ejemplo](55541789.xlsx) y accede al primer mapa XML e imprime su propiedad [**XmlMap.GetRootElementName()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmap/getrootelementname/). Consulte la salida de la consola del código de ejemplo a continuación.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleRootElementNameOfXmlMap.xlsx";

    // Load sample Excel file having Xml Map
    Workbook wb(inputFilePath);

    // Access first Xml Map inside the Workbook
    XmlMap xmap = wb.GetWorksheets().GetXmlMaps().Get(0);

    // Print Root Element Name of Xml Map on Console
    std::cout << "Root Element Name Of Xml Map: " << xmap.GetRootElementName().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Salida de la consola**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
