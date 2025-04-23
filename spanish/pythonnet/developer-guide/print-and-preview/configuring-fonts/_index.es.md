---
title: Configuración de fuentes para la representación de hojas de cálculo
type: docs
weight: 10
url: /es/python-net/configuring-fonts-for-rendering-spreadsheets/
---

## **Escenarios de uso posibles**

Aspose.Cells para Python via .NET API proporciona la capacidad de representar hojas de cálculo en formatos de imagen así como convertirlas a formatos PDF y XPS. Para maximizar la fidelidad de la conversión, es necesario que las fuentes utilizadas en la hoja de cálculo estén disponibles en el directorio de fuentes predeterminado del sistema operativo. En caso de que las fuentes requeridas no estén presentes, la API Aspose.Cells para Python via .NET intentará sustituir las fuentes requeridas con las disponibles.

## **Selección de Fuentes**

A continuación se muestra el proceso que sigue Aspose.Cells para Python via .NET detrás de escena.

1. La API intenta encontrar las fuentes en el sistema de archivos que coincidan con el nombre de fuente exacto utilizado en la hoja de cálculo.
2. Si la API no puede encontrar las fuentes con el nombre exacto, intenta utilizar la fuente predeterminada especificada en la propiedad [**DefaultStyle.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) del libro de trabajo.
3. Si la API no puede localizar la fuente definida en la propiedad [**DefaultStyle.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) del libro de trabajo, intenta usar la fuente especificada en la propiedad [**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) o [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font).
4. Si la API no puede localizar la fuente definida en las propiedades [**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) o [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font), intenta usar la fuente especificada en la propiedad [**FontConfigs.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/default_font_name).
5. Si la API no puede localizar la fuente definida en la propiedad [**FontConfigs.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/default_font_name), intenta seleccionar las fuentes más adecuadas de todas las fuentes disponibles.
6. Por último, si la API no puede encontrar ninguna fuente en el sistema de archivos, representa la hoja de cálculo utilizando Arial.

## **Establecer Carpetas de Fuentes Personalizadas**

Aspose.Cells para Python via .NET busca en el directorio de fuentes predeterminado del sistema operativo las fuentes requeridas. En caso de que las fuentes no estén disponibles en el directorio del sistema, las API buscan en los directorios personalizados (definidos por el usuario). La clase [**FontConfigs**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs) ha expuesto varias formas de configurar directorios de fuentes personalizadas, como se detalla abajo.

1. [**FontConfigs.set_font_folder**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folder/): Este método es útil si solo hay una carpeta que se va a establecer.
2. [**FontConfigs.set_font_folders**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folders/): Este método es útil cuando las fuentes residen en varias carpetas y el usuario desea establecer todas las carpetas por separado en lugar de combinar todas las fuentes en una sola carpeta.
3. [**FontConfigs.set_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_sources/#list): Este mecanismo es útil cuando el usuario desea cargar fuentes desde varias carpetas o un solo archivo de fuente o datos de fuente de un array de bytes.

{{% alert color="primary" %}}

Ambos métodos [**FontConfigs.set_font_folder**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folder/) y [**FontConfigs.set_font_folders**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folders/) aceptan un segundo parámetro de tipo Booleano. Pasar **true** como segundo parámetro dirigirá a Aspose.Cells para Python via .NET a buscar archivos de fuentes en las subcarpetas.

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetCustomFontFolders-1.py" >}}

{{% alert color="primary" %}}

Por favor, usa cualquiera de los métodos mencionados anteriormente al inicio de la aplicación, es decir; antes de invocar otros objetos de Aspose.Cells para Python via .NET.

{{% /alert %}} {{% alert color="primary" %}}

Si se utilizan todos los métodos mencionados anteriormente para establecer las fuentes, solo los últimos ajustes tendrán efecto.

{{% /alert %}}

## **Mecanismo de Sustitución de Fuentes**

La API Aspose.Cells para Python via .NET también ofrece la capacidad de especificar la fuente de sustitución para fines de renderizado. Este mecanismo es útil cuando la fuente requerida no está disponible en la máquina donde se realiza la conversión. Los usuarios pueden proporcionar una lista de nombres de fuentes como alternativa a la fuente originalmente requerida. Para lograr esto, Aspose.Cells para Python via .NET ha expuesto el método [**FontConfigs.set_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_substitutes/#str-list) que acepta 2 parámetros. El primer parámetro es de tipo **string**, que debe ser el nombre de la fuente que necesita ser sustituida. El segundo parámetro es un arreglo de tipo **string**. Los usuarios pueden proporcionar una lista de nombres de fuentes como sustitución del nombre de fuente original (especificado en el primer parámetro).

Aquí hay un escenario de uso simple.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetCustomFontFolders-FontSubstitution.py" >}}

## **Recopilación de información**

Además de los métodos mencionados, Aspose.Cells para Python via .NET también ha proporcionado medios para recopilar información sobre las fuentes y las sustituciones que se han configurado.

1. El método [**FontConfigs.get_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_sources/#) devuelve un array de tipo [**FontSourceBase**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsourcebase) que contiene la lista de fuentes especificadas. En caso de que no se hayan establecido fuentes, el método [**FontConfigs.get_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_sources/#) devolverá un array vacío.
1. El método [**FontConfigs.get_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_substitutes/#str) acepta un parámetro de tipo **string** que permite especificar el nombre de la fuente para la cual se ha establecido una sustitución. En caso de que no se haya establecido una sustitución para el nombre de fuente especificado, entonces el método [**FontConfigs.get_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_substitutes/#str) devolverá nulo.

## **Temas avanzados**
- [Establecer la fuente predeterminada al renderizar la hoja de cálculo a imágenes](/cells/es/python-net/set-default-font-while-rendering-spreadsheet-to-images/)
- [Establecer la propiedad DefaultFont de PdfSaveOptions e ImageOrPrintOptions para tener prioridad](/cells/es/python-net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Formatos de fuente soportados](/cells/es/python-net/supported-font-formats/)
- [Hoja de cálculo a imagen - Establecer formato de píxel para la imagen renderizada](/cells/es/python-net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)

