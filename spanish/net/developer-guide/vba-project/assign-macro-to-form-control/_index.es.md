---
title: Asignar macro al control de formulario
type: docs
weight: 60
url: /es/net/assign-macro-to-form-control/
---
{{% alert color="primary" %}}

 Aspose.Cells le permite asignar un código de macro a un control de formulario como un botón. Por favor use el[**Forma.MarcoNombre**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/macroname) propiedad para asignar un nuevo código de macro a un control de formulario dentro del libro de trabajo.

{{% /alert %}}

El siguiente código de ejemplo crea un nuevo libro, asigna un código de macro a un botón de formulario y guarda el resultado en formato XLSM. Una vez, abrirá el archivo XLSM de salida en Microsoft Excel y verá el siguiente código de macro.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Asignar macro a control de formulario en C#**

Aquí está el código de muestra para generar el archivo XLSM de salida con código macro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AssignMacroToFormControl-1.cs" >}}
