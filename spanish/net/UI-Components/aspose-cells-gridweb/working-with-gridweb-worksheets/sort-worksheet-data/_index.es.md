---
title: Ordenar datos de la hoja de trabajo
type: docs
weight: 80
url: /es/net/sort-worksheet-data/
---
{{% alert color="primary" %}} 

La clasificación es una característica muy valiosa cuando se trata de procesamiento de datos. Los datos desordenados son una molestia para los usuarios cuando buscan información específica. Aspose.Cells.GridWeb admite potentes funciones de clasificación. Este tema trata sobre la clasificación de datos mediante Aspose.Cells.GridWeb API.

{{% /alert %}} 
## **Clasificación de datos**
Aspose.Cells.GridWeb permite a los desarrolladores ordenar los datos horizontal y verticalmente para que los desarrolladores puedan ordenar los datos de arriba a abajo o de izquierda a derecha.
### **De arriba a abajo**
Para ordenar los datos de arriba a abajo:

1. Agregue el control Aspose.Cells.GridWeb a su formulario web.
1. Acceda a la hoja de trabajo que desea ordenar.
1. Ordene el rango de datos en cualquier orden (ascendente o descendente). Asegúrese de seleccionar la orientación de arriba hacia abajo.

El siguiente ejemplo ordena los datos en cuatro columnas de una hoja de trabajo en orden descendente. Solo veinte filas de las cuatro columnas se ordenan de arriba a abajo.

Antes de aplicar el código, la hoja de trabajo contiene datos desordenados.

![todo:imagen_alternativa_texto](sort-worksheet-data_1.png)

Después de ejecutar el código, los datos se ordenan en orden ascendente.

![todo:imagen_alternativa_texto](sort-worksheet-data_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortTopToBottom.cs" >}}
### **De izquierda a derecha**
Para ordenar los datos de izquierda a derecha:

1. Agregue el control Aspose.Cells.GridWeb a su formulario web.
1. Acceda a la hoja de trabajo que desea ordenar.
1. Ordene el rango de datos en cualquier orden (ascendente o descendente). Asegúrese de seleccionar de izquierda a derecha.

El siguiente ejemplo ordena los datos en cuatro filas en orden ascendente. Solo cuatro filas de siete columnas se ordenan de izquierda a derecha.

Antes de aplicar el código, la hoja de trabajo contiene datos desordenados.

![todo:imagen_alternativa_texto](sort-worksheet-data_3.png)

Después de ejecutar el código, los datos se ordenan en orden ascendente.

![todo:imagen_alternativa_texto](sort-worksheet-data_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortLeftToRight.cs" >}}

{{% alert color="primary" %}} 

IMPORTANTE: Los ejemplos anteriores demuestran la clasificación de datos sobre la base de una columna (de arriba a abajo) o una fila (de izquierda a derecha). Aspose.Cells. GridWeb también puede ordenar los datos según más de una columna o fila. Para hacerlo, pase una matriz de índices de columna o fila al método Sort. También se admite la clasificación de tipos de datos híbridos.

{{% /alert %}}
