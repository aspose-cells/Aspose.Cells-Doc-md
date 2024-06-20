---
title: Cómo crear un gráfico de Gantt
linktitle: Cómo crear un gráfico de Gantt
type: docs
weight: 72
url: /es/net/how-to-create-gantt-chart/
description: Cómo crear un gráfico de Gantt en Aspose.Cells.
keywords: crear/insertar Gráfico Gantt en Excel Aspose
---
## Qué es un gráfico Gantt

Un gráfico Gantt te ayuda a programar las tareas de tu proyecto y luego te ayuda a realizar un seguimiento de tu progreso.

## Agregar un gráfico Gantt en Excel

¿Necesitas mostrar el estado de un simple cronograma de proyecto con un gráfico Gantt? Aunque Excel no tiene un tipo de gráfico Gantt predefinido, puedes simular uno personalizando un gráfico de barras apiladas para mostrar las fechas de inicio y finalización de las tareas, como este:

![todo:image_alt_text](00.png)

![todo:image_alt_text](0.png)

## Cómo crear

- Selecciona los datos que quieres graficar. En nuestro ejemplo, eso sería B1:B7, y luego inserta un gráfico **de barras apiladas**.

![todo:image_alt_text](1.png)

- Selecciona el gráfico, **Seleccionar datos** -> **Agregar**, establece el **Nombre de la serie** y los **Valores de la serie** según lo siguiente

![todo:image_alt_text](2.png)

- Selecciona el gráfico, Edita las **Etiquetas del eje horizontal (categorías)**

![todo:image_alt_text](3.png)

- **Formato del Eje** Y, selecciona **Categorías en orden inverso**
- Selecciona la **Serie Azul** y conifgura el **Relleno->Sin Relleno**
- **Formato del Eje** X, establece el **Mínimo y Máximo**(1/5/2019:43470,1/30/2019:43494)

![todo:image_alt_text](4.png)

- **Agregar etiquetas de datos** para el gráfico
Ahora tienes un gráfico de Gantt.

## Agregar gráfico de Gantt en Aspose.Cells

El siguiente código de ejemplo crea un gráfico de Gantt abriendo un [archivo de ejemplo](muestra.xlsx)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-gantt-chart.cs" >}}

Obtendrás un archivo similar a [archivo de resultado](result.xlsx). En el archivo, verás lo siguiente:

![todo:image_alt_text](5.png)

