---
title: Temas y colores de Excel
type: docs
weight: 130
url: /es/java/excel-2007-themes-and-colors/
---
{{% alert color="primary" %}}

Los temas brindan una apariencia unificada con estilos con nombre, efectos gráficos y otros objetos utilizados en un libro de trabajo. Por ejemplo, el estilo Accent1 se ve diferente en los temas de Office y Apex. A menudo, aplica un tema de documento y luego lo modifica según sus necesidades.

**Aplicando temas en Microsoft Excel**

![todo:imagen_alternativa_texto](excel-2007-themes-and-colors_1.png)

{{% /alert %}}

## **Obtener y establecer colores de tema**

Aspose.Cells Las API proporcionan funciones para personalizar temas y colores. A continuación se muestran algunos métodos y propiedades que implementan los colores del tema.

- La propiedad Style.ForegroundThemeColor se puede utilizar para establecer el color de primer plano.
- La propiedad Style.BackgroundThemeColor se puede utilizar para establecer el color de fondo.
- La propiedad Font.ThemeColor se puede utilizar para establecer el color de la fuente.
- El método Workbook.getThemeColor se puede usar para obtener un color de tema.
- El método Workbook.setThemeColor se puede usar para establecer un color de tema.

El siguiente ejemplo muestra cómo obtener y establecer los colores del tema.

El siguiente ejemplo utiliza un archivo de plantilla XLSX, obtiene los colores para diferentes tipos de colores de tema, cambia los colores y guarda el archivo de Excel Microsoft.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSetThemeColors-GetSetThemeColors.java" >}}

### **Personalización de temas**

El siguiente ejemplo muestra cómo aplicar temas personalizados con los colores deseados. El ejemplo utiliza un archivo de plantilla de muestra creado manualmente en Microsoft Excel 2007.

**El archivo de plantilla CustomThemeColor.xlsx**

![todo:imagen_alternativa_texto](excel-2007-themes-and-colors_2.png)

El siguiente ejemplo carga un archivo de plantilla XLSX, define colores para diferentes tipos de colores de tema, aplica los colores personalizados y guarda el archivo de Excel.

**El archivo generado con colores de tema personalizados.**

![todo:imagen_alternativa_texto](excel-2007-themes-and-colors_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomizingThemes-CustomizingThemes.java" >}}

### **Uso de los colores del tema**

El siguiente ejemplo aplica los colores de fuente y de primer plano de una celda en función de los tipos de color del tema predeterminado (del libro de trabajo). También guarda el archivo de Excel en el disco.

El siguiente resultado se genera al ejecutar el código.

**Los colores del tema aplicados a la celda D3 de la hoja de cálculo** 

![todo:imagen_alternativa_texto](excel-2007-themes-and-colors_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseThemeColors-UseThemeColors.java" >}}

## **Temas avanzados**
- [Extraer datos del tema de un archivo de Excel](/cells/es/java/extract-theme-data-from-excel-file/)
