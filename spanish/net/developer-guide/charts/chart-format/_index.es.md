---
title: Configuración de la Apariencia del Gráfico
description: Aprenda a configurar la apariencia de los gráficos en Aspose.Cells for .NET. Nuestra guía le mostrará cómo modificar los diseños, colores, fuentes y efectos del gráfico para lograr el estilo visual deseado y mejorar sus hojas de cálculo.
keywords: Aspose.Cells for .NET, gráficos, apariencia de gráficos, diseños, colores, fuentes, efectos, hojas de cálculo.
linktitle: Formato del Gráfico
type: docs
weight: 20
url: /es/net/setting-chart-appearance/
---

## **Configurar la apariencia del gráfico**
En Cómo crear un gráfico dimos una breve introducción a los tipos de gráficos y objetos de gráficos ofrecidos por Aspose.Cells, y describimos cómo crear uno. Este artículo discute cómo personalizar la apariencia de los gráficos configurando sus propiedades:

- Configurando el área del gráfico.
- Configurando las líneas del gráfico.
- Aplicando temas.
- Configurando títulos para gráficos y ejes.
- Trabajando con líneas de cuadrícula.
### **Configurando el área del gráfico**
Hay diferentes tipos de áreas en un gráfico y Aspose.Cells proporciona la flexibilidad para modificar la apariencia de cada área. Los desarrolladores pueden aplicar diferentes configuraciones de formato en un área cambiando su color de primer plano, color de fondo y formato de relleno, etc.

En el ejemplo dado a continuación, hemos aplicado diferentes configuraciones de formato en diferentes tipos de áreas de un gráfico. Estas áreas incluyen:

- Área de trazado
- Área del gráfico
- Área de la colección de series
- Área de un solo punto en una colección de series

El siguiente fragmento de código demuestra cómo configurar el área del gráfico.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartArea-1.cs" >}}
### **Configurando las líneas del gráfico**
Los desarrolladores también pueden aplicar diferentes tipos de estilos en las líneas o marcadores de datos de la [SeriesCollection](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection). El siguiente fragmento de código demuestra cómo configurar las líneas del gráfico usando la API de Aspose.Cells.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartLines-1.cs" >}}
### **Aplicando temas de Microsoft Excel 2007/2010 a gráficos**
Los desarrolladores pueden aplicar diferentes temas/colores de Microsoft Excel a la [SeriesCollection](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) u otros objetos de gráfico como se muestra a continuación en el ejemplo.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ApplyingThemes-1.cs" >}}
### **Configuración de los Títulos de Gráficos o Ejes**
Puede utilizar Microsoft Excel para establecer los títulos de un gráfico y sus ejes en un entorno WYSIWYG. Aspose.Cells también permite a los desarrolladores establecer los títulos de un gráfico y sus ejes en tiempo de ejecución. Todos los gráficos y sus ejes contienen una propiedad [Title](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/title) que se puede utilizar para establecer sus títulos como se muestra a continuación en un ejemplo.

El siguiente fragmento de código demuestra cómo establecer títulos en gráficos y ejes.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingTitlesAxes-1.cs" >}}
### **Trabajar con líneas de cuadrícula principales**
Es posible personalizar el aspecto de las líneas de cuadrícula principales. Ocultar o mostrar las líneas de cuadrícula, o definir su color y otras configuraciones. A continuación, mostramos cómo ocultar las líneas de cuadrícula y cómo cambiar su color.
#### **Ocultar líneas de cuadrícula principales**
Los desarrolladores pueden controlar la visibilidad de las líneas de cuadrícula principales estableciendo la [propiedad IsVisible](https://reference.aspose.com/cells/net/aspose.cells.drawing/line/properties/isvisible) del objeto [Línea](https://reference.aspose.com/cells/net/aspose.cells.drawing/line) en **true** o **false**.

El siguiente fragmento de código demuestra cómo ocultar las líneas de cuadrícula principales. Después de ocultar las líneas de cuadrícula principales, se agregará un gráfico de columnas a la hoja de cálculo sin líneas de cuadrícula.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-MajorGridlines-1.cs" >}}
#### **Cambiando la configuración de las líneas de cuadrícula principales**
Los desarrolladores no solo pueden controlar la visibilidad de las líneas de cuadrícula principales, sino también otras propiedades, incluido su color, etc.

El siguiente fragmento de código demuestra cómo cambiar el color de las líneas de cuadrícula principales. Después de establecer el color de las líneas de cuadrícula principales, se agregará un gráfico de columnas a la hoja de cálculo con líneas de cuadrícula modificadas.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ChangingMajorGridlines-1.cs" >}}

## **Temas avanzados**
- [Establecer el código de formato de valores de la serie del gráfico](/cells/es/net/set-the-values-format-code-of-chart-series/)
- [Establecer una imagen como relleno de fondo en el gráfico](/cells/es/net/set-picture-as-background-fill-in-the-chart/)
{{< app/cells/assistant language="csharp" >}}
