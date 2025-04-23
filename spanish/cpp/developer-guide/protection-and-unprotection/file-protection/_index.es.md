---
title: Cifrar y descifrar archivos de Excel con C++
linktitle: Cifrar y Descifrar archivos de Excel
type: docs
weight: 10
url: /es/cpp/encrypt-and-decrypt-excel-files/
description: Cómo cifrar y descifrar archivos de Excel usando C++. Bloquea y desbloquea archivos de Excel.
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) te permite cifrar y proteger con contraseña tus hojas de cálculo. Utiliza algoritmos proporcionados por un proveedor de servicios criptográficos, o CSP, un conjunto de algoritmos criptográficos con diferentes propiedades. El CSP predeterminado es 'Compatible con Office 97/2000' o 'Cifrado débil (XOR)'. Es importante elegir la longitud adecuada de la clave de cifrado. Algunos CSP no admiten más de 40 o 56 bits, considerándose un cifrado débil. Para un cifrado fuerte, se requiere una longitud mínima de clave de 128 bits. Microsoft Windows contiene CSP que ofrecen tipos de cifrado fuertes, como por ejemplo el 'Proveedor Criptográfico Fuerte de Microsoft'. Para darte una idea, los bancos utilizan un cifrado de 128 bits para encriptar la conexión con sus sistemas de Banca por Internet.

Aspose.Cells te permite cifrar y proteger con contraseña archivos de Microsoft Excel con el tipo de cifrado que desees.

{{% /alert %}}

## **Usar Microsoft Excel**

Para configurar los ajustes de cifrado de archivos en Microsoft Excel (aquí Microsoft Excel 2003):

1. Desde el menú **Herramientas**, selecciona **Opciones**. Aparecerá un cuadro de diálogo.
1. Selecciona la pestaña **Seguridad**.
1. Ingresa una contraseña y haz clic en **Avanzado**.
1. Elige el tipo de cifrado y confirma la contraseña.

## **Cifrar archivo de Excel con Aspose.Cells**

El siguiente ejemplo muestra cómo cifrar y proteger por contraseña un archivo Excel usando la API Aspose.Cells.

```c++
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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"encryptedBook1.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Specify XOR encryption type
    workbook.SetEncryptionOptions(EncryptionType::XOR, 40);

    // Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider)
    workbook.SetEncryptionOptions(EncryptionType::StrongCryptographicProvider, 128);

    // Password protect the file
    workbook.GetSettings().SetPassword(u"1234");

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Workbook encrypted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Especificar la opción de Contraseña para modificar**

El siguiente ejemplo muestra cómo establecer la opción de **Contraseña para modificar** en Microsoft Excel para un archivo existente utilizando la API de Aspose.Cells.

```c++
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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"SpecifyPasswordToModifyOption.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Set the password for modification
    workbook.GetSettings().GetWriteProtection().SetPassword(u"1234");

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Password for modification set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Descifrar archivo Excel con Aspose.Cells**

Es muy fácil abrir un archivo Excel protegido por contraseña y descifrarlo usando la API Aspose.Cells como se muestra en el siguiente código:

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create load options and set password
    LoadOptions loadOptions;
    loadOptions.SetPassword(u"password");

    // Open encrypted Excel file
    Workbook workbook(u"Book1.xlsx", loadOptions);

    // Remove password protection
    workbook.GetSettings().SetPassword(nullptr);

    // Save the modified workbook
    workbook.Save(u"Book1.xlsx");

    std::cout << "Password removed and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Temas avanzados**

- [Encriptar y Desencriptar archivos ODS](/cells/es/cpp/encrypt-and-decrypt-ods-files/)
- [Configurar Tipo de Encriptación Fuerte](/cells/es/cpp/setting-strong-encryption-type/)
- [Especificar Autor al Proteger la Escritura del Libro de Trabajo](/cells/es/cpp/specify-author-while-write-protecting-workbook/)
- [Verificar Contraseña de Archivos Encriptados](/cells/es/cpp/verify-password-of-encrypted-excel-and-ods-files/)
