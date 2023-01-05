---
title: Configuración de fuentes para renderizar hojas de cálculo
type: docs
weight: 10
url: /es/java/configuring-fonts-for-rendering-spreadsheets/
---
## **Posibles escenarios de uso**

Las API Aspose.Cells brindan la posibilidad de representar las hojas de cálculo en formatos de imagen, así como convertirlas a los formatos PDF y XPS. Para maximizar la fidelidad de la conversión, es necesario que las fuentes utilizadas en la hoja de cálculo estén disponibles en el directorio de fuentes predeterminado del sistema operativo. En caso de que las fuentes requeridas no estén presentes, las API Aspose.Cells intentarán sustituir las fuentes requeridas por las disponibles.

## **Selección de fuentes**

A continuación se muestra el proceso que siguen las API Aspose.Cells detrás de escena.

1. El API intenta encontrar las fuentes en el sistema de archivos que coincidan con el nombre de fuente exacto utilizado en la hoja de cálculo.
1.  Si API no puede encontrar las fuentes con exactamente el mismo nombre, intenta usar la fuente predeterminada especificada en el Libro de trabajo.[**DefaultStyle.Fuente**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) propiedad.
1.  Si API no puede localizar la fuente definida en el libro de trabajo[**DefaultStyle.Fuente**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) propiedad, intenta utilizar la fuente especificada en[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) o[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont) propiedad.
1.  Si API no puede localizar la fuente definida en[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) o[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont) propiedad, intenta utilizar la fuente especificada en[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName) propiedad.
1.  Si API no puede localizar la fuente definida en[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName) propiedad, intenta seleccionar las fuentes más adecuadas de todas las fuentes disponibles.
1. Finalmente, si API no puede encontrar ninguna fuente en el sistema de archivos, procesa la hoja de cálculo usando Arial.

{{% alert color="primary" %}}

 Las API Aspose.Cells siempre escanean el directorio de fuentes predeterminado del sistema operativo con una excepción, es decir; cuando los argumentos de JVM**-DAspose.Cells.FontDirExc="TuFontDir"**se establecen. En ese caso, las API Aspose.Cells omitirán el escaneo del directorio de fuentes predeterminado del sistema operativo y solo buscarán la ruta como se especifica en los argumentos JVM mencionados anteriormente.

{{% /alert %}}

## **Establecer carpetas de fuentes personalizadas**

 Aspose.Cells Las API buscan en el directorio de fuentes predeterminado del sistema operativo las fuentes requeridas. En caso de que las fuentes requeridas no estén disponibles en el directorio de fuentes del sistema, las API buscan en los directorios personalizados (definidos por el usuario). Él[**FontConfigs**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs)class ha expuesto varias formas de establecer directorios de fuentes personalizados como se detalla a continuación.

1. [**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)): este método es útil si solo hay una carpeta para configurar.
1. [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean)): este método es útil cuando las fuentes residen en varias carpetas y el usuario desea configurar todas las carpetas por separado en lugar de combinar todas las fuentes en una sola carpeta.
1. [**FontConfigs.setFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontSources(com.aspose.cells.FontSourceBase[])): este mecanismo es útil cuando el usuario desea cargar fuentes de varias carpetas o un solo archivo de fuentes o datos de fuentes de una matriz de bytes.

{{% alert color="primary" %}}

 Ambos[**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)) & [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean) ) Los métodos aceptan un segundo parámetro de tipo booleano. Paso**verdadero**como segundo parámetro dirigirá las API Aspose.Cells para buscar las subcarpetas de los archivos de fuentes.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetCustomFontFolders-SetCustomFontFolders.java" >}}

{{% alert color="primary" %}}

Utilice cualquiera de los métodos mencionados anteriormente al inicio de la aplicación, es decir; antes de invocar cualquier otro objeto de las API Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Si se utiliza más de uno de los métodos mencionados anteriormente para configurar las fuentes de fuente, solo se aplicará la última configuración.

{{% /alert %}}

## **Mecanismo de sustitución de fuentes**

Las API Aspose.Cells también brindan la capacidad de especificar la fuente sustituta para fines de representación. Este mecanismo es útil cuando una fuente requerida no está disponible en la máquina donde se debe realizar la conversión. Los usuarios pueden proporcionar una lista de nombres de fuentes como alternativa a la fuente requerida originalmente. Para lograr esto, las API Aspose.Cells han expuesto el método FontConfigs.setFontSubstitutes que acepta 2 parámetros. El primer parámetro es de tipo**Cadena** , que debe ser el nombre de la fuente que debe sustituirse. El segundo parámetro es una matriz de tipo**Cadena**. Los usuarios pueden proporcionar una lista de nombres de fuentes como sustitutos de la fuente original (especificada en el primer parámetro).

Aquí hay un escenario de uso simple.

{{< highlight "java" >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[]{ "Times New Roman", "Calibri" });

{{< /highlight >}}

## **Recopilación de información**

Además de los métodos mencionados anteriormente, las API Aspose.Cells también han proporcionado medios para recopilar información sobre qué fuentes y sustituciones se han establecido.

1. [**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources() ): este método devuelve una matriz de tipo[**FuenteFuenteBase**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFontSource)que contiene la lista de fuentes de fuentes especificadas. En caso de que no se hayan establecido fuentes, el[**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources()) devolverá una matriz vacía.
1. [**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String) ): este método acepta un parámetro de tipo**Cadena** permitiendo especificar el nombre de la fuente para la que se ha establecido la sustitución. En caso de que no se haya establecido ninguna sustitución para el nombre de fuente especificado, el[**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String)) método devolverá nulo.
