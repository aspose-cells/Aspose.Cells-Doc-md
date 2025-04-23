---
title: Agregar mapa XML dentro del libro de trabajo usando el método XmlMapCollection.Add con C++
linktitle: Agregar mapa XML dentro del libro usando el método XmlMapCollection.Add
type: docs
weight: 10
url: /es/cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/
description: Agregar mapa XML dentro del libro usando el método XmlMapCollection.Add con C++.
---

## **Escenarios de uso posibles**

Aspose.Cells proporciona el método [**XmlMapCollection.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmapcollection/add/) que puede usar para importar su mapa XML dentro del libro.

## **Agregar mapa XML dentro del libro utilizando el método XmlMapCollection.Add**

El siguiente código de ejemplo agrega un mapa XML dentro del libro utilizando el método [**XmlMapCollection.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmapcollection/add/) y lo guarda como [archivo de Excel de salida](5115434.xlsx). La captura de pantalla muestra el mapa XML que se ha importado de [sample.xml](5115433.xml) dentro del archivo de Excel de salida.

![add-xml-map](add-xml-map.png)

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

    // Path of input XML file
    U16String inputXmlMap = srcDir + u"sample.xml";

    // Create workbook object
    Workbook workbook;

    // Add XML map found inside the sample.xml inside the workbook
    workbook.GetWorksheets().GetXmlMaps().Add(inputXmlMap);

    // Save the workbook in xlsx format
    U16String outputFilePath = srcDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully as xlsx format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
