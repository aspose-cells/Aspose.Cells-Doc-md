---
title: Configuración de la Apariencia del Gráfico
description: Aprende cómo configurar la apariencia de los gráficos en Aspose.Cells para Python via .NET. Nuestra guía te mostrará cómo modificar diseños de gráficos, colores, fuentes y efectos para lograr el estilo visual deseado y mejorar tus hojas de cálculo.
keywords: Aspose.Cells para Python via .NET, gráficos, apariencia del gráfico, diseños, colores, fuentes, efectos, hojas de cálculo.
linktitle: Formato del Gráfico
type: docs
weight: 20
url: /es/python-net/setting-chart-appearance/
---

## **Configurar la apariencia del gráfico**
En Cómo Crear un Gráfico dimos una breve introducción a los tipos de gráficos y objetos de gráficos ofrecidos por Aspose.Cells para Python via .NET, y describimos cómo crear uno. Este artículo discute cómo personalizar la apariencia de los gráficos configurando sus propiedades:

- Configurando el área del gráfico.
- Configurando las líneas del gráfico.
- Aplicando temas.
- Configurando títulos para gráficos y ejes.
- Trabajando con líneas de cuadrícula.
### **Configurando el área del gráfico**
Existen diferentes tipos de áreas en un gráfico y Aspose.Cells para Python via .NET proporciona la flexibilidad para modificar la apariencia de cada área. Los desarrolladores pueden aplicar diferentes configuraciones de formato en un área cambiando su color de primer plano, fondo y formato de relleno, etc.

En el ejemplo dado a continuación, hemos aplicado diferentes configuraciones de formato en diferentes tipos de áreas de un gráfico. Estas áreas incluyen:

- Área de trazado
- Área del gráfico
- Área de la colección de series
- Área de un solo punto en una colección de series

El siguiente fragmento de código demuestra cómo configurar el área del gráfico.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-SettingChartArea-1.py" >}}

### **Configurando las líneas del gráfico**
Los desarrolladores también pueden aplicar diferentes estilos en las líneas o marcadores de datos de la [SeriesCollection](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection). El siguiente fragmento de código demuestra cómo establecer líneas de gráficos usando la API de Aspose.Cells para Python via .NET.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-SettingChartLines-1.py" >}}

### **Aplicando temas de Microsoft Excel 2007/2010 a gráficos**
Los desarrolladores pueden aplicar diferentes temas/colores de Microsoft Excel a [SeriesCollection](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) u otros objetos de gráficos como se muestra en el ejemplo a continuación.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-ApplyingThemes-1.py" >}}

### **Configuración de los Títulos de Gráficos o Ejes**
Puedes usar Microsoft Excel para establecer los títulos de un gráfico y sus ejes en un entorno WYSIWYG. Aspose.Cells para Python via .NET también permite a los desarrolladores establecer los títulos de un gráfico y sus ejes en tiempo de ejecución. Todos los gráficos y sus ejes contienen la propiedad [Chart.title](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/title) que puede usarse para establecer sus títulos como se muestra en el ejemplo a continuación.

El siguiente fragmento de código demuestra cómo establecer títulos en gráficos y ejes.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-SettingTitlesAxes-1.py" >}}

### **Trabajar con líneas de cuadrícula principales**
Es posible personalizar el aspecto de las líneas de cuadrícula principales. Ocultar o mostrar las líneas de cuadrícula, o definir su color y otras configuraciones. A continuación, mostramos cómo ocultar las líneas de cuadrícula y cómo cambiar su color.

#### **Ocultar líneas de cuadrícula principales**
Los desarrolladores pueden controlar la visibilidad de las líneas de cuadrícula principales estableciendo la propiedad [is_visible](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/line/is_visible) del objeto [Line](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/line) en **true** o **false**.

El siguiente fragmento de código demuestra cómo ocultar las líneas de cuadrícula principales. Después de ocultar las líneas de cuadrícula principales, se agregará un gráfico de columnas a la hoja de cálculo sin líneas de cuadrícula.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-MajorGridlines-1.py" >}}

#### **Cambiando la configuración de las líneas de cuadrícula principales**
Los desarrolladores no solo pueden controlar la visibilidad de las líneas de cuadrícula principales, sino también otras propiedades, incluido su color, etc.

El siguiente fragmento de código demuestra cómo cambiar el color de las líneas de cuadrícula principales. Después de establecer el color de las líneas de cuadrícula principales, se agregará un gráfico de columnas a la hoja de cálculo con líneas de cuadrícula modificadas.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-ChangingMajorGridlines-1.py" >}}

## **Temas avanzados**
- [Establecer el código de formato de valores de la serie del gráfico](/cells/es/python-net/set-the-values-format-code-of-chart-series/)
- [Establecer una imagen como relleno de fondo en el gráfico](/cells/es/python-net/set-picture-as-background-fill-in-the-chart/)
{{< app/cells/assistant language="python-net" >}}
