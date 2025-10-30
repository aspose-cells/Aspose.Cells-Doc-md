---
title: Optimización del uso de memoria al trabajar con archivos grandes que contienen conjuntos de datos extensos
type: docs
weight: 110
url: /es/nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

Cuando se construye un libro con grandes conjuntos de datos o se lee un archivo grande de Microsoft Excel, la cantidad total de RAM que utilizará el proceso siempre es una preocupación. Existen medidas que se pueden adaptar para enfrentar el desafío. Aspose.Cells proporciona algunas opciones y llamadas de API relevantes para reducir y optimizar el uso de memoria, lo que puede ayudar al proceso a trabajar de manera más eficiente y rápida.

Utilice la opción [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) para optimizar el uso de memoria para los datos de las celdas y así disminuir el costo total de memoria. Al construir un conjunto de datos grande para las celdas, puede ahorrar una cierta cantidad de memoria en comparación con el uso de la configuración predeterminada [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/).

{{% /alert %}}

## **Optimización de memoria**

El siguiente ejemplo muestra cómo optimizar el uso de memoria al trabajar con grandes cantidades de datos en Aspose.Cells for Node.js via C++.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "OptimizingMemory.js" >}}

## **Precaución**

La opción predeterminada, [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) se aplica a todas las versiones. Para algunas situaciones, como la creación de un libro de trabajo con un gran conjunto de datos para celdas, la opción [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) puede optimizar el uso de memoria y disminuir el costo de memoria para la aplicación. Sin embargo, esta opción puede degradar el rendimiento en algunos casos especiales como sigue.

1. **Acceso a celdas de forma aleatoria y repetida**: La secuencia más eficiente para acceder a la colección de celdas es celda por celda en una fila, y luego fila por fila. Especialmente, si accede a filas/celdas mediante el Enumerador adquirido de [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells/), [**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection) y [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row), el rendimiento será maximizado con [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/).
1. **Inserción y eliminación de celdas y filas**: Tenga en cuenta que si hay muchas operaciones de inserción/eliminación para Celdas/Filas, la degradación del rendimiento será notable para el modo [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) en comparación con el modo [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) .
1. **Operación en diferentes tipos de celdas**: Si la mayoría de las celdas contienen valores de cadena o fórmulas, el costo de memoria será el mismo que el modo [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) pero si hay muchas celdas vacías, o los valores de las celdas son numéricos, booleanos, etc., la opción [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) dará un mejor rendimiento.

{{< app/cells/assistant language="nodejs-cpp" >}}
