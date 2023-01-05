---
title: Desproteger una hoja de trabajo
type: docs
weight: 20
url: /es/net/unprotect-a-worksheet/
---
{{% alert color="primary" %}}

¿Si un desarrollador necesita eliminar la protección de una hoja de trabajo protegida en tiempo de ejecución para que se puedan realizar algunos cambios en el archivo? Esto se puede hacer fácilmente con Aspose.Cells.

{{% /alert %}}

## **Desproteger una hoja de trabajo**

### **Usando Microsoft Excel**

Para eliminar la protección de una hoja de trabajo:

 Desde el**Herramientas** menú, seleccione**Proteccion** seguido por**Desproteger hoja**. La protección se eliminará a menos que la hoja de trabajo esté protegida con contraseña. En este caso, un cuadro de diálogo solicita la contraseña. Ingrese la contraseña y la hoja de trabajo quedará desprotegida entonces.

### **Desprotección de una hoja de trabajo simplemente protegida con Aspose.Cells**

 Una hoja de trabajo se puede desproteger llamando al[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase'[**Desproteger**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index)método.
 Una hoja de trabajo simplemente protegida es aquella que no está protegida con una contraseña. Estas hojas de trabajo se pueden desproteger llamando al[**Desproteger**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index)método sin pasar un parámetro.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingSimplyProtectedWorksheet-1.cs" >}}

### **Desprotección de una hoja de trabajo protegida con contraseña usando Aspose.Cells**

Una hoja de trabajo protegida con contraseña es aquella que está protegida con una contraseña. Estas hojas de trabajo pueden desprotegerse llamando a una versión sobrecargada del[**Desproteger**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/unprotect/methods/1)método que toma la contraseña como parámetro.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingPasswordProtectedWorksheet-1.cs" >}}
