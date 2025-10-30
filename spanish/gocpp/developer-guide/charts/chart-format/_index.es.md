---
title: Configuración de la apariencia del gráfico con Golang a través de C++
linktitle: Formato del Gráfico
description: Aprenda cómo configurar la apariencia de los gráficos en Aspose.Cells for C++. Nuestra guía mostrará cómo modificar el diseño, colores, fuentes y efectos del gráfico para lograr el estilo visual deseado y mejorar sus hojas de cálculo.
keywords: Aspose.Cells for C++, gráficos, apariencia del gráfico, diseños, colores, fuentes, efectos, hojas de cálculo.
type: docs
weight: 20
url: /es/go-cpp/setting-chart-appearance/
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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat.go" >}}
### **Configurando las líneas del gráfico**
Los desarrolladores también pueden aplicar diferentes estilos en las líneas o marcadores de datos de la [SeriesCollection](https://reference.aspose.com/cells/go-cpp/seriescollection/). El siguiente fragmento de código demuestra cómo configurar las líneas del gráfico usando la API de Aspose.Cells.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-1.go" >}}
### **Aplicando temas de Microsoft Excel 2007/2010 a gráficos**
Los desarrolladores pueden aplicar diferentes temas/colores de Microsoft Excel a la [SeriesCollection](https://reference.aspose.com/cells/go-cpp/seriescollection/) u otros objetos de gráficos, como se muestra en el ejemplo.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-2.go" >}}
### **Configuración de los Títulos de Gráficos o Ejes**
Puedes usar Microsoft Excel para establecer los títulos de un gráfico y sus ejes en un entorno WYSIWYG. Aspose.Cells también permite a los desarrolladores establecer los títulos de un gráfico y sus ejes en tiempo de ejecución. Todos los gráficos y sus ejes contienen una propiedad [Title](https://reference.aspose.com/cells/go-cpp/title/) que puede usarse para establecer sus títulos, como se muestra en el ejemplo.

El siguiente fragmento de código demuestra cómo establecer títulos en gráficos y ejes.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-3.go" >}}
### **Trabajar con líneas de cuadrícula principales**
Es posible personalizar el aspecto de las líneas de cuadrícula principales. Ocultar o mostrar las líneas de cuadrícula, o definir su color y otras configuraciones. A continuación, mostramos cómo ocultar las líneas de cuadrícula y cómo cambiar su color.

#### **Ocultar líneas de cuadrícula principales**
Los desarrolladores pueden controlar la visibilidad de las principales líneas de cuadrícula configurando la propiedad [IsVisible](https://reference.aspose.com/cells/go-cpp/line/isvisible/) del objeto [Line](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/line/) a **true** o **false**.

El siguiente fragmento de código demuestra cómo ocultar las líneas de cuadrícula principales. Después de ocultar las líneas de cuadrícula principales, se agregará un gráfico de columnas a la hoja de cálculo sin líneas de cuadrícula.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-4.go" >}}
#### **Cambiando la configuración de las líneas de cuadrícula principales**
Los desarrolladores no solo pueden controlar la visibilidad de las líneas de cuadrícula principales, sino también otras propiedades, incluido su color, etc.

El siguiente fragmento de código demuestra cómo cambiar el color de las líneas de cuadrícula principales. Después de establecer el color de las líneas de cuadrícula principales, se agregará un gráfico de columnas a la hoja de cálculo con líneas de cuadrícula modificadas.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-5.go" >}}
## **Temas avanzados**
- [Establecer el código de formato de valores de la serie del gráfico](/cells/es/cpp/set-the-values-format-code-of-chart-series/)
- [Establecer una imagen como relleno de fondo en el gráfico](/cells/es/cpp/set-picture-as-background-fill-in-the-chart/)
