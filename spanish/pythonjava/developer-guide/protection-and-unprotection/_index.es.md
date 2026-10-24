---
title: Proteger y Desproteger
linktitle: Protección
description: Esta sección presenta cómo cifrar y descifrar archivos de Excel y proteger los datos de Excel, cubriendo el cifrado de archivos, la protección de solo lectura, la protección de la estructura del libro, la protección de hojas de cálculo y las firmas digitales usando código Python
keywords: Aspose.Cells, Python via Java, cifrar, descifrar, contraseña, proteger, desproteger, protección del libro, protección de hojas de cálculo, solo lectura, firma digital, Python
type: docs
weight: 68
url: /es/python-java/protect-and-unprotect/
alias: [/python-java/security-features/]
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Los libros de Excel suelen almacenar información financiera, empresarial o personal confidencial que debe mantenerse fuera del acceso no autorizado. Aspose.Cells for Python via Java ofrece un conjunto completo de funciones de protección que refleja las capacidades de Microsoft Excel, permitiéndole asegurar sus datos a nivel de archivo, nivel de libro y nivel de hoja de cálculo.

{{% alert color="primary" %}}
Aspose.Cells for Python via Java ofrece una amplia gama de funciones de protección, desde el nivel de archivo hasta el nivel de datos, similar a MS Excel. Estas capacidades incluyen cifrar archivos con una contraseña, aplicar acceso de solo lectura mediante una contraseña para modificar, proteger la estructura del libro, proteger las hojas de cálculo y firmar digitalmente los libros.
{{% /alert %}}

## Cifrar y descifrar archivos de Excel
Una contraseña establecida en un archivo Excel impide que los usuarios no autorizados abran o vean el contenido del libro. Para cifrar un libro, asigne una cadena de contraseña a `workbook.getSettings().setPassword(...)` y luego guarde el libro. Aspose.Cells escribe el archivo en forma cifrada. Para abrir un libro cifrado para descifrarlo, cree una instancia de un objeto `LoadOptions`, configure la contraseña mediante `load_options.setPassword(...)` con la misma contraseña que se usó durante el cifrado, y pásela al constructor `Workbook`. Aspose.Cells aplica la contraseña proporcionada de forma transparente para que el resto de su código pueda interactuar con el contenido descifrado como si el archivo fuera un libro normal.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cell, LoadOptions
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cell = sheet.getCells().get("A1")
cell.putValue("Confidential Data")
workbook.getSettings().setPassword("OpenPassword123")
workbook.save("encrypted.xlsx")
load_options = LoadOptions()
load_options.setPassword("OpenPassword123")
decrypted_workbook = Workbook("encrypted.xlsx", load_options)
print("Decrypted cell A1 value: " + decrypted_workbook.getWorksheets().get(0).getCells().get("A1").getStringValue())
jpype.shutdownJVM()
```

## Protección de solo lectura (contraseña para modificar)
Excel admite dos capas distintas de contraseñas. La primera es una contraseña para abrir, que cifra el archivo en sí y se trata en la sección anterior. La segunda es una contraseña para modificar, que no impide a los usuarios abrir el libro; en su lugar, Excel recomienda abrir el archivo en modo de solo lectura a menos que se proporcione la contraseña de modificación. Configure este comportamiento en Aspose.Cells mediante `workbook.getSettings().getWriteProtection()`. Establezca la contraseña mediante `setPassword(...)` con la contraseña de modificación y el autor mediante `setAuthor(...)` para identificar quién aplicó la protección. Use el método `writeProtection.validatePassword(String)` para comprobar si una contraseña de modificación proporcionada es correcta, devolviendo `true` para una coincidencia y `false` en caso contrario.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# Crear un nuevo libro desde cero
workbook = Workbook()
# Escribir un valor de muestra en la celda A1 de la primera hoja de cálculo
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data")
# Configurar la protección de escritura: establecer la contraseña para modificar y el autor
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd")
workbook.getSettings().getWriteProtection().setAuthor("AuthorName")
# Guardar el libro para que la protección de escritura persista
workbook.save("WriteProtectedWorkbook.xlsx")
# Validar la contraseña para modificar usando la contraseña correcta
is_correct_valid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd")
print("ValidatePassword(\"ModifyPwd\") returned: " + str(is_correct_valid))
# Validar la contraseña para modificar usando una contraseña incorrecta para demostrar la otra rama
is_wrong_valid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd")
print("ValidatePassword(\"WrongPwd\") returned: " + str(is_wrong_valid))
jpype.shutdownJVM()
```

## Proteger y desproteger la estructura del libro
Proteger la estructura del libro impide a otros usuarios ver hojas de cálculo ocultas, agregar nuevas hojas de cálculo, mover hojas de cálculo, eliminar hojas de cálculo, ocultar hojas de cálculo o cambiar el nombre de hojas de cálculo. El estado protegido se aplica a la estructura de la hoja y no al contenido de las celdas dentro de ninguna hoja. Para aplicar la protección de la estructura, llame a `workbook.protect(ProtectionType.STRUCTURE, "password")`. Para eliminar la protección, llame a `workbook.unprotect("password")` y proporcione la contraseña correcta. El valor de enumeración `ProtectionType.STRUCTURE` se utiliza aquí y es distinto de otros tipos de protección como `ProtectionType.WINDOWS`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, ProtectionType
# Crear un nuevo libro
workbook = Workbook()
# Agregar una segunda hoja de cálculo
workbook.getWorksheets().add()
# Escribir un valor de muestra en la celda A1 de la primera hoja de cálculo
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data")
# Proteger la estructura del libro
workbook.protect(ProtectionType.STRUCTURE, "StructPwd")
# Guardar el libro como structure_protected.xlsx
file_path = "structure_protected.xlsx"
workbook.save(file_path)
# Recargar el archivo en una nueva instancia de Workbook
loaded_workbook = Workbook(file_path)
# Eliminar la protección de estructura
loaded_workbook.unprotect("StructPwd")
# Imprimir mensaje de confirmación
print("Structure protection has been successfully removed from the workbook.")
jpype.shutdownJVM()
```

## Proteger y desproteger hojas de cálculo
La protección de la hoja de cálculo bloquea las celdas de una hoja de cálculo contra cambios accidentales o deliberados. Los usuarios no pueden editar celdas bloqueadas sin proporcionar la contraseña. Esta es la protección típica que se utiliza para proteger fórmulas, encabezados o áreas designadas para la entrada de datos en hojas de cálculo compartidas. Para proteger una hoja de cálculo, llame a `worksheet.protect(ProtectionType.ALL, "password")`. El uso de `ProtectionType.ALL` habilita todas las opciones de protección disponibles, como seleccionar celdas bloqueadas, dar formato a celdas, insertar filas y columnas, y eliminar filas y columnas. Para eliminar la protección, llame a `worksheet.unprotect("password")` con la contraseña correcta. Hay un control más granular disponible combinando otros tipos de protección como `ProtectionType.CONTENTS`, `ProtectionType.OBJECTS` y `ProtectionType.SCENARIOS` mediante OR bit a bit.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, ProtectionType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sample Data")
worksheet.protect(ProtectionType.ALL, "SheetPwd", None)
workbook.save("sheet_protected.xlsx")
workbook_reloaded = Workbook("sheet_protected.xlsx")
sheet_reloaded = workbook_reloaded.getWorksheets().get(0)
sheet_reloaded.unprotect("SheetPwd")
print("Worksheet protection removed successfully.")
jpype.shutdownJVM()
```

## Agregar y validar firmas digitales
Una firma digital garantiza a los destinatarios que el contenido del libro es auténtico y no se ha alterado desde que se firmó. Aspose.Cells ofrece soporte para firmas digitales a través del espacio de nombres `Aspose.Cells.DigitalSignatures`. El flujo de trabajo típico carga un archivo de certificado `.pfx` mediante `java.security.KeyStore`, lo envuelve en un `Aspose.Cells.DigitalSignatures.DigitalSignature`, agrega la firma a una `DigitalSignatureCollection`, y aplica la colección al libro mediante `workbook.addDigitalSignature(digitalSignatureCollection)`. La propiedad `digitalSignature.getComments()` puede registrar el contexto de la firma, como la hora y el propósito de la firma. Cualquier modificación realizada en el libro después de la firma invalida la firma, por lo que un paso de validación en el lado receptor puede detectar manipulaciones.

```python
import jpype
import jpype.imports
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, DigitalSignature, DigitalSignatureCollection
from java.security import KeyStore
from java.io import FileInputStream
from java.util import Date
# Cargar certificado desde archivo PFX usando Java KeyStore
key_store = KeyStore.getInstance("PKCS12")
fis = FileInputStream("signature.pfx")
key_store.load(fis, "pfx-password")
fis.close()
# Obtener el certificado
alias = key_store.aliases().nextElement()
certificate = key_store.getCertificate(alias)
# Crear firma digital
signature = DigitalSignature(certificate, "Signed by Aspose.Cells", Date())
signatures = DigitalSignatureCollection()
signatures.add(signature)
# Crear libro y agregar firma
workbook = Workbook()
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value")
workbook.addDigitalSignature(signatures)
workbook.save("signed_workbook.xlsx")
print("The workbook has been digitally signed.")
jpype.shutdownJVM()
```

## Artículos relacionados
- [Cifrar y descifrar archivos de Excel](/cells/es/python-java/encrypt-and-decrypt-excel-files/)
- [Proteger y desproteger la estructura del libro](/cells/es/python-java/protect-and-unprotect-workbook-structure/)
- [Proteger y desproteger la hoja de cálculo](/cells/es/python-java/protect-and-unprotect-worksheet/)
- [Comprobar la contraseña para modificar con Aspose.Cells](/cells/es/python-java/check-password-to-modify-using-aspose-cells/)

{{< app/cells/assistant language="python" >}}