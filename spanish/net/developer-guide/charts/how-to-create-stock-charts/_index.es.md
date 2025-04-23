---
title: Cómo crear gráficos de cotización
description: Los gráficos de cotización son un tipo específico de gráfico utilizado para rastrear cambios en el precio de los activos negociados. En esta sección, te mostraremos cómo crear fácilmente diferentes tipos de gráficos de cotización utilizando las APIs de Aspose.Cells. Específicamente, cubriremos los siguientes tipos de gráficos de cotización el gráfico de cotización Alto Bajo Cierre (HLC), el gráfico de cotización Apertura Alto Bajo Cierre (OHLC), el gráfico de cotización Volumen Alto Bajo Cierre (VHLC) y el gráfico de cotización Volumen Apertura Alto Bajo Cierre (VOHLC). 
keywords: Crear gráficos de cotización, Aspose.Cells, Visualización de Datos de Mercado, Análisis de Mercado de Valores, Guía Paso a Paso.
type: docs
weight: 71
url: /es/net/how-to-create-stock-charts/
---

{{% alert color="primary" %}}

Este párrafo te indicará cómo crear un gráfico de cotización, que incluye cuatro tipos:
- **HLC** – Alto-Bajo-Cierre.
- **OHLC** – Apertura-Alto-Bajo-Cierre.
- **VHLC** – Volumen-Alto-Bajo-Cierre.
- **VOHLC** – Volumen-Apertura-Alto-Bajo-Cierre.

{{% /alert %}}

## **¿Qué es un gráfico de cotización?**

Los gráficos de cotización son un tipo específico de gráfico utilizado para rastrear los cambios en el precio de los activos negociados, como materias primas, acciones y criptomonedas. Permiten ver los valores máximos y mínimos a lo largo del tiempo, junto con los valores de apertura y cierre en un solo gráfico. Aspose.Cells ofrece 4 tipos de gráficos de cotización y, para usarlos, debes tener los conjuntos de datos correctos disponibles y debes seleccionar las columnas en el orden correcto.

El conjunto de datos siguiente muestra la información de operaciones diarias para una acción. Utilizaremos estos datos para crear cuatro tipos de gráficos de cotización: gráfico de cotización Alto-Bajo-Cierre (HLC), gráfico de cotización Apertura-Alto-Bajo-Cierre (OHLC), gráfico de cotización Volumen-Alto-Bajo-Cierre (VHLC) y gráfico de cotización Volumen-Apertura-Alto-Bajo-Cierre (VOHLC). 

![todo:image_alt_text](stock.chart.data.png)
{{< app/cells/assistant language="csharp" >}}
