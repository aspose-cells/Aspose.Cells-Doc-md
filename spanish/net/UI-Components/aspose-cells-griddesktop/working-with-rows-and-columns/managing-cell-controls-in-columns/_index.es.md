---
title: Gestión de controles Cell en columnas
type: docs
weight: 100
url: /es/net/managing-cell-controls-in-columns/
---
{{% alert color="primary" %}} 

Este tema analiza algunos conceptos importantes sobre la administración de controles de celda en columnas mediante Aspose.Cells.GridDesktop API. Explicaremos cómo pueden los desarrolladores acceder, modificar y eliminar controles de celda de las columnas de sus hojas de trabajo. Echémosle un vistazo.

{{% /alert %}} 
## **Acceso a los controles Cell**
 Para acceder y modificar un control de celda existente en la columna, los desarrolladores pueden usar la propiedad CellControl de un**Aspose.Cells.GridDesktop.Data.GridColumn** . Una vez que se accede a un control de celda, los desarrolladores pueden modificar sus propiedades en tiempo de ejecución. Por ejemplo, en el ejemplo que se muestra a continuación, hemos accedido a un**Caja** control celular de un determinado**Aspose.Cells.GridDesktop.Data.GridColumn** y modificó su propiedad Checked.

**IMPORTANTE:** La propiedad CellControl proporciona un control de celda en forma de**CellControl**objeto. Entonces, si necesita acceder a un tipo específico de control de celda, digamos**Caja** entonces tendrás que encasillar el**CellControl** oponerse a**Caja** clase.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-AccessCheckbox.cs" >}}
## **Extracción de los controles Cell**
 Para eliminar un control de celda existente, los desarrolladores simplemente pueden acceder a la hoja de trabajo deseada y luego**Remover** el control de celda de la columna específica usando el**RemoveCellControl** método de**Aspose.Cells.GridDesktop.Data.GridColumn**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-RemoveCheckbox.cs" >}}

{{% alert color="primary" %}} 

 Cada columna en el**columnas** colección de la**Hoja de cálculo** está representado por una instancia de**Aspose.Cells.GridDesktop.Data.GridColumn** clase.

{{% /alert %}}
