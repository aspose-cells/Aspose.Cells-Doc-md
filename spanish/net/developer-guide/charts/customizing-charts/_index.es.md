---
title: Personalización de gráficos
description: Aprenda a personalizar gráficos en Aspose.Cells for .NET. Nuestra guía le mostrará cómo modificar diseños de gráficos, agregar y formatear series de datos, ajustar ejes y aplicar varias opciones de formato para mejorar la apariencia y usabilidad de sus gráficos.
keywords: Aspose.Cells for .NET, charting, customization, layouts, data series, axes, formatting, appearance, usability.
type: docs
weight: 40
url: /es/net/customizing-charts/
---
{{% alert color="primary" %}}

##  **Crear gráficos personalizados**

Hasta ahora, cuando hemos analizado los gráficos, hemos analizado los gráficos estándar que tienen sus configuraciones de formato estándar. Solo definimos la fuente de datos, configuramos algunas propiedades y el gráfico se crea con su configuración de formato predeterminada. Pero las API Aspose.Cells también admiten la creación de gráficos personalizados que permiten a los desarrolladores crear gráficos con sus propias configuraciones de formato.

Los desarrolladores pueden crear gráficos personalizados en tiempo de ejecución utilizando Aspose.Cells.

 Un gráfico se compone de una serie de datos. Cada serie de datos en Aspose.Cells está representada por un[**Serie**](https://reference.aspose.com/cells/net/aspose.cells.charts/series) objeto mientras que[**SerieColección**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) objeto sirve como una colección de[**Serie**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)objetos. Al crear un gráfico personalizado, los desarrolladores tienen la libertad de utilizar diferentes tipos de gráficos para diferentes series de datos (recopilados en el[**SerieColección**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)objeto).

El siguiente código de ejemplo demuestra cómo crear gráficos personalizados. En este ejemplo, usaremos un gráfico de columnas para la primera serie de datos y un gráfico de líneas para la segunda serie. El resultado es que agregamos un gráfico de columnas, combinado con un gráfico de líneas, a la hoja de trabajo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateCustomChart-1.cs" >}}

{{% alert color="primary" %}}

Actualmente, Aspose.Cells solo admite gráficos personalizados que combinan gráficos circulares, de líneas, de columnas y de pila de columnas, pero en futuras versiones se admitirán más gráficos.

{{% /alert %}}
