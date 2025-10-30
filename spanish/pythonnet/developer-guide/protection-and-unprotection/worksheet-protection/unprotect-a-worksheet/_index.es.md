---
title: Desproteger una hoja de cálculo
type: docs
weight: 20
url: /es/python-net/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

¿Se necesita eliminar la protección de una hoja protegida en tiempo de ejecución para hacer algunos cambios en el archivo? Esto se puede hacer fácilmente con Aspose.Cells para Python via .NET.

{{% /alert %}}

## **Desproteger una Hoja de Cálculo**

### **Usar Microsoft Excel**

Para quitar la protección de una hoja de cálculo:

Desde el menú **Herramientas**, selecciona **Proteger** seguido de **Desproteger hoja**. La protección se quitará a menos que la hoja de cálculo esté protegida con contraseña. En este caso, aparecerá un cuadro de diálogo solicitando la contraseña. Introduce la contraseña y la hoja de cálculo quedará desprotegida.

### **Desproteger una hoja protegida sencilla usando Aspose.Cells para Python via .NET**

Una hoja de cálculo puede desprotegerse llamando al método [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/unprotect) de la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).
Una hoja de cálculo simplemente protegida es aquella que no está protegida con una contraseña. Estas hojas de cálculo pueden desprotegerse llamando al método [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/unprotect) sin pasar un parámetro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-UnprotectingSimplyProtectedWorksheet-1.py" >}}

### **Desproteger una hoja protegida con contraseña usando Aspose.Cells para Python via .NET**

Una hoja de cálculo protegida con contraseña es aquella que está protegida con una contraseña. Estas hojas de cálculo pueden desprotegerse llamando a una versión sobrecargada del método [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/unprotect/) que toma la contraseña como parámetro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-UnprotectingPasswordProtectedWorksheet-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
