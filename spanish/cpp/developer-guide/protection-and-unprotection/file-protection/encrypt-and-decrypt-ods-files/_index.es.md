---  
title: Cifrar y descifrar archivos ODS con C++  
linktitle: Cifrar y Descifrar archivos ODS  
type: docs  
weight: 10  
url: /es/cpp/encrypt-and-decrypt-ods-files/  
description: Protege con contraseña y cifra archivos ODS usando Aspose.Cells for C++, que es una biblioteca pura en C++.  
---  

{{% alert color="primary" %}}  
OpenOffice.org es una suite de oficina completa que soporta protección con contraseña y cifrado de archivos. Sin embargo, un archivo ODS cifrado solo puede ser abierto por OpenOffice después de proporcionar la contraseña. Excel no puede abrir el archivo ODS cifrado y puede mostrar un mensaje de advertencia. Las opciones de cifrado no son aplicables a archivos ODS a diferencia de otros tipos de archivo.  
Aspose.Cells permite cifrar y descifrar archivos ODS. Los archivos ODS descifrados pueden ser abiertos en Excel y OpenOffice.  
{{% /alert %}}  

## **Cifrar con OpenOffice Calc**  
1. Selecciona **Guardar como** y haz clic en la casilla **Guardar con contraseña**.  
1. Haz clic en el botón **Guardar**.  
1. Escribe tu contraseña deseada en los campos **Introducir Contraseña para Abrir** y **Confirmar Contraseña** en la ventana Establecer Contraseña que se abre.  
1. Haz clic en el botón **Aceptar** para guardar el archivo.  

## **Cifrar archivo ODS con Aspose.Cells for C++**  
Para cifrar un archivo ODS, carga el archivo y establece el valor [**WorkbookSettings.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getpassword/) a la contraseña real antes de guardarlo. El archivo ODS cifrado resultante puede abrirse solo en OpenOffice.  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C++

    // Source directory path
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory path
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Open an ODS file
    Workbook workbook(sourceDir + u"sampleODSFile.ods");

    // Password protect the file
    workbook.GetSettings().SetPassword(u"1234");

    // Save the ODS file
    workbook.Save(outputDir + u"outputEncryptedODSFile.ods");

    std::cout << "ODS file password protected and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```  

## **Descifrar archivo ODS con Aspose.Cells for C++**  

Para descifrar un archivo ODS, carga el archivo proporcionando una contraseña en la propiedad [**LoadOptions.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getpassword/). Una vez cargado el archivo, establece la cadena [**WorkbookSettings.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getpassword/) en null.  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path to the source directory
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Open an encrypted ODS file
    LoadOptions loadOptions(LoadFormat::Ods);

    // Set original password
    loadOptions.SetPassword(u"1234");

    // Load the encrypted ODS file with the appropriate load options
    Workbook workbook(sourceDir + u"sampleEncryptedODSFile.ods", loadOptions);

    // Set the password to null
    workbook.GetSettings().SetPassword(nullptr);

    // Save the decrypted ODS file
    workbook.Save(outputDir + u"outputDecryptedODSFile.ods");

    std::cout << "Decrypted ODS file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
{{< app/cells/assistant language="cpp" >}}
