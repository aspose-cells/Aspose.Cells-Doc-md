---
title: Desproteger una hoja de cálculo
type: docs
weight: 20
url: /es/net/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

Si un desarrollador necesita quitar la protección de una hoja de cálculo protegida en tiempo de ejecución para poder realizar algunos cambios en el archivo, esto se puede hacer fácilmente con Aspose.Cells.

{{% /alert %}}

## **Desproteger una Hoja de Cálculo**

### **Usar Microsoft Excel**

Para quitar la protección de una hoja de cálculo:

Desde el menú **Herramientas**, selecciona **Proteger** seguido de **Desproteger hoja**. La protección se quitará a menos que la hoja de cálculo esté protegida con contraseña. En este caso, aparecerá un cuadro de diálogo solicitando la contraseña. Introduce la contraseña y la hoja de cálculo quedará desprotegida.

### **Desproteger una hoja de cálculo simplemente protegida utilizando Aspose.Cells**

Una hoja de cálculo puede desprotegerse llamando al método [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index) de la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).
Una hoja de cálculo simplemente protegida es aquella que no está protegida con una contraseña. Estas hojas de cálculo pueden desprotegerse llamando al método [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index) sin pasar un parámetro.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingSimplyProtectedWorksheet-1.cs" >}}

### **Desproteger una hoja de cálculo protegida con contraseña utilizando Aspose.Cells**

Una hoja de cálculo protegida con contraseña es aquella que está protegida con una contraseña. Estas hojas de cálculo pueden desprotegerse llamando a una versión sobrecargada del método [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/unprotect/methods/1) que toma la contraseña como parámetro.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingPasswordProtectedWorksheet-1.cs" >}}
