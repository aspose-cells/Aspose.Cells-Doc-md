---
title: Proteger y Desproteger con Node.js a través de C++
linktitle: Cifrado y protección
description: Esta sección presenta cómo cifrar y descifrar archivos de Excel y proteger los datos de Excel, cubriendo el cifrado de archivos, la protección de solo lectura, la protección de la estructura del libro, la protección de hojas de cálculo y las firmas digitales mediante código JavaScript
keywords: Aspose.Cells, Node.js, C++, cifrar, descifrar, contraseña, proteger, desproteger, protección del libro, protección de hojas de cálculo, solo lectura, firma digital, JavaScript
type: docs
weight: 68
url: /es/nodejs-cpp/protect-and-unprotect/
alias: [/nodejs-cpp/security-features/]
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Los libros de Excel suelen almacenar información financiera, comercial o personal sensible que debe protegerse frente al acceso no autorizado. Aspose.Cells for Node.js via C++ ofrece un conjunto completo de funciones de protección que refleja las capacidades de Microsoft Excel, lo que le permite proteger sus datos en los niveles de archivo, libro y hoja de cálculo.

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++ ofrece una amplia gama de funciones de protección, desde el nivel de archivo hasta el nivel de datos, similares a las de MS Excel. Estas capacidades incluyen cifrar archivos con una contraseña, imponer el acceso de solo lectura mediante una contraseña de modificación, proteger la estructura del libro, proteger hojas de cálculo y firmar digitalmente libros.
{{% /alert %}}

## Cifrar y descifrar archivos Excel
La contraseña establecida en un archivo Excel impide que los usuarios no autorizados abran o vean el contenido del libro. Para cifrar un libro, asigne una cadena de contraseña a `workbook.getSettings().setPassword()` y, a continuación, guarde el libro. Aspose.Cells escribe el archivo en forma cifrada. Para abrir un libro cifrado y descifrarlo, instancie un objeto `LoadOptions`, configure `loadOptions.setPassword()` con la misma contraseña utilizada durante el cifrado y páselo al constructor `Workbook`. Aspose.Cells aplica de forma transparente la contraseña proporcionada, de modo que el resto del código pueda interactuar con el contenido descifrado como si el archivo fuera un libro normal.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
let cell = sheet.getCells().get("A1");
cell.putValue("Confidential Data");
workbook.getSettings().setPassword("OpenPassword123");
workbook.save("encrypted.xlsx");
let loadOptions = new AsposeCells.LoadOptions();
loadOptions.setPassword("OpenPassword123");
let decryptedWorkbook = new AsposeCells.Workbook("encrypted.xlsx", loadOptions);
console.log("Decrypted cell A1 value: " + decryptedWorkbook.getWorksheets().get(0).getCells().get("A1").getStringValue());
```

## Protección de solo lectura (contraseña de modificación)
Excel admite dos capas de contraseña distintas. La primera es una contraseña para abrir, que cifra el propio archivo y se aborda en la sección anterior. La segunda es una contraseña para modificar, que no impide a los usuarios abrir el libro; en su lugar, Excel recomienda abrir el archivo en modo de solo lectura a menos que se proporcione la contraseña de modificación. Configure este comportamiento en Aspose.Cells mediante `workbook.getSettings().getWriteProtection()`. Establezca su propiedad `password` en la contraseña de modificación y su propiedad `author` para identificar quién aplicó la protección. Utilice el método `writeProtection.validatePassword(string)` para comprobar si la contraseña de modificación proporcionada es correcta; devuelve `true` si coincide y `false` en caso contrario.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
// Escribir un valor de muestra en la celda A1 de la primera hoja de cálculo
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data");
// Configurar la protección contra escritura: establecer la contraseña para modificar y el autor
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd");
workbook.getSettings().getWriteProtection().setAuthor("AuthorName");
// Guardar el libro para que la protección contra escritura quede guardada
workbook.save("WriteProtectedWorkbook.xlsx");
// Validar la contraseña para modificar usando la contraseña correcta
let isCorrectValid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd");
console.log("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
// Validar la contraseña para modificar usando una contraseña incorrecta para demostrar la otra rama
let isWrongValid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd");
console.log("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## Proteger y desproteger la estructura del libro
Proteger la estructura del libro impide que otros usuarios vean hojas de cálculo ocultas, agreguen nuevas hojas de cálculo, muevan hojas de cálculo, eliminen hojas de cálculo, oculten hojas de cálculo o renombren hojas de cálculo. El estado protegido se aplica a la estructura de las hojas, no al contenido de las celdas de ninguna hoja. Para aplicar la protección de la estructura, llame a `workbook.protect(ProtectionType.Structure, "password")`. Para quitarla, llame a `workbook.unprotect("password")` y proporcione la contraseña correcta. El valor de enumeración `ProtectionType.Structure` se utiliza aquí y es distinto de otros tipos de protección, como `ProtectionType.Windows`.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
// Agregar una segunda hoja de cálculo
workbook.getWorksheets().add();
// Escribir un valor de muestra en la celda A1 de la primera hoja de cálculo
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// Proteger la estructura del libro
workbook.protect(AsposeCells.ProtectionType.Structure, "StructPwd");
// Guardar el libro como structure_protected.xlsx
let filePath = "structure_protected.xlsx";
workbook.save(filePath);
// Recargar el archivo en una nueva instancia de Workbook
let loadedWorkbook = new AsposeCells.Workbook(filePath);
// Eliminar la protección de estructura
loadedWorkbook.unprotect("StructPwd");
// Imprimir mensaje de confirmación
console.log("Structure protection has been successfully removed from the workbook.");
```

## Proteger y desproteger hojas de cálculo
La protección de una hoja de cálculo bloquea las celdas de la hoja frente a cambios accidentales o deliberados. Los usuarios no pueden editar las celdas bloqueadas sin proporcionar la contraseña. Esta es la protección habitual que se utiliza para salvaguardar fórmulas, encabezados o áreas designadas de introducción de datos en hojas de cálculo compartidas. Para proteger una hoja de cálculo, llame a `worksheet.protect(ProtectionType.All, "password")`. El uso de `ProtectionType.All` habilita todas las opciones de protección disponibles, como seleccionar celdas bloqueadas, dar formato a las celdas, insertar filas y columnas, y eliminar filas y columnas. Para quitar la protección, llame a `worksheet.unprotect("password")` con la contraseña correcta. Se ofrece un control más granular combinando otros tipos de protección, como `Contents`, `Objects` y `Scenarios`, mediante el operador OR bit a bit.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
sheet.getCells().get("A1").putValue("Sample Data");
sheet.protect(AsposeCells.ProtectionType.All, "SheetPwd");
workbook.save("sheet_protected.xlsx");
let workbookReloaded = new AsposeCells.Workbook("sheet_protected.xlsx");
let sheetReloaded = workbookReloaded.getWorksheets().get(0);
sheetReloaded.unprotect("SheetPwd");
console.log("Worksheet protection removed successfully.");
```

## Agregar y validar firmas digitales
Una firma digital garantiza a los destinatarios que el contenido del libro es auténtico y no se ha modificado desde que se firmó. Aspose.Cells ofrece soporte para firmas digitales mediante el espacio de nombres `Aspose.Cells.DigitalSignatures`. El flujo de trabajo habitual consiste en cargar un archivo de certificado `.pfx` mediante las utilidades criptográficas de Node.js, envolverlo en un `Aspose.Cells.DigitalSignatures.DigitalSignature`, agregar la firma a un `DigitalSignatureCollection` y aplicar la colección al libro mediante `workbook.addDigitalSignature(digitalSignatureCollection)`. La propiedad `digitalSignature.comments` puede registrar el contexto de la firma, como la hora y el propósito. Cualquier modificación realizada en el libro después de firmarlo invalida la firma, por lo que un paso de validación en el lado receptor puede detectar manipulaciones.

```javascript
const AsposeCells = require("aspose.cells.node");
let signature = new AsposeCells.DigitalSignature("signature.pfx", "pfx-password", "Signed by Aspose.Cells", new Date());
let signatures = new AsposeCells.DigitalSignatureCollection();
signatures.add(signature);
let workbook = new AsposeCells.Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value");
workbook.addDigitalSignature(signatures);
workbook.save("signed_workbook.xlsx");
console.log("The workbook has been digitally signed.");
```

## Artículos relacionados
- [Cifrar y descifrar archivos Excel](/cells/es/nodejs-cpp/encrypt-and-decrypt-excel-files/)
- [Proteger y desproteger la estructura del libro](/cells/es/nodejs-cpp/protect-and-unprotect-workbook-structure/)
- [Proteger y desproteger hojas de cálculo](/cells/es/nodejs-cpp/protect-and-unprotect-worksheets/)
- [Proteger o desproteger el libro compartido con una contraseña](/cells/es/nodejs-cpp/password-protect-or-unprotect-the-shared-workbook/)
- [Asignar y validar firmas digitales](/cells/es/nodejs-cpp/assign-and-validate-digital-signatures/)
- [Comprobar la contraseña de modificación mediante Aspose.Cells](/cells/es/nodejs-cpp/check-password-to-modify-using-aspose-cells/)
- [Detectar el formato de los archivos cifrados de Office Open XML - OOXML](/cells/es/nodejs-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Cifrado de archivos Excel](/cells/es/nodejs-cpp/encrypting-excel-files/)
- [Cómo detectar el formato de un archivo y comprobar si está cifrado](/cells/es/nodejs-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="nodejs-cpp" >}}