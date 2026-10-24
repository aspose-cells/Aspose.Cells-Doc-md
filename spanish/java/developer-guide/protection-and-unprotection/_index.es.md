---
title: Cifrar, descifrar, proteger y desproteger archivos de Excel
linktitle: Cifrado y Protección
description: Esta sección presenta cómo cifrar y descifrar archivos de Excel y proteger datos de Excel, cubriendo el cifrado de archivos, la protección de solo lectura, la protección de la estructura del libro, la protección de hojas de cálculo y las firmas digitales mediante código Java
keywords: Aspose.Cells, Java, cifrar, descifrar, contraseña, proteger, desproteger, protección del libro, protección de hojas de cálculo, solo lectura, firma digital
type: docs
weight: 68
url: /es/java/protect-and-unprotect/
alias: [/java/security-features/]
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Los libros de Excel suelen almacenar información financiera, empresarial o personal sensible que debe mantenerse fuera del acceso no autorizado. Aspose.Cells for Java ofrece un conjunto completo de funciones de protección que reflejan las capacidades de Microsoft Excel, permitiéndole proteger sus datos a nivel de archivo, a nivel de libro y a nivel de hoja de cálculo.

{{% alert color="primary" %}}
Aspose.Cells for Java ofrece una amplia gama de funciones de protección, desde el nivel de archivo hasta el nivel de datos, similares a MS Excel. Estas capacidades incluyen el cifrado de archivos con una contraseña, la aplicación de acceso de solo lectura mediante una contraseña de modificación, la protección de la estructura del libro, la protección de hojas de cálculo y la firma digital de libros.
{{% /alert %}}

## Cifrar y descifrar archivos de Excel
Una contraseña establecida en un archivo de Excel impide que usuarios no autorizados abran o vean el contenido del libro. Para cifrar un libro, asigne una cadena de contraseña a `Workbook.Settings.Password` (al que se accede mediante `workbook.getSettings().setPassword(...)`) y luego guarde el libro. Aspose.Cells escribe el archivo en forma cifrada. Para abrir un libro cifrado para descifrarlo, cree una instancia de un objeto `LoadOptions`, establezca `LoadOptions.Password` (mediante `loadOptions.setPassword(...)`) en la misma contraseña que se usó durante el cifrado y páselo al constructor `Workbook`. Aspose.Cells aplica la contraseña proporcionada de forma transparente para que el resto del código pueda interactuar con el contenido descifrado como si el archivo fuera un libro normal.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cell cell = sheet.getCells().get("A1");
cell.putValue("Confidential Data");
workbook.getSettings().setPassword("OpenPassword123");
workbook.save("encrypted.xlsx");
LoadOptions loadOptions = new LoadOptions();
loadOptions.setPassword("OpenPassword123");
Workbook decryptedWorkbook = new Workbook("encrypted.xlsx", loadOptions);
System.out.println("Decrypted cell A1 value: " + decryptedWorkbook.getWorksheets().get(0).getCells().get("A1").getStringValue());
```

## Protección de solo lectura (contraseña para modificar)
Excel admite dos capas de contraseña distintas. La primera es una contraseña para abrir, que cifra el archivo en sí y se trata en la sección anterior. La segunda es una contraseña para modificar, que no impide que los usuarios abran el libro; en su lugar, Excel recomienda abrir el archivo en modo de solo lectura a menos que se proporcione la contraseña de modificación. Configure este comportamiento en Aspose.Cells mediante `Workbook.Settings.WriteProtection` (al que se accede mediante `workbook.getSettings().getWriteProtection()`). Establezca su propiedad `Password` (mediante `writeProtection.setPassword(...)`) en la contraseña de modificación y su propiedad `Author` (mediante `writeProtection.setAuthor(...)`) para identificar quién aplicó la protección. Utilice el método `WriteProtection.validatePassword(String)` para comprobar si una contraseña de modificación proporcionada es correcta, devolviendo `true` si coincide y `false` en caso contrario.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data");
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd");
workbook.getSettings().getWriteProtection().setAuthor("AuthorName");
workbook.save("WriteProtectedWorkbook.xlsx");
boolean isCorrectValid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd");
System.out.println("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
boolean isWrongValid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd");
System.out.println("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## Proteger y desproteger la estructura del libro
Proteger la estructura del libro impide que otros usuarios vean hojas de cálculo ocultas, agreguen nuevas hojas de cálculo, muevan hojas de cálculo, eliminen hojas de cálculo, oculten hojas de cálculo o cambien el nombre de las hojas de cálculo. El estado protegido se aplica a la estructura de las hojas en lugar del contenido de las celdas dentro de cualquier hoja. Para aplicar la protección de estructura, llame a `workbook.protect(ProtectionType.STRUCTURE, "password")`. Para eliminar la protección, llame a `workbook.unprotect("password")` y proporcione la contraseña correcta. El valor de enumeración `ProtectionType.STRUCTURE` se utiliza aquí y es distinto de otros tipos de protección como `ProtectionType.WINDOWS`.

```java
import com.aspose.cells.*;
// Crear un nuevo libro
Workbook workbook = new Workbook();
// Agregar una segunda hoja de cálculo
workbook.getWorksheets().add();
// Escribir un valor de muestra en la celda A1 de la primera hoja de cálculo
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// Proteger la estructura del libro
workbook.protect(ProtectionType.STRUCTURE, "StructPwd");
// Guardar el libro como structure_protected.xlsx
String filePath = "structure_protected.xlsx";
workbook.save(filePath);
// Recargar el archivo en una nueva instancia de Workbook
Workbook loadedWorkbook = new Workbook(filePath);
// Eliminar la protección de la estructura
loadedWorkbook.unprotect("StructPwd");
// Imprimir mensaje de confirmación
System.out.println("Structure protection has been successfully removed from the workbook.");
```

## Proteger y desproteger hojas de cálculo
La protección de la hoja de cálculo bloquea las celdas de una hoja de cálculo contra cambios accidentales o deliberados. Los usuarios no pueden editar celdas bloqueadas sin proporcionar la contraseña. Esta es la protección típica utilizada para resguardar fórmulas, encabezados o áreas designadas para la entrada de datos en hojas de cálculo compartidas. Para proteger una hoja de cálculo, llame a `worksheet.protect(ProtectionType.ALL, "password")`. Usar `ProtectionType.ALL` habilita todas las opciones de protección disponibles, como seleccionar celdas bloqueadas, dar formato a celdas, insertar filas y columnas, y eliminar filas y columnas. Para eliminar la protección, llame a `worksheet.unprotect("password")` con la contraseña correcta. Hay un control más granular disponible combinando otros tipos de protección como `CONTENTS`, `OBJECTS` y `SCENARIOS` mediante el operador OR a nivel de bits.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
sheet.getCells().get("A1").putValue("Sample Data");
sheet.protect(ProtectionType.ALL, "SheetPwd", "SheetPwd");
workbook.save("sheet_protected.xlsx");
Workbook workbookReloaded = new Workbook("sheet_protected.xlsx");
Worksheet sheetReloaded = workbookReloaded.getWorksheets().get(0);
sheetReloaded.unprotect("SheetPwd");
System.out.println("Worksheet protection removed successfully.");
```

## Agregar y validar firmas digitales
Una firma digital garantiza a los destinatarios que el contenido del libro es auténtico y no se ha modificado desde que se firmó. Aspose.Cells proporciona compatibilidad con firmas digitales a través del paquete `com.aspose.cells.DigitalSignatures`. El flujo de trabajo típico carga un archivo de certificado `.pfx` mediante las APIs de seguridad de Java (como `java.security.KeyStore` y `java.security.cert.X509Certificate`), lo envuelve en un `com.aspose.cells.DigitalSignatures.DigitalSignature`, agrega la firma a un `DigitalSignatureCollection` y aplica la colección al libro mediante `workbook.addDigitalSignature(DigitalSignatureCollection)`. La propiedad `DigitalSignature.getComments()` puede registrar el contexto de la firma, como la hora y el propósito de la firma. Cualquier modificación realizada en el libro después de la firma invalida la firma, por lo que un paso de validación en el lado del receptor puede detectar manipulaciones.

```java
import com.aspose.cells.*;
import java.io.FileInputStream;
import java.security.KeyStore;
KeyStore pfxKeyStore = KeyStore.getInstance("PKCS12");
pfxKeyStore.load(new FileInputStream("signature.pfx"), "pfx-password".toCharArray());
DigitalSignature signature = new DigitalSignature(pfxKeyStore, "pfx-password", "Signed by Aspose.Cells", new DateTime());
DigitalSignatureCollection signatures = new DigitalSignatureCollection();
signatures.add(signature);
Workbook workbook = new Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value");
workbook.addDigitalSignature(signatures);
workbook.save("signed_workbook.xlsx");
System.out.println("The workbook has been digitally signed.");
```

## Artículos relacionados
- [Cifrar y descifrar archivos de Excel](/cells/es/java/encrypt-and-decrypt-excel-files/)
- [Proteger y desproteger la estructura del libro](/cells/es/java/protect-and-unprotect-workbook-structure/)
- [Proteger y desproteger la hoja de cálculo](/cells/es/java/protect-and-unprotect-worksheet/)
- [Proteger con contraseña o desproteger el libro compartido](/cells/es/java/password-protect-or-unprotect-the-shared-workbook/)
- [Asignar y validar firmas digitales](/cells/es/java/assign-and-validate-digital-signatures/)
- [Detectar el formato de archivo de archivos Office Open XML cifrados - OOXML](/cells/es/java/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Cómo detectar el formato de un archivo y comprobar si el archivo está cifrado](/cells/es/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="java" >}}