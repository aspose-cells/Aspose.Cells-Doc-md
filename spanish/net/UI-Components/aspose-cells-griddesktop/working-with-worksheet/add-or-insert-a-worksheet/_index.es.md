---
title: Agregar o insertar una hoja de trabajo
type: docs
weight: 20
url: /es/net/add-or-insert-a-worksheet/
---
{{% alert color="primary" %}} 

En este tema, discutiremos las técnicas para agregar o insertar hojas de trabajo en un archivo de Excel usando Aspose.Cells.GridDesktop. La diferencia entre agregar e insertar hojas de trabajo es que, además, una hoja de trabajo simplemente se agrega al final de la colección de hojas de trabajo del archivo de Excel; sin embargo, la inserción significa agregar una hoja de trabajo a una posición específica en la colección de hojas de trabajo.

{{% /alert %}} 
## **Agregar una hoja de trabajo**
Para agregar una hoja de trabajo usando Aspose.Cells.GridDesktop, siga los pasos a continuación:

1. Agregue el control Aspose.Cells.GridDesktop a un formulario.
1. Llame al método Add de la colección Worksheet en el control GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheet.cs" >}}


Muchas versiones sobrecargadas del método Add están disponibles. Usando la versión sobrecargada anterior, por ejemplo, se agrega una hoja de trabajo al archivo de Excel con un nombre de hoja predeterminado. Usando otras versiones sobrecargadas del método Add, es posible definir el nombre como se muestra a continuación en el ejemplo.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheetWithName.cs" >}}
## **Insertar una hoja de trabajo**
Para insertar una hoja de trabajo usando Aspose.Cells.GridDesktop, siga los pasos a continuación:

1. Agregue el control Aspose.Cells.GridDesktop a un formulario.
1. Llame al método Insertar de la colección Worksheets en el control GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-InsertingWorksheet.cs" >}}

{{% alert color="primary" %}} 

IMPORTANTE: Microsoft Excel (97-2003 XLS) admite hojas de Excel con hasta 65 536 filas y 256 columnas. Aspose.Cells. GridDesktop sigue los mismos estándares. En el control Aspose.Cells.GridDesktop, los desarrolladores pueden agregar o insertar hojas de trabajo con más filas y columnas que el límite estándar, pero cuando intentan guardar los datos de Grid en un archivo de Excel, se genera una excepción. Significa que solo los datos contenidos en las 65 536 filas y las 256 columnas se pueden guardar en un archivo XLS de Excel usando Aspose.Cells.GridDesktop, si usa el formato de archivo XLSX (MS Excel 2007/2010), no existe tal limitación.

{{% /alert %}}
