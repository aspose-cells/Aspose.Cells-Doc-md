---
title: Cómo detectar el formato de archivo y verificar si el archivo está cifrado con C++
linktitle: Cómo Detectar el Formato de un Archivo y Verificar si el Archivo está Encriptado
type: docs
weight: 2700
url: /es/cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
description: Aprende cómo detectar el formato de un archivo y verificar si está cifrado usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

A veces necesitas detectar el formato de un archivo antes de abrirlo porque la extensión del archivo no garantiza que el contenido sea adecuado. El archivo podría estar cifrado (protegido con contraseña) por lo que no puede leerse directamente, o simplemente no deberías leerlo. Aspose.Cells proporciona el método estático [**FileFormatUtil::DetectFileFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/detectfileformat/) y algunas APIs relevantes que puedes usar para procesar documentos.

{{% /alert %}}

El siguiente código de ejemplo ilustra cómo detectar el formato de un archivo (usando la ruta del archivo) y verificar su extensión. También puedes determinar si el archivo está encriptado.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Detect file format
    FileFormatInfo info = FileFormatUtil::DetectFileFormat(srcDir + u"Book1.xlsx");

    // Gets the detected load format
    std::cout << "The spreadsheet format is: " << FileFormatUtil::LoadFormatToExtension(info.GetLoadFormat()).ToUtf8() << std::endl;

    // Check if the file is encrypted
    std::cout << "The file is encrypted: " << (info.IsEncrypted() ? "true" : "false") << std::endl;

    Aspose::Cells::Cleanup();
}
```
