---
title: Proteger y Desproteger con C++
linktitle: Cifrado y protección
description: Esta sección presenta cómo cifrar y descifrar archivos de Excel y proteger los datos de Excel, incluyendo el cifrado de archivos, la protección de solo lectura, la protección de la estructura del libro, la protección de las hojas de cálculo y las firmas digitales mediante código C++
keywords: Aspose.Cells, Aspose.Cells for C++, cifrar, descifrar, contraseña, proteger, desproteger, protección del libro, protección de hojas de cálculo, solo lectura, firma digital, C++
type: docs
weight: 68
url: /es/cpp/protect-and-unprotect/
alias: [/cpp/security-features/]
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Los libros de Excel suelen almacenar información financiera, empresarial o personal confidencial que debe mantenerse fuera del acceso no autorizado. Aspose.Cells for C++ ofrece un conjunto completo de funciones de protección que refleja las capacidades de Microsoft Excel, lo que le permite proteger sus datos a nivel de archivo, a nivel de libro y a nivel de hoja de cálculo.

{{% alert color="primary" %}}
Aspose.Cells for C++ ofrece una amplia gama de funciones de protección, desde el nivel de archivo hasta el nivel de datos, similar a MS Excel. Estas capacidades incluyen el cifrado de archivos con contraseña, la aplicación de acceso de solo lectura mediante una contraseña de modificación, la protección de la estructura del libro, la protección de hojas de cálculo y la firma digital de los libros.
{{% /alert %}}

## Cifrar y descifrar archivos de Excel
Una contraseña establecida en un archivo de Excel impide que usuarios no autorizados abran o visualicen el contenido del libro. Para cifrar un libro, asigne una cadena de contraseña a `workbook.GetSettings().SetPassword()` y luego guarde el libro. Aspose.Cells escribe el archivo en forma cifrada. Para abrir un libro cifrado para descifrarlo, cree una instancia de un objeto `LoadOptions`, establezca `LoadOptions.SetPassword()` con la misma contraseña que se usó durante el cifrado y páselo al constructor de `Workbook`. Aspose.Cells aplica la contraseña proporcionada de forma transparente, de modo que el resto de su código pueda interactuar con el contenido descifrado como si el archivo fuera un libro normal.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cell cell = sheet.GetCells().Get(u"A1");
    cell.PutValue(u"Confidential Data");
    workbook.GetSettings().SetPassword(U16String("OpenPassword123"));
    workbook.Save(u"encrypted.xlsx");
    LoadOptions loadOptions;
    loadOptions.SetPassword(U16String("OpenPassword123"));
    Workbook decryptedWorkbook(u"encrypted.xlsx", loadOptions);
    U16String cellValue = decryptedWorkbook.GetWorksheets().Get(0).GetCells().Get(u"A1").GetStringValue();
    std::cout << "Decrypted cell A1 value: " << cellValue.ToUtf8() << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Protección de solo lectura (contraseña para modificar)
Excel admite dos capas distintas de contraseña. La primera es una contraseña para abrir, que cifra el propio archivo y se aborda en la sección anterior. La segunda es una contraseña para modificar, que no impide a los usuarios abrir el libro; en su lugar, Excel recomienda abrir el archivo en modo de solo lectura a menos que se proporcione la contraseña de modificación. Configure este comportamiento en Aspose.Cells mediante `workbook.GetSettings().GetWriteProtection()`. Establezca la propiedad `Password` con la contraseña de modificación y la propiedad `Author` para identificar quién aplicó la protección. Utilice el método `WriteProtection.ValidatePassword()` para comprobar si una contraseña de modificación proporcionada es correcta, devolviendo `true` si coincide y `false` en caso contrario.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    Cell a1 = cells.Get(u"A1");
    a1.PutValue(u"Sample Data");
    workbook.GetSettings().GetWriteProtection().SetPassword(u"ModifyPwd");
    workbook.GetSettings().GetWriteProtection().SetAuthor(u"AuthorName");
    workbook.Save(u"WriteProtectedWorkbook.xlsx");
    bool isCorrectValid = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"ModifyPwd");
    std::cout << "ValidatePassword(\"ModifyPwd\") returned: " << (isCorrectValid ? "True" : "False") << std::endl;
    bool isWrongValid = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"WrongPwd");
    std::cout << "ValidatePassword(\"WrongPwd\") returned: " << (isWrongValid ? "True" : "False") << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Proteger y desproteger la estructura del libro
Proteger la estructura del libro impide que otros usuarios vean hojas de cálculo ocultas, agreguen nuevas hojas, muevan hojas, eliminen hojas, oculten hojas o cambien el nombre de las hojas. El estado protegido se aplica a la estructura de las hojas y no al contenido de las celdas dentro de ninguna hoja. Para aplicar la protección de estructura, llame a `workbook.Protect(ProtectionType::Structure, "password")`. Para eliminar la protección, llame a `workbook.Unprotect("password")` y proporcione la contraseña correcta. El valor de la enumeración `ProtectionType::Structure` se utiliza aquí y es distinto de otros tipos de protección como `ProtectionType::Windows`.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Crear un nuevo libro
    Workbook workbook;
    // Agregar una segunda hoja de cálculo
    workbook.GetWorksheets().Add();
    // Escribir un valor de muestra en la celda A1 de la primera hoja de cálculo
    workbook.GetWorksheets().Get(0).GetCells().Get(0, 0).PutValue(u"Sample Data");
    // Proteger la estructura del libro
    workbook.Protect(ProtectionType::Structure, u"StructPwd");
    // Guardar el libro como structure_protected.xlsx
    U16String filePath = u"structure_protected.xlsx";
    workbook.Save(filePath);
    // Recargar el archivo en una nueva instancia del libro
    Workbook loadedWorkbook(filePath);
    // Eliminar la protección de la estructura
    loadedWorkbook.Unprotect(u"StructPwd");
    // Imprimir mensaje de confirmación
    std::cout << "Structure protection has been successfully removed from the workbook." << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Proteger y desproteger hojas de cálculo
La protección de la hoja de cálculo bloquea las celdas de una hoja contra cambios accidentales o deliberados. Los usuarios no pueden editar las celdas bloqueadas sin proporcionar la contraseña. Esta es la protección típica utilizada para proteger fórmulas, encabezados o áreas designadas para la entrada de datos en hojas de cálculo compartidas. Para proteger una hoja de cálculo, llame a `worksheet.Protect(ProtectionType::All, "password")`. El uso de `ProtectionType::All` habilita todas las opciones de protección disponibles, como seleccionar celdas bloqueadas, dar formato a las celdas, insertar filas y columnas, y eliminar filas y columnas. Para eliminar la protección, llame a `worksheet.Unprotect("password")` con la contraseña correcta. Existe un control más granular mediante la combinación de otros tipos de protección como `Contents`, `Objects` y `Scenarios` utilizando el operador OR bit a bit.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Sample Data");
    sheet.Protect(ProtectionType::All, u"SheetPwd");
    workbook.Save(u"sheet_protected.xlsx");
    Workbook workbookReloaded(u"sheet_protected.xlsx");
    Worksheet sheetReloaded = workbookReloaded.GetWorksheets().Get(0);
    sheetReloaded.Unprotect(u"SheetPwd");
    std::cout << "Worksheet protection removed successfully.\n";
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Agregar y validar firmas digitales
Una firma digital garantiza a los destinatarios que el contenido del libro es auténtico y no se ha alterado desde que se firmó. Aspose.Cells ofrece compatibilidad con firmas digitales a través del espacio de nombres `Aspose::Cells::DigitalSignatures`. El flujo de trabajo habitual carga un archivo de certificado `.pfx`, lo envuelve en un `Aspose::Cells::DigitalSignatures::DigitalSignature`, agrega la firma a un `DigitalSignatureCollection` y aplica la colección al libro mediante `workbook.AddDigitalSignature(DigitalSignatureCollection)`. La propiedad `DigitalSignature.GetComments()` puede registrar el contexto de la firma, como la hora y el propósito. Cualquier modificación realizada en el libro después de la firma invalida la firma, por lo que un paso de validación en el lado receptor puede detectar manipulaciones.

```cpp
#include "Aspose.Cells.h"
#include <chrono>
#include <ctime>
using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;
int main() {
    Aspose::Cells::Startup();
    std::time_t t = std::time(nullptr);
    std::tm tm{};
    localtime_s(&tm, &t);
    Date currentDate{0};
    currentDate.year = tm.tm_year + 1900;
    currentDate.month = tm.tm_mon + 1;
    currentDate.day = tm.tm_mday;
    currentDate.hour = tm.tm_hour;
    currentDate.minute = tm.tm_min;
    currentDate.second = tm.tm_sec;
    DigitalSignature signature(u"signature.pfx", u"pfx-password", u"Signed by Aspose.Cells", currentDate);
    DigitalSignatureCollection signatures;
    signatures.Add(signature);
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Sample Value");
    workbook.AddDigitalSignature(signatures);
    workbook.Save(u"signed_workbook.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Artículos relacionados
- [Cifrar y descifrar archivos de Excel](/cells/es/cpp/encrypt-and-decrypt-excel-files/)
- [Proteger y desproteger la estructura del libro](/cells/es/cpp/protect-and-unprotect-workbook-structure/)
- [Proteger y desproteger hojas de cálculo](/cells/es/cpp/protect-and-unprotect-worksheets/)
- [Proteger con contraseña o desproteger el libro compartido](/cells/es/cpp/password-protect-or-unprotect-the-shared-workbook/)
- [Comprobar la contraseña para modificar con Aspose.Cells](/cells/es/cpp/check-password-to-modify-using-aspose-cells/)
- [Detectar el formato de archivo de archivos cifrados de Office Open XML (OOXML)](/cells/es/cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Cifrado de archivos de Excel](/cells/es/cpp/encrypting-excel-files/)
- [Cómo detectar el formato de un archivo y comprobar si el archivo está cifrado](/cells/es/cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="cpp" >}}