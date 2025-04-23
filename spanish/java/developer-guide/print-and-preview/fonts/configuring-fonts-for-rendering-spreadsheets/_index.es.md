---
title: Configuración de fuentes para la representación de hojas de cálculo
type: docs
weight: 10
url: /es/java/configuring-fonts-for-rendering-spreadsheets/
---

## **Escenarios de uso posibles**

Las API de Aspose.Cells proporcionan la capacidad de representar las hojas de cálculo en formatos de imagen, así como convertirlas a formatos PDF y XPS. Para maximizar la fidelidad de la conversión, es necesario que las fuentes utilizadas en la hoja de cálculo estén disponibles en el directorio de fuentes predeterminado del sistema operativo. En caso de que las fuentes requeridas no estén presentes, las API de Aspose.Cells intentarán sustituir las fuentes requeridas por las disponibles.

## **Selección de Fuentes**

A continuación se presenta el proceso que las API de Aspose.Cells siguen detrás de escena.

1. La API intenta encontrar las fuentes en el sistema de archivos que coincidan con el nombre de fuente exacto utilizado en la hoja de cálculo.
2. Si la API no puede encontrar las fuentes con el nombre exacto, intenta utilizar la fuente predeterminada especificada en la propiedad [**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) del libro de trabajo.
3. Si la API no puede localizar la fuente definida en la propiedad [**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) del libro de trabajo, intenta usar la fuente especificada en la propiedad [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) o [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont).
4. Si la API no puede localizar la fuente definida en las propiedades [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) o [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont), intenta usar la fuente especificada en la propiedad [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName).
5. Si la API no puede localizar la fuente definida en la propiedad [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName), intenta seleccionar las fuentes más adecuadas de todas las fuentes disponibles.
6. Por último, si la API no puede encontrar ninguna fuente en el sistema de archivos, representa la hoja de cálculo utilizando Arial.

{{% alert color="primary" %}}

Por lo general, las APIs de Aspose.Cells escanean los directorios de fuentes predeterminados del sistema operativo en Windows, Linux, MacOS por defecto. A partir de [Aspose.Cells for Java 24.7](https://releases.aspose.com/cells/java/release-notes/2024/aspose-cells-for-java-24-7-release-notes/), las APIs además escanean los directorios de fuentes en la nube en caché de Office por defecto.

{{% /alert %}}

{{% alert color="primary" %}}

Las APIs de Aspose.Cells siempre escanean el directorio de fuentes predeterminado del sistema operativo con una excepción, que es; cuando se establecen los argumentos JVM **-DAspose.Cells.FontDirExc="YourFontDir"**. En ese caso, las APIs de Aspose.Cells omitirán la exploración del directorio de fuentes predeterminado del sistema operativo y buscarán solo en la ruta especificada en los argumentos JVM mencionados.

{{% /alert %}}

## **Establecer Carpetas de Fuentes Personalizadas**

Las API Aspose.Cells buscan el directorio de fuentes predeterminado del sistema operativo para las fuentes requeridas. En caso de que las fuentes requeridas no estén disponibles en el directorio de fuentes del sistema, las APIs buscarán en los directorios personalizados (definidos por el usuario). La clase [**FontConfigs**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs) ha expuesto varias formas de establecer directorios de fuentes personalizados como se detalla a continuación.

1. [**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder-java.lang.String-boolean-): Este método es útil si solo hay una carpeta que se va a establecer.
2. [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders-java.lang.String[]-boolean-): Este método es útil cuando las fuentes residen en varias carpetas y el usuario desea establecer todas las carpetas por separado en lugar de combinar todas las fuentes en una sola carpeta.
3. [**FontConfigs.setFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontSources-com.aspose.cells.FontSourceBase[]-): Este mecanismo es útil cuando el usuario desea cargar fuentes desde varias carpetas o un solo archivo de fuente o datos de fuente de un array de bytes.

{{% alert color="primary" %}}

Ambos métodos [**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder-java.lang.String-boolean-) y [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders-java.lang.String[]-boolean-) aceptan un segundo parámetro de tipo Booleano. Pasar **true** como segundo parámetro dirigirá a las APIs Aspose.Cells a buscar en las subcarpetas de los archivos de fuentes.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetCustomFontFolders-SetCustomFontFolders.java" >}}

{{% alert color="primary" %}}

Utilice cualquiera de los métodos mencionados anteriormente al inicio de la aplicación, es decir; antes de invocar cualquier otro objeto de las APIs Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Si se utilizan más de uno de los métodos mencionados anteriormente para establecer las fuentes, solo la última configuración tendrá efecto.

{{% /alert %}}

## **Mecanismo de Sustitución de Fuentes**

Las APIs Aspose.Cells también proporcionan la capacidad de especificar la fuente de sustitución para fines de renderizado. Este mecanismo es útil cuando una fuente requerida no está disponible en la máquina donde se va a realizar la conversión. Los usuarios pueden proporcionar una lista de nombres de fuentes como alternativa a la fuente originalmente requerida. Para lograr esto, las APIs Aspose.Cells han expuesto el método FontConfigs.setFontSubstitutes que acepta 2 parámetros. El primer parámetro es de tipo **String**, que debe ser el nombre de la fuente que debe ser sustituida. El segundo parámetro es una matriz de tipo **String**. Los usuarios pueden proporcionar una lista de nombres de fuentes como sustitutos de la fuente original (especificada en el primer parámetro).

Aquí hay un escenario de uso simple.

{{< highlight java >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[] { "Times New Roman", "Calibri" });

{{< /highlight >}}

## **Recopilación de información**

Además de los métodos mencionados anteriormente, las APIs de Aspose.Cells también han proporcionado medios para recopilar información sobre qué fuentes y sustituciones se han establecido.

1. [**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources--): Este método devuelve una matriz de tipo [**FontSourceBase**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFontSource) que contiene la lista de fuentes especificadas. En caso de que no se hayan establecido fuentes, el método [**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources--) devolverá una matriz vacía.
1. [**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes-java.lang.String-): Este método acepta un parámetro de tipo **String** que permite especificar el nombre de la fuente para la cual se ha establecido la sustitución. En caso de que no se haya establecido ninguna sustitución para el nombre de fuente especificado, entonces el método [**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes-java.lang.String-) devolverá null.
{{< app/cells/assistant language="java" >}}
