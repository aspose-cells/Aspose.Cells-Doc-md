---
title: Modificación de VBA o código de macro usando Aspose.Cells
type: docs
weight: 90
url: /es/java/modifying-vba-or-macro-code-using-aspose-cells/
---
{{% alert color="primary" %}} 

Puede modificar VBA o código de macro usando Aspose.Cells. Aspose.Cells ha agregado las siguientes clases para leer y modificar el proyecto de VBA en el archivo de Excel.

- Proyecto Vba
- VbaModuleCollection
- Módulo Vba

Este artículo le mostrará cómo cambiar el código VBA o macro dentro del archivo fuente de Excel usando Aspose.Cells.

{{% /alert %}} 
## **Ejemplo**
El siguiente código de muestra carga el archivo fuente de Excel que tiene un código VBA o macro siguiente dentro de él.

{{< highlight "java" >}}

 Sub Button1_Click()

MsgBox "This is test message."

End Sub

{{< /highlight >}}

Después de la ejecución del código de muestra Aspose.Cells, el código VBA o Macro se modificará de esta manera

{{< highlight "java" >}}

 Sub Button1_Click()

MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

 Puedes descargar el[archivo fuente de Excel](5472596.xlsm) y el[archivo de salida de Excel](5472597.xlsm) de los enlaces dados.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyVBAorMacroCode-ModifyVBAorMacroCode.java" >}}






