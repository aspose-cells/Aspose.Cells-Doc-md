---
title: Proteger y Desproteger
linktitle: Cifrado y protección
type: docs
weight: 68
url: /es/net/protect-and-unprotect/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
alias: [/net/security-features/]
description: Esta sección explica cómo cifrar y descifrar archivos de Excel y proteger datos de Excel, e incluye el cifrado de archivos, la protección de solo lectura, la protección de la estructura del libro, la protección de hojas de cálculo y las firmas digitales mediante código C#
keywords: Aspose.Cells, .NET, cifrar, descifrar, contraseña, proteger, desproteger, protección del libro, protección de hojas de cálculo, solo lectura, firma digital, C#
---

Los libros de Excel suelen almacenar información financiera, empresarial o personal confidencial que debe mantenerse fuera del acceso no autorizado. Aspose.Cells for .NET ofrece un conjunto completo de funciones de protección que refleja las capacidades de Microsoft Excel, lo que le permite proteger sus datos a nivel de archivo, a nivel de libro y a nivel de hoja de cálculo.

{{% alert color="primary" %}}
Aspose.Cells for .NET ofrece una amplia gama de funciones de protección, desde el nivel de archivo hasta el nivel de datos, de forma similar a MS Excel. Estas capacidades incluyen el cifrado de archivos con contraseña, la aplicación del acceso de solo lectura mediante una contraseña para modificar, la protección de la estructura del libro, la protección de las hojas de cálculo y la firma digital de los libros.
{{% /alert %}}

## Cifrar y descifrar archivos de Excel
Una contraseña establecida en un archivo de Excel impide que usuarios no autorizados abran o visualicen el contenido del libro. Para cifrar un libro, asigne una cadena de contraseña a `Workbook.Settings.Password` y luego guarde el libro. Aspose.Cells escribe el archivo en forma cifrada. Para abrir un libro cifrado y descifrarlo, cree una instancia de un objeto `LoadOptions`, establezca `LoadOptions.Password` en la misma contraseña utilizada durante el cifrado y páselo al constructor de `Workbook`. Aspose.Cells aplica la contraseña proporcionada de forma transparente, de modo que el resto del código pueda interactuar con el contenido descifrado como si el archivo fuera un libro normal.

```csharp
using System;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cell cell = sheet.Cells["A1"];
cell.PutValue("Confidential Data");
workbook.Settings.Password = "OpenPassword123";
workbook.Save("encrypted.xlsx");
LoadOptions loadOptions = new LoadOptions();
loadOptions.Password = "OpenPassword123";
Workbook decryptedWorkbook = new Workbook("encrypted.xlsx", loadOptions);
Console.WriteLine("Decrypted cell A1 value: " + decryptedWorkbook.Worksheets[0].Cells["A1"].StringValue);
```

## Protección de solo lectura (contraseña para modificar)
Excel admite dos capas distintas de contraseña. La primera es una contraseña para abrir, que cifra el archivo en sí y se trata en la sección anterior. La segunda es una contraseña para modificar, que no impide a los usuarios abrir el libro; en su lugar, Excel recomienda abrir el archivo en modo de solo lectura a menos que se proporcione la contraseña de modificación. Configure este comportamiento en Aspose.Cells mediante `Workbook.Settings.WriteProtection`. Establezca su propiedad `Password` en la contraseña de modificación y su propiedad `Author` para identificar quién aplicó la protección. Utilice el método `WriteProtection.ValidatePassword(string)` para comprobar si una contraseña de modificación proporcionada es correcta; devolverá `true` si coincide y `false` en caso contrario.

```csharp
using System;
using Aspose.Cells;
// Crear un nuevo libro desde cero
Workbook workbook = new Workbook();
// Escribir un valor de ejemplo en la celda A1 de la primera hoja de cálculo
workbook.Worksheets[0].Cells["A1"].PutValue("Sample Data");
// Configurar la protección contra escritura: establecer la contraseña de modificación y el autor
workbook.Settings.WriteProtection.Password = "ModifyPwd";
workbook.Settings.WriteProtection.Author = "AuthorName";
// Guardar el libro para que la protección contra escritura se conserve
workbook.Save("WriteProtectedWorkbook.xlsx");
// Validar la contraseña de modificación usando la contraseña correcta
bool isCorrectValid = workbook.Settings.WriteProtection.ValidatePassword("ModifyPwd");
Console.WriteLine("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
// Validar la contraseña de modificación usando una contraseña incorrecta para demostrar la otra rama
bool isWrongValid = workbook.Settings.WriteProtection.ValidatePassword("WrongPwd");
Console.WriteLine("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## Proteger y desproteger la estructura del libro
La protección de la estructura del libro impide que otros usuarios visualicen hojas de cálculo ocultas, agreguen nuevas hojas, muevan hojas, eliminen hojas, oculten hojas o cambien el nombre de las hojas. El estado protegido se aplica a la estructura de las hojas y no al contenido de las celdas dentro de ninguna hoja. Para aplicar la protección de la estructura, llame a `workbook.Protect(ProtectionType.Structure, "password")`. Para eliminar la protección, llame a `workbook.Unprotect("password")` y proporcione la contraseña correcta. El valor de enumeración `ProtectionType.Structure` se utiliza aquí y es distinto de otros tipos de protección como `ProtectionType.Windows`.

```csharp
using System;
using Aspose.Cells;
// Crear un nuevo libro
Workbook workbook = new Workbook();
// Agregar una segunda hoja de cálculo
workbook.Worksheets.Add();
// Escribir un valor de muestra en la celda A1 de la primera hoja de cálculo
workbook.Worksheets[0].Cells[0, 0].PutValue("Sample Data");
// Proteger la estructura del libro
workbook.Protect(ProtectionType.Structure, "StructPwd");
// Guardar el libro como structure_protected.xlsx
string filePath = "structure_protected.xlsx";
workbook.Save(filePath);
// Recargar el archivo en una nueva instancia de Workbook
Workbook loadedWorkbook = new Workbook(filePath);
// Eliminar la protección de estructura
loadedWorkbook.Unprotect("StructPwd");
// Imprimir mensaje de confirmación
Console.WriteLine("Structure protection has been successfully removed from the workbook.");
```

## Proteger y desproteger hojas de cálculo
La protección de la hoja de cálculo bloquea las celdas de una hoja frente a cambios accidentales o deliberados. Los usuarios no pueden editar las celdas bloqueadas sin proporcionar la contraseña. Esta es la protección habitual utilizada para proteger fórmulas, encabezados o áreas designadas para la introducción de datos en hojas de cálculo compartidas. Para proteger una hoja de cálculo, llame a `worksheet.Protect(ProtectionType.All, "password")`. El uso de `ProtectionType.All` habilita todas las opciones de protección disponibles, como seleccionar celdas bloqueadas, dar formato a celdas, insertar filas y columnas, y eliminar filas y columnas. Para eliminar la protección, llame a `worksheet.Unprotect("password")` con la contraseña correcta. Existe un control más granular mediante la combinación de otros tipos de protección como `Contents`, `Objects` y `Scenarios` utilizando el operador OR bit a bit.

```csharp
using System;
using Aspose.Cells;
var workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
sheet.Cells["A1"].PutValue("Sample Data");
sheet.Protect(ProtectionType.All, "SheetPwd");
workbook.Save("sheet_protected.xlsx");
var workbookReloaded = new Workbook("sheet_protected.xlsx");
Worksheet sheetReloaded = workbookReloaded.Worksheets[0];
sheetReloaded.Unprotect("SheetPwd");
Console.WriteLine("Worksheet protection removed successfully.");
```

## Agregar y validar firmas digitales
Una firma digital garantiza a los destinatarios que el contenido del libro es auténtico y no se ha modificado desde que se firmó. Aspose.Cells ofrece compatibilidad con firmas digitales a través del espacio de nombres `Aspose.Cells.DigitalSignatures`. El flujo de trabajo típico carga un archivo de certificado `.pfx` mediante `System.Security.Cryptography.X509Certificates.X509Certificate2`, lo envuelve en un `Aspose.Cells.DigitalSignatures.DigitalSignature`, agrega la firma a un `DigitalSignatureCollection` y aplica la colección al libro mediante `Workbook.AddDigitalSignature(DigitalSignatureCollection)`. La propiedad `DigitalSignature.Comments` puede registrar el contexto de la firma, como la hora y el propósito de la firma. Cualquier modificación realizada en el libro después de firmarlo invalida la firma, por lo que un paso de validación en el lado receptor puede detectar manipulaciones.

```csharp
using System;
using System.IO;
using System.Security.Cryptography.X509Certificates;
using Aspose.Cells;
using Aspose.Cells.DigitalSignatures;
X509Certificate2 certificate = new X509Certificate2("signature.pfx", "pfx-password");
DigitalSignature signature = new DigitalSignature(certificate, "Signed by Aspose.Cells", DateTime.Now);
DigitalSignatureCollection signatures = new DigitalSignatureCollection();
signatures.Add(signature);
Workbook workbook = new Workbook();
workbook.Worksheets[0].Cells["A1"].PutValue("Sample Value");
workbook.AddDigitalSignature(signatures);
workbook.Save("signed_workbook.xlsx");
Console.WriteLine("The workbook has been digitally signed.");
```

## Artículos relacionados
- [Cifrar y descifrar archivos de Excel](/cells/es/net/encrypt-and-decrypt-excel-files/)
- [Proteger y desproteger la estructura del libro](/cells/es/net/protect-and-unprotect-workbook-structure/)
- [Proteger y desproteger la hoja de cálculo](/cells/es/net/protect-and-unprotect-worksheets/)
- [Proteger o desproteger con contraseña el libro compartido](/cells/es/net/password-protect-or-unprotect-the-shared-workbook/)
- [Asignar y validar firmas digitales](/cells/es/net/assign-and-validate-digital-signatures/)
- [Comprobar la contraseña para modificar con Aspose.Cells](/cells/es/net/check-password-to-modify-using-aspose-cells/)
- [Detectar el formato de archivo de archivos Office Open XML cifrados - OOXML](/cells/es/net/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Cifrado de archivos de Excel](/cells/es/net/encrypting-excel-files/)
- [Cómo detectar el formato de un archivo y comprobar si el archivo está cifrado](/cells/es/net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="csharp" >}}