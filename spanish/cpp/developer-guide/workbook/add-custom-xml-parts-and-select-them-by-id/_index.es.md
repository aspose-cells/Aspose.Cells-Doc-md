---
title: Agregar partes XML personalizadas y seleccionarlas por ID con C++
linktitle: Agregar partes XML personalizadas y seleccionarlas por ID
type: docs
weight: 70
url: /es/cpp/add-custom-xml-parts-and-select-them-by-id/
description: Aprenda cómo agregar y seleccionar partes XML personalizadas en archivos de Excel usando Aspose.Cells con C++.
---

## **Escenarios de uso posibles**

Las partes XML personalizadas son datos XML almacenados dentro de documentos de Microsoft Excel y son utilizadas por aplicaciones que interactúan con ellos. Actualmente, no hay una forma directa de agregarlas usando la interfaz de usuario de Microsoft Excel. Sin embargo, puede agregarlas programáticamente de varias maneras, como usando VSTO o Aspose.Cells. Use el método [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/add/) para agregar una Parte XML Personalizada usando la API de Aspose.Cells. También puede establecer su ID usando la propiedad [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/). De manera similar, si desea seleccionar una Parte XML Personalizada por ID, puede usar el método [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/).

## **Agregar partes XML personalizadas y seleccionarlas por ID**

El siguiente código de ejemplo primero agrega cuatro Partes XML Personalizadas usando el método [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/add/). Luego establece sus IDs usando la propiedad [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/). Finalmente, encuentra o selecciona una de las Partes XML Personalizadas agregadas usando el método [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/). Por favor, consulte también la salida de la consola del código dado a continuación como referencia.

## **Código de muestra**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Markup;

int main()
{
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Some data in the form of byte array
    // Please use correct XML and Schema instead
    Vector<uint8_t> btsData = { 1, 2, 3 };
    Vector<uint8_t> btsSchema = { 1, 2, 3 };

    // Create four custom xml parts
    wb.GetCustomXmlParts().Add(btsData, btsSchema);
    wb.GetCustomXmlParts().Add(btsData, btsSchema);
    wb.GetCustomXmlParts().Add(btsData, btsSchema);
    wb.GetCustomXmlParts().Add(btsData, btsSchema);

    // Assign ids to custom xml parts
    wb.GetCustomXmlParts().Get(0).SetID(u"Fruit");
    wb.GetCustomXmlParts().Get(1).SetID(u"Color");
    wb.GetCustomXmlParts().Get(2).SetID(u"Sport");
    wb.GetCustomXmlParts().Get(3).SetID(u"Shape");

    // Specify search custom xml part id
    U16String srchID = u"Fruit";
    srchID = u"Color";
    srchID = u"Sport";

    // Search custom xml part by the search id
    CustomXmlPart cxp = wb.GetCustomXmlParts().SelectByID(srchID);

    // Print the found or not found message on console
    if (cxp.IsNull())
    {
        std::cout << "Not Found: CustomXmlPart ID " << srchID.ToUtf8() << std::endl;
    }
    else
    {
        std::cout << "Found: CustomXmlPart ID " << srchID.ToUtf8() << std::endl;
    }

    std::cout << "AddCustomXMLPartsAndSelectThemByID executed successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Salida de la consola**

{{< highlight java >}}
Found: CustomXmlPart ID Sport
{{< /highlight >}}
