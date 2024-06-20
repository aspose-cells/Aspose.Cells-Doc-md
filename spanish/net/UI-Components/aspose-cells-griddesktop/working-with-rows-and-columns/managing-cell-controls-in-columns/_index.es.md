---
title: Gestión de Controles de Celda en Columnas
type: docs
weight: 100
url: /es/net/aspose-cells-griddesktop/manage-cell-controls-in-columns/
keywords: GridDesktop, controles, control
description: Este artículo presenta cómo establecer controles en columna GridDesktop.
---

{{% alert color="primary" %}} 

Este tema discute algunos conceptos importantes sobre la gestión de controles de celda en columnas utilizando la API Aspose.Cells.GridDesktop. Explicaremos cómo los desarrolladores pueden acceder, modificar y eliminar controles de celda de las columnas de sus hojas de cálculo. Echemos un vistazo.

{{% /alert %}} 
## **Acceso a los Controles de Celda**
Para acceder y modificar un control de celda existente en la columna, los desarrolladores pueden usar la propiedad CellControl de un **Aspose.Cells.GridDesktop.Data.GridColumn**. Una vez que se accede a un control de celda, los desarrolladores pueden modificar sus propiedades en tiempo de ejecución. Por ejemplo, en el ejemplo dado a continuación, hemos accedido a un control de celda **CheckBox** existente de una **Aspose.Cells.GridDesktop.Data.GridColumn** específica y modificado su propiedad Checked.

**IMPORTANTE:** La propiedad CellControl proporciona un control de celda en forma de un objeto **CellControl**. Por lo tanto, si necesita acceder a un tipo específico de control de celda, por ejemplo **CheckBox**, entonces tendrá que convertir el objeto **CellControl** a la clase **CheckBox**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-AccessCheckbox.cs" >}}
## **Eliminación de Controles de Celda**
Para eliminar un control de celda existente, los desarrolladores pueden simplemente acceder a una hoja de cálculo deseada y luego **Eliminar** el control de celda de la columna específica usando el método **RemoveCellControl** de **Aspose.Cells.GridDesktop.Data.GridColumn**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-RemoveCheckbox.cs" >}}

{{% alert color="primary" %}} 

Cada columna en la colección **Columns** de la **Hoja de cálculo** está representada por una instancia de la clase **Aspose.Cells.GridDesktop.Data.GridColumn**.

{{% /alert %}}
