---
title: Convertir Gráfico a Imagen para la Región Japonesa
description: Aprenda cómo usar Aspose.Cells for .NET establece la configuración japonesa para el gráfico. Nuestra guía demostrará cómo configurar gráficos para admitir caracteres y formatos japoneses, incluidas fuentes, tamaño, dirección del texto y más.
keywords: Aspose.Cells for .NET, Gráficos, configuración japonesa, fuente, tamaño de fuente, dirección del texto, soporte.
linktitle: Establecer Región Japonesa
type: docs
weight: 10
url: /es/net/convert-chart-to-image-for-japanese-region/
alias: [/net/set-japanese-configuration-for-chart/]
---

{{% alert color="primary" %}}

En este tema, te mostraremos cómo configurar la Región japonesa para un gráfico.

{{% /alert %}}

## **Define una clase de herencia**

Primer paso, necesitas definir una clase "ChartJapaneseSetttings" que hereda de [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
Luego, al reescribir las funciones relacionadas, puedes establecer el texto de los elementos del gráfico en tu propio idioma.
Ejemplo de código:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartJapaneseSetttings.cs" >}}

## **Configurar Ajustes Japoneses Para Gráfico**

En este paso, usarás la clase "ChartJapaneseSetttings" que definiste en el paso anterior.
Ejemplo de código:

```
	Workbook wb = new Workbook("Japanese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartJapaneseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

Entonces puedes ver el efecto en la imagen de salida, los elementos en el gráfico se renderizarán de acuerdo a tu configuración.

## **Conclusión**

En este ejemplo, si no defines la Región japonesa para un gráfico, es posible que los siguientes elementos del gráfico se rendericen en el idioma predeterminado, como el inglés.
Después de la operación anterior, podemos obtener una imagen de gráfico de salida con la Región japonesa.

|**Elementos soportados**|**Valor en este ejemplo**|**valor predeterminado en el entorno inglés**|
| :- | :- | :- |
|Nombre del Título del Eje|軸タイトル|Título del Eje|
|Nombre de la Unidad del Eje|百,千...|Cientos, Miles...|
|Nombre del Título del Gráfico|グラフ タイトル|Título del Gráfico|
|Nombre de Aumento de Leyenda|ぞうか|Aumento|
|Nombre de Disminución de Leyenda|削減|Disminución|
|Nombre Total de Leyenda|すべての|Total|
|Otro Nombre|その他|Otro|
|Nombre de la Serie|シリーズ|Serie|
