---
title: Convertir gráfico a imagen localizada
linktitle: Establecer región localizada
type: docs
weight: 50
url: /es/net/convert-chart-to-localized-image/
alias: [/net/how-to-set-globalization-configuration-for-chart/]
---
{{% alert color="primary" %}}

En este tema, le mostraremos cómo convertir un gráfico en una imagen localizada, sabrá cómo establecer una región localizada para un gráfico.

{{% /alert %}}

##  **Guión**

¿En qué escenario necesitaríamos establecer una región localizada para un gráfico?

 Cuando abre un archivo xlsx con un gráfico en Excel, en este caso, suponga que lo abre con una Configuración regional en español en Excel, puede ver los elementos en el área del gráfico, como el Título del gráfico, Lengend, están traducidos al español. Pero cuando guarda este cuadro como una imagen con Aspose.Cells, puede encontrar el siguiente problema:

**![Problema global](Problema global.png)**

En este escenario, la longitud del gráfico en la imagen de salida no es la misma que en Excel, se muestran en inglés de forma predeterminada. Ahora puede resolver este problema configurando una región localizada para el gráfico. Con la configuración correcta, los siguientes elementos se representarán de acuerdo con su configuración de localización.

##  **Elementos compatibles**

Los siguientes elementos en el gráfico se pueden representar de acuerdo con su configuración de localización.

|**Elementos compatibles**|**valor predeterminado en el entorno inglés**|
| :- | :- |
|Nombre del título del eje|Título del eje|
|Nombre de la unidad del eje|Cientos, miles...|
|Nombre del título del gráfico|Titulo del gráfico|
|Leyenda Aumentar nombre|Aumentar|
|Leyenda Disminuir Nombre|Disminuir|
|Leyenda Total Nombre|Total|
|Otro nombre|Otro|
|Nombre de la serie|Serie|

##  **Pasos de operación**

El siguiente ejemplo le mostrará en detalle cómo configurar una región localizada para lograr el efecto que desea.

- [Cómo configurar la región china para el gráfico](/cells/es/net/convert-chart-to-image-for-chinese-region/)
- [Cómo configurar la región japonesa para el gráfico](/cells/es/net/convert-chart-to-image-for-japanese-region/)

