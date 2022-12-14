---
title: Configuración de fuentes para renderizar hojas de cálculo
type: docs
weight: 10
url: /es/net/configuring-fonts-for-rendering-spreadsheets/
---
## **Posibles escenarios de uso**

Las API Aspose.Cells brindan la posibilidad de representar las hojas de cálculo en formatos de imagen, así como convertirlas a formatos PDF y XPS. Para maximizar la fidelidad de la conversión, es necesario que las fuentes utilizadas en la hoja de cálculo estén disponibles en el directorio de fuentes predeterminado del sistema operativo. En caso de que las fuentes requeridas no estén presentes, las API Aspose.Cells intentarán sustituir las fuentes requeridas por las disponibles.

## **Selección de fuentes**

A continuación se muestra el proceso que siguen las API Aspose.Cells detrás de escena.

1. El API intenta encontrar las fuentes en el sistema de archivos que coincidan con el nombre de fuente exacto utilizado en la hoja de cálculo.
1.  Si API no puede encontrar las fuentes con exactamente el mismo nombre, intenta usar la fuente predeterminada especificada en el Libro de trabajo.**[DefaultStyle.Font](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)** propiedad.
1.  Si API no puede localizar la fuente definida en el libro de trabajo**[DefaultStyle.Font](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)** propiedad, intenta utilizar la fuente especificada en**[PdfSaveOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)** o**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)** propiedad.
1.  Si API no puede localizar la fuente definida en**[PdfSaveOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)** o**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)** propiedad, intenta utilizar la fuente especificada en**[FontConfigs.DefaultFontName](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname)** propiedad.
1.  Si API no puede localizar la fuente definida en**[FontConfigs.DefaultFontName](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname)** propiedad, intenta seleccionar las fuentes más adecuadas de todas las fuentes disponibles.
1. Finalmente, si API no puede encontrar ninguna fuente en el sistema de archivos, procesa la hoja de cálculo usando Arial.

## **Establecer carpetas de fuentes personalizadas**

 Aspose.Cells Las API buscan en el directorio de fuentes predeterminado del sistema operativo las fuentes requeridas. En caso de que las fuentes requeridas no estén disponibles en el directorio de fuentes del sistema, las API buscan en los directorios personalizados (definidos por el usuario). los**[Configuraciones de fuentes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs)**class ha expuesto varias formas de establecer directorios de fuentes personalizados como se detalla a continuación.

1. **[FontConfigs.SetFontFolder](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder)**: Este método es útil si solo hay una carpeta para configurar.
1. **[FontConfigs.SetFontFolders](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders)**: este método es útil cuando las fuentes residen en varias carpetas y el usuario desea configurar todas las carpetas por separado en lugar de combinar todas las fuentes en una sola carpeta.
1. **[FontConfigs.SetFontSources](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsources)**: este mecanismo es útil cuando el usuario desea cargar fuentes de varias carpetas o un solo archivo de fuentes o datos de fuentes de una matriz de bytes.

{{% alert color="primary" %}}

 Ambas cosas**[FontConfigs.SetFontFolder](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder)** & **[FontConfigs.SetFontFolders](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders)** Los métodos aceptan un segundo parámetro de tipo booleano. Paso**verdadero** ya que el segundo parámetro dirigirá a las API Aspose.Cells para buscar las subcarpetas de los archivos de fuentes.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-1.cs" >}}

{{% alert color="primary" %}}

Utilice cualquiera de los métodos mencionados anteriormente al inicio de la aplicación, es decir; antes de invocar cualquier otro objeto de las API Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Si se utilizan todos los métodos mencionados anteriormente para configurar las fuentes de fuente, solo tendrán efecto los últimos ajustes.

{{% /alert %}}

## **Mecanismo de sustitución de fuentes**

 Las API Aspose.Cells también brindan la capacidad de especificar la fuente sustituta para fines de representación. Este mecanismo es útil cuando una fuente requerida no está disponible en la máquina donde se debe realizar la conversión. Los usuarios pueden proporcionar una lista de nombres de fuentes como alternativa a la fuente requerida originalmente. Para lograr esto, las API Aspose.Cells han expuesto el**[FontConfigs.SetFontSubstitutes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsubstitutes)** método que acepta 2 parámetros. El primer parámetro es de tipo**cuerda** , que debe ser el nombre de la fuente que debe sustituirse. El segundo parámetro es una matriz de tipo**cuerda**Los usuarios pueden proporcionar una lista de nombres de fuentes como sustitución del nombre de fuente original (especificado en el primer parámetro).

Aquí hay un escenario de uso simple.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-FontSubstitution.cs" >}}

## **Recopilación de información**

Además de los métodos mencionados anteriormente, las API Aspose.Cells también han proporcionado medios para recopilar información sobre qué fuentes y sustituciones se han establecido.

1. **[FontConfigs.GetFontSources](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources)** método devuelve una matriz de tipo**[FuenteFuenteBase](https://reference.aspose.com/cells/net/aspose.cells/fontsourcebase)**que contiene la lista de fuentes de fuentes especificadas. En caso de que no se hayan establecido fuentes, el**[FontConfigs.GetFontSources](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources)**El método devolverá una matriz vacía.
1. **[FontConfigs.GetFontSubstitutes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes)** método acepta un parámetro de tipo**cuerda** permitiendo especificar el nombre de la fuente para la que se ha establecido la sustitución. En caso de que no se haya establecido ninguna sustitución para el nombre de fuente especificado, el**[FontConfigs.GetFontSubstitutes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes)**método devolverá nulo.

## **Temas avanzados**
- [Establezca la fuente predeterminada al representar la hoja de cálculo en imágenes](/cells/es/net/set-default-font-while-rendering-spreadsheet-to-images/)
- [Establezca la propiedad DefaultFont de PdfSaveOptions e ImageOrPrintOptions para que tenga prioridad](/cells/es/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Formatos de fuente admitidos](/cells/es/net/supported-font-formats/)
- [Hoja de trabajo a imagen: establezca el formato de píxel para la imagen renderizada](/cells/es/net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
