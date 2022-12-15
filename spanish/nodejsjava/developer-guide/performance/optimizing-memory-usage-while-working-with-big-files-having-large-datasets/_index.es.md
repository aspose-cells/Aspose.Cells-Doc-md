---
title: Optimización del uso de la memoria mientras se trabaja con archivos grandes que tienen grandes conjuntos de datos
type: docs
weight: 110
url: /es/nodejs-java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---
{{% alert color="primary" %}}

Al crear un libro de trabajo con grandes conjuntos de datos, o al leer un gran archivo de Excel Microsoft, la cantidad total de RAM que necesitará el proceso siempre es una preocupación. Hay medidas que se pueden adaptar para hacer frente al desafío. Aspose.Cells proporciona algunas opciones relevantes y API llamadas para reducir, reducir y optimizar el uso de la memoria. Además, puede ayudar a que el proceso funcione de manera más eficiente y se ejecute más rápido.

 Usar[**Configuración de memoria.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) Opción para optimizar la memoria utilizada para los datos de las celdas para disminuir el costo total de la memoria. Al crear un gran conjunto de datos para celdas, puede ahorrar una cierta cantidad de memoria en comparación con el uso de la configuración predeterminada[**AjusteMemoria.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL).

{{% /alert %}}

## **Optimización de la memoria**

El siguiente ejemplo muestra cómo optimizar el uso de la memoria mientras se trabaja con datos de gran tamaño en Aspose.Cells for Node.js via Java.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-nodejs-optimize-memory-usage-while-working-with-large-data.java" >}}

## **Precaución**

 La opción por defecto,[**AjusteMemoria.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)se aplica para todas las versiones. Para algunas situaciones, como crear un libro de trabajo con un gran conjunto de datos para celdas, el[**Configuración de memoria.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)La opción puede optimizar el uso de la memoria y disminuir el costo de la memoria para la aplicación. Sin embargo, esta opción puede degradar el rendimiento en algunos casos especiales, como el siguiente.

1. **Acceso al Cells de forma aleatoria y repetida** : La secuencia más eficiente para acceder a la colección de celdas es celda por celda en una fila y luego fila por fila. Especialmente, si accede a filas/celdas por el Enumerador adquirido de[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), [**RowCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/RowCollection) y[**Fila**](https://reference.aspose.com/cells/java/com.aspose.cells/Row) , el rendimiento se maximizaría con[**Configuración de memoria.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE).
1. **Inserción y eliminación de Cells y filas** : Tenga en cuenta que si hay muchas operaciones de inserción/eliminación para Cells/Rows, la degradación del rendimiento será notable para[**Configuración de memoria.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) modo en comparación con el[**AjusteMemoria.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)modo.
1. **Operando en diferentes tipos Cell** : Si la mayoría de las celdas contienen valores de cadena o fórmulas, el costo de memoria será el mismo que[**AjusteMemoria.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)pero si hay muchas celdas vacías, o los valores de las celdas son numéricos, booleanos, etc., el[**Configuración de memoria.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)opción dará un mejor rendimiento.

