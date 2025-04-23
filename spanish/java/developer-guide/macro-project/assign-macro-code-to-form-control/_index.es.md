---
title: Asignar Código de Macro a un Control de Formulario
type: docs
weight: 400
url: /es/java/assign-macro-code-to-form-control/
---

{{% alert color="primary" %}} 

Aspose.Cells te permite asignar un código Macro a un Control de formulario como un botón. Por favor, usa el método [ShapeCollection.addShape()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape-int-int-int-int-int-int-int-) para asignar un nuevo código Macro a un control de formulario dentro del libro de trabajo.

{{% /alert %}} 
## **Asignación de Código de Macro a un Control de Formulario usando Aspose.Cells**
El siguiente código de muestra crea un nuevo libro, asigna un Código de Macro a un Botón de Formulario y guarda la salida en formato XLSM. Una vez que abra el archivo XLSM de salida en Microsoft Excel, verá el siguiente código de macro.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Aquí hay un código de ejemplo para generar el archivo XLSM de salida con Código de Macro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AssignMacroToFormControl-AssignMacroToFormControl.java" >}}
{{< app/cells/assistant language="java" >}}
