---
title: Personalización de gráficos con Golang mediante C++
linktitle: Personalización de gráficos
description: Aprende cómo personalizar gráficos en Aspose.Cells for C++. Nuestra guía te mostrará cómo modificar diseños de gráficos, agregar y dar formato a series de datos, ajustar ejes y aplicar varias opciones de formato para mejorar la apariencia y usabilidad de tus gráficos.
keywords: Aspose.Cells for C++, creación de gráficos, personalización, diseños, series de datos, ejes, formato, apariencia, usabilidad.
type: docs
weight: 40
url: /es/go-cpp/customizing-charts/
---


## **Creación de gráficos personalizados**

Hasta ahora, cuando hemos hablado de gráficos, hemos visto gráficos estándar que tienen su configuración de formato estándar. Solo definimos la fuente de datos, establecemos algunas propiedades y el gráfico se crea con sus configuraciones de formato predeterminadas. Pero las APIs de Aspose.Cells también soportan crear gráficos personalizados que permiten a los desarrolladores crear gráficos con sus propias configuraciones de formato.

Los desarrolladores pueden crear gráficos personalizados en tiempo de ejecución utilizando Aspose.Cells.

Un gráfico está compuesto por una serie de datos. Cada serie de datos en Aspose.Cells está representada por un objeto [**Series**](https://reference.aspose.com/cells/go-cpp/series/), mientras que un objeto [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/) sirve como una colección de objetos [**Series**](https://reference.aspose.com/cells/go-cpp/series/). Al crear un gráfico personalizado, los desarrolladores tienen la libertad de usar diferentes tipos de gráficos para diferentes series de datos (recopilados en el objeto [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/)).

El código de ejemplo a continuación demuestra cómo crear gráficos personalizados. En este ejemplo, vamos a usar un gráfico de columnas para la primera serie de datos y un gráfico de líneas para la segunda serie. El resultado es que agregamos un gráfico de columnas, combinado con un gráfico de líneas, a la hoja de cálculo.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CustomizingCharts.go" >}}
{{% alert color="primary" %}}

Actualmente, Aspose.Cells solo soporta gráficos personalizados que combinan gráficos de pastel, línea, columna y apilados, pero en futuras versiones se soportarán más gráficos.

{{% /alert %}}
