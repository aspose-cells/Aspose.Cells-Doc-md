---
title: Convertir gráfico a imagen para la región china
linktitle: Establecer región china
type: docs
weight: 9
url: /es/net/convert-chart-to-image-for-chinese-region/
alias: [/net/set-chinese-configuration-for-chart/]
---
{{% alert color="primary" %}}

En este tema, le mostraremos cómo configurar la región china para un gráfico.

{{% /alert %}}

##  **Define una clase de herencia**

Primer paso, debe definir una clase "ChartChineseSetttings" que herede de[**GráficoGlobalizaciónConfiguración**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
Luego, al reescribir las funciones relacionadas, puede configurar el texto de los elementos del gráfico en su propio idioma.
Ejemplo de código:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartChineseSetttings.cs" >}}

##  **Configuración de configuración china para el gráfico**

En este paso, utilizará la clase "ChartChineseSetttings" que definió en el paso anterior.
Ejemplo de código:

```
	Workbook wb = new Workbook("Chinese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartChineseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

Luego puede ver el efecto en la imagen de salida, los elementos en el gráfico se representarán de acuerdo con su configuración.

##  **Conclusión**

En este ejemplo, si no establece la región china para un gráfico, los siguientes elementos del gráfico se pueden representar en el idioma predeterminado, como el inglés.
Después de la operación anterior, podemos obtener una imagen del gráfico de salida con la región china.

|**Elementos compatibles**|**Valor en este ejemplo**|**valor predeterminado en el entorno inglés**|
| :- | :- | :- |
|Nombre del título del eje|坐标轴标题|Título del eje|
|Nombre de la unidad del eje|百,千...|Cientos, miles...|
|Nombre del título del gráfico|图表标题|Titulo del gráfico|
|Leyenda Aumentar nombre|增加|Aumentar|
|Leyenda Disminuir Nombre|减少|Disminuir|
|Leyenda Total Nombre|汇总|Total|
|Otro nombre|其他|Otro|
|Nombre de la serie|系列|Serie|
