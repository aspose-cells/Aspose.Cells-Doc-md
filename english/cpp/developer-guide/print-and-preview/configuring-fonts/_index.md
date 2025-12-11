---
title: Configuring Fonts for Rendering Spreadsheets with C++
linktitle: Configuring Fonts for Rendering Spreadsheets
type: docs
weight: 10
url: /cpp/configuring-fonts-for-rendering-spreadsheets/
description: Learn how to configure fonts for rendering spreadsheets to images, PDF, and XPS formats using Aspose.Cells for C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Aspose.Cells APIs provide the facility to render spreadsheets in image formats as well as convert them to PDF and XPS formats. To maximize conversion fidelity, it is necessary that the fonts used in the spreadsheet are available in the operating system's default font directory. If the required fonts are not present, Aspose.Cells APIs will attempt to substitute the required fonts with the ones available.

## **Selection of Fonts**

Below is the process that Aspose.Cells APIs follow behind the scenes:

1. The API tries to find the fonts on the file system matching the exact font name used in the spreadsheet.  
2. If the API cannot find the fonts with the exact same name, it attempts to use the default font specified under the Workbook's [**DefaultStyle.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) property.  
3. If the API cannot locate the font defined under the workbook's [**DefaultStyle.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) property, it attempts to use the font specified under [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) or [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) property.  
4. If the API cannot locate the font defined under [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) or [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) property, it attempts to use the font specified under [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getdefaultfontname/) property.  
5. If the API cannot locate the font defined under [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getdefaultfontname/) property, it attempts to select the most suitable fonts from all of the available fonts.  
6. Finally, if the API cannot find any fonts on the file system, it renders the spreadsheet using Arial.

## **Set Custom Font Folders**

Aspose.Cells APIs search the operating system's default font directory for the required fonts. If the required fonts are not available in the system's font directory, the APIs search through custom (user‑defined) directories. The [**FontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/) class provides several ways to set custom font directories, as detailed below:

1. [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolder/): This method is useful if there is only one folder to be set.  
2. [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolders/): This method is useful when the fonts reside in multiple folders, and the user wishes to set all folders separately rather than combining all fonts in a single folder.  
3. [**FontConfigs.SetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontsources/): This mechanism is useful when the user wishes to load fonts from multiple folders, a single font file, or font data from an array of bytes.

{{% alert color="primary" %}}

Both [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolder/) and [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolders/) methods accept a Boolean‑type second parameter. Passing **true** as the second parameter will direct the Aspose.Cells APIs to search the subfolders for the font files.

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
        // Return an empty vector on error
        return Vector<uint8_t>();
    }

    // Get file size
    fileStream.seekg(0, std::ios::end);
    std::streampos fileSize = fileStream.tellg();
    fileStream.seekg(0, std::ios::beg);

    // Read file contents into uint8_t array
    uint8_t* buffer = new uint8_t[fileSize];
    fileStream.read(reinterpret_cast<char*>(buffer), fileSize);
    fileStream.close();

    Vector<uint8_t> data(buffer, fileSize);
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

Please use any of the above‑mentioned methods at the start of the application, that is, before invoking any other objects of Aspose.Cells APIs.

{{% /alert %}}

{{% alert color="primary" %}}

If all of the above‑mentioned methods are used to set the font sources, only the last settings will take effect.

{{% /alert %}}

## **Font Substitution Mechanism**

Aspose.Cells APIs also provide the ability to specify substitute fonts for rendering purposes. This mechanism is helpful when a required font is not available on the machine where the conversion has to take place. Users can provide a list of font names as an alternative to the originally required font. To achieve this, the Aspose.Cells APIs have exposed the [**FontConfigs.SetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontsubstitutes/) method, which accepts two parameters. The first parameter is of type **string**, which should be the name of the font that needs to be substituted. The second parameter is an array of type **string**. Users can provide a list of font names as a substitution for the original font name (specified in the first parameter).

Here is a simple usage scenario:

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

## **Information Gathering**

In addition to the above‑mentioned methods, the Aspose.Cells APIs also provide means to gather information on what sources and substitutions have been set:

1. [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsources/) method returns an array of type [**FontSourceBase**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsourcebase/) containing the list of specified font sources. If no sources have been set, the [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsources/) method will return an empty array.  
2. [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsubstitutes/) method accepts a parameter of type **string**, allowing you to specify the font name for which substitution has been set. If no substitution has been set for the specified font name, the [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsubstitutes/) method will return null.

## **Advanced Topics**
- [Set Default Font while rendering spreadsheet to images](/cells/cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [Set DefaultFont property of PdfSaveOptions and ImageOrPrintOptions to have priority](/cells/cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Supported Font Formats](/cells/cpp/supported-font-formats/)
{{< app/cells/assistant language="cpp" >}}
