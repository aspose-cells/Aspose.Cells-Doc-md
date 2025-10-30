---
title: Temas y colores de Excel
type: docs
weight: 100
url: /es/python-net/excel-themes-and-colors/
description: Código C# para usar el esquema de colores de Excel con Aspose.Cells para Python via .NET API
keywords: C# para crear y aplicar esquemas de colores, crear programáticamente un esquema de color personalizado, cómo aplicar programáticamente un esquema de color personalizado, c# cómo usar esquema de color en excel
---

## **Cómo aplicar y crear un esquema de colores en Excel**
Los temas de documento facilitan la coordinación de colores, fuentes y efectos de formato gráfico de los documentos de Excel y su actualización rápida. 
Los temas proporcionan un aspecto unificado con estilos nombrados, efectos gráficos y otros objetos utilizados en un libro. Por ejemplo, el estilo Acento 1, se ve diferente en los temas Oficina y Apex. A menudo, aplicas un tema de documento y luego lo modificas según tus preferencias.

### **Cómo aplicar un esquema de colores en Excel**
1. Abre Excel y ve a la pestaña "Diseño de página" en la cinta de opciones de Excel.
1. Haz clic en el botón "Colores" en la sección de "Temas".
<br>
<img src="color.png" width=70% />
1. Elige una paleta de colores que se ajuste a tus requisitos o pasa el cursor sobre un esquema para ver una vista previa en vivo.

### **Cómo crear un esquema de colores personalizado en Excel**
Puedes crear tu propio conjunto de colores para darle a tu documento un aspecto fresco y único o cumplir con los estándares de marca de tu organización.

1. Abre Excel y ve a la pestaña "Diseño de página" en la cinta de opciones de Excel.
1. Haz clic en el botón "Colores" en la sección de "Temas".
1. Haz clic en el botón "Personalizar colores...".
<br>
<img src="color2.png" width=70% />

1. En el cuadro de diálogo "Crear nuevos colores de tema", puedes seleccionar colores para cada elemento haciendo clic en las listas desplegables de colores junto a ellos. Puedes elegir colores de la paleta o definir colores personalizados usando la opción "Más colores".
<br>
<img src="color3.png" width=70% />
1. Después de seleccionar todos los colores deseados, proporciona un nombre para tu esquema de colores personalizado en el campo de "Nombre".

1. Haz clic en el botón "Guardar" para guardar tu esquema de colores personalizado. Ahora tu esquema de colores personalizado estará disponible en el menú desplegable de "Colores" para uso futuro.

## **Cómo crear y aplicar esquemas de color en Aspose.Cells para Python via .NET**
Aspose.Cells para Python via .NET ofrece funciones para personalizar temas y colores.

### **Cómo crear un tema de color personalizado en Aspose.Cells para Python via .NET**
Si se utilizan colores de tema en el archivo, no es necesario modificar cada celda individualmente, solo necesitamos modificar los colores en el tema.

El siguiente ejemplo muestra cómo aplicar temas personalizados con tus colores deseados. Usamos un archivo de plantilla de ejemplo creado manualmente en Microsoft Excel 2007.

El siguiente ejemplo carga un archivo XLSX de plantilla, define colores para diferentes tipos de colores de tema, aplica los colores personalizados y guarda el archivo de Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-CustomizeThemes-1.py" >}}

### **Cómo aplicar colores de tema en Aspose.Cells para Python via .NET**

El siguiente ejemplo aplica colores de primer plano y fuente de una celda basados en los tipos de colors de tema predeterminados (del libro de trabajo). También guarda el archivo de Excel en disco.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UtilizeThemeColors-1.py" >}}

### **Cómo obtener y establecer colores de tema en Aspose.Cells para Python via .NET**
 A continuación se presentan algunos métodos y propiedades que implementan los colores de tema.

- [**Style.foreground_theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_theme_color): Utilizado para establecer el color de primer plano.
- [**Style.background_theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/background_theme_color): Utilizado para establecer el color de fondo.
- [**Font.theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/theme_color): Utilizado para establecer el color de fuente.
- [**Workbook.get_theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/get_theme_color): Utilizado para obtener un color de tema.
- [**Workbook.set_theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/set_theme_color): Utilizado para establecer un color de tema.

El siguiente ejemplo muestra cómo obtener y establecer colores de tema.

El siguiente ejemplo utiliza un archivo XLSX de plantilla, obtiene los colores para diferentes tipos de colores de tema, cambia los colores y guarda el archivo de Microsoft Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-GetSetThemeColors-1.py" >}}

## **Temas avanzados**
- [Extraer datos de tema del archivo de Excel](/cells/es/python-net/extract-theme-data-from-excel-file/)

{{< app/cells/assistant language="python-net" >}}
