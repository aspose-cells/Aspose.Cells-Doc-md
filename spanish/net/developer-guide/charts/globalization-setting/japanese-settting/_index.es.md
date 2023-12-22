---
title: Convertir gráfico en imagen para la región japonesa
description: Aprenda a utilizar Aspose.Cells for .NET establece la configuración japonesa para el gráfico. Nuestra guía demostrará cómo configurar gráficos para admitir caracteres y formatos japoneses, incluidas fuentes, tamaño, dirección del texto y más.
keywords: Aspose.Cells for .NET, Charts, Japanese configuration, font, font size, text direction, support.
linktitle: Establecer región japonesa
type: docs
weight: 10
url: /es/net/convert-chart-to-image-for-japanese-region/
alias: [/net/set-japanese-configuration-for-chart/]
---
{{% alert color="primary" %}}

En este tema, le mostraremos cómo configurar la región japonesa para un gráfico.

{{% /alert %}}

##  **Define una clase de herencia**

 El primer paso es definir una clase "ChartJapaneseSetttings" que herede de[**GráficoGlobalizaciónConfiguración**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
Luego, al reescribir las funciones relacionadas, puede configurar el texto de los elementos del gráfico en su propio idioma.
Ejemplo de código:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartJapaneseSetttings.cs" >}}

##  **Configurar la configuración japonesa para el gráfico**

En este paso, utilizará la clase "ChartJapaneseSetttings" que definió en el paso anterior.
Ejemplo de código:

```
	Workbook wb = new Workbook("Japanese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartJapaneseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

Luego podrá ver el efecto en la imagen de salida; los elementos del gráfico se representarán de acuerdo con su configuración.

##  **Conclusión**

En este ejemplo, si no configura la región japonesa para un gráfico, los siguientes elementos del gráfico pueden representarse en el idioma predeterminado, como el inglés.
Después de la operación anterior, podemos obtener una imagen del gráfico de salida con la región japonesa.

|**Elementos soportados**|**Valor en este ejemplo**|**valor predeterminado en el entorno inglés**|
| :- | :- | :- |
|Nombre del título del eje|軸タイトル|Título del eje|
|Nombre de la unidad del eje|百,千...|Cientos, miles...|
|Nombre del título del gráfico|グラフ タイトル|Titulo del gráfico|
|Leyenda Aumentar Nombre|ぞうか|Aumentar|
|Leyenda Disminución Nombre|削減|Disminuir|
|Nombre total de la leyenda|すべての|Total|
|Otro nombre|その他|Otro|
|Nombre de la serie|シリーズ|Serie|
