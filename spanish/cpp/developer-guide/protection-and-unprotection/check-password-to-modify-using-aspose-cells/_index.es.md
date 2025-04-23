---
title: Verificar contraseña para modificar usando Aspose.Cells con C++
linktitle: Verificar contraseña para modificar
type: docs
weight: 2400
url: /es/cpp/check-password-to-modify-using-aspose-cells/
description: Verifica si la contraseña dada coincide con la contraseña para modificar usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

A veces, necesitas verificar si la contraseña dada coincide con la **Contraseña para modificar** de forma programática. Aspose.Cells proporciona el método WorkbookSettings.WriteProtection.ValidatePassword() que puedes usar para verificar si la Contraseña para modificar es correcta o no.

{{% /alert %}}

## **Verificar Contraseña para modificar en Microsoft Excel**

Puedes asignar **Contraseña para abrir** y **Contraseña para modificar** al crear tus libros de trabajo en Microsoft Excel. Por favor, mira esta captura de pantalla que muestra la interfaz que Microsoft Excel proporciona para especificar estas contraseñas.

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **Verificar contraseña para modificar usando Aspose.Cells**

Los siguientes códigos de muestra cargan el archivo de Excel fuente. Tiene una contraseña para abrir como 1234 y una contraseña para modificar como 5678. El código primero verifica si 567 es la contraseña correcta para modificar y devuelve falso, luego verifica si 5678 es la contraseña para modificar y devuelve verdadero.

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
    U16String inputFilePath = srcDir + u"sampleBook.xlsx";

    // Specify password to open inside the load options
    LoadOptions opts;
    opts.SetPassword(u"1234");

    // Open the source Excel file with load options
    Workbook workbook(inputFilePath, opts);

    // Check if "567" is the password to modify
    bool ret = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"567");
    std::wcout << L"Is 567 correct Password to modify: " << ret << std::endl;

    // Check if "5678" is the password to modify
    ret = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"5678");
    std::wcout << L"Is 5678 correct Password to modify: " << ret << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Salida de la consola**

Aquí está la salida de la consola del código de muestra anterior después de cargar el archivo de Excel fuente.

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
