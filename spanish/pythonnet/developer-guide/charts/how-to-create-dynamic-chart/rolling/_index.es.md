---
title: Cómo crear un Gráfico Dinámico Continuo
description: Aprende cómo crear un gráfico rodante dinámico usando Aspose.Cells para Python via .NET. Nuestra guía demostrará cómo implementar transiciones suaves de datos y promedios móviles en tu gráfico para una visualización continua y actualizada.
keywords: Aspose.Cells para Python via .NET, Gráfico Rodante Dinámico, Transiciones de Datos, Promedios Suaves, Visualización Continua, Actualización de Visualizaciones.
type: docs
weight: 74
url: /es/python-net/create-dynamic-rolling-chart/
---

## **Escenarios de uso posibles**
Un gráfico de desplazamiento dinámico se refiere a una representación gráfica que muestra puntos de datos en constante cambio y actualización a lo largo del tiempo. Es un tipo de gráfico que se actualiza continuamente, mostrando una ventana en tiempo real de los puntos de datos más recientes mientras descarta los puntos de datos antiguos a medida que ingresan nuevos.

Los gráficos de desplazamiento dinámico se utilizan comúnmente para visualizar tendencias y patrones en datos en tiempo real o en streaming. Son particularmente útiles en escenarios donde los aspectos temporales y los cambios a lo largo del tiempo son críticos, como análisis del mercado de valores, monitoreo del clima o seguimiento de actuaciones en vivo.

Estos gráficos suelen emplear mecanismos de animación o desplazamiento automático para garantizar que la información más actualizada siempre se presente. La longitud de la ventana de desplazamiento se puede personalizar para mostrar un período de tiempo específico, como la última hora, día o semana.

En resumen, un gráfico de desplazamiento dinámico es una representación gráfica actualizada continuamente que muestra los últimos puntos de datos mientras descarta los antiguos, lo que permite a los usuarios observar tendencias y patrones en tiempo real.

## **Usa Aspose.Cells para Python via .NET para crear un Gráfico Rodante Dinámico**
En los siguientes párrafos, te mostraremos cómo crear un Gráfico Rodante Dinámico usando Aspose.Cells para Python via .NET. Mostraremos el código para el ejemplo, así como el archivo Excel creado con este código.

## **Código de muestra**
El siguiente código de ejemplo generará el [Archivo de Gráfico de Desplazamiento Dinámico](DynamicRollingChart.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-create-dynamic-rolling-chart.py" >}}

## **Notas**
En el archivo generado, puedes seguir agregando datos en las columnas A y B, mientras que el gráfico cuenta dinámicamente los últimos 5 conjuntos de datos. Esto se hace usando la fórmula "OFFSET" en el código de muestra:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

Puedes intentar cambiar el número "-5" por "-10" en la fórmula, y el gráfico dinámico contará los últimos 10 conjuntos de datos. Ahora hemos creado un gráfico rodante dinámico usando Aspose.Cells para Python via .NET con éxito.
