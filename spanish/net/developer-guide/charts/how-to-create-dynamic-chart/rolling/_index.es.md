---
title: Cómo crear un gráfico dinámico dinámico
description: Aprenda a crear un gráfico móvil dinámico usando Aspose.Cells for .NET. Nuestra guía le demostrará cómo implementar transiciones de datos fluidas y promedios móviles en su gráfico para una visualización continua y actualizada.
keywords: Aspose.Cells for .NET, Dynamic Rolling Chart, Data Transitions, Smooth Averages, Continuous Display, Updating Visualization.
type: docs
weight: 74
url: /es/net/create-dynamic-rolling-chart/
---
##  **Posibles escenarios de uso**
Un gráfico móvil dinámico se refiere a una representación gráfica que muestra puntos de datos que cambian y se actualizan constantemente con el tiempo. Es un tipo de gráfico que se actualiza continuamente, mostrando una ventana móvil de los puntos de datos más recientes y descartando los puntos de datos más antiguos a medida que aparecen nuevos.

Los gráficos dinámicos se utilizan comúnmente para visualizar tendencias y patrones en tiempo real o en tiempo real. Son particularmente útiles en escenarios donde los aspectos temporales y los cambios en el tiempo son críticos, como el análisis del mercado de valores, el monitoreo del clima o el seguimiento del desempeño en vivo.

Estos gráficos suelen emplear mecanismos de animación o desplazamiento automático para garantizar que siempre se presente la información más actualizada. La duración de la ventana móvil se puede personalizar para mostrar un período de tiempo específico, como la última hora, día o semana.

En resumen, un gráfico móvil dinámico es una representación gráfica que se actualiza continuamente y que muestra los puntos de datos más recientes y descarta los más antiguos, lo que permite a los usuarios observar tendencias y patrones en tiempo real.

##  **Utilice Aspose Cells para crear un gráfico dinámico dinámico**
En los siguientes párrafos, le mostraremos cómo crear un gráfico dinámico dinámico usando Aspose.Cells. Le mostraremos el código del ejemplo, así como el archivo de Excel creado con este código.

##  **Código de muestra**
 El siguiente código de muestra generará el[Archivo de gráfico dinámico dinámico](DynamicRollingChart.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-dynamic-rolling-chart.cs" >}}

##  **Notas**
En el archivo generado, puede continuar agregando datos en las columnas A y B, mientras el gráfico cuenta dinámicamente los últimos 5 conjuntos de datos. Esto se hace usando la fórmula "OFFSET" en el código de muestra:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

Puede intentar cambiar el número "-5" a "-10" en la fórmula y el gráfico dinámico contará los últimos 10 conjuntos de datos. Ahora hemos creado un gráfico móvil dinámico utilizando Aspose.Cells con éxito.
