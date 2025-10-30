---
title: Configuración de fuentes para renderizar hojas de cálculo con C++
linktitle: Configuración de fuentes para la representación de hojas de cálculo
type: docs
weight: 10
url: /es/cpp/configuring-fonts-for-rendering-spreadsheets/
description: Aprende cómo configurar las fuentes para renderizar hojas de cálculo en imágenes, PDF y formatos XPS usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Las APIs de Aspose.Cells ofrecen la facilidad de renderizar hojas de cálculo en formatos de imagen así como convertirlas a PDF y XPS. Para maximizar la fidelidad de la conversión, es necesario que las fuentes usadas en la hoja de cálculo estén disponibles en el directorio de fuentes predeterminado del sistema operativo. Si las fuentes requeridas no están presentes, Aspose.Cells intentará sustituir las fuentes necesarias con las disponibles.

## **Selección de Fuentes**

A continuación, el proceso que siguen las APIs de Aspose.Cells tras bambalinas:

1. La API intenta encontrar las fuentes en el sistema de archivos que coincidan con el nombre de fuente exacto utilizado en la hoja de cálculo.
1. Si la API no puede encontrar las fuentes con el mismo nombre exacto, intenta usar la fuente predeterminada especificada bajo la propiedad [**DefaultStyle.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) del Workbook.
1. Si la API no puede localizar la fuente definida bajo la propiedad [**DefaultStyle.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) del libro, intenta usar la fuente especificada en [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) o en la propiedad [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/).
1. Si la API no puede localizar la fuente definida bajo [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) o en la propiedad [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/), intenta usar la fuente especificada en la propiedad [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getdefaultfontname/).
1. Si la API no puede localizar la fuente definida en la propiedad [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getdefaultfontname/), intenta seleccionar las fuentes más apropiadas de entre todas las fuentes disponibles.
1. Finalmente, si la API no encuentra ninguna fuente en el sistema de archivos, renderiza la hoja de cálculo usando Arial.

## **Establecer Carpetas de Fuentes Personalizadas**

Las APIs de Aspose.Cells buscan en el directorio de fuentes predeterminado del sistema operativo las fuentes necesarias. Si las fuentes requeridas no están en el directorio de fuentes del sistema, las APIs buscan en directorios personalizados (definidos por el usuario). La clase [**FontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/) ofrece varias formas de establecer directorios personalizados de fuentes, como se detalla a continuación:

1. [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolder/): Este método es útil si solo hay una carpeta que se va a establecer.
1. [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolders/): Este método es útil cuando las fuentes residen en múltiples carpetas, y el usuario desea configurar cada carpeta por separado en lugar de combinar todas las fuentes en una sola carpeta.
1. [**FontConfigs.SetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontsources/): Este mecanismo es útil cuando el usuario desea cargar fuentes desde varias carpetas, un único archivo de fuente o datos de fuente desde un array de bytes.

{{% alert color="primary" %}}

Ambos métodos [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolder/) y [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolders/) aceptan un segundo parámetro de tipo Booleano. Pasar **true** como el segundo parámetro indicará a las APIs de Aspose.Cells buscar en las subcarpetas los archivos de fuente.

{{% /alert %}}

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

Vector<uint8_t> GetDataFromFile(const U16String& file)
{
    std::string f = file.ToUtf8();
    // open a file 
    std::ifstream fileStream(f, std::ios::binary);

    if (!fileStream.is_open()) {
        std::cerr << "Failed to open the file." << std::endl;
        return 1;
    }

    // Get file size
    fileStream.seekg(0, std::ios::end);
    std::streampos fileSize = fileStream.tellg();
    fileStream.seekg(0, std::ios::beg);

    // Read file contents into uint8_t array
    uint8_t* buffer = new uint8_t[fileSize];
    fileStream.read(reinterpret_cast<char*>(buffer), fileSize);
    fileStream.close();

    Vector<uint8_t>data(buffer, fileSize);
    delete[] buffer;

    return data;
}

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String fontFolder1 = srcDir + u"Arial";
    U16String fontFolder2 = srcDir + u"Calibri";
    U16String fontFile = srcDir + u"arial.ttf";

    FontConfigs::SetFontFolder(fontFolder1, true);

    Vector<U16String> fontFolders{ fontFolder1 , fontFolder2 };

    FontConfigs::SetFontFolders(fontFolders, false);

    FolderFontSource sourceFolder(fontFolder1, false);
    FileFontSource sourceFile(fontFile);
    Vector<uint8_t> fontData = GetDataFromFile(fontFile);
    MemoryFontSource sourceMemory(fontData);

    Vector<FontSourceBase> fontSources{ sourceFolder ,sourceFile ,sourceMemory };

    FontConfigs::SetFontSources(fontSources);

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Utilice cualquiera de los métodos mencionados anteriormente al inicio de la aplicación, es decir, antes de invocar otros objetos de las APIs de Aspose.Cells.

{{% /alert %}}

{{% alert color="primary" %}}

Si se utilizan todos los métodos mencionados anteriormente para establecer las fuentes, solo los últimos ajustes tendrán efecto.

{{% /alert %}}

## **Mecanismo de Sustitución de Fuentes**

Las APIs de Aspose.Cells también ofrecen la capacidad de especificar fuentes sustitutivas para fines de renderizado. Este mecanismo es útil cuando una fuente requerida no está disponible en la máquina donde se realiza la conversión. Los usuarios pueden proporcionar una lista de nombres de fuentes como alternativa a la fuente originalmente requerida. Para lograr esto, las APIs de Aspose.Cells han expuesto el método [**FontConfigs.SetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontsubstitutes/), que acepta dos parámetros. El primer parámetro es de tipo **string**, que debe ser el nombre de la fuente que necesita ser sustituida. El segundo parámetro es un array de tipo **string**. Los usuarios pueden proporcionar una lista de nombres de fuentes como sustitución del nombre de fuente original (especificado en el primer parámetro).

Aquí hay un escenario simple de uso:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Substituting the Arial font with Times New Roman & Calibri
    Vector<U16String> substituteFonts{ u"Times New Roman", u"Calibri" };
    FontConfigs::SetFontSubstitutes(u"Arial", substituteFonts);

    Aspose::Cells::Cleanup();
}
```

## **Recopilación de información**

Además de los métodos mencionados anteriormente, las APIs de Aspose.Cells también proporcionan medios para recopilar información sobre las fuentes y sustituciones que se han configurado:

1. El método [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsources/) devuelve un array del tipo [**FontSourceBase**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsourcebase/) que contiene la lista de fuentes especificadas. Si no se han configurado fuentes, el método [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsources/) devolverá un array vacío.
1. El método [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsubstitutes/) acepta un parámetro de tipo **string**, permitiéndote especificar el nombre de la fuente para la cual se ha establecido una sustitución. Si no se ha establecido ninguna sustitución para el nombre de fuente especificado, el método [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsubstitutes/) devolverá null.

## **Temas Avanzados**
- [Establecer la fuente predeterminada al renderizar la hoja de cálculo a imágenes](/cells/es/cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [Establecer la propiedad DefaultFont de PdfSaveOptions e ImageOrPrintOptions para tener prioridad](/cells/es/cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Formatos de fuente soportados](/cells/es/cpp/supported-font-formats/)
{{< app/cells/assistant language="cpp" >}}
