---
title: Convertir gráfico a imagen localizada con Node.js via C++
description: Aprende cómo configurar las opciones de globalización para gráficos usando Aspose.Cells for Node.js via C++. Nuestra guía demuestra cómo configurar el gráfico para admitir múltiples idiomas y formatos regionales para mostrar correctamente el texto, fechas y números en diferentes idiomas.
keywords: Aspose.Cells for Node.js via C++, gráficos, configuración de globalización, múltiples idiomas, formatos regionales, visualización, texto, fechas, números.
linktitle: Establecer Región Localizada
type: docs
weight: 50
url: /es/nodejs-cpp/convert-chart-to-localized-image/
alias: [/nodejs-cpp/how-to-set-globalization-configuration-for-chart/]
---

{{% alert color="primary" %}}

En este tema, te mostraremos cómo convertir un gráfico en una imagen localizada, aprenderás cómo establecer una región localizada para un gráfico.

{{% /alert %}}

## **Escenario**

¿En qué escenario necesitaríamos establecer una región localizada para un gráfico? 

Cuando abres un archivo xlsx con un gráfico en Excel, en este caso, supón que lo abres con una configuración regional en español en Excel, puedes ver que elementos en el área del gráfico, como el título del gráfico, la leyenda, están traducidos al español. Pero cuando guardas este gráfico como una imagen con Aspose.Cells, puedes encontrar el siguiente problema: 

**![Problema Global](GlobalIssue.png)**

En este escenario, la leyenda del gráfico en la imagen de salida no es la misma que en Excel; permanece en inglés por defecto. Ahora puedes solucionar este problema estableciendo una región localizada para el gráfico. Con la configuración correcta, los siguientes elementos se renderizarán de acuerdo a tu configuración de localización.

## **Elementos soportados**

Los siguientes elementos en el gráfico pueden ser renderizados de acuerdo a tu configuración de localización.

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

- [Cómo establecer la región china para el gráfico](/cells/es/nodejs-cpp/convert-chart-to-image-for-chinese-region/)
- [Cómo establecer la región japonesa para el gráfico](/cells/es/nodejs-cpp/convert-chart-to-image-for-japanese-region/)


{{< app/cells/assistant language="nodejs-cpp" >}}
