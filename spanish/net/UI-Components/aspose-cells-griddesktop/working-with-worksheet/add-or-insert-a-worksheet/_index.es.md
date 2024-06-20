---
title: Agregar o Insertar una Hoja de Cálculo
type: docs
weight: 20
url: /es/net/aspose-cells-griddesktop/add-or-insert-a-worksheet/
keywords: GridDesktop,insertar,hoja de cálculo,insertar hoja de cálculo
description: Este artículo presenta cómo añadir o insertar una hoja de cálculo en GridDesktop.
---

{{% alert color="primary" %}} 

En este tema, vamos a discutir las técnicas para añadir o insertar hojas de cálculo en un archivo de Excel usando Aspose.Cells.GridDesktop. La diferencia entre añadir e insertar hojas de cálculo es que además, una hoja de cálculo simplemente se añade al final de la colección de hojas de cálculo del archivo de Excel; sin embargo, la inserción significa añadir una hoja de cálculo a una posición específica en la colección de hojas de cálculo.

{{% /alert %}} 
## **Agregando una hoja de cálculo**
Para agregar una hoja de cálculo usando Aspose.Cells.GridDesktop, por favor siga los pasos a continuación:

1. Agregar el control Aspose.Cells.GridDesktop a un formulario.
1. Llame al método Add de la colección de hojas de cálculo en el control GridDesktop



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheet.cs" >}}


Muchas versiones sobrecargadas del método Add están disponibles. Usando la versión sobrecargada anterior, por ejemplo, se añade una hoja de cálculo al archivo de Excel con un nombre de hoja predeterminado. Usando otras versiones sobrecargadas del método Add, es posible definir el nombre como se muestra a continuación en el ejemplo.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheetWithName.cs" >}}
## **Insertando una hoja de cálculo**
Para insertar una hoja de cálculo usando Aspose.Cells.GridDesktop, por favor siga los pasos a continuación:

1. Agregue el control Aspose.Cells.GridDesktop a un formulario.
1. Llame al método Insert de la colección de hojas de cálculo en el control GridDesktop



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-InsertingWorksheet.cs" >}}

{{% alert color="primary" %}} 

IMPORTANTE: Microsoft Excel (97-2003 XLS) admite hojas de Excel con hasta 65,536 filas y 256 columnas. Aspose.Cells.GridDesktop sigue los mismos estándares. En el control Aspose.Cells.GridDesktop, los desarrolladores pueden añadir o insertar hojas de cálculo con más filas y columnas que el límite estándar, pero cuando intenten guardar los datos de la cuadrícula en un archivo de Excel, se generará un error. Esto significa que solo se pueden guardar datos contenidos en las 65,536 filas y 256 columnas en un archivo de Excel XLS utilizando Aspose.Cells.GridDesktop. Si utiliza el formato de archivo XLSX (MS Excel 2007/2010), no hay tal limitación.

{{% /alert %}}
