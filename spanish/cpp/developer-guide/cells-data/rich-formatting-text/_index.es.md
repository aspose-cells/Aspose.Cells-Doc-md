---
title: Accede y actualiza las porciones del texto enriquecido de la celda con C++
linktitle: Texto con Formato Enriquecido
type: docs
weight: 40
url: /es/cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Aprende cómo acceder y actualizar las porciones del texto enriquecido de la celda a través de la API Aspose.Cells for C++.
keywords: Acceder y Actualizar Texto Enriquecido de la Celda, Obtener Texto Enriquecido de la Celda, Editar Texto Enriquecido de la Celda, Acceder a Texto Enriquecido de la Celda, Actualizar Texto Enriquecido de la Celda, Cambiar Texto Enriquecido de la Celda
---

{{% alert color="primary" %}}

Aspose.Cells te permite acceder y actualizar las porciones de texto enriquecido de la celda. Para este propósito, puedes usar los métodos [**Cell->GetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcharacters/) y [**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/). Estos métodos devolverán y aceptarán el arreglo de objetos [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/), que puedes usar para acceder y actualizar varias propiedades de fuente como el nombre de la fuente, color de la fuente, negrita, etc.

{{% /alert %}}

## **Acceder y actualizar partes de texto enriquecido de la celda**

El siguiente código demuestra el uso de los métodos [**Cell->GetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcharacters/) y [**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/) usando el [archivo de Excel fuente](5112369.xlsx). El archivo de Excel fuente tiene un texto enriquecido en la celda A1 con 3 porciones, cada una con una fuente diferente. El código accede a estas porciones y actualiza la fuente de la primera porción a **"Arial"**. El libro modificado se guarda como [archivo de Excel de salida](5112366.xlsx).

### Código C++ para acceder y actualizar las porciones del texto enriquecido

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputPath = srcDir + u"Sample.xlsx";
    U16String outputPath = outDir + u"Output.out.xlsx";

    Workbook workbook(inputPath);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Cell cell = worksheet.GetCells().Get(U16String(u"A1"));

    std::cout << "Before updating the font settings...." << std::endl;

    Vector<FontSetting> fnts = cell.GetCharacters();

    for (int i = 0; i < fnts.GetLength(); ++i)
    {
        FontSetting& fs = fnts[i];
        std::cout << fs.GetFont().GetName().ToUtf8() << std::endl;
    }

    if (fnts.GetLength() > 0)
    {
        FontSetting& fs = fnts[0];
        fs.GetFont().SetName(u"Arial");
        cell.SetCharacters(fnts);
    }

    std::cout << std::endl << "After updating the font settings...." << std::endl;

    fnts = cell.GetCharacters();

    for (int i = 0; i < fnts.GetLength(); ++i)
    {
        FontSetting& fs = fnts[i];
        std::cout << fs.GetFont().GetName().ToUtf8() << std::endl;
    }

    workbook.Save(outputPath);

    Aspose::Cells::Cleanup();
    return 0;
}
```

### Salida de consola generada por el código de ejemplo

Aquí está la salida de la consola al usar el [archivo de Excel fuente](5112369.xlsx):

{{< highlight java >}}

Before updating the font settings....
Century
Courier New
Verdana

After updating the font settings....
Arial
Courier New
Verdana

{{< /highlight >}}
