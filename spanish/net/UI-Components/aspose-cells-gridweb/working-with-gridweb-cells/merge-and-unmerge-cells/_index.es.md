---
title: Combinar y separar Cells
type: docs
weight: 60
url: /es/net/merge-and-unmerge-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb tiene una función de utilidad útil que le permite combinar celdas en una celda grande. Este tema describe cómo fusionar celdas mediante programación.

{{% /alert %}} 
## **Fusionando Cells**
Combine varias celdas en una hoja de trabajo en una sola celda llamando al método Merge de la colección Cells. Especifique el rango de celdas que se combinarán al llamar al método Merge.

{{% alert color="primary" %}} 

Si combina varias celdas y cada celda contiene datos, solo se conserva el contenido de la celda superior izquierda del rango después de la combinación. Los datos en las otras celdas no se pierden. Si separa las celdas, cada celda recupera sus datos.

{{% /alert %}} 

**Cuatro celdas fusionadas en una** 

![todo:imagen_alternativa_texto](merge-and-unmerge-cells_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-MergeCells.cs" >}}
## **Separación Cells**
Para separar celdas, use el método UnMerge de la colección Cells que toma los mismos parámetros que el método Merge y realiza la separación de celdas.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-UnmergeCells.cs" >}}
