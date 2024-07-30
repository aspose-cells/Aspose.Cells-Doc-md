---
title: Detectar Celdas Fusionadas en una Hoja de Trabajo
type: docs
weight: 3000
url: /es/java/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

En Microsoft Excel, varias celdas pueden fusionarse en una. Esto se usa a menudo para crear tablas complejas o para crear una celda que tenga un encabezado que abarque varias columnas.

Aspose.Cells te permite identificar áreas de celdas fusionadas en una hoja de trabajo. También puedes deshacer la fusión. Este artículo proporciona las líneas de código más simples para realizar la tarea usando Aspose.Cells.

Este artículo proporciona instrucciones compactas sobre cómo encontrar y luego deshacer la fusión de celdas en una hoja de trabajo.

{{% /alert %}}

## **Demostración**

Este ejemplo utiliza un archivo plantilla de Microsoft Excel llamado **MergeTrial**. Tiene algunas áreas de celdas fusionadas en una hoja también llamada Merge Trial.

**El archivo de plantilla**

![todo:image_alt_text](detect-merged-cells-in-a-worksheet_1.png)

Aspose.Cells proporciona el método [**Cells.getMergedCells()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells/#getMergedCells--) que se utiliza para obtener todas las celdas combinadas.

Cuando se ejecuta el código a continuación, se borra el contenido de la hoja y se deshacen todas las áreas de celdas fusionadas antes de guardar el archivo nuevamente.

**El Archivo de Salida**

![todo:image_alt_text](detect-merged-cells-in-a-worksheet_2.png)

## **Ejemplo de Código**

Por favor, vea el siguiente código de muestra para encontrar cómo identificar áreas de celdas fusionadas en una hoja de trabajo y deshacer la fusión de las mismas.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectMergedCells-DetectMergedCells.java" >}}

## **Artículos relacionados**

- [Combinar y dividir celdas](/cells/es/java/combinar-y-dividir-celdas/).
