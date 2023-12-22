---
title: Cómo crear un diagrama de Gantt
linktitle: Cómo crear un diagrama de Gantt
type: docs
weight: 72
url: /es/net/how-to-create-gantt-chart/
description: Cómo crear un diagrama de Gantt en Aspose.Cells.
keywords: create/insert Gantt Chart Excel Aspose
---
##  ¿Qué es el diagrama de Gantt?

Un diagrama de Gantt le ayuda a programar las tareas de su proyecto y luego le ayuda a realizar un seguimiento de su progreso.

##  Agregar diagrama de Gantt en Excel

¿Necesita mostrar el estado de un cronograma de proyecto simple con un diagrama de Gantt? Aunque Excel no tiene un tipo de diagrama de Gantt predefinido, puede simular uno personalizando un gráfico de barras apiladas para mostrar las fechas de inicio y finalización de las tareas, como este:

![todo:image_alt_text](00.png)

![todo:image_alt_text](0.png)

##  Como crear

-  Seleccione los datos que desea graficar. En nuestro ejemplo, eso es B1:B7, y luego Insertar**Barra apilada** cuadro.

![todo:image_alt_text](1.png)

- Seleccione el gráfico, **Seleccione datos**->**Agregar**, establecer el **Nombre de la serie** y**Valores de serie** como sigue

![todo:image_alt_text](2.png)

-  Seleccione el gráfico, edite el**Etiquetas de eje horizontal (categoría)**

![todo:image_alt_text](3.png)

- **Eje de formato** el eje Y, seleccione**Categorías en orden inverso**
-  Seleccione el**Serie Azul** y establecer el**Rellenar->NO Rellenar**
- **Eje de formato** el eje X, establezca el *Mínimo y Máximo**(5/1/2019:43470,30/1/2019:43494)

![todo:image_alt_text](4.png)

- **Agregar archivos de datos** para el gráfico
Ahora obtienes un diagrama de Gantt.

## Agregar diagrama de Gantt en Aspose.Cells

 El siguiente código de muestra crea un diagrama de Gantt abriendo un[archivo de muestra](sample.xlsx)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-gantt-chart.cs" >}}

 Obtendrá un archivo similar a[archivo de resultados](result.xlsx).En el archivo, verá lo siguiente:

![todo:image_alt_text](5.png)

