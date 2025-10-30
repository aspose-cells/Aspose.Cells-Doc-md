---  
title: Convertir gráfico a imagen para la región japonesa con Node.js vía C++  
description: Aprende cómo usar Aspose.Cells for Node.js via C++ para configurar la configuración japonesa para el gráfico. Nuestra guía demostrará cómo configurar gráficos para soportar caracteres y formatos japoneses, incluyendo fuentes, tamaño, dirección del texto y más.  
keywords: Aspose.Cells for Node.js via C++, gráficos, configuración japonesa, fuente, tamaño de fuente, dirección del texto, soporte.  
linktitle: Establecer Región Japonesa  
type: docs  
weight: 10  
url: /es/nodejs-cpp/convert-chart-to-image-for-japanese-region/  
alias: [/nodejs-cpp/set-japanese-configuration-for-chart/]  
---  

{{% alert color="primary" %}}  
En este tema, te mostraremos cómo configurar la Región japonesa para un gráfico.  
{{% /alert %}}  

## **Define una clase de herencia**  

Primer paso, debes definir una clase "ChartJapaneseSettings" que herede de [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/).  
Luego, al reescribir las funciones relacionadas, puedes establecer el texto de los elementos del gráfico en tu propio idioma.  
Ejemplo de código:  
```javascript
const AsposeCells = require("aspose.cells.node");

class ChartJapaneseSettings extends AsposeCells.ChartGlobalizationSettings {
getAxisTitleName() {
return "軸タイトル";
}

getAxisUnitName(type) {
switch (type) {
case AsposeCells.DisplayUnitType.None:
return '';
case AsposeCells.DisplayUnitType.Hundreds:
return "百";
case AsposeCells.DisplayUnitType.Thousands:
return "千";
case AsposeCells.DisplayUnitType.TenThousands:
return "万";
case AsposeCells.DisplayUnitType.HundredThousands:
return "10万";
case AsposeCells.DisplayUnitType.Millions:
return "百万";
case AsposeCells.DisplayUnitType.TenMillions:
return "千万";
case AsposeCells.DisplayUnitType.HundredMillions:
return "億";
case AsposeCells.DisplayUnitType.Billions:
return "10億";
case AsposeCells.DisplayUnitType.Trillions:
return "兆";
default:
return '';
}
}

getChartTitleName() {
return "グラフ タイトル";
}

getLegendDecreaseName() {
return "削減";
}

getLegendIncreaseName() {
return "ぞうか";
}

getLegendTotalName() {
return "すべての";
}

getOtherName() {
return "その他";
}

getSeriesName() {
return "シリーズ";
}
}
```  

## **Configurar Ajustes Japoneses Para Gráfico**  

En este paso, usarás la clase "ChartJapaneseSettings" que definiste en el paso anterior.  
Ejemplo de código:  

```javascript  
const { Workbook } = require('aspose.cells');

let wb = new Workbook("Japanese.xls");
wb.settings.globalizationSettings.chartSettings = new ChartJapaneseSettings();
let chart0 = wb.worksheets[0].charts[0];
chart0.toImage("Output.png");
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

{{< app/cells/assistant language="nodejs-cpp" >}}
