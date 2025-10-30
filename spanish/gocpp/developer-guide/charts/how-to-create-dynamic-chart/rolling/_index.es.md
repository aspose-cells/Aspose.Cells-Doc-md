---
title: Cómo crear un gráfico de rodamiento dinámico con Golang a través de C++
linktitle: Cómo crear un Gráfico Dinámico Continuo
description: Aprenda a crear un gráfico de rodamiento dinámico usando Aspose.Cells for C++. Nuestra guía demostrará cómo implementar transiciones de datos suaves y promedios móviles en su gráfico para una visualización continua y actualizada.
keywords: Aspose.Cells for C++, Gráfico de Rodamiento Dinámico, Transiciones de Datos, Promedios Suaves, Visualización Continua, Actualizaciones.
type: docs
weight: 74
url: /es/go-cpp/create-dynamic-rolling-chart/
---

## **Escenarios de uso posibles**
Un gráfico de desplazamiento dinámico se refiere a una representación gráfica que muestra puntos de datos en constante cambio y actualización a lo largo del tiempo. Es un tipo de gráfico que se actualiza continuamente, mostrando una ventana en tiempo real de los puntos de datos más recientes mientras descarta los puntos de datos antiguos a medida que ingresan nuevos.

Los gráficos de desplazamiento dinámico se utilizan comúnmente para visualizar tendencias y patrones en datos en tiempo real o en streaming. Son particularmente útiles en escenarios donde los aspectos temporales y los cambios a lo largo del tiempo son críticos, como análisis del mercado de valores, monitoreo del clima o seguimiento de actuaciones en vivo.

Estos gráficos suelen emplear mecanismos de animación o desplazamiento automático para garantizar que la información más actualizada siempre se presente. La longitud de la ventana de desplazamiento se puede personalizar para mostrar un período de tiempo específico, como la última hora, día o semana.

En resumen, un gráfico de desplazamiento dinámico es una representación gráfica actualizada continuamente que muestra los últimos puntos de datos mientras descarta los antiguos, lo que permite a los usuarios observar tendencias y patrones en tiempo real.

## **Use Aspose Cells para crear un gráfico de desplazamiento dinámico**
En los siguientes párrafos, le mostraremos cómo crear un gráfico de desplazamiento dinámico usando Aspose.Cells. Le mostraremos el código del ejemplo, así como el archivo de Excel creado con este código.

## **Código de muestra**
El siguiente código de ejemplo generará el [Archivo de Gráfico de Desplazamiento Dinámico](DynamicRollingChart.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Rolling.go" >}}
## **Notas**
En el archivo generado, puedes seguir agregando datos en las columnas A y B, mientras que el gráfico cuenta dinámicamente los últimos 5 conjuntos de datos. Esto se hace usando la fórmula "OFFSET" en el código de muestra:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Rolling-1.go" >}}
Puedes intentar cambiar el número "-5" por "-10" en la fórmula, y el gráfico dinámico contará los últimos 10 conjuntos de datos. Ahora hemos creado un gráfico de desplazamiento dinámico usando Aspose.Cells con éxito.
