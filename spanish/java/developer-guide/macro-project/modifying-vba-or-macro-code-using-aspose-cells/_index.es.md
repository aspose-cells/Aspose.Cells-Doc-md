---
title: Modificar el Código VBA o Macro utilizando Aspose.Cells
type: docs
weight: 90
url: /es/java/modifying-vba-or-macro-code-using-aspose-cells/
---

{{% alert color="primary" %}} 

Puede modificar el Código VBA o Macro utilizando Aspose.Cells. Aspose.Cells ha agregado las siguientes clases para leer y modificar el proyecto VBA en el archivo de Excel.

- VbaProject
- VbaModuleCollection
- VbaModule

Este artículo te mostrará cómo cambiar el código de VBA o macro dentro del archivo de Excel fuente utilizando Aspose.Cells.

{{% /alert %}} 
## **Ejemplo**
El siguiente código de ejemplo carga el archivo de Excel fuente que contiene el siguiente código de VBA o macro.

{{< highlight java >}}

 Sub Button1_Click()

MsgBox "This is test message."

End Sub

{{< /highlight >}}

Después de la ejecución del código de ejemplo de Aspose.Cells, el código de VBA o macro será modificado de la siguiente manera

{{< highlight java >}}

 Sub Button1_Click()

MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

Puedes descargar el [archivo de Excel fuente](5472596.xlsm) y el [archivo de Excel de salida](5472597.xlsm) desde los enlaces proporcionados.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyVBAorMacroCode-ModifyVBAorMacroCode.java" >}}






