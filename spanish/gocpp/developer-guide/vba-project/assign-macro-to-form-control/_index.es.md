---
title: Asignar macro al control de formulario con Golang vía C++
linktitle: Asigna Macro a Control de Formulario
type: docs
weight: 60
url: /es/go-cpp/assign-macro-to-form-control/
description: Aprende cómo asignar un código Macro a un Control de formulario como un botón usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells te permite asignar un Código de Macro a un Control de Formulario como un Botón. Por favor utiliza la propiedad [**Shape.GetMacroName()**](https://reference.aspose.com/cells/go-cpp/shape/getmacroname/) para asignar un nuevo Código de Macro a un Control de Formulario dentro del libro.

{{% /alert %}}

El siguiente ejemplo de código crea un nuevo libro de trabajo, asigna un Código Macro a un Botón de formulario y guarda el resultado en formato XLSM. Una vez que abres el archivo XLSM en Microsoft Excel, verás el siguiente código macro.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Asignar Macro a Control de formulario en C++**

Aquí está el código de muestra para generar el archivo de salida XLSM con Código de Macro.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AssignMacroToFormControl.go" >}}
