---
title: Gestión de objetos OLE con C++
linktitle: Gestión de objetos OLE
type: docs
weight: 50
url: /es/cpp/managing-ole-objects/
description: Aprende cómo agregar, extraer y manipular objetos OLE en hojas de cálculo usando Aspose.Cells con C++.
---

## **Introducción**

OLE (Object Linking and Embedding) es el marco de Microsoft para una tecnología de documento compuesto. En resumen, un documento compuesto es algo similar a un escritorio de visualización que puede contener objetos visuales e informativos de todo tipo: texto, calendarios, animaciones, sonido, video en movimiento, 3D, noticias actualizadas continuamente, controles, y mucho más. Cada objeto de escritorio es una entidad de programa independiente que puede interactuar con un usuario y también comunicarse con otros objetos en el escritorio.

OLE (Object Linking and Embedding) es compatible con muchos programas diferentes y se utiliza para hacer que el contenido creado en un programa esté disponible en otro. Por ejemplo, puedes insertar un documento de Microsoft Word en Microsoft Excel. Para ver qué tipos de contenido puedes insertar, haz clic en **Objeto** en el menú **Insertar**. Solo aparecen en el cuadro **Tipo de objeto** los programas instalados en el equipo y que admiten objetos OLE.

### **Inserción de objetos OLE en la hoja de cálculo**

Aspose.Cells soporta agregar, extraer y manipular objetos OLE en hojas de cálculo. Por esta razón, Aspose.Cells tiene la clase [**OleObjectCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobjectcollection/), utilizada para agregar un nuevo objeto OLE a la lista de colección. Otra clase, [**OleObject**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/), representa un objeto OLE. Tiene algunos miembros importantes:

- La propiedad [**ImageData**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getimagedata/) especifica los datos de la imagen (ícono) de tipo arreglo de bytes. La imagen se mostrará para mostrar el objeto OLE en la hoja de cálculo.
- La propiedad [**ObjectData**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/) especifica los datos del objeto en forma de un arreglo de bytes. Estos datos se mostrarán en su programa relacionado cuando hagas doble clic en el ícono del objeto OLE.

El siguiente ejemplo muestra cómo agregar un objeto(s) OLE a una hoja de cálculo.

```c++
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

std::vector<uint8_t> ReadFileToVector(const U16String& filePath) {
    std::ifstream file(filePath.ToUtf8(), std::ios::binary | std::ios::ate);
    if (!file) return {};
    std::streamsize size = file.tellg();
    file.seekg(0, std::ios::beg);
    std::vector<uint8_t> buffer(size);
    if (size > 0)
        file.read(reinterpret_cast<char*>(buffer.data()), size);
    return buffer;
}

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    U16String imagePath = srcDir + u"logo.jpg";
    std::vector<uint8_t> imageData = ReadFileToVector(imagePath);

    U16String objectPath = srcDir + u"book1.xls";
    std::vector<uint8_t> objectData = ReadFileToVector(objectPath);
    Vector<uint8_t> data(objectData.data(), static_cast<int32_t>(objectData.size()));
    sheet.GetOleObjects().Add(14, 3, 200, 220, data);
    if (sheet.GetOleObjects().GetCount() > 0) {
        sheet.GetOleObjects().Get(0).SetObjectData(data);
    }

    workbook.Save(outDir + u"output.out.xls");
    std::cout << "OLE object added successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Extracción de objetos OLE en el libro de trabajo**

El siguiente ejemplo muestra cómo extraer objetos OLE en un libro de trabajo. El ejemplo obtiene diferentes objetos OLE de un archivo XLS existente y guarda diferentes archivos (DOC, XLS, PPT, PDF, etc.) basándose en el tipo de formato de archivo del objeto OLE.

Después de ejecutar el código, podemos guardar diferentes archivos basados en sus respectivos tipos de formato de objetos OLE.

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the template file
    Workbook workbook(srcDir + u"book1.xls");

    // Get the OleObject Collection in the first worksheet
    OleObjectCollection oles = workbook.GetWorksheets().Get(0).GetOleObjects();

    // Loop through all the oleobjects and extract each object
    for (int32_t i = 0; i < oles.GetCount(); i++)
    {
        OleObject ole = oles.Get(i);

        // Specify the output filename
        U16String fileName = srcDir + u"ole_" + U16String(std::to_string(i).c_str()) + u".";

        // Specify each file format based on the oleobject format type
        switch (ole.GetFileFormatType())
        {
        case FileFormatType::Doc:
            fileName += u"doc";
            break;
        case FileFormatType::Xlsx:
            fileName += u"Xlsx";
            break;
        case FileFormatType::Ppt:
            fileName += u"Ppt";
            break;
        case FileFormatType::Pdf:
            fileName += u"Pdf";
            break;
        case FileFormatType::Unknown:
            fileName += u"Jpg";
            break;
        default:
            // Handle other formats if needed
            break;
        }

        // Save the oleobject as a new excel file if the object type is xls
        if (ole.GetFileFormatType() == FileFormatType::Xlsx)
        {
            Vector<uint8_t> objectData = ole.GetObjectData();
            Workbook oleBook(objectData);
            oleBook.GetSettings().SetIsHidden(false);
            oleBook.Save(srcDir + u"Excel_File" + U16String(std::to_string(i).c_str()) + u".out.xlsx");
        }
        else
        {
            // Create the files based on the oleobject format types
            std::ofstream fs(fileName.ToUtf8().c_str(), std::ios::binary);
            Vector<uint8_t> objectData = ole.GetObjectData();
            fs.write(reinterpret_cast<const char*>(objectData.GetData()), objectData.GetLength());
            fs.close();
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Extrayendo archivo MOL incrustado**

Aspose.Cells admite la extracción de objetos de tipos poco comunes como MOL (archivo de datos moleculares que contiene información sobre átomos y enlaces). El siguiente fragmento de código demuestra cómo extraer un archivo MOL incrustado y guardarlo en el disco usando este [archivo de Excel de ejemplo](94896196.xlsx).

```c++
#include <iostream>
#include <fstream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"EmbeddedMolSample.xlsx");

    int index = 1;

    WorksheetCollection sheets = workbook.GetWorksheets();
    for (int i = 0; i < sheets.GetCount(); i++)
    {
        Worksheet sheet = sheets.Get(i);
        OleObjectCollection oles = sheet.GetOleObjects();

        for (int j = 0; j < oles.GetCount(); j++)
        {
            OleObject ole = oles.Get(j);

            std::wstring indexWStr = std::to_wstring(index);
            U16String fileName = outDir + u"OleObject" + U16String(reinterpret_cast<const char16_t*>(indexWStr.c_str())) + u".mol";

            std::ofstream fs(fileName.ToUtf8(), std::ios::binary);
            if (fs.is_open())
            {
                Vector<uint8_t> objectData = ole.GetObjectData();
                fs.write(reinterpret_cast<const char*>(objectData.GetData()), objectData.GetLength());
                fs.close();
                index++;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Temas Avanzados**
- [Acceder y Modificar la Etiqueta de Visualización del Objeto Ole Vinculado](/cells/es/cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Actualizar automáticamente el objeto OLE a través de Microsoft Excel usando Aspose.Cells](/cells/es/cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Extraer objetos OLE del libro de trabajo](/cells/es/cpp/extract-ole-objects-from-workbook/)
- [Obtener o establecer el identificador de clase del objeto OLE incrustado](/cells/es/cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Insertar un archivo WAV como un objeto OLE](/cells/es/cpp/inserting-a-wav-file-as-an-ole-object/)
