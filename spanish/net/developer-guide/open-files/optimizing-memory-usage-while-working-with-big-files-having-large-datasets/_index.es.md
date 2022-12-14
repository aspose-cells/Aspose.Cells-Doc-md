---
title: Optimización del uso de la memoria mientras se trabaja con archivos grandes que tienen grandes conjuntos de datos
type: docs
weight: 180
url: /es/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---
{{% alert color="primary" %}}

Al crear un libro de trabajo con grandes conjuntos de datos, o al leer un gran archivo de Excel Microsoft, la cantidad total de RAM que necesitará el proceso siempre es una preocupación. Hay medidas que se pueden adaptar para hacer frente al desafío. Aspose.Cells proporciona algunas opciones relevantes y API llamadas para reducir, reducir y optimizar el uso de la memoria. Además, puede ayudar a que el proceso funcione de manera más eficiente y se ejecute más rápido.

 Utilizar el[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) Opción para optimizar el uso de la memoria para los datos de las celdas y disminuir el costo total de la memoria. Al crear un gran conjunto de datos para celdas, puede ahorrar una cierta cantidad de memoria en comparación con el uso de la configuración predeterminada ([**AjusteMemoria.Normal**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)).

{{% /alert %}}

## **Optimización de la memoria**

### **Leer archivos grandes de Excel**

El siguiente ejemplo muestra cómo leer un archivo de Excel grande Microsoft en modo optimizado.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-ReadingLargeExcelFiles-1.cs" >}}

### **Escribir archivos grandes de Excel**

El siguiente ejemplo muestra cómo escribir un conjunto de datos grande en una hoja de trabajo en un modo optimizado.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-WritingLargeExcelFiles-1.cs" >}}

## **Precaución**

 La opción por defecto,[**AjusteMemoria.Normal**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)se aplica para todas las versiones. Para algunas situaciones, como crear un libro de trabajo con un gran conjunto de datos para celdas, el[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)La opción puede optimizar el uso de la memoria y disminuir el costo de la memoria para la aplicación. Sin embargo, esta opción puede degradar el rendimiento en algunos casos especiales, como el siguiente.

1. **Acceso al Cells de forma aleatoria y repetida** : La secuencia más eficiente para acceder a la colección de celdas es celda por celda en una fila y luego fila por fila. Especialmente, si accede a filas/celdas por el Enumerador adquirido de[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), [**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection) y[**Fila**](https://reference.aspose.com/cells/net/aspose.cells/row) , el rendimiento se maximizaría con[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting).
1. **Inserción y eliminación de Cells y filas** : Tenga en cuenta que si hay muchas operaciones de inserción/eliminación para Cells/Rows, la degradación del rendimiento será notable para*MemoriaPreferencia* modo en comparación con el*Normal*modo.
1. **Operando en diferentes tipos Cell** : Si la mayoría de las celdas contienen valores de cadena o fórmulas, el costo de memoria será el mismo que*Normal* pero si hay muchas celdas vacías, o los valores de las celdas son numéricos, booleanos, etc., el[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)opción dará un mejor rendimiento.
