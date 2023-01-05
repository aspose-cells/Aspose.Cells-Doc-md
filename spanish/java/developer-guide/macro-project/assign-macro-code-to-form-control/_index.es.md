---
title: Asignar código de macro al control de formulario
type: docs
weight: 400
url: /es/java/assign-macro-code-to-form-control/
---
{{% alert color="primary" %}} 

 Aspose.Cells le permite asignar un código de macro a un control de formulario como un botón. Por favor use el[ColecciónFormas.addShape()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape\(int,%20int,%20int,%20int,%20int,%20int,%20int\)) para asignar un nuevo código de macro a un control de formulario dentro del libro de trabajo.

{{% /alert %}} 
## **Asignación de código de macro a control de formulario usando Aspose.Cells**
El siguiente código de ejemplo crea un nuevo libro de trabajo, asigna un código de macro a un botón de formulario y guarda el resultado en el formato XLSM. Una vez, abrirá el archivo de salida XLSM en Microsoft Excel y verá el siguiente código de macro.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Aquí hay un código de muestra para generar el archivo de salida XLSM con código de macro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AssignMacroToFormControl-AssignMacroToFormControl.java" >}}
