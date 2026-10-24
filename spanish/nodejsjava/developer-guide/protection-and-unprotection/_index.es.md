---
title: Proteger y Desproteger
linktitle: Cifrado y protección
description: Esta sección presenta cómo cifrar y descifrar archivos de Excel y proteger datos de Excel, incluyendo el cifrado de archivos, la protección de solo lectura, la protección de la estructura del libro, la protección de hojas de cálculo y firmas digitales mediante código JavaScript
keywords: Aspose.Cells, Node.js via Java, cifrar, descifrar, contraseña, proteger, desproteger, protección del libro, protección de hojas de cálculo, solo lectura, firma digital, JavaScript
type: docs
weight: 68
url: /es/nodejs-java/protect-and-unprotect/
alias: [/nodejs-java/security-features/]
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Los libros de Excel a menudo almacenan información financiera, comercial o personal confidencial que debe protegerse del acceso no autorizado. Aspose.Cells for Node.js via Java ofrece un conjunto completo de funciones de protección que refleja las capacidades de Microsoft Excel, lo que le permite proteger sus datos a nivel de archivo, nivel de libro y nivel de hoja de cálculo.

{{% alert color="primary" %}}
Aspose.Cells for Node.js via Java ofrece una amplia gama de funciones de protección, desde el nivel de archivo hasta el nivel de datos, similar a MS Excel. Estas capacidades incluyen cifrar archivos con una contraseña, imponer acceso de solo lectura mediante una contraseña para modificar, proteger la estructura del libro, proteger hojas de cálculo y firmar digitalmente los libros.
{{% /alert %}}

## Cifrar y descifrar archivos de Excel
Una contraseña establecida en un archivo de Excel impide que usuarios no autorizados abran o vean el contenido del libro. Para cifrar un libro, asigne una cadena de contraseña a `workbook.getSettings().setPassword(...)` y luego guarde el libro. Aspose.Cells escribe el archivo en forma cifrada. Para abrir un libro cifrado para descifrarlo, cree una instancia de un objeto `LoadOptions`, establezca `loadOptions.setPassword(...)` con la misma contraseña utilizada durante el cifrado y páselo al constructor `Workbook`. Aspose.Cells aplica la contraseña proporcionada de forma transparente para que el resto de su código pueda interactuar con el contenido descifrado como si el archivo fuera un libro normal.

```javascript
const AsposeCells = require("aspose.cells");
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

## Protección de solo lectura (contraseña para modificar)
Excel admite dos capas distintas de contraseñas. La primera es una contraseña para abrir, que cifra el archivo en sí y se trata en la sección anterior. La segunda es una contraseña para modificar, que no impide que los usuarios abran el libro; en su lugar, Excel recomienda abrir el archivo en modo de solo lectura a menos que se proporcione la contraseña de modificación. Configure este comportamiento en Aspose.Cells mediante `workbook.getSettings().getWriteProtection()`. Asigne a la propiedad `Password` la contraseña de modificación y la propiedad `Author` para identificar quién aplicó la protección. Utilice el método `writeProtection.validatePassword(string)` para comprobar si una contraseña de modificación proporcionada es correcta, devolviendo `true` si coincide y `false` en caso contrario.

```javascript
const AsposeCells = require("aspose.cells");
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
Proteger la estructura del libro impide que otros usuarios vean hojas de cálculo ocultas, agreguen nuevas hojas, muevan hojas, eliminen hojas, oculten hojas o renombren las hojas. El estado protegido se aplica a la estructura de las hojas, no al contenido de las celdas dentro de cualquier hoja. Para aplicar la protección de estructura, llame a `workbook.protect(ProtectionType.Structure, "password")`. Para eliminar la protección, llame a `workbook.unprotect("password")` y proporcione la contraseña correcta. El valor de enumeración `ProtectionType.Structure` se utiliza aquí y es distinto de otros tipos de protección como `ProtectionType.Windows`.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
// Agregar una segunda hoja de cálculo
workbook.getWorksheets().add();
// Escribir un valor de muestra en la celda A1 de la primera hoja de cálculo
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// Proteger la estructura del libro
workbook.protect(AsposeCells.ProtectionType.STRUCTURE, "StructPwd");
// Guardar el libro como structure_protected.xlsx
let filePath = "structure_protected.xlsx";
workbook.save(filePath);
// Recargar el archivo en una nueva instancia del libro
let loadedWorkbook = new AsposeCells.Workbook(filePath);
// Eliminar la protección de la estructura
loadedWorkbook.unprotect("StructPwd");
// Imprimir mensaje de confirmación
console.log("Structure protection has been successfully removed from the workbook.");
```

## Proteger y desproteger hojas de cálculo
La protección de hojas de cálculo bloquea las celdas de una hoja de cálculo contra cambios accidentales o deliberados. Los usuarios no pueden editar celdas bloqueadas sin proporcionar la contraseña. Esta es la protección típica que se utiliza para proteger fórmulas, encabezados o áreas designadas para la entrada de datos en hojas de cálculo compartidas. Para proteger una hoja de cálculo, llame a `worksheet.protect(ProtectionType.All, "password")`. Usar `ProtectionType.All` habilita todas las opciones de protección disponibles, como seleccionar celdas bloqueadas, formatear celdas, insertar filas y columnas, y eliminar filas y columnas. Para eliminar la protección, llame a `worksheet.unprotect("password")` con la contraseña correcta. Hay un control más granular disponible combinando otros tipos de protección como `Contents`, `Objects` y `Scenarios` mediante OR bit a bit.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
sheet.getCells().get("A1").putValue("Sample Data");
sheet.protect(AsposeCells.ProtectionType.ALL, "SheetPwd");
workbook.save("sheet_protected.xlsx");
let workbookReloaded = new AsposeCells.Workbook("sheet_protected.xlsx");
let sheetReloaded = workbookReloaded.getWorksheets().get(0);
sheetReloaded.unprotect("SheetPwd");
console.log("Worksheet protection removed successfully.");
```

## Agregar y validar firmas digitales
Una firma digital garantiza a los destinatarios que el contenido del libro es auténtico y no se ha alterado desde que se firmó. Aspose.Cells proporciona compatibilidad con firmas digitales mediante clases como `AsposeCells.DigitalSignature` y `AsposeCells.DigitalSignatureCollection`. El flujo típico crea un `AsposeCells.DigitalSignature` directamente a partir de un archivo de certificado `.pfx` junto con su contraseña y comentarios de firma, agrega la firma a una `DigitalSignatureCollection` y aplica la colección al libro mediante `workbook.addDigitalSignature(DigitalSignatureCollection)`. La propiedad `DigitalSignature.Comments` puede registrar el contexto de firma, como la hora y el propósito de la firma. Cualquier modificación realizada en el libro después de firmar invalida la firma, por lo que un paso de validación en el lado receptor puede detectar manipulaciones.

```javascript
const AsposeCells = require("aspose.cells");
let signature = new AsposeCells.DigitalSignature("signature.pfx", "pfx-password", "Signed by Aspose.Cells", new Date());
let signatures = new AsposeCells.DigitalSignatureCollection();
signatures.add(signature);
let workbook = new AsposeCells.Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value");
workbook.addDigitalSignature(signatures);
workbook.save("signed_workbook.xlsx");
console.log("The workbook has been digitally signed.");
```

{{< app/cells/assistant language="nodejs-java" >}}