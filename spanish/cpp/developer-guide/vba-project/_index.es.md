---
title: Gestiona códigos VBA de libros de Excel habilitados para macros con C++
linktitle: Proyecto de Macros
type: docs
weight: 200
url: /es/cpp/manage-vba-project/
description: Agrega módulos VBA y modifica VBA o macros con la biblioteca Aspose.Cells en C++.
---

## **Agregar un módulo VBA en C++**
{{% alert color="primary" %}}

Aspose.Cells te permite agregar un nuevo módulo VBA y código de macro usando Aspose.Cells. Utiliza el método [**Workbook.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/add/) para agregar el nuevo módulo VBA dentro del libro de trabajo.

{{% /alert %}}

El siguiente código de ejemplo crea un nuevo libro de trabajo y agrega un nuevo módulo VBA y código de macro y guarda la salida en formato XLSM. Una vez que abres el archivo XLSM de salida en Microsoft Excel y haces clic en los comandos de menú **Desarrollador > Visual Basic**, verás un módulo llamado "TestModule" y dentro, verás el siguiente código de macro.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Aquí tienes el código de ejemplo para generar el archivo de salida XLSM con módulo de VBA y código de macro.

```cpp
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

    // Create new workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add VBA Module
    int32_t idx = workbook.GetVbaProject().GetModules().Add(worksheet);

    // Access the VBA Module, set its name and codes
    VbaModule module = workbook.GetVbaProject().GetModules().Get(idx);
    module.SetName(u"TestModule");

    U16String codes = u"Sub ShowMessage()\r\n"
                      u"    MsgBox \"Welcome to Aspose!\"\r\n"
                      u"End Sub";
    module.SetCodes(codes);

    // Save the workbook
    U16String outputPath = outDir + u"output_out.xlsm";
    workbook.Save(outputPath, SaveFormat::Xlsm);

    std::cout << "VBA module added and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Modificar VBA o macro en C++**

{{% alert color="primary" %}} 

Puedes modificar el código de VBA o macro utilizando Aspose.Cells. Aspose.Cells ha añadido el siguiente espacio de nombres y clases para leer y modificar el proyecto de VBA en el archivo de Excel.

- Aspose::Cells::Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Este artículo te mostrará cómo cambiar el código de VBA o macro dentro del archivo de Excel fuente utilizando Aspose.Cells.

{{% /alert %}} 

El siguiente código de ejemplo carga el archivo Excel fuente que contiene el siguiente código VBA o macro dentro de él:

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

Después de la ejecución del código de ejemplo de Aspose.Cells, el código VBA o macro será modificado de esta manera:

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

Puedes descargar el [archivo de Excel fuente](5112508.xlsm) y el [archivo de Excel de salida](5112511.xlsm) desde los enlaces proporcionados.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"sample.xlsm";
    U16String outputFilePath = outDir + u"output_out.xlsm";

    Workbook workbook(inputFilePath);

    VbaProject vbaProject = workbook.GetVbaProject();
    VbaModuleCollection modules = vbaProject.GetModules();

    for (int i = 0; i < modules.GetCount(); ++i)
    {
        VbaModule module = modules.Get(i);
        U16String code = module.GetCodes();
        U16String searchStr = u"This is test message.";
        U16String replaceStr = u"This is Aspose.Cells message.";

        if (code.IndexOf(searchStr) != -1)
        {
            U16String newCode;
            const char16_t* codeData = code.GetData();
            const char16_t* searchData = searchStr.GetData();
            int codeLen = code.GetLength();
            int searchLen = searchStr.GetLength();

            int pos = 0;
            int searchPos;

            while ((searchPos = code.IndexOf(searchStr)) != -1)
            {
                for (int j = pos; j < searchPos; j++)
                {
                    newCode += codeData[j];
                }

                newCode += replaceStr;

                pos = searchPos + searchLen;
            }

            for (int j = pos; j < codeLen; j++)
            {
                newCode += codeData[j];
            }

            module.SetCodes(newCode);
        }
    }

    workbook.Save(outputFilePath);

    std::cout << "VBA module codes updated successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Temas Avanzados**
- [Agregar una referencia de biblioteca al proyecto VBA en el libro de trabajo](/cells/es/cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [Asignar Macro a un control de formulario](/cells/es/cpp/assign-macro-to-form-control/)
- [Comprobar si la firma digital del código VBA es válida](/cells/es/cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [Comprobar si el código VBA está firmado](/cells/es/cpp/check-if-vba-code-is-signed/)
- [Verifica si el proyecto VBA en un libro de trabajo está firmado](/cells/es/cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [Comprobar si el proyecto de VBA está protegido y bloqueado para ver](/cells/es/cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Copiar el diseñador de almacenamiento de formularios de usuario Macro de VBA de la plantilla al libro de Excel de destino](/cells/es/cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Firmar digitalmente un proyecto de código VBA con certificado](/cells/es/cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [Exportar certificado de VBA a archivo o flujo de datos](/cells/es/cpp/export-vba-certificate-to-file-or-stream/)
- [Filtrar el proyecto VBA al cargar un libro de trabajo](/cells/es/cpp/filter-vba-project-while-loading-a-workbook/)
- [Descubrir si el proyecto de VBA está protegido](/cells/es/cpp/find-out-if-vba-project-is-protected/)
- [Proteger con contraseña el proyecto de VBA del libro de Excel](/cells/es/cpp/password-protect-the-vba-project-of-excel-workbook/)
