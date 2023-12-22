---
title: Temas y colores de Excel
type: docs
weight: 100
url: /es/net/excel-themes-and-colors/
description: Código C# para usar el esquema de color de Excel con Aspose.Cells for .NET API
keywords: C# to Create and Apply Color Schemes, c# programmatically Create a Custom Color Scheme, programmatically how to Apply a Custom Color Scheme, c# how to Use Color Scheme in excel
---
##  **Cómo aplicar y crear una combinación de colores en Excel**
Los temas de documentos facilitan la coordinación de colores, fuentes y efectos de formato gráfico de documentos de Excel y su actualización rápida.
Los temas brindan una apariencia unificada con estilos con nombre, efectos gráficos y otros objetos utilizados en un libro. Por ejemplo, el estilo Accent1 se ve diferente en los temas Office y Apex. A menudo, aplica un tema de documento y luego lo modifica como lo desea.

###  **Cómo aplicar una combinación de colores en Excel**
1. Abra Excel y vaya a la pestaña "Diseño de página" en la cinta de Excel.
1. Haga clic en el botón "Colores" en la sección "Temas".
<br>
<img src="color.png" width=70% />
1. Elija una paleta de colores que coincida con sus requisitos o coloque el cursor sobre un esquema para ver una vista previa en vivo.

###  **Cómo crear una combinación de colores personalizada en Excel**
Puede crear su propio conjunto de colores para darle a su documento una apariencia nueva y única o cumplir con los estándares de marca de su organización.

1. Abra Excel y vaya a la pestaña "Diseño de página" en la cinta de Excel.
1. Haga clic en el botón "Colores" en la sección "Temas".
1. Haga clic en el botón "Personalizar colores...".
<br>
<img src="color2.png" width=70% />

1. En el cuadro de diálogo "Crear nuevos colores de tema", puede seleccionar colores para cada elemento haciendo clic en los menús desplegables de colores junto a ellos. Puede elegir colores de la paleta o definir colores personalizados usando la opción "Más colores".
<br>
<img src="color3.png" width=70% />
1. Después de seleccionar todos los colores deseados, proporcione un nombre para su combinación de colores personalizada en el campo "Nombre".

1. Haga clic en el botón "Guardar" para guardar su combinación de colores personalizada. Su combinación de colores personalizada ahora estará disponible en el menú desplegable "Colores" para uso futuro.

##  **Cómo crear y aplicar una combinación de colores en Aspose.Cells**
Aspose.Cells proporciona funciones para personalizar temas y colores.

###  **Cómo crear un tema de color personalizado en Aspose.Cells**
Si se usan colores de tema en el archivo, no necesitamos modificar cada celda individualmente, solo necesitamos modificar los colores en el tema.

El siguiente ejemplo muestra cómo aplicar temas personalizados con los colores deseados. Usamos un archivo de plantilla de muestra creado manualmente en Microsoft Excel 2007.

El siguiente ejemplo carga un archivo de plantilla XLSX, define colores para diferentes tipos de colores de tema, aplica los colores personalizados y guarda el archivo de Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-CustomizeThemes-1.cs" >}}

###  **Cómo aplicar colores de tema en Aspose.Cells**

El siguiente ejemplo aplica los colores de primer plano y de fuente de una celda según los tipos de color del tema predeterminado (del libro). También guarda el archivo de Excel en el disco.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-UtilizeThemeColors-1.cs" >}}

###  **Cómo obtener y configurar colores de tema en Aspose.Cells**
 A continuación se muestran algunos métodos y propiedades que implementan colores de tema.

- [**Estilo.ForegroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundthemecolor): Se utiliza para establecer el color de primer plano.
- [**Estilo.FondoTemaColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundthemecolor): Se utiliza para establecer el color de fondo.
- [**Fuente.TemaColor**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/themecolor): Se utiliza para configurar el color de fuente.
- [**Libro de trabajo.GetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getthemecolor): Se utiliza para obtener un color de tema.
- [**Libro de trabajo.SetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/setthemecolor): Se utiliza para establecer un color de tema.

El siguiente ejemplo muestra cómo obtener y configurar colores de tema.

El siguiente ejemplo utiliza un archivo de plantilla XLSX, obtiene los colores para diferentes tipos de colores de tema, cambia los colores y guarda el archivo de Excel Microsoft.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-GetSetThemeColors-1.cs" >}}

##  **Temas avanzados**
- [Extraer datos del tema del archivo Excel](/cells/es/net/extract-theme-data-from-excel-file/)
