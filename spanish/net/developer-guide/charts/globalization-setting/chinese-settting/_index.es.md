---
title: Convertir gráfico a imagen para la región china
description: Aprende a usar Aspose.Cells for .NET para configurar la región china en gráficos. Nuestra guía demostrará cómo configurar gráficos para admitir caracteres y formatos chinos, incluyendo fuentes, tamaños, direcciones de texto y más.
keywords: Aspose.Cells for .NET, Gráficos, Configuración china, Fuentes, Tamaño de fuente, Dirección del texto, Soporte.
linktitle: Establecer región china
type: docs
weight: 9
url: /es/net/convert-chart-to-image-for-chinese-region/
alias: [/net/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

En este tema, te mostraremos cómo configurar la región china para un gráfico.

{{% /alert %}}

## **Define una clase de herencia**

Como primer paso, necesitas definir una clase "Configuración china del gráfico" que herede de [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
Luego, al reescribir las funciones relacionadas, puedes establecer el texto de los elementos del gráfico en tu propio idioma.
Ejemplo de código:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartChineseSetttings.cs" >}}

## **Configuración China para el gráfico**

En este paso, utilizará la clase "Configuración China de Gráficos" que definió en el paso anterior.
Ejemplo de código:

```
	Workbook wb = new Workbook("Chinese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartChineseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

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
