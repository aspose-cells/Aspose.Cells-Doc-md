---
title: Personalización de gráficos
description: Aprende cómo personalizar gráficos en Aspose.Cells para Python via .NET. Nuestra guía te mostrará cómo modificar el diseño del gráfico, agregar y dar formato a series de datos, ajustar los ejes y aplicar varias opciones de formato para mejorar la apariencia y usabilidad de tus gráficos.
keywords: Aspose.Cells para Python via .NET, gráficos, personalización, diseños, series de datos, ejes, formato, apariencia, usabilidad.
type: docs
weight: 40
url: /es/python-net/customizing-charts/
---


## **Creación de gráficos personalizados**

Hasta ahora, cuando hemos hablado de gráficos, hemos visto gráficos estándar que tienen sus configuraciones de formato predeterminadas. Solo definimos la fuente de datos, configuramos algunas propiedades, y el gráfico se crea con su formato predeterminado. Pero las API de Aspose.Cells para Python via .NET también admiten la creación de gráficos personalizados que permiten a los desarrolladores crear gráficos con sus propias configuraciones de formato.

Los desarrolladores pueden crear gráficos personalizados en tiempo de ejecución usando Aspose.Cells para Python via .NET.

Un gráfico está compuesto por una serie de datos. Cada serie en Aspose.Cells para Python via .NET está representada por un objeto [**Series**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series) mientras que el objeto [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) sirve como colección de objetos [**Series**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series). Al crear un gráfico personalizado, los desarrolladores tienen la libertad de usar diferentes tipos de gráficos para diferentes series de datos (recolectados en el objeto [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection)).

El código de ejemplo a continuación demuestra cómo crear gráficos personalizados. En este ejemplo, vamos a usar un gráfico de columnas para la primera serie de datos y un gráfico de líneas para la segunda serie. El resultado es que agregamos un gráfico de columnas, combinado con un gráfico de líneas, a la hoja de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-HowToCreateCustomChart-1.py" >}}

{{% alert color="primary" %}}

Actualmente, Aspose.Cells para Python via .NET solo admite gráficos personalizados que combinan gráficos de pastel, línea, columna y columna apilada, pero en futuras versiones se admitirá más variedad de gráficos.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
