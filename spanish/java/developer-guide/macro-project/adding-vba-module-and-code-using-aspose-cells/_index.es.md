---
title: Agregar Módulo y Código VBA usando Aspose.Cells
type: docs
weight: 20
url: /es/java/adding-vba-module-and-code-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells le permite agregar un nuevo Módulo VBA y Código de Macro usando Aspose.Cells. Por favor, use el método [**Workbook.getVbaProject().getModules().add(**)](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#add(com.aspose.cells.Worksheet)) para agregar el nuevo Módulo VBA dentro del libro

{{% /alert %}}

## **Agregar Módulo y Código VBA usando Aspose.Cells**

El siguiente código de ejemplo crea un nuevo libro de trabajo y agrega un nuevo módulo de VBA y código de macro, y guarda la salida en formato XLSM. Una vez que abras el archivo de salida XLSM en Microsoft Excel y hagas clic en los comandos del menú **Desarrollador > Visual Basic**, verás un módulo llamado "TestModule" y dentro de él verás el siguiente código de macro.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## Código de Muestra

Aquí hay un código de muestra para generar el archivo de salida XLSM con Módulo VBA y Código de Macro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddVBAModuleAndCode-AddVBAModuleAndCode.java" >}}
