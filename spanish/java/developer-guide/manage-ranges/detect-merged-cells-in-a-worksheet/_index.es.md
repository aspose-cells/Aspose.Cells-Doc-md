---
title: Detectar fusionado Cells en una hoja de trabajo
type: docs
weight: 3000
url: /es/java/detect-merged-cells-in-a-worksheet/
---
{{% alert color="primary" %}}

En Microsoft Excel, se pueden combinar varias celdas en una sola. Esto se usa a menudo para crear tablas complejas o para crear una celda que contiene un encabezado que abarca varias columnas.

Aspose.Cells le permite identificar áreas de celdas combinadas en una hoja de trabajo. También puedes separarlos. Este artículo proporciona las líneas de código más simples para realizar la tarea usando Aspose.Cells.

Este artículo proporciona instrucciones compactas sobre cómo encontrar y luego deshacer la combinación de celdas en una hoja de trabajo.

{{% /alert %}}

## **Demostración**

 Este ejemplo utiliza una plantilla Microsoft archivo de Excel llamado**MergeTrial**. Tiene algunas áreas de celdas fusionadas en una hoja también llamada Merge Trial.

**El archivo de plantilla**

![todo:imagen_alternativa_texto](detect-merged-cells-in-a-worksheet_1.png)

 Aspose.Cells proporciona el[**Cells.getMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MergedCells)método que se utiliza para obtener una ArrayList de áreas de celdas combinadas.

Cuando se ejecuta el siguiente código, borra el contenido de la hoja y elimina todas las áreas de celda antes de guardar el archivo nuevamente.

**El archivo de salida**

![todo:imagen_alternativa_texto](detect-merged-cells-in-a-worksheet_2.png)

## **Ejemplo de código**

Consulte el siguiente código de ejemplo para saber cómo identificar áreas de celdas combinadas en una hoja de trabajo y deshacerlas.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectMergedCells-DetectMergedCells.java" >}}

## **Artículos relacionados**

- [Combinar y dividir celdas](/cells/es/java/merging-and-unmerging-cells/).
