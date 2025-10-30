---
title: Verificar contraseña para modificar usando Aspose.Cells para Python via .NET
type: docs
weight: 2400
url: /es/python-net/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

A veces, necesitas verificar si la contraseña dada coincide con la **Contraseña para modificar** de manera programática. Aspose.Cells para Python via .NET proporciona el método WorkbookSettings.write_protection.validate_password() que puedes usar para verificar si la contraseña para modificar es correcta o no.

{{% /alert %}}

## **Verificar Contraseña para modificar en Microsoft Excel**

Puedes asignar **Contraseña para abrir** y **Contraseña para modificar** al crear tus libros de trabajo en Microsoft Excel. Por favor, mira esta captura de pantalla que muestra la interfaz que Microsoft Excel proporciona para especificar estas contraseñas.

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **Verificar contraseña para modificar usando Aspose.Cells para Python via .NET**

Los siguientes códigos de muestra cargan el archivo de Excel fuente. Tiene una contraseña para abrir como 1234 y una contraseña para modificar como 5678. El código primero verifica si 567 es la contraseña correcta para modificar y devuelve falso, luego verifica si 5678 es la contraseña para modificar y devuelve verdadero.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-CheckPasswordToModifyUsingAsposeCells.py" >}}

### **Salida de la consola**

Aquí está la salida de la consola del código de muestra anterior después de cargar el archivo de Excel fuente.

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
