---
title: Asigna Macro a Control de Formulario
type: docs
weight: 60
url: /es/python-net/assign-macro-to-form-control/
---

{{% alert color="primary" %}}

Aspose.Cells para Python via .NET te permite asignar un código Macro a un Control de Formulario como un botón. Por favor, usa la propiedad [**Shape.macro_name**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/macro_name) para asignar un nuevo código Macro a un Control de formulario dentro del libro de trabajo.

{{% /alert %}}

El siguiente código de muestra crea un nuevo libro, asigna un Código de Macro a un Botón de Formulario y guarda la salida en formato XLSM. Una vez que abras el archivo XLSM de salida en Microsoft Excel, verás el siguiente código de macro.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Asignar Macro a Control de Formulario en Python**

Aquí está el código de muestra para generar el archivo de salida XLSM con Código de Macro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-AssignMacroToFormControl-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
