---
title: Gestionar controles de celda en hojas de cálculo
type: docs
weight: 130
url: /es/net/aspose-cells-griddesktop/manage-cell-controls-in-worksheets/
keywords: GridDesktop,control de celda,control,controles
description: Este artículo presenta cómo trabajar con controles de celda en GridDesktop.
---

{{% alert color="primary" %}} 

Este tema discute algunos conceptos importantes sobre la gestión de controles de celda utilizando la API de Aspose.Cells.GridDesktop. Explicaremos cómo puede el desarrollador acceder, modificar y eliminar controles de celda de sus hojas de cálculo. Echemos un vistazo.

{{% /alert %}} 
## **Acceso a los Controles de Celda**
Para acceder y modificar un control de celda existente en la hoja de cálculo, los desarrolladores pueden acceder a un control de celda específico desde la colección **Controles** de la **Hoja de Cálculo** especificando la celda (usando el nombre de la celda o su ubicación en términos de números de fila y columna) en la que se muestra el control de celda. Una vez que se accede a un control de celda, los desarrolladores pueden modificar sus propiedades en tiempo de ejecución. Por ejemplo, en el ejemplo a continuación, hemos accedido a un control de celda de tipo **CheckBox** existente en la **Hoja de Cálculo** y modificamos su propiedad Checked.

**IMPORTANTE:** La colección **Controles** contiene todos los tipos de controles de celda en forma de objetos de tipo **CellControl**. Por lo tanto, si necesita acceder a un tipo específico de control de celda, por ejemplo, **CheckBox**, deberá convertir el objeto **CellControl** a la clase **CheckBox**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-AccessCheckbox.cs" >}}
## **Eliminación de Controles de Celda**
Para eliminar un control de celda existente, los desarrolladores pueden simplemente acceder a la hoja de cálculo deseada y luego eliminar el control de celda de la colección **Controles** de la **Hoja de Cálculo** especificando la celda (usando su nombre o número de fila y columna) que contiene el control de celda.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-RemoveCheckbox.cs" >}}
