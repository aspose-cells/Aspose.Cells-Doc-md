---
title: Ordenar datos de la hoja de cálculo
type: docs
weight: 80
url: /es/net/aspose-cells-gridweb/sort-worksheet-data/
keywords: GridWeb, ordenar
description: Este artículo presenta cómo ordenar datos en GridWeb.
---

{{% alert color="primary" %}} 

Ordenar es una característica muy valiosa cuando se trata de procesamiento de datos. Los datos no ordenados son una molestia para los usuarios al buscar información específica. Aspose.Cells.GridWeb soporta potentes características de ordenación. Este tema discute la ordenación de datos usando la API de Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Ordenar datos**
Aspose.Cells.GridWeb permite a los desarrolladores ordenar datos horizontal y verticalmente para que puedan ordenar datos de arriba abajo o de izquierda a derecha.
### **De arriba abajo**
Para ordenar datos de orientación de arriba abajo:

1. Agrega el control Aspose.Cells.GridWeb a tu Formulario Web.
1. Accede a la hoja de cálculo que deseas ordenar.
1. Ordena el rango de datos en cualquier orden (ascendente o descendente). Asegúrate de seleccionar la orientación de arriba hacia abajo.

El siguiente ejemplo ordena datos en cuatro columnas de una hoja de cálculo en orden descendente. Solo veinte filas de las cuatro columnas se ordenan en orientación de arriba abajo.

Antes de aplicar el código, la hoja de cálculo contiene datos desordenados.

![todo:image_alt_text](sort-worksheet-data_1.png)

Después de ejecutar el código, los datos se ordenan en orden ascendente.

![todo:image_alt_text](sort-worksheet-data_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortTopToBottom.cs" >}}
### **De Izquierda a Derecha**
Para ordenar los datos de izquierda a derecha:

1. Agrega el control Aspose.Cells.GridWeb a tu Formulario Web.
1. Accede a la hoja de cálculo que deseas ordenar.
1. Ordena el rango de datos en cualquier orden (ascendente o descendente). Asegúrate de seleccionar de izquierda a derecha.

El ejemplo a continuación ordena los datos en cuatro filas en orden ascendente. Solo se ordenan cuatro filas de siete columnas de izquierda a derecha.

Antes de aplicar el código, la hoja de cálculo contiene datos desordenados.

![todo:image_alt_text](sort-worksheet-data_3.png)

Después de ejecutar el código, los datos se ordenan en orden ascendente.

![todo:image_alt_text](sort-worksheet-data_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortLeftToRight.cs" >}}

{{% alert color="primary" %}} 

IMPORTANTE: Los ejemplos anteriores demuestran la ordenación de datos en función de una columna (de arriba hacia abajo) o fila (de izquierda a derecha). Aspose.Cells.GridWeb también puede ordenar datos de acuerdo con más de una columna o fila. Para hacerlo, pase una matriz de índices de columnas o filas al método Sort. También se admite la ordenación de tipos de datos híbridos.

{{% /alert %}}
