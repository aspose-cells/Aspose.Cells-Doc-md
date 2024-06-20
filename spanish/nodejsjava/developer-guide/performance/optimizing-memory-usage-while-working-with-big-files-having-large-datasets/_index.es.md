---
title: Optimización del uso de memoria al trabajar con archivos grandes que contienen conjuntos de datos extensos
type: docs
weight: 110
url: /es/nodejs-java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

Cuando se construye un libro con grandes conjuntos de datos o se lee un archivo grande de Microsoft Excel, la cantidad total de RAM que utilizará el proceso siempre es una preocupación. Existen medidas que se pueden adaptar para enfrentar el desafío. Aspose.Cells proporciona algunas opciones y llamadas de API relevantes para reducir y optimizar el uso de memoria, lo que puede ayudar al proceso a trabajar de manera más eficiente y rápida.

Utilice la opción [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) para optimizar el uso de memoria para los datos de las celdas y así disminuir el costo total de memoria. Al construir un conjunto de datos grande para las celdas, puede ahorrar una cierta cantidad de memoria en comparación con el uso de la configuración predeterminada [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL).

{{% /alert %}}

## **Optimización de memoria**

El siguiente ejemplo muestra cómo optimizar el uso de memoria al trabajar con grandes conjuntos de datos en Aspose.Cells para Node.js via Java.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-nodejs-optimize-memory-usage-while-working-with-large-data.java" >}}

## **Precaución**

La opción predeterminada, [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL) se aplica a todas las versiones. Para algunas situaciones, como la creación de un libro de trabajo con un gran conjunto de datos para celdas, la opción [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) puede optimizar el uso de memoria y disminuir el costo de memoria para la aplicación. Sin embargo, esta opción puede degradar el rendimiento en algunos casos especiales como sigue.

1. **Acceso a celdas de forma aleatoria y repetida**: La secuencia más eficiente para acceder a la colección de celdas es celda por celda en una fila, y luego fila por fila. Especialmente, si accede a filas/celdas mediante el Enumerador adquirido de [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), [**RowCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/RowCollection) y [**Row**](https://reference.aspose.com/cells/java/com.aspose.cells/Row), el rendimiento será maximizado con [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE).
1. **Inserción y eliminación de celdas y filas**: Tenga en cuenta que si hay muchas operaciones de inserción/eliminación para Celdas/Filas, la degradación del rendimiento será notable para el modo [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) en comparación con el modo [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL) .
1. **Operación en diferentes tipos de celdas**: Si la mayoría de las celdas contienen valores de cadena o fórmulas, el costo de memoria será el mismo que el modo [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL) pero si hay muchas celdas vacías, o los valores de las celdas son numéricos, booleanos, etc., la opción [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) dará un mejor rendimiento.

