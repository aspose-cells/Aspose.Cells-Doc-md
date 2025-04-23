---
title: Configuración de fuentes para la representación de hojas de cálculo
type: docs
weight: 10
url: /es/net/configuring-fonts-for-rendering-spreadsheets/
---

## **Escenarios de uso posibles**

Las API de Aspose.Cells proporcionan la capacidad de representar las hojas de cálculo en formatos de imagen, así como convertirlas a formatos PDF y XPS. Para maximizar la fidelidad de la conversión, es necesario que las fuentes utilizadas en la hoja de cálculo estén disponibles en el directorio de fuentes predeterminado del sistema operativo. En caso de que las fuentes requeridas no estén presentes, las API de Aspose.Cells intentarán sustituir las fuentes requeridas por las disponibles.

## **Selección de Fuentes**

A continuación se presenta el proceso que las API de Aspose.Cells siguen detrás de escena.

1. La API intenta encontrar las fuentes en el sistema de archivos que coincidan con el nombre de fuente exacto utilizado en la hoja de cálculo.
2. Si la API no puede encontrar las fuentes con el nombre exacto, intenta utilizar la fuente predeterminada especificada en la propiedad [**DefaultStyle.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) del libro de trabajo.
3. Si la API no puede localizar la fuente definida en la propiedad [**DefaultStyle.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) del libro de trabajo, intenta usar la fuente especificada en la propiedad [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont) o [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont).
4. Si la API no puede localizar la fuente definida en las propiedades [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont) o [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont), intenta usar la fuente especificada en la propiedad [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname).
5. Si la API no puede localizar la fuente definida en la propiedad [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname), intenta seleccionar las fuentes más adecuadas de todas las fuentes disponibles.
6. Por último, si la API no puede encontrar ninguna fuente en el sistema de archivos, representa la hoja de cálculo utilizando Arial.

{{% alert color="primary" %}}

Por lo general, las APIs de Aspose.Cells escanean los directorios de fuentes predeterminados del sistema operativo en Windows, Linux y MacOS por defecto. A partir de [Aspose.Cells for .NET 24.7](https://releases.aspose.com/cells/net/release-notes/2024/aspose-cells-for-net-24-7-release-notes/), las APIs también escanean los directorios de fuentes en la nube cacheados de Office por defecto.

{{% /alert %}}

## **Establecer Carpetas de Fuentes Personalizadas**

Las API de Aspose.Cells buscan en el directorio de fuentes predeterminado del sistema operativo las fuentes requeridas. En caso de que las fuentes requeridas no estén disponibles en el directorio de fuentes del sistema, las APIs buscarán en los directorios personalizados (definidos por el usuario). La clase [**FontConfigs**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs) ha expuesto varias formas de establecer directorios de fuentes personalizados, como se detalla a continuación.

1. [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder): Este método es útil si solo hay una carpeta que se va a establecer.
2. [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders): Este método es útil cuando las fuentes residen en varias carpetas y el usuario desea establecer todas las carpetas por separado en lugar de combinar todas las fuentes en una sola carpeta.
3. [**FontConfigs.SetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsources): Este mecanismo es útil cuando el usuario desea cargar fuentes desde varias carpetas o un solo archivo de fuente o datos de fuente de un array de bytes.

{{% alert color="primary" %}}

Ambos métodos [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder) y [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders) aceptan un segundo parámetro de tipo Boolean. Pasar **true** como segundo parámetro dirigirá a las API de Aspose.Cells a buscar subcarpetas para los archivos de fuentes.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-1.cs" >}}

{{% alert color="primary" %}}

Por favor, utilice cualquiera de los métodos mencionados anteriormente al iniciar la aplicación, es decir, antes de invocar otros objetos de las APIs de Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Si se utilizan todos los métodos mencionados anteriormente para establecer las fuentes, solo los últimos ajustes tendrán efecto.

{{% /alert %}}

## **Mecanismo de Sustitución de Fuentes**

Las API de Aspose.Cells también brindan la capacidad de especificar la fuente de sustitución para fines de representación. Este mecanismo es útil cuando una fuente requerida no está disponible en la máquina donde se debe realizar la conversión. Los usuarios pueden proporcionar una lista de nombres de fuentes como alternativa a la fuente originalmente requerida. Para lograr esto, las API de Aspose.Cells han expuesto el método [**FontConfigs.SetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsubstitutes) que acepta 2 parámetros. El primer parámetro es de tipo **string**, que debería ser el nombre de la fuente que necesita ser sustituida. El segundo parámetro es una matriz de tipo **string**. Los usuarios pueden proporcionar una lista de nombres de fuentes como sustitución del nombre de fuente original (especificado en el primer parámetro).

Aquí hay un escenario de uso simple.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-FontSubstitution.cs" >}}

## **Recopilación de información**

Además de los métodos mencionados anteriormente, las APIs de Aspose.Cells también han proporcionado medios para recopilar información sobre qué fuentes y sustituciones se han establecido.

1. El método [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources) devuelve un array de tipo [**FontSourceBase**](https://reference.aspose.com/cells/net/aspose.cells/fontsourcebase) que contiene la lista de fuentes especificadas. En caso de que no se hayan establecido fuentes, el método [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources) devolverá un array vacío.
1. El método [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes) acepta un parámetro de tipo **string** que permite especificar el nombre de la fuente para la cual se ha establecido una sustitución. En caso de que no se haya establecido una sustitución para el nombre de fuente especificado, entonces el método [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes) devolverá nulo.

## **Temas avanzados**
- [Establecer la fuente predeterminada al renderizar la hoja de cálculo a imágenes](/cells/es/net/set-default-font-while-rendering-spreadsheet-to-images/)
- [Establecer la propiedad DefaultFont de PdfSaveOptions e ImageOrPrintOptions para tener prioridad](/cells/es/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Formatos de fuente soportados](/cells/es/net/supported-font-formats/)
- [Hoja de cálculo a imagen - Establecer formato de píxel para la imagen renderizada](/cells/es/net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
{{< app/cells/assistant language="csharp" >}}
