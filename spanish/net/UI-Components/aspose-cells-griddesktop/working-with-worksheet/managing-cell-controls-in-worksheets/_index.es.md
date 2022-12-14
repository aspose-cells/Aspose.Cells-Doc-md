---
title: Gestión de controles Cell en hojas de trabajo
type: docs
weight: 130
url: /es/net/managing-cell-controls-in-worksheets/
---
{{% alert color="primary" %}} 

Este tema analiza algunos conceptos importantes sobre la administración de controles de celda mediante API de Aspose.Cells.GridDesktop. Explicaremos cómo pueden los desarrolladores acceder, modificar y eliminar controles de celda de sus hojas de trabajo. Echémosle un vistazo.

{{% /alert %}} 
## **Acceso a los controles Cell**
 Para acceder y modificar un control de celda existente en la hoja de trabajo, los desarrolladores pueden acceder a un control de celda específico desde el**Control S** colección de la**Hoja de cálculo** especificando la celda (utilizando el nombre de celda o su ubicación en términos de números de fila y columna) en la que se muestra el control de celda. Una vez que se accede a un control de celda, los desarrolladores pueden modificar sus propiedades en tiempo de ejecución. Por ejemplo, en el ejemplo que se muestra a continuación, hemos accedido a un**Caja** control celular desde el**Hoja de cálculo** y modificó su propiedad Checked.

**IMPORTANTE:** **Control S** colección contiene todo tipo de controles de celda en forma de**CellControl** objetos. Entonces, si necesita acceder a un tipo específico de control de celda, digamos**Caja** entonces tendrás que encasillar el**CellControl** oponerse a**Caja** clase.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-AccessCheckbox.cs" >}}
## **Extracción de los controles Cell**
 Para eliminar un control de celda existente, los desarrolladores simplemente pueden acceder a la hoja de trabajo deseada y luego**Remover** el control celular desde el**Control S** colección de la**Hoja de cálculo** especificando la celda (usando su nombre o número de fila y columna) que contiene el control de celda.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-RemoveCheckbox.cs" >}}
