---
title: Extraer objetos OLE del libro de trabajo con C++
linktitle: Extraer objetos OLE del libro de trabajo
type: docs
weight: 110
url: /es/cpp/extract-ole-objects-from-workbook/
description: Aprende cómo extraer objetos OLE de un libro de trabajo usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

A veces, necesitas extraer objetos OLE de un libro de trabajo. Aspose.Cells soporta extraer y guardar esos objetos OLE.

Este artículo muestra cómo crear una aplicación de consola en Visual Studio y extraer diferentes objetos OLE de un libro de trabajo con unas pocas líneas de código.

{{% /alert %}}

## **Extraer objetos OLE de un libro de trabajo**

### **Crear un libro de trabajo de plantilla**

1. Crea un libro de trabajo en Microsoft Excel.
1. Agrega un documento de Microsoft Word, un libro de Excel y un documento PDF como objetos OLE en la primera hoja de trabajo.

| **Documento de plantilla con objetos OLE (OleFile.xls)** |
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

Luego, extrae los objetos OLE y guárdalos en el disco duro con sus respectivos tipos de archivo.

### **Descargar e instalar Aspose.Cells**

1. [Descargar Aspose.Cells for C++](https://downloads.aspose.com/cells/cpp).
1. Instálelo en su equipo de desarrollo.

Todos los componentes de Aspose, al instalarse, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos producidos.

### **Crear un proyecto**

Inicia **Visual Studio** y crea una nueva aplicación de consola. Este ejemplo mostrará una aplicación de consola en C++.

1. Agregar referencias
   1. Agrega una referencia al componente Aspose.Cells en tu proyecto, por ejemplo, agregando una referencia a ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll.

### **Extraer objetos OLE**

El código a continuación realiza la tarea de encontrar y extraer objetos OLE. Los objetos OLE (archivos DOC, XLS y PDF) se guardan en el disco.

```cpp
#include <iostream>
#include <fstream>
#include <memory>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the template file
    Workbook workbook(srcDir + u"oleFile.xlsx");

    // Get the OleObject Collection in the first worksheet
    OleObjectCollection oles = workbook.GetWorksheets().Get(0).GetOleObjects();

    // Loop through all the oleobjects and extract each object in the worksheet
    for (int i = 0; i < oles.GetCount(); i++)
    {
        OleObject ole = oles.Get(i);

        // Specify the output filename
        U16String fileName = srcDir + u"outOle" + U16String(std::to_string(i).c_str()) + u".";

        // Specify each file format based on the oleobject format type
        switch (ole.GetFileFormatType())
        {
            case FileFormatType::Doc:
                fileName += u"doc";
                break;
            case FileFormatType::Excel97To2003:
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
            if (objectData.GetLength() > 0)
            {
                Workbook oleBook(objectData);
                oleBook.GetSettings().SetIsHidden(false);
                oleBook.Save(srcDir + u"outOle" + U16String(std::to_string(i).c_str()) + u".out.xlsx");
            }
        }
        // Create the files based on the oleobject format types
        else
        {
            Vector<uint8_t> objectData = ole.GetObjectData();
            if (objectData.GetLength() > 0)
            {
                std::ofstream fs(fileName.ToUtf8().c_str(), std::ios::binary);
                fs.write(reinterpret_cast<const char*>(objectData.GetData()), objectData.GetLength());
                fs.close();
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
