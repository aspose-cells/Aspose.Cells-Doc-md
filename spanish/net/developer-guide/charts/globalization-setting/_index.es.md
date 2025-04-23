---
title: Convertir gráfico a imagen localizada
description: Aprende cómo configurar las configuraciones de globalización para gráficos usando Aspose.Cells for .NET. Nuestra guía demuestra cómo configurar el gráfico para admitir múltiples idiomas y formatos regionales para mostrar correctamente el texto, las fechas y los números en diferentes idiomas.
keywords: Aspose.Cells for .NET, Gráficos, Configuraciones de Globalización, Múltiples Idiomas, Formatos Regionales, Mostrar, Texto, Fechas, Números.
linktitle: Establecer Región Localizada
type: docs
weight: 50
url: /es/net/convert-chart-to-localized-image/
alias: [/net/how-to-set-globalization-configuration-for-chart/]
---

{{% alert color="primary" %}}

En este tema, te mostraremos cómo convertir un gráfico en una imagen localizada, aprenderás cómo establecer una región localizada para un gráfico.

{{% /alert %}}

## **Escenario**

¿En qué escenario necesitaríamos establecer una región localizada para un gráfico? 

Cuando abres un archivo xlsx con un gráfico en Excel, en este caso, supongamos que lo abres con una Configuración Regional en Español en Excel, puedes ver los elementos en el área del gráfico, como el Título del Gráfico, Leyenda, que están traducidos al español. Pero al guardar este gráfico como una imagen con Aspose.Cells, es posible que te encuentres con el siguiente problema: 

**![Problema Global](GlobalIssue.png)**

En este escenario, la Leyenda del Gráfico en la imagen de salida no es la misma que en Excel, siguen mostrándose en inglés por defecto. Ahora puedes solucionar este problema estableciendo una región localizada para el gráfico. Con la configuración correcta, los siguientes elementos se representarán según tu configuración de localización.

## **Elementos soportados**

Los siguientes elementos en el gráfico pueden representarse según tu configuración de localización.

|**Elementos soportados**|**valor por defecto en el entorno en inglés**|
| :- | :- |
|Nombre del Título del Eje|Título del Eje|
|Nombre de la Unidad del Eje|Cientos, Miles...|
|Nombre del Título del Gráfico|Título del Gráfico|
|Nombre del Aumento de la Leyenda|Aumento|
|Nombre de la Disminución de la Leyenda|Disminución|
|Nombre Total de la Leyenda|Total|
|Otros Nombre|Otros|
|Nombre de la Serie|Serie|

## **Pasos de la Operación**

El siguiente ejemplo te mostrará en detalle cómo establecer una región localizada para lograr el efecto que deseas.

- [Cómo establecer la región china para el gráfico](/cells/es/net/convert-chart-to-image-for-chinese-region/)
- [Cómo establecer la región japonesa para el gráfico](/cells/es/net/convert-chart-to-image-for-japanese-region/)

{{< app/cells/assistant language="csharp" >}}
