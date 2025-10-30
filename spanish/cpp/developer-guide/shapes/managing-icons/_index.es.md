---
title: Agregar iconos a la hoja de cálculo con C++
linktitle: Gestionar iconos
type: docs
weight: 100
url: /es/cpp/insert-svg-to-excel/
description: Aprende cómo agregar iconos a hojas de cálculo de Excel usando Aspose.Cells con C++.
---

## Agregar iconos a la hoja de cálculo en Aspose.Cells

Si necesita usar [Aspose.Cells](https://products.aspose.com/cells/) para agregar 'iconos' en un archivo de Excel, este documento puede ofrecerle ayuda.

La interfaz de Excel correspondiente a la operación de insertar icono es la siguiente:

![](1.png)

- Seleccione la posición del icono a insertar en la hoja de cálculo
- Haga clic izquierdo *Insertar*->*Iconos*
- En la ventana que se abre, seleccione el icono en el rectángulo rojo en la figura anterior
- Haz clic izquierdo en *Insertar*, se insertará en el archivo de Excel.

El efecto es el siguiente:

![](2.png)

Aquí, hemos preparado *código de ejemplo* para ayudarte a insertar íconos usando [Aspose.Cells](https://products.aspose.com/cells/). También hay un [archivo de ejemplo](sample.xlsx) y un [archivo de recursos](icon.zip). Usamos la interfaz de Excel para insertar un ícono con el mismo efecto visual que el [archivo de recursos](icon.zip) en el [archivo de ejemplo](sample.xlsx).

### C++

```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    U16String fileName = u"icon.svg";
    std::ifstream fsSource(fileName.ToUtf8(), std::ios::binary);
    if (!fsSource) {
        std::cerr << "Failed to open file: " << fileName.ToUtf8() << std::endl;
        return -1;
    }

    fsSource.seekg(0, std::ios::end);
    size_t fileSize = fsSource.tellg();
    fsSource.seekg(0, std::ios::beg);

    std::vector<uint8_t> bytes(fileSize);
    fsSource.read(reinterpret_cast<char*>(bytes.data()), fileSize);
    fsSource.close();

    Aspose::Cells::Vector<uint8_t> asposeBytes(bytes.size());
    if (!bytes.empty()) {
        memcpy(asposeBytes.GetData(), bytes.data(), bytes.size());
    }

    Workbook workbook(u"sample.xlsx");
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    sheet.GetShapes().AddIcons(3, 0, 7, 0, 100, 100, asposeBytes, Aspose::Cells::Vector<uint8_t>());

    Cell c = sheet.GetCells().Get(8, 7);
    c.PutValue(u"Insert via Aspose.Cells");
    Style s = c.GetStyle();
    s.GetFont().SetColor(Color::Blue());
    c.SetStyle(s);

    workbook.Save(u"sample2.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```

Cuando ejecute el código anterior en su proyecto, obtendrá los siguientes resultados:

![](3.png)
{{< app/cells/assistant language="cpp" >}}
