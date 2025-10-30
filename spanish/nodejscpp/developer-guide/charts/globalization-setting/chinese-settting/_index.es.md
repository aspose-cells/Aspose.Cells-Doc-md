---  
title: Convertir gráfico a imagen para la región china con Node.js vía C++  
description: Aprende cómo usar Aspose.Cells for Node.js via C++ para configurar gráficos para caracteres y formatos chinos, incluyendo fuentes, tamaños, direcciones de texto y más.  
keywords: Aspose.Cells para Node.js, gráficos, configuración china, fuentes, tamaño de fuente, dirección de texto, soporte.  
linktitle: Establecer región china  
type: docs  
weight: 9  
url: /es/nodejs-cpp/convert-chart-to-image-for-chinese-region/  
alias: [/nodejs-cpp/set-chinese-configuration-for-chart/]  
---  

{{% alert color="primary" %}}  
En este tema, te mostraremos cómo configurar la región china para un gráfico.  
{{% /alert %}}  

## **Define una clase de herencia**  

El primer paso, necesita definir una clase "ChartChineseSetttings" que herede de [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/).  
Luego, al reescribir las funciones relacionadas, puedes establecer el texto de los elementos del gráfico en tu propio idioma.  
Ejemplo de código:  
```javascript
const AsposeCells = require("aspose.cells.node");

class ChartChineseSettings extends AsposeCells.ChartGlobalizationSettings {
getAxisTitleName() {
return "坐标轴标题";
}

getAxisUnitName(type) {
switch (type) {
case AsposeCells.DisplayUnitType.None:
return '';
case AsposeCells.DisplayUnitType.Hundreds:
return '百';
case AsposeCells.DisplayUnitType.Thousands:
return '千';
case AsposeCells.DisplayUnitType.TenThousands:
return '万';
case AsposeCells.DisplayUnitType.HundredThousands:
return '十万';
case AsposeCells.DisplayUnitType.Millions:
return '百万';
case AsposeCells.DisplayUnitType.TenMillions:
return '千万';
case AsposeCells.DisplayUnitType.HundredMillions:
return '亿';
case AsposeCells.DisplayUnitType.Billions:
return '十亿';
case AsposeCells.DisplayUnitType.Trillions:
return '兆';
default:
return '';
}
}

getChartTitleName() {
return "图表标题";
}

getLegendDecreaseName() {
return "减少";
}

getLegendIncreaseName() {
return "增加";
}

getLegendTotalName() {
return "汇总";
}

getOtherName() {
return "其他";
}

getSeriesName() {
return "系列";
}
}
```  

## **Configuración China para el gráfico**  

En este paso, utilizará la clase "Configuración China de Gráficos" que definió en el paso anterior.  
Ejemplo de código:  

```javascript  
const Workbook = require('aspose.cells');  
const wb = new Workbook("Chinese.xls");  
wb.settings.globalizationSettings.chartSettings = new ChartChineseSetttings();  
const chart0 = wb.worksheets[0].charts[0];  
chart0.toImage("Output.png");  
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

{{< app/cells/assistant language="nodejs-cpp" >}}
