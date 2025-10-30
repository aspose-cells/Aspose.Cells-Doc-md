---  
title: Temas y colores de Excel
linktitle: Temas y colores de Excel  
type: docs  
weight: 100  
url: /es/nodejs-cpp/excel-themes-and-colors/  
description: Aprende cómo usar esquemas de colores personalizados con Aspose.Cells for Node.js via C++.  
keywords: Crear y aplicar esquemas de colores en Node.js, Crear un esquema de color personalizado programáticamente en Node.js, cómo aplicar programáticamente un esquema de color personalizado en Node.js, Cómo usar esquemas de color en Excel con Node.js  
---  

## **Cómo aplicar y crear un esquema de colores en Excel**  
Los temas de documento facilitan la coordinación de colores, fuentes y efectos de formato gráfico de los documentos de Excel y su actualización rápida.  
Los temas proporcionan una apariencia unificada con estilos nombrados, efectos gráficos y otros objetos utilizados en un libro de trabajo. Por ejemplo, el estilo Accent1 se ve diferente en los temas Office y Apex. A menudo, aplicas un tema de documento y luego lo modificas según tus necesidades.  

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
Si se usan colores de tema en el archivo, no es necesario modificar cada celda individualmente; solo hay que modificar los colores en el tema.  

El siguiente ejemplo muestra cómo aplicar temas personalizados con tus colores deseados. Usamos un archivo de plantilla de ejemplo creado manualmente en Microsoft Excel 2007.  

El siguiente ejemplo carga un archivo de plantilla XLSX, define colores para diferentes tipos de colores de tema, aplica los colores personalizados y guarda el archivo de Excel.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-CreateCustomColorTheme.js" >}}



### **Cómo aplicar colores de tema en Aspose.Cells**  
El siguiente ejemplo aplica los colores de primer plano y fuente de una celda según los tipos de colores del tema predeterminado (del libro). También guarda el archivo de Excel en disco.  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-ApplyThemeColors.js" >}}


### **Cómo obtener y establecer colores de tema en Aspose.Cells**  
A continuación se presentan algunos métodos y propiedades que implementan los colores de tema.  

- [**Style.setForegroundThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setForegroundThemeColor-themecolor-): Se usa para establecer el color de primer plano.  
- [**Style.setBackgroundThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setBackgroundThemeColor-themecolor-): Se usa para establecer el color de fondo.  
- [**Font.setThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setThemeColor-themecolor-): Se usa para establecer el color de fuente.  
- [**Workbook.getThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getThemeColor-themecolortype-): Se usa para obtener un color de tema.  
- [**Workbook.setThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#setThemeColor-themecolortype-color-): Se usa para establecer un color de tema.  

El siguiente ejemplo muestra cómo obtener y establecer colores de tema.  

El siguiente ejemplo usa un archivo de plantilla XLSX, obtiene los colores para diferentes tipos de colores de tema, cambia los colores y guarda el archivo de Microsoft Excel.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-GetAndSetThemeColors.js" >}}


## **Temas avanzados**  
- [Extraer datos de tema del archivo de Excel](/cells/es/nodejs-cpp/extract-theme-data-from-excel-file/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
