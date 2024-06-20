---
title: Asigna Macro a Control de Formulario
type: docs
weight: 60
url: /es/net/assign-macro-to-form-control/
---

{{% alert color="primary" %}}

Aspose.Cells te permite asignar un Código de Macro a un Control de Formulario como un Botón. Por favor utiliza la propiedad [**Shape.MarcoName**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/macroname) para asignar un nuevo Código de Macro a un Control de Formulario dentro del libro.

{{% /alert %}}

El siguiente código de muestra crea un nuevo libro, asigna un Código de Macro a un Botón de Formulario y guarda la salida en formato XLSM. Una vez que abras el archivo XLSM de salida en Microsoft Excel, verás el siguiente código de macro.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Asigna Macro a Control de Formulario en C#**

Aquí está el código de muestra para generar el archivo de salida XLSM con Código de Macro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AssignMacroToFormControl-1.cs" >}}
