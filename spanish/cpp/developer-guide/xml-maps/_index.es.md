---
title: Importar XML a libro de trabajo de Excel con C++
linktitle: Mapas XML
type: docs
weight: 210
url: /es/cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: Importar datos de un archivo XML a Microsoft Excel usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Aspose.Cells permite importar el mapa XML dentro del libro usando el método [**Workbook.ImportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/importxml/). Puedes importar Mapas XML usando Microsoft Excel con los siguientes pasos:

- Seleccione la pestaña **Developer**.
- Haz clic en **Importar** en la sección de XML y sigue los pasos requeridos.

Deberás proporcionar tus datos XML para completar la importación. Aquí tienes un [ejemplo de datos XML](5115037.txt) que puedes usar para pruebas.

{{% /alert %}}

## **Importar Mapa XML usando Microsoft Excel**

La siguiente captura de pantalla muestra cómo importar un Mapa XML usando Microsoft Excel.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **Importar Mapa XML usando Aspose.Cells**

El siguiente código de ejemplo muestra cómo usar el método [**Workbook.ImportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/importxml/). Genera el [archivo Excel de salida](5115036.xlsx) como se muestra en esta captura de pantalla.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

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

    // Create a workbook
    Workbook workbook;

    // URL that contains your XML data for mapping
    U16String XML(u"http://www.aspose.com/docs/download/attachments/434475650/sampleXML.txt");

    // Import your XML Map data starting from cell A1
    workbook.ImportXml(XML, u"Sheet1", 0, 0);

    // Save workbook
    U16String outputPath = outDir + u"output_out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully with imported XML data!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Temas avanzados**
- [Agregar mapa XML dentro del libro utilizando el método XmlMapCollection.Add](/cells/es/cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [Exportar datos XML vinculados al mapa XML dentro del libro](/cells/es/cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [Encontrar el nombre del elemento raíz del mapa XML](/cells/es/cpp/find-the-root-element-name-of-xml-map/)
- [Vincular celdas a elementos del mapa XML](/cells/es/cpp/link-cells-to-xml-map-elements/)
