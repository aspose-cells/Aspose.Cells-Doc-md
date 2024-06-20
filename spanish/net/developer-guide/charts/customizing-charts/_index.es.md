---
title: Personalización de gráficos
description: Aprenda cómo personalizar gráficos en Aspose.Cells for .NET. Nuestra guía le mostrará cómo modificar diseños de gráficos, agregar y formatear series de datos, ajustar ejes y aplicar varias opciones de formato para mejorar la apariencia y usabilidad de sus gráficos.
keywords: Aspose.Cells for .NET, graficación, personalización, diseños, series de datos, ejes, formato, apariencia, usabilidad.
type: docs
weight: 40
url: /es/net/customizing-charts/
---

{{% alert color="primary" %}}

## **Creación de gráficos personalizados**

Hasta ahora, cuando hemos discutido gráficos, hemos visto gráficos estándar que tienen su configuración de formato estándar. Solo definimos la fuente de datos, configuramos algunas propiedades y el gráfico se crea con su configuración de formato predeterminada. Pero las API de Aspose.Cells también admiten la creación de gráficos personalizados que permiten a los desarrolladores crear gráficos con su propia configuración de formato.

Los desarrolladores pueden crear gráficos personalizados en tiempo de ejecución utilizando Aspose.Cells.

Un gráfico está compuesto por una serie de datos. Cada serie de datos en Aspose.Cells está representada por un objeto [**Series**](https://reference.aspose.com/cells/net/aspose.cells.charts/series), mientras que un objeto [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) sirve como una colección de objetos [**Series**](https://reference.aspose.com/cells/net/aspose.cells.charts/series). Al crear un gráfico personalizado, los desarrolladores tienen la libertad de usar diferentes tipos de gráficos para diferentes series de datos (recopilados en el objeto [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)).

El código de ejemplo a continuación demuestra cómo crear gráficos personalizados. En este ejemplo, vamos a usar un gráfico de columnas para la primera serie de datos y un gráfico de líneas para la segunda serie. El resultado es que agregamos un gráfico de columnas, combinado con un gráfico de líneas, a la hoja de cálculo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateCustomChart-1.cs" >}}

{{% alert color="primary" %}}

Actualmente, Aspose.Cells solo admite gráficos personalizados que combinan gráficos circulares, de líneas, de columnas y de columnas apiladas, pero se admitirán más gráficos en futuras versiones.

{{% /alert %}}
