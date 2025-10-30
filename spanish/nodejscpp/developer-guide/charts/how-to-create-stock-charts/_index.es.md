---
title: Cómo crear gráficos de acciones con Node.js vía C++
linktitle: Cómo crear gráficos de cotización
description: Aprenda a crear diferentes tipos de gráficos de acciones incluyendo HLC, OHLC, VHLC y VOHLC usando las API de Aspose.Cells para Node.js vía C++. 
keywords: Crear gráficos de acciones en Node.js vía C++, Aspose.Cells, Visualización de datos de mercado, Análisis de mercado de acciones, Guía paso a paso.
type: docs
weight: 71
url: /es/nodejs-cpp/how-to-create-stock-charts/
---

{{% alert color="primary" %}}

Este párrafo te indicará cómo crear un gráfico de cotización, que incluye cuatro tipos:
- **HLC** – Alto-Bajo-Cierre.
- **OHLC** – Apertura-Alto-Bajo-Cierre.
- **VHLC** – Volumen-Alto-Bajo-Cierre.
- **VOHLC** – Volumen-Apertura-Alto-Bajo-Cierre.

{{% /alert %}}

## **¿Qué es un gráfico de cotización?**

Los gráficos de acciones son un gráfico específico utilizado para rastrear los cambios en el precio de activos negociados como mercancías, acciones y criptomonedas. Permiten ver los valores máximos y mínimos a lo largo del tiempo, junto con los valores de apertura y cierre en un solo gráfico. Aspose.Cells for Node.js via C++ ofrece cuatro gráficos de acciones, y para usarlos, debes tener los conjuntos de datos adecuados disponibles, y debes seleccionar las columnas en el orden correcto.

El conjunto de datos a continuación muestra la información de negociación diaria de una acción. Usaremos estos datos para crear cuatro tipos de gráficos de acciones: gráfico HLC (Alta-Baja-Cierre), gráfico OHLC (Apertura-Alta-Baja-Cierre), gráfico VHLC (Volumen-Alta-Baja-Cierre), y gráfico VOHLC (Volumen-Apertura-Alta-Baja-Cierre).

![todo:image_alt_text](stock.chart.data.png)
{{< app/cells/assistant language="nodejs-cpp" >}}
