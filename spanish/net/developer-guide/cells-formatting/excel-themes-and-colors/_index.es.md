---
title: Temas y colores de Excel
type: docs
weight: 100
url: /es/net/excel-themes-and-colors/
---
## **Temas y colores de Excel**

Los temas brindan una apariencia unificada con estilos con nombre, efectos gráficos y otros objetos utilizados en un libro de trabajo. Por ejemplo, el estilo Accent1, por ejemplo, se ve diferente en los temas de Office y Apex. A menudo, aplica un tema de documento y luego lo modifica como lo desea.

Aspose.Cells proporciona funciones para personalizar temas y colores.

### **Obtener y establecer colores de tema**

A continuación se muestran algunos métodos y propiedades que implementan los colores del tema.

- [**Estilo.ForegroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundthemecolor): Se utiliza para establecer el color de primer plano.
- [**Estilo.BackgroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundthemecolor): Se utiliza para establecer el color de fondo.
- [**Fuente.TemaColor**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/themecolor): Se utiliza para establecer el color de la fuente.
- [**Libro de trabajo.GetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getthemecolor): Se utiliza para obtener un color de tema.
- [**Libro de trabajo.SetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/setthemecolor): Se utiliza para establecer un color de tema.

El siguiente ejemplo muestra cómo obtener y establecer los colores del tema.

El siguiente ejemplo utiliza un archivo de plantilla XLSX, obtiene los colores para diferentes tipos de colores de tema, cambia los colores y guarda el archivo de Excel Microsoft.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-GetSetThemeColors-1.cs" >}}

#### **Personalizar temas**

El siguiente ejemplo muestra cómo aplicar temas personalizados con los colores deseados. Usamos un archivo de plantilla de muestra creado manualmente en Microsoft Excel 2007.

El siguiente ejemplo carga un archivo de plantilla XLSX, define colores para diferentes tipos de colores de tema, aplica los colores personalizados y guarda el archivo de Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-CustomizeThemes-1.cs" >}}

#### **Usar colores del tema**

El siguiente ejemplo aplica los colores de fuente y de primer plano de una celda en función de los tipos de color del tema predeterminado (del libro de trabajo). También guarda el archivo de Excel en el disco.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-UtilizeThemeColors-1.cs" >}}

## **Temas avanzados**
- [Extraer datos del tema de un archivo de Excel](/cells/es/net/extract-theme-data-from-excel-file/)
