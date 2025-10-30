---
title: Cómo crear un gráfico de desplazamiento dinámico con Golang a través de C++
linktitle: Crear Gráfico de Desplazamiento Dinámico
description: Aprenda a crear un gráfico de desplazamiento dinámico usando Aspose.Cells for C++. Nuestra guía paso a paso demostrará cómo implementar transiciones de datos suaves y desplazamiento automático en su gráfico para una visualización continua y actualizada.
keywords: Aspose.Cells for C++, Gráfico de Desplazamiento Dinámico, Transiciones de Datos, Desplazamiento Suave, Visualización Continua, Actualizaciones.
type: docs
weight: 75
url: /es/go-cpp/create-dynamic-scrolling-chart/
---

## **Escenarios de uso posibles**
El gráfico de desplazamiento dinámico es un tipo de representación gráfica utilizada para mostrar datos que cambian con el tiempo. Está diseñado para proporcionar una vista en tiempo real de los datos, permitiendo a los usuarios rastrear actualizaciones continuas y tendencias. El gráfico se actualiza continuamente a medida que se agregan nuevos datos, y se desplaza automáticamente para mostrar la información más reciente.

Los gráficos de desplazamiento dinámico se utilizan comúnmente en diversas industrias, como finanzas, análisis del mercado de valores, seguimiento del clima y análisis de redes sociales. Permiten a los usuarios visualizar y analizar patrones de datos y tomar decisiones informadas basadas en información en tiempo real.

Estos gráficos suelen ser interactivos, permitiendo al usuario hacer zoom o desplazarse por datos históricos, y ajustar intervalos de tiempo. A menudo admiten múltiples series de datos, proporcionando una vista integral de diferentes métricas y sus correlaciones.

En general, los gráficos de desplazamiento dinámico son herramientas valiosas para monitorear y analizar datos de series temporales, facilitando la toma de decisiones en tiempo real y mejorando las capacidades de visualización de datos.

## **Use Aspose Cells para Crear Gráfico de Desplazamiento Dinámico**
En los siguientes párrafos, le mostraremos cómo crear un Gráfico de Desplazamiento Dinámico usando Aspose.Cells. Le mostraremos el código del ejemplo, así como el archivo de Excel creado con este código.

## **Código de muestra**
El siguiente código de ejemplo generará el [Archivo de Gráfico de Desplazamiento Dinámico](DynamicScrollingChart.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Scrolling.go" >}}
## **Notas**
En el archivo generado, puedes operar en la barra de desplazamiento, mientras el gráfico cuenta dinámicamente los últimos 10 conjuntos de datos. Esto se hace usando la fórmula "OFFSET" en el código de ejemplo:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Scrolling-1.go" >}}
Puedes intentar cambiar el número "10" a "15" en la celda "Sheet1!$H$20", y el gráfico dinámico contará los últimos 15 conjuntos de datos. Ahora hemos creado exitosamente un gráfico de desplazamiento dinámico usando Aspose.Cells.
