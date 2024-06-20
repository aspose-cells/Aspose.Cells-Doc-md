---
title: Cómo crear un gráfico de desplazamiento dinámico
description: Aprende cómo crear un gráfico de desplazamiento dinámico usando Aspose.Cells for .NET. Nuestra guía paso a paso demostrará cómo implementar transiciones de datos suaves y desplazamiento automático en tu gráfico para una visualización continua y actualizada.
keywords: Aspose.Cells for .NET, Gráfico de Desplazamiento Dinámico, Transiciones de Datos, Desplazamiento Suave, Visualización Continua, Actualización de la Visualización.
type: docs
weight: 75
url: /es/net/create-dynamic-scrolling-chart/
---

## **Escenarios de uso posibles**
El gráfico de desplazamiento dinámico es un tipo de representación gráfica utilizada para mostrar datos que cambian con el tiempo. Está diseñado para proporcionar una vista en tiempo real de los datos, permitiendo a los usuarios rastrear actualizaciones continuas y tendencias. El gráfico se actualiza continuamente a medida que se agregan nuevos datos, y se desplaza automáticamente para mostrar la información más reciente.

Los gráficos de desplazamiento dinámico se utilizan comúnmente en diversas industrias, como finanzas, análisis del mercado de valores, seguimiento del clima y análisis de redes sociales. Permiten a los usuarios visualizar y analizar patrones de datos y tomar decisiones informadas basadas en información en tiempo real.

Estos gráficos suelen ser interactivos, permitiendo al usuario hacer zoom o desplazarse por datos históricos, y ajustar intervalos de tiempo. A menudo admiten múltiples series de datos, proporcionando una vista integral de diferentes métricas y sus correlaciones.

En general, los gráficos de desplazamiento dinámico son herramientas valiosas para monitorear y analizar datos de series temporales, facilitando la toma de decisiones en tiempo real y mejorando las capacidades de visualización de datos.

## **Use Aspose Cells para crear un gráfico de desplazamiento dinámico**
En los siguientes párrafos, te mostraremos cómo crear un Gráfico de Desplazamiento Dinámico utilizando Aspose.Cells. Te mostraremos el código del ejemplo, así como el archivo de Excel creado con este código.

## **Código de muestra**
El siguiente código de ejemplo generará el [Archivo de Gráfico de Desplazamiento Dinámico](DynamicScrollingChart.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-dynamic-scrolling-chart.cs" >}}

## **Notas**
En el archivo generado, puedes operar en la barra de desplazamiento, mientras el gráfico cuenta dinámicamente los últimos 10 conjuntos de datos. Esto se hace usando la fórmula "OFFSET" en el código de ejemplo:

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

Puedes intentar cambiar el número "10" a "15" en la celda "Sheet1!$H$20", y el gráfico dinámico contará los últimos 15 conjuntos de datos. Ahora hemos creado exitosamente un gráfico de desplazamiento dinámico usando Aspose.Cells.
