---
title: Temas y colores de Excel
type: docs
weight: 130
url: /es/java/excel-2007-themes-and-colors/
---

{{% alert color="primary" %}}

Los temas proporcionan un aspecto unificado con estilos denominados, efectos gráficos y otros objetos utilizados en un libro de trabajo. Por ejemplo, el estilo Acento1 se ve diferente en los temas de Office y Apex. A menudo, se aplica un tema de documento y luego se modifica según sus necesidades.

**Aplicar temas en Microsoft Excel**

![todo:image_alt_text](excel-2007-themes-and-colors_1.png)

{{% /alert %}}

## **Obtener y configurar colores de tema**

Las API de Aspose.Cells proporcionan funciones para personalizar temas y colores. A continuación se muestran algunos métodos y propiedades que implementan colores de tema.

- La propiedad Style.ForegroundThemeColor se puede utilizar para establecer el color de primer plano.
- La propiedad Style.BackgroundThemeColor se puede utilizar para establecer el color de fondo.
- La propiedad Font.ThemeColor se puede utilizar para establecer el color de fuente.
- El método Workbook.getThemeColor se puede utilizar para obtener un color de tema.
- El método Workbook.setThemeColor se puede utilizar para establecer un color de tema.

El siguiente ejemplo muestra cómo obtener y establecer colores de tema.

El siguiente ejemplo utiliza un archivo XLSX de plantilla, obtiene los colores para diferentes tipos de colores de tema, cambia los colores y guarda el archivo de Microsoft Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSetThemeColors-GetSetThemeColors.java" >}}

### **Personalización de Temas**

El siguiente ejemplo muestra cómo aplicar temas personalizados con los colores deseados. El ejemplo utiliza un archivo de plantilla de muestra creado manualmente en Microsoft Excel 2007.

**El archivo de plantilla CustomThemeColor.xlsx**

![todo:image_alt_text](excel-2007-themes-and-colors_2.png)

El siguiente ejemplo carga un archivo XLSX de plantilla, define colores para diferentes tipos de colores de tema, aplica los colores personalizados y guarda el archivo de Excel.

**El archivo generado con colores de tema personalizados**

![todo:image_alt_text](excel-2007-themes-and-colors_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomizingThemes-CustomizingThemes.java" >}}

### **Uso de Colores de Tema**

El siguiente ejemplo aplica colores de primer plano y fuente de una celda basados en los tipos de colors de tema predeterminados (del libro de trabajo). También guarda el archivo de Excel en disco.

La siguiente salida se genera al ejecutar el código.

**Los colores de tema se aplican a la celda D3 de la hoja de cálculo** 

![todo:image_alt_text](excel-2007-themes-and-colors_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseThemeColors-UseThemeColors.java" >}}

## **Temas avanzados**
- [Extraer datos de tema del archivo de Excel](/cells/es/java/extract-theme-data-from-excel-file/)
{{< app/cells/assistant language="java" >}}
