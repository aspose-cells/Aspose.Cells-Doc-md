---
title: Agregar módulo y código VBA usando Aspose.Cells
type: docs
weight: 20
url: /es/java/adding-vba-module-and-code-using-aspose-cells/
---
{{% alert color="primary" %}}

 Aspose.Cells le permite agregar un nuevo módulo VBA y código de macro usando Aspose.Cells. Utilice el[**Libro de trabajo.getVbaProject().getModules().add(**)](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#add(com.aspose.cells.Worksheet)) método para agregar el nuevo Módulo VBA dentro del libro de trabajo

{{% /alert %}}

## **Agregar módulo y código VBA usando Aspose.Cells**

El siguiente código de muestra crea un nuevo libro de trabajo y agrega un nuevo módulo VBA y código de macro y guarda la salida en el formato XLSM. Una vez, abrirá el archivo de salida XLSM en Microsoft Excel y haga clic en el**Desarrollador > Visual Basic** comandos de menú, verá un módulo llamado "TestModule" y dentro de él, verá el siguiente código de macro.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## Código de muestra

Aquí hay un código de muestra para generar el archivo de salida XLSM con el módulo VBA y el código de macro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddVBAModuleAndCode-AddVBAModuleAndCode.java" >}}
