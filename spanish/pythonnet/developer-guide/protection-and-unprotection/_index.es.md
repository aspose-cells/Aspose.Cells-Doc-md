---
title: Proteger y Desproteger
linktitle: Cifrado y protección
description: Esta sección presenta cómo cifrar y descifrar archivos de Excel y proteger datos de Excel, incluyendo el cifrado de archivos, la protección de solo lectura, la protección de la estructura del libro, la protección de hojas de cálculo y las firmas digitales mediante código Python
keywords: Aspose.Cells, Python via .NET, cifrar, descifrar, contraseña, proteger, desproteger, protección del libro, protección de hojas de cálculo, solo lectura, firma digital, Python
type: docs
weight: 68
url: /es/python-net/protect-and-unprotect/
alias: [/python-net/security-features/]
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Los libros de Excel suelen almacenar información financiera, empresarial o personal sensible que debe mantenerse alejada del acceso no autorizado. Aspose.Cells for Python via .NET ofrece un conjunto completo de funciones de protección que refleja las capacidades de Microsoft Excel, lo que le permite proteger sus datos a nivel de archivo, a nivel de libro y a nivel de hoja de cálculo.

{{% alert color="primary" %}}
Aspose.Cells for Python via .NET ofrece una amplia variedad de funciones de protección, desde el nivel de archivo hasta el nivel de datos, de forma similar a MS Excel. Estas capacidades incluyen el cifrado de archivos con contraseña, la aplicación de acceso de solo lectura mediante una contraseña de modificación, la protección de la estructura del libro, la protección de hojas de cálculo y la firma digital de los libros.
{{% /alert %}}

## Cifrar y descifrar archivos de Excel
Una contraseña establecida en un archivo Excel impide que usuarios no autorizados abran o visualicen el contenido del libro. Para cifrar un libro, asigne una cadena de contraseña a `workbook.settings.password` y, a continuación, guarde el libro. Aspose.Cells escribe el archivo en forma cifrada. Para abrir un libro cifrado y descifrarlo, cree una instancia de un objeto `LoadOptions`, establezca `load_options.password` con la misma contraseña utilizada durante el cifrado y páselo al constructor de `Workbook`. Aspose.Cells aplica la contraseña proporcionada de forma transparente, de modo que el resto de su código pueda interactuar con el contenido descifrado como si el archivo fuera un libro normal.

```python
import aspose.cells as ac
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cell = sheet.cells.get("A1")
cell.put_value("Confidential Data")
workbook.settings.password = "OpenPassword123"
workbook.save("encrypted.xlsx")
load_options = ac.LoadOptions()
load_options.password = "OpenPassword123"
decrypted_workbook = ac.Workbook("encrypted.xlsx", load_options)
print("Decrypted cell A1 value: " + decrypted_workbook.worksheets[0].cells.get("A1").string_value)
```

## Protección de solo lectura (contraseña de modificación)
Excel admite dos capas de contraseña diferenciadas. La primera es una contraseña para abrir, que cifra el archivo en sí y se trata en la sección anterior. La segunda es una contraseña de modificación, que no impide que los usuarios abran el libro; en su lugar, Excel recomienda abrir el archivo en modo de solo lectura a menos que se proporcione la contraseña de modificación. Configure este comportamiento en Aspose.Cells mediante `workbook.settings.write_protection`. Establezca su propiedad `password` con la contraseña de modificación y su propiedad `author` para identificar quién aplicó la protección. Utilice el método `write_protection.validate_password(string)` para comprobar si una contraseña de modificación proporcionada es correcta, devolviendo `true` si coincide y `false` en caso contrario.

```python
import aspose.cells as ac
# Crear un nuevo libro desde cero
workbook = ac.Workbook()
# Escribir un valor de muestra en la celda A1 de la primera hoja de cálculo
workbook.worksheets[0].cells.get("A1").put_value("Sample Data")
# Configurar la protección contra escritura: establecer la contraseña para modificar y el autor
workbook.settings.write_protection.password = "ModifyPwd"
workbook.settings.write_protection.author = "AuthorName"
# Guardar el libro para que la protección contra escritura se mantenga
workbook.save("WriteProtectedWorkbook.xlsx")
# Validar la contraseña para modificar usando la contraseña correcta
is_correct_valid = workbook.settings.write_protection.validate_password("ModifyPwd")
print("ValidatePassword(\"ModifyPwd\") returned: " + str(is_correct_valid))
# Validar la contraseña para modificar usando una contraseña incorrecta para demostrar la otra rama
is_wrong_valid = workbook.settings.write_protection.validate_password("WrongPwd")
print("ValidatePassword(\"WrongPwd\") returned: " + str(is_wrong_valid))
```

## Proteger y desproteger la estructura del libro
Proteger la estructura del libro impide que otros usuarios vean hojas de cálculo ocultas, agreguen nuevas hojas de cálculo, muevan hojas de cálculo, eliminen hojas de cálculo, oculten hojas de cálculo o cambien el nombre de las hojas de cálculo. El estado protegido se aplica a la estructura de las hojas y no al contenido de las celdas dentro de ninguna hoja. Para aplicar la protección de estructura, llame a `workbook.protect(ProtectionType.STRUCTURE, "password")`. Para eliminar la protección, llame a `workbook.unprotect("password")` y proporcione la contraseña correcta. Aquí se utiliza el valor de enumeración `ProtectionType.STRUCTURE`, que se distingue de otros tipos de protección como `ProtectionType.WINDOWS`.

```python
import aspose.cells as ac
# Crear un nuevo libro
workbook = ac.Workbook()
# Agregar una segunda hoja de cálculo
workbook.worksheets.add()
# Escribir un valor de muestra en la celda A1 de la primera hoja de cálculo
workbook.worksheets[0].cells.get(0, 0).put_value("Sample Data")
# Proteger la estructura del libro
workbook.protect(ac.ProtectionType.STRUCTURE, "StructPwd")
# Guardar el libro como structure_protected.xlsx
file_path = "structure_protected.xlsx"
workbook.save(file_path)
# Recargar el archivo en una nueva instancia de Workbook
loaded_workbook = ac.Workbook(file_path)
# Eliminar la protección de la estructura
loaded_workbook.unprotect("StructPwd")
# Imprimir mensaje de confirmación
print("Structure protection has been successfully removed from the workbook.")
```

## Proteger y desproteger hojas de cálculo
La protección de la hoja de cálculo bloquea las celdas de una hoja frente a modificaciones accidentales o intencionadas. Los usuarios no pueden editar las celdas bloqueadas sin proporcionar la contraseña. Esta es la protección habitual utilizada para resguardar fórmulas, encabezados o áreas designadas para la entrada de datos en hojas de cálculo compartidas. Para proteger una hoja de cálculo, llame a `worksheet.protect(ProtectionType.ALL, "password")`. El uso de `ProtectionType.ALL` habilita todas las opciones de protección disponibles, como seleccionar celdas bloqueadas, dar formato a celdas, insertar filas y columnas, y eliminar filas y columnas. Para eliminar la protección, llame a `worksheet.unprotect("password")` con la contraseña correcta. Existe un control más granular mediante la combinación de otros tipos de protección como `Contents`, `Objects` y `Scenarios` utilizando el operador OR a nivel de bits.

```python
import aspose.cells as ac
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
sheet.cells.get("A1").put_value("Sample Data")
sheet.protect(ac.ProtectionType.ALL, "SheetPwd")
workbook.save("sheet_protected.xlsx")
workbook_reloaded = ac.Workbook("sheet_protected.xlsx")
sheet_reloaded = workbook_reloaded.worksheets[0]
sheet_reloaded.unprotect("SheetPwd")
print("Worksheet protection removed successfully.")
```

## Agregar y validar firmas digitales
Una firma digital garantiza a los destinatarios que el contenido del libro es auténtico y que no se ha alterado desde que se firmó. Aspose.Cells ofrece compatibilidad con firmas digitales a través del espacio de nombres `aspose.cells.digital_signatures`. El flujo de trabajo típico carga un archivo de certificado `.pfx` mediante `System.Security.Cryptography.X509Certificates.X509Certificate2`, lo envuelve en un `aspose.cells.digital_signatures.DigitalSignature`, agrega la firma a un `DigitalSignatureCollection` y aplica la colección al libro mediante `workbook.add_digital_signature(DigitalSignatureCollection)`. La propiedad `digital_signature.comments` puede registrar el contexto de la firma, como la hora y el propósito de la firma. Cualquier modificación realizada en el libro después de la firma invalida la firma, por lo que un paso de validación en el lado receptor puede detectar manipulaciones.

```python
from datetime import datetime
import aspose.cells as ac
from aspose.cells.digitalsignatures import DigitalSignature, DigitalSignatureCollection
with open("signature.pfx", "rb") as certificate_file:
    certificate = certificate_file.read()
signature = DigitalSignature(certificate, "Signed by Aspose.Cells", datetime.now())
signatures = DigitalSignatureCollection()
signatures.add(signature)
workbook = ac.Workbook()
workbook.worksheets[0].cells.get("A1").put_value("Sample Value")
workbook.add_digital_signature(signatures)
workbook.save("signed_workbook.xlsx")
print("The workbook has been digitally signed.")
```

## Artículos relacionados
- [Cifrar y descifrar archivos de Excel](/cells/es/python-net/encrypt-and-decrypt-excel-files/)
- [Proteger y desproteger la estructura del libro](/cells/es/python-net/protect-and-unprotect-workbook-structure/)
- [Proteger y desproteger hojas de cálculo](/cells/es/python-net/protect-and-unprotect-worksheets/)
- [Proteger o desproteger con contraseña el libro compartido](/cells/es/python-net/password-protect-or-unprotect-the-shared-workbook/)
- [Asignar y validar firmas digitales](/cells/es/python-net/assign-and-validate-digital-signatures/)
- [Comprobar la contraseña de modificación con Aspose.Cells](/cells/es/python-net/check-password-to-modify-using-aspose-cells/)
- [Detectar el formato de archivo de archivos cifrados Office Open XML (OOXML)](/cells/es/python-net/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Cifrado de archivos de Excel](/cells/es/python-net/encrypting-excel-files/)
- [Cómo detectar el formato de un archivo y comprobar si está cifrado](/cells/es/python-net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="python-net" >}}