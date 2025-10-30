---
title: Convertir el gráfico a imagen para la región de China con Golang a través de C++
linktitle: Establecer región china
description: Aprenda cómo usar Aspose.Cells for C++ para configurar la configuración china para gráficos. Nuestra guía mostrará cómo configurar gráficos para soportar caracteres y formatos chinos, incluidos fuentes, tamaños, direcciones de texto y más.
keywords: Aspose.Cells for C++, gráficos, configuración china, fuentes, tamaño de fuente, dirección del texto, soporte.
type: docs
weight: 9
url: /es/go-cpp/convert-chart-to-image-for-chinese-region/
alias: [/cpp/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

En este tema, te mostraremos cómo configurar la región china para un gráfico.

{{% /alert %}}

## **Define una clase de herencia**

El primer paso, necesita definir una clase "ChartChineseSetttings" que herede de [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/). 
Luego, al sobrescribir las funciones relacionadas, puede configurar el texto de los elementos del gráfico en su propio idioma.

Ejemplo de código:
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChineseSettting.go" >}}
Entonces puedes ver el efecto en la imagen de salida, los elementos en el gráfico se renderizarán de acuerdo a tu configuración.

## **Conclusión**

En este ejemplo, si no se establece la Región China para un gráfico, los siguientes elementos del gráfico pueden renderizarse en el idioma predeterminado, como el inglés.
Después de la operación anterior, podemos obtener una imagen de gráfico de salida con la Región China.

|**Elementos soportados**|**Valor en este ejemplo**|**valor predeterminado en el entorno inglés**|
| :- | :- | :- |
|Nombre del Título del Eje|坐标轴标题|Título del Eje|
|Nombre de la Unidad del Eje|百,千...|Cientos, Miles...|
|Nombre del Título del Gráfico|图表标题|Título del Gráfico|
|Nombre del Aumento de la Leyenda|增加|Aumento|
|Nombre de la Disminución de la Leyenda|减少|Disminución|
|Nombre Total de la Leyenda|汇总|Total|
|Otro Nombre|其他|Otro|
|Nombre de la Serie|系列|Serie|
