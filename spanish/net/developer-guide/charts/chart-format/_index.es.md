---
title: Configuración de la apariencia del gráfico
description: Aprenda a configurar la apariencia de los gráficos en Aspose.Cells for .NET. Nuestra guía le mostrará cómo modificar los diseños, colores, fuentes y efectos de los gráficos para lograr el estilo visual deseado y mejorar sus hojas de trabajo.
keywords: Aspose.Cells for .NET, charting, chart appearance, layouts, colors, fonts, effects, worksheets.
linktitle: Formato de gráfico
type: docs
weight: 20
url: /es/net/setting-chart-appearance/
---
##  **Configuración de la apariencia del gráfico**
En Cómo crear un gráfico, brindamos una breve introducción a los tipos de gráficos y objetos de gráficos que ofrece Aspose.Cells y describimos cómo crear uno. Este artículo analiza cómo personalizar la apariencia de los gráficos estableciendo sus propiedades:

- Configuración del área del gráfico.
- Configuración de líneas del gráfico.
- Aplicando temas.
- Establecer títulos para gráficos y ejes.
- Trabajar con líneas de cuadrícula.
###  **Configuración del área del gráfico**
Hay diferentes tipos de áreas en un gráfico y Aspose.Cells brinda la flexibilidad de modificar la apariencia de cada área. Los desarrolladores pueden aplicar diferentes configuraciones de formato en un área cambiando su color de primer plano, color de fondo y formato de relleno, etc.

En el ejemplo que se muestra a continuación, hemos aplicado diferentes configuraciones de formato en diferentes tipos de áreas de un gráfico. Estas áreas incluyen:

- Área de parcela
- Área del gráfico
- Área de colección de series
- Área de un solo punto en una colección de series

El siguiente fragmento de código demuestra cómo configurar el área del gráfico.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartArea-1.cs" >}}
###  **Configuración de líneas de gráfico**
 Los desarrolladores también pueden aplicar diferentes tipos de estilos en las líneas o marcadores de datos del[SerieColección](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection). El siguiente fragmento de código demuestra cómo configurar líneas de gráfico usando Aspose.Cells API.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartLines-1.cs" >}}
###  **Aplicación de temas Microsoft Excel 2007/2010 a gráficos**
 Los desarrolladores pueden aplicar diferentes Microsoft temas/colores de Excel a[SerieColección](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)u otros objetos del gráfico como se muestra a continuación en el ejemplo.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ApplyingThemes-1.cs" >}}
###  **Establecer los títulos de gráficos o ejes**
 Puede utilizar Microsoft Excel para configurar los títulos de un gráfico y sus ejes en un entorno WYSIWYG. Aspose.Cells también permite a los desarrolladores configurar los títulos de un gráfico y sus ejes en tiempo de ejecución. Todos los gráficos y sus ejes contienen una[Título](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/title)propiedad que se puede utilizar para establecer sus títulos como se muestra a continuación en un ejemplo.

El siguiente fragmento de código demuestra cómo configurar títulos para gráficos y ejes.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingTitlesAxes-1.cs" >}}
###  **Trabajar con líneas de cuadrícula principales**
Es posible personalizar el aspecto de las líneas de cuadrícula principales. Oculte o muestre líneas de cuadrícula, o defina su color y otras configuraciones. A continuación, mostramos cómo ocultar líneas de cuadrícula y cómo cambiar su color.
####  **Ocultar líneas de división principales**
 Los desarrolladores pueden controlar la visibilidad de las principales líneas de cuadrícula configurando el[Es visible](https://reference.aspose.com/cells/net/aspose.cells.drawing/line/properties/isvisible) propiedad de la[Línea](https://reference.aspose.com/cells/net/aspose.cells.drawing/line) oponerse a**verdadero** o falso**.

El siguiente fragmento de código demuestra cómo ocultar las líneas de cuadrícula principales. Después de ocultar las líneas de cuadrícula principales, se agregará un gráfico de columnas a la hoja de trabajo que no tendrá líneas de cuadrícula.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-MajorGridlines-1.cs" >}}
####  **Cambiar la configuración de las líneas de división principales**
Los desarrolladores no sólo pueden controlar la visibilidad de las principales líneas de cuadrícula, sino también otras propiedades, incluido su color, etc.

El siguiente fragmento de código demuestra cómo cambiar el color de las líneas de cuadrícula principales. Después de configurar el color de las líneas de la cuadrícula principales, se agregará un gráfico de columnas a la hoja de trabajo con las líneas de la cuadrícula modificadas.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ChangingMajorGridlines-1.cs" >}}

##  **Temas avanzados**
- [Establecer el código de formato de valores de la serie de gráficos](/cells/es/net/set-the-values-format-code-of-chart-series/)
- [Establecer imagen como fondo Complete el gráfico](/cells/es/net/set-picture-as-background-fill-in-the-chart/)
