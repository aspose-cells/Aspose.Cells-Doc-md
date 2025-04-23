---
title: Temas y colores de Excel
type: docs
weight: 100
url: /es/net/excel-themes-and-colors/
description: Código C# para usar el esquema de colores de Excel con la API Aspose.Cells for .NET
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

## **Cómo crear y aplicar un esquema de colores en Aspose.Cells**
Aspose.Cells proporciona funciones para personalizar temas y colores.

### **Cómo crear un tema de colores personalizado en Aspose.Cells**
Si se utilizan colores de tema en el archivo, no es necesario modificar cada celda individualmente, solo necesitamos modificar los colores en el tema.

El siguiente ejemplo muestra cómo aplicar temas personalizados con tus colores deseados. Usamos un archivo de plantilla de ejemplo creado manualmente en Microsoft Excel 2007.

El siguiente ejemplo carga un archivo XLSX de plantilla, define colores para diferentes tipos de colores de tema, aplica los colores personalizados y guarda el archivo de Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-CustomizeThemes-1.cs" >}}

### **Cómo aplicar colores de tema en Aspose.Cells**

El siguiente ejemplo aplica colores de primer plano y fuente de una celda basados en los tipos de colors de tema predeterminados (del libro de trabajo). También guarda el archivo de Excel en disco.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-UtilizeThemeColors-1.cs" >}}

### **Cómo obtener y establecer colores de tema en Aspose.Cells**
 A continuación se presentan algunos métodos y propiedades que implementan los colores de tema.

- [**Style.ForegroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundthemecolor): Utilizado para establecer el color de primer plano.
- [**Style.BackgroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundthemecolor): Utilizado para establecer el color de fondo.
- [**Font.ThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/themecolor): Utilizado para establecer el color de fuente.
- [**Workbook.GetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getthemecolor): Utilizado para obtener un color de tema.
- [**Workbook.SetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/setthemecolor): Utilizado para establecer un color de tema.

El siguiente ejemplo muestra cómo obtener y establecer colores de tema.

El siguiente ejemplo utiliza un archivo XLSX de plantilla, obtiene los colores para diferentes tipos de colores de tema, cambia los colores y guarda el archivo de Microsoft Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-GetSetThemeColors-1.cs" >}}

## **Temas avanzados**
- [Extraer datos de tema del archivo de Excel](/cells/es/net/extract-theme-data-from-excel-file/)
{{< app/cells/assistant language="csharp" >}}
