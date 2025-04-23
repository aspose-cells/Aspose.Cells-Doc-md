---
title: Cómo crear un gráfico de desplazamiento dinámico
description: Aprende cómo crear un gráfico de desplazamiento dinámico usando Aspose.Cells para Python via .NET. Nuestra guía paso a paso demostrará cómo implementar transiciones suaves de datos y desplazamiento automático en tu gráfico para una visualización continua y actualizada.
keywords: Aspose.Cells para Python via .NET, Gráfico de Desplazamiento Dinámico, Transiciones de Datos, Desplazamiento Suave, Visualización Continua, Actualización de Visualizaciones.
type: docs
weight: 75
url: /es/python-net/create-dynamic-scrolling-chart/
---

## **Escenarios de uso posibles**
El gráfico de desplazamiento dinámico es un tipo de representación gráfica utilizada para mostrar datos que cambian con el tiempo. Está diseñado para proporcionar una vista en tiempo real de los datos, permitiendo a los usuarios rastrear actualizaciones continuas y tendencias. El gráfico se actualiza continuamente a medida que se agregan nuevos datos, y se desplaza automáticamente para mostrar la información más reciente.

Los gráficos de desplazamiento dinámico se utilizan comúnmente en diversas industrias, como finanzas, análisis del mercado de valores, seguimiento del clima y análisis de redes sociales. Permiten a los usuarios visualizar y analizar patrones de datos y tomar decisiones informadas basadas en información en tiempo real.

Estos gráficos suelen ser interactivos, permitiendo al usuario hacer zoom o desplazarse por datos históricos, y ajustar intervalos de tiempo. A menudo admiten múltiples series de datos, proporcionando una vista integral de diferentes métricas y sus correlaciones.

En general, los gráficos de desplazamiento dinámico son herramientas valiosas para monitorear y analizar datos de series temporales, facilitando la toma de decisiones en tiempo real y mejorando las capacidades de visualización de datos.

## **Usa Aspose.Cells para Python via .NET para crear un Gráfico de Desplazamiento Dinámico**
En los siguientes párrafos, te mostraremos cómo crear un Gráfico de Desplazamiento Dinámico usando Aspose.Cells para Python via .NET. Mostraremos el código para el ejemplo, así como el archivo Excel creado con este código.

## **Código de muestra**
El siguiente código de ejemplo generará el [Archivo de Gráfico de Desplazamiento Dinámico](DynamicScrollingChart.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-create-dynamic-scrolling-chart.py" >}}

## **Notas**
En el archivo generado, puedes operar en la barra de desplazamiento, mientras el gráfico cuenta dinámicamente los últimos 10 conjuntos de datos. Esto se hace usando la fórmula "OFFSET" en el código de ejemplo:

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

Puedes intentar cambiar el número "10" por "15" en la celda "Sheet1!$H$20", y el gráfico dinámico contará los últimos 15 conjuntos de datos. Ahora hemos creado un gráfico de desplazamiento dinámico usando Aspose.Cells para Python via .NET con éxito.
