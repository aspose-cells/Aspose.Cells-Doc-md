---
title: Convertir gráfico en imagen para la región japonesa
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

 Primer paso, debe definir una clase "ChartJapaneseSetttings" que hereda de[**GráficoGlobalizaciónConfiguración**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
Luego, al reescribir las funciones relacionadas, puede configurar el texto de los elementos del gráfico en su propio idioma.
Ejemplo de código:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartJapaneseSetttings.cs" >}}

##  **Configuración de la configuración japonesa para el gráfico**

En este paso, utilizará la clase "ChartJapaneseSetttings" que definió en el paso anterior.
Ejemplo de código:

```
	Workbook wb = new Workbook("Japanese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartJapaneseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

Luego puede ver el efecto en la imagen de salida, los elementos en el gráfico se representarán de acuerdo con su configuración.

##  **Conclusión**

En este ejemplo, si no establece la región japonesa para un gráfico, los siguientes elementos del gráfico se pueden representar en el idioma predeterminado, como el inglés.
Después de la operación anterior, podemos obtener una imagen del gráfico de salida con la región japonesa.

|**Elementos compatibles**|**Valor en este ejemplo**|**valor predeterminado en el entorno inglés**|
| :- | :- | :- |
|Nombre del título del eje|軸タイトル|Título del eje|
|Nombre de la unidad del eje|百,千...|Cientos, miles...|
|Nombre del título del gráfico|グラフ タイトル|Titulo del gráfico|
|Leyenda Aumentar nombre|ぞうか|Aumentar|
|Leyenda Disminuir Nombre|削減|Disminuir|
|Leyenda Total Nombre|すべての|Total|
|Otro nombre|その他|Otro|
|Nombre de la serie|シリーズ|Serie|
