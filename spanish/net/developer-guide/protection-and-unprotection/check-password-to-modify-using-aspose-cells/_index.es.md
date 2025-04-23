---
title: Verificar Contraseña para modificar con Aspose.Cells
type: docs
weight: 2400
url: /es/net/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

A veces, necesitas verificar si la contraseña proporcionada coincide con la **Contraseña para modificar** programáticamente. Aspose.Cells proporciona el método WorkbookSettings.WriteProtection.ValidatePassword() que puedes usar para verificar si la Contraseña para modificar proporcionada es correcta o no.

{{% /alert %}}

## **Verificar Contraseña para modificar en Microsoft Excel**

Puedes asignar **Contraseña para abrir** y **Contraseña para modificar** al crear tus libros de trabajo en Microsoft Excel. Por favor, mira esta captura de pantalla que muestra la interfaz que Microsoft Excel proporciona para especificar estas contraseñas.

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **Verificar contraseña para modificar usando Aspose.Cells**

Los siguientes códigos de muestra cargan el archivo de Excel fuente. Tiene una contraseña para abrir como 1234 y una contraseña para modificar como 5678. El código primero verifica si 567 es la contraseña correcta para modificar y devuelve falso, luego verifica si 5678 es la contraseña para modificar y devuelve verdadero.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckPasswordToModify-CheckPasswordToModifyUsingAsposeCells.cs" >}}

### **Salida de la consola**

Aquí está la salida de la consola del código de muestra anterior después de cargar el archivo de Excel fuente.

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
