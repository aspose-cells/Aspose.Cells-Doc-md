---
title: Optimizar el uso de memoria al trabajar con archivos grandes con conjuntos de datos extensos con Golang a través de C++
linktitle: Optimización del uso de memoria
type: docs
weight: 180
url: /es/go-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
description: Aprenda a optimizar el uso de memoria al trabajar con archivos Excel grandes usando Aspose.Cells con Golang a través de C++.
---

{{% alert color="primary" %}}

Al construir una hoja de cálculo con conjuntos de datos grandes, o al leer un archivo grande de Microsoft Excel, la cantidad total de RAM que el proceso utilizará siempre es una preocupación. Hay medidas que se pueden adoptar para hacer frente al desafío. Aspose.Cells proporciona algunas opciones relevantes y llamadas de API para reducir, disminuir y optimizar el uso de memoria. Además, puede ayudar al proceso a trabajar de manera más eficiente y ejecutarse más rápido.

Utilice la opción [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/go-cpp/memorysetting/) para optimizar el uso de memoria para los datos de las celdas y disminuir el costo total de memoria. Al construir un conjunto de datos grande para las celdas, se puede ahorrar una cierta cantidad de memoria en comparación con el uso de la configuración predeterminada ([**MemorySetting.Normal**](https://reference.aspose.com/cells/go-cpp/memorysetting/)).

{{% /alert %}}

## **Optimización de memoria**

### **Lectura de archivos Excel grandes**

El siguiente ejemplo muestra cómo leer un archivo grande de Microsoft Excel en modo optimizado.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OptimizingMemoryUsageWhileWorkingWithBigFilesHavingLargeDatasets.go" >}}
### **Escribiendo Archivos de Excel Grandes**

El siguiente ejemplo muestra cómo escribir un conjunto de datos grande en una hoja de trabajo en modo optimizado.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OptimizingMemoryUsageWhileWorkingWithBigFilesHavingLargeDatasets-1.go" >}}
## **Precaución**

La opción predeterminada, [**MemorySetting.Normal**](https://reference.aspose.com/cells/go-cpp/memorysetting/) se aplica para todas las versiones. Para algunas situaciones, como construir una hoja de cálculo con un conjunto de datos grande para celdas, la opción [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/go-cpp/memorysetting/) puede optimizar el uso de memoria y disminuir el costo de memoria para la aplicación. Sin embargo, esta opción puede degradar el rendimiento en algunos casos especiales como los siguientes.

1. **Acceso a celdas de forma aleatoria y repetida**: La secuencia más eficiente para acceder a la colección de celdas es celda por celda en una fila, y luego fila por fila. Especialmente, si accede a filas/celdas mediante el Enumerador adquirido de [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/), [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/) y [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/), el rendimiento será maximizado con [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/).
1. **Insertar y Eliminar Celdas y Filas**: Tenga en cuenta que si hay muchas operaciones de inserción/eliminación de Celdas/Filas, la degradación del rendimiento será notable para el modo de *Preferencia de Memoria* en comparación con el modo *Normal*.
1. **Operando en Diferentes Tipos de Celda**: Si la mayoría de las celdas contienen valores de texto o fórmulas, el costo de memoria será el mismo que en el modo *Normal*, pero si hay muchas celdas vacías, o los valores de las celdas son numéricos, bool, etc., la opción [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/go-cpp/memorysetting/) dará mejor rendimiento.
