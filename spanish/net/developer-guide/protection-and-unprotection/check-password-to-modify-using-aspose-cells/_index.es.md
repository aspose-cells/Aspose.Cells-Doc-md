---
title: Verifique la contraseña para modificar usando Aspose.Cells
type: docs
weight: 2400
url: /es/net/check-password-to-modify-using-aspose-cells/
---
{{% alert color="primary" %}}

 A veces, es necesario comprobar si la contraseña proporcionada coincide con la**Contraseña para modificar** programáticamente. Aspose.Cells proporciona el método WorkbookSettings.WriteProtection.ValidatePassword() que puede usar para verificar si la contraseña dada para modificar es correcta o no.

{{% /alert %}}

## **Consultar Contraseña a modificar en Microsoft Excel**

Puedes asignar**Contraseña para abrir** y**Contraseña para modificar** mientras crea sus libros de trabajo en Microsoft Excel. Consulte esta captura de pantalla que muestra la interfaz Microsoft que proporciona Excel para especificar estas contraseñas.

|![todo:imagen_alternativa_texto](check-password-to-modify-using-aspose-cells_1.png)|
|:- |

## **Verifique la contraseña para modificar usando Aspose.Cells**

 Los siguientes códigos de muestra cargan el[Excel fuente](5112232.xlsx) expediente. Tiene una Contraseña para abrir como 1234 y una Contraseña para modificar como 5678. El código primero comprueba si 567 es la Contraseña para modificar correcta y devuelve falso y luego comprueba si 5678 es la Contraseña para modificar y devuelve verdadero.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckPasswordToModify-CheckPasswordToModifyUsingAsposeCells.cs" >}}

### **Salida de consola**

 Aquí está la salida de la consola del código de muestra anterior después de cargar el[Excel fuente](5112232.xlsx) expediente.

{{< highlight "java" >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
