---
title: Combinar y Dividir Celdas
type: docs
weight: 60
url: /es/net/aspose-cells-gridweb/merge-and-unmerge-cells/
keywords: GridWeb, combinar, dividir
description: Este artículo presenta cómo combinar/dividir celdas en GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb tiene una útil característica que permite combinar celdas en una sola celda grande. Este tema describe cómo combinar celdas programáticamente.

{{% /alert %}} 
## **Combinar celdas**
Combinar múltiples celdas en una hoja de cálculo en una sola celda mediante la llamada al método Merge de la colección Cells. Especifique el rango de celdas que se combinará al llamar al método Merge.

{{% alert color="primary" %}} 

Si combina múltiples celdas y cada celda contiene datos, solo se conserva el contenido de la celda superior izquierda en el rango después de la combinación. Los datos en las otras celdas no se pierden. Si deshace la combinación de las celdas, cada celda recupera sus datos.

{{% /alert %}} 

**Cuatro celdas combinadas en una** 

![todo:image_alt_text](merge-and-unmerge-cells_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-MergeCells.cs" >}}
## **Descombinar Celdas**
Para descombinar celdas, use el método UnMerge de la colección Cells que toma los mismos parámetros que el método Merge y realiza la descombinación de celdas.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-UnmergeCells.cs" >}}
