---
title: Convertir Excel en Pdf, Image, et autres formats avec C++
linktitle: Conversions de classeur
type: docs
weight: 65
url: /fr/cpp/convert-workbook-to-different-formats/
description: Convertir des fichiers Excel en Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML, et plus encore avec Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells supporte la conversion entre de nombreux formats. Techniquement, la conversion consiste à charger un classeur dans un format de fichier et à le sauvegarder dans un autre.

{{% /alert %}}

## **Convertir un classeur Excel en PDF**

Les fichiers PDF sont largement utilisés pour échanger des documents entre organisations, secteurs gouvernementaux, et particuliers. C'est un format de document standard, et les développeurs de logiciels sont souvent sollicités pour trouver un moyen de convertir les fichiers Microsoft Excel en documents PDF.

Aspose.Cells prend en charge la conversion de fichiers Excel en PDF et maintient une haute fidélité visuelle dans la conversion.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Instantiate the Workbook object and open an Excel file
    Workbook workbook(u"Book1.xlsx");

    // Save the document in PDF format
    workbook.Save(u"output.pdf", SaveFormat::Pdf);

    std::cout << "Excel file converted to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Convertir un classeur Excel en JPG**
Aspose.Cells prend en charge la conversion de fichiers Excel en JPG.
L'exemple de code ci-dessous montre comment sauvegarder un classeur en JPG.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String inputFilePath(u"Book1.xlsx");
    Workbook book(inputFilePath);

    U16String outputFilePath(u"Image1.jpg");
    book.Save(outputFilePath, SaveFormat::Jpg);

    std::cout << "Workbook converted to JPG image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Convertir un classeur Excel en image**
Aspose.Cells prend en charge la conversion de fichiers Excel en images.
L'exemple de code ci-dessous montre comment sauvegarder un classeur en images.

```c++
#include <iostream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook workbook(srcDir + u"Book1.xlsx");

    workbook.Save(outDir + u"Image1.bmp", SaveFormat::Bmp);
    workbook.Save(outDir + u"Image1.jpg", SaveFormat::Jpg);
    workbook.Save(outDir + u"Image1.png", SaveFormat::Png);
    workbook.Save(outDir + u"Image1.emf", SaveFormat::Emf);
    workbook.Save(outDir + u"Image1.gif", SaveFormat::Gif);

    std::cout << "Workbook converted to images successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Convertir un classeur Excel en XPS**

Le format de document XPS se compose de balises XML structurées qui définissent la mise en page d'un document et l'apparence visuelle de chaque page, ainsi que des règles de rendu pour la distribution, l'archivage, le rendu, le traitement et l'impression de documents.

Le langage de balisage pour XPS est un sous-ensemble de XAML, ce qui lui permet d’incorporer des éléments graphiques vectoriels dans les documents, en utilisant XAML pour marquer les primitives de Windows Presentation Foundation (WPF). Les éléments utilisés sont décrits en termes de chemins et autres primitives géométriques.

Un fichier XPS est, en fait, une archive ZIP Unicode utilisant les Conventions d’Emballage Ouvert, contenant les fichiers qui composent le document. Ceux-ci incluent un fichier de balisage XML pour chaque page, du texte, des polices intégrées, des images raster, des graphiques vectoriels 2D, ainsi que des informations de gestion des droits numériques. Le contenu d’un fichier XPS peut être examiné simplement en l’ouvrant dans une application prenant en charge ZIP.

À partir de Aspose.Cells 6.0.0, la conversion de Microsoft Excel en XPS est prise en charge.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"Book1.xls";
    Workbook workbook(inputFilePath);

    Worksheet sheet = workbook.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetImageType(ImageType::Png);

    SheetRender sr(sheet, options);
    sr.ToImage(0, outDir + u"out_image.png");

    XpsSaveOptions xpsOptions;
    workbook.Save(outDir + u"out_whole_printingxps.out.xps", xpsOptions);

    std::cout << "Files created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Convertir Excel en Ods, Sxc, et Fods (OpenOffice / LibreOffice Calc)**
Aspose.Cells supporte la conversion de fichiers Excel en fichiers Ods, Sxc, et Fods. L’exemple de code ci-dessous montre comment convertir le [modèle](book1.xlsx) en fichiers Ods, Sxc, et Fods.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    Workbook workbook(u"book1.xlsx");

    // Save as ods file
    workbook.Save(u"Out.ods");

    // Save as sxc file
    workbook.Save(u"Out.sxc");

    // Save as fods file
    workbook.Save(u"Out.fods");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Conversion de Classeur Excel en Fichiers MHTML**

Le format MHTML combine du HTML normal avec des ressources externes (c'est-à-dire du contenu généralement lié tel que des images, des animations, de l'audio, etc.) dans un seul fichier. Ils sont utilisés pour les e-mails avec l'extension de fichier .mht.

Aspose.Cells prend en charge la lecture et l'écriture des fichiers MHTML.

L'exemple de code ci-dessous montre comment enregistrer un classeur sous forme de fichier MHTML.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"Book1.xlsx";

    // Specify the HTML Saving Options
    HtmlSaveOptions sv(SaveFormat::MHtml);

    // Instantiate a workbook and open the template XLSX file
    Workbook wb(filePath);

    // Save the MHT file
    wb.Save(filePath + u".out.mht", sv);

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Conversion de Classeur Excel en HTML**

L’API Aspose.Cells offre un support pour l’exportation de feuilles de calcul au format HTML. À cette fin, Aspose.Cells utilise la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/) pour offrir la flexibilité de contrôler plusieurs aspects du HTML de sortie.

L'exemple de code ci-dessous montre comment enregistrer un classeur sous forme de fichier HTML.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"sample.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"ConvertingToHTMLFiles_out.html";

    // Load the sample excel file into a workbook object
    Workbook wb(filePath);

    // Save the workbook in HTML format
    wb.Save(outputFilePath, SaveFormat::Html);

    std::cout << "File converted to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Configuration des Préférences d'Image pour le HTML**

Depuis la version 8.0.2, Aspose.Cells expose [**GetImageOptions()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getimageoptions/) pour la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/), permettant aux développeurs de spécifier les préférences d’image lors de l’enregistrement de feuilles de calcul en HTML.

Voici certains des paramètres d’image pouvant être appliqués :

- [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/): Spécifie le type d'image. Veuillez noter que toutes les formes, y compris les graphiques, sont rendues sous forme d'images dans le HTML de sortie.
- [**GetQuality()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getquality/) : Spécifie la qualité de l’image entre 0 et 100 lorsque [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) est défini comme Jpeg.
- [**GetVerticalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/): Obtient ou définit la résolution verticale de l'image en points par pouce.
- [**GetHorizontalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/): Obtient ou définit la résolution horizontale de l'image en points par pouce.
- [**TiffCompression**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/tiffcompression/) : Obtient ou définit le type de compression pour les images lorsque [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) est défini comme Tiff.
- [**GetTransparent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettransparent/): Indique si l'arrière-plan d'une image doit être transparent lorsque ImageFormat est spécifié comme Png.

Le code ci-dessous démontre comment utiliser [**HtmlSaveOptions.GetImageOptions()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getimageoptions/) pour spécifier différentes préférences.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String filePath = srcDir + u"Book1.xlsx";

    Workbook book(filePath);
    HtmlSaveOptions saveOptions(SaveFormat::Html);

    saveOptions.GetImageOptions().SetImageType(ImageType::Png);

    book.Save(outDir + u"output.html", saveOptions);

    std::cout << "Spreadsheet converted to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Convertir un classeur Excel en Markdown**

L’API Aspose.Cells supporte l’exportation des feuilles de calcul au format Markdown. Pour exporter la feuille active en Markdown, passez [**SaveFormat.Markdown**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) en tant que second paramètre de la méthode [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). Vous pouvez également utiliser la classe [**MarkdownSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/markdownsaveoptions/) pour spécifier des paramètres supplémentaires pour l’exportation de la feuille de calcul en Markdown.

L’exemple de code suivant montre comment exporter la feuille de calcul active au format Markdown en utilisant le membre d’énumération [**SaveFormat.Markdown**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/). Veuillez voir le [fichier Markdown de sortie](md_sample.txt) généré par le code à titre de référence.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Markdown file
    U16String outputFilePath = outDir + u"Book1.md";

    // Create workbook from the input Excel file
    Workbook workbook(inputFilePath);

    // Save the workbook as Markdown
    workbook.Save(outputFilePath, SaveFormat::Markdown);

    std::cout << "Workbook saved as Markdown successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Convertir un classeur Excel en JSON**

Aspose.Cells supporte la conversion d’un classeur en fichier JSON (JavaScript Object Notation).

L’exemple de code suivant montre comment exporter la feuille active en JSON en utilisant le membre d’énumération [**SaveFormat.Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/). Veuillez voir le code pour convertir le [fichier source](Book1.xlsx) en le [fichier JSON de sortie](Book1.Json) généré par le code à titre de référence.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output json file
    U16String outputFilePath = outDir + u"book1.json";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save the workbook as JSON
    workbook.Save(outputFilePath, SaveFormat::Json);

    std::cout << "Workbook converted to JSON successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Convertir Excel en XML**
Aspose.Cells prend en charge la conversion d'un classeur en XML de feuille de calcul Excel 2003 et en données XML brutes.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath = u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Save as Excel 2003 Spreadsheet XML
    U16String outputFilePath1 = u"Spreadsheet.xml";
    workbook.Save(outputFilePath1);

    // Save as plain XML data
    U16String outputFilePath2 = u"data.xml";
    XmlSaveOptions xmlSaveOptions;
    workbook.Save(outputFilePath2, xmlSaveOptions);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Convertir un classeur Excel en TIFF**
Aspose.Cells prend en charge la conversion d'un classeur en fichier TIFF.

Le code ci-dessous montre comment convertir Excel en TIFF :

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open a template excel file
    U16String inputFilePath(u"Book1.xlsx");
    Workbook book(inputFilePath);

    // Save file to TIFF
    U16String outputFilePath(u"out.tiff");
    book.Save(outputFilePath);

    std::cout << "File saved successfully to TIFF format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Convertir un classeur Excel en DOCX**

L’API Aspose.Cells offre un support pour la conversion des feuilles de calcul en format DOCX. Pour exporter le classeur en DOCX, passez [**SaveFormat.Docx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) comme second paramètre de la méthode [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). Vous pouvez également utiliser la classe [**DocxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/docxsaveoptions/) pour spécifier des paramètres supplémentaires pour l’exportation de la feuille de calcul en DOCX.

L’exemple de code suivant montre comment exporter la feuille active en DOCX en utilisant le membre d’énumération [**SaveFormat.Docx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/). Veuillez voir le [fichier DOCX de sortie](Book1.docx) généré par le code à titre de référence.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output docx file
    U16String outputFilePath = outDir + u"Book1.docx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save as DOCX
    workbook.Save(outputFilePath, SaveFormat::Docx);

    std::cout << "File saved successfully as DOCX!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Convertir un classeur Excel en PPTX**

L’API Aspose.Cells supporte la conversion des feuilles de calcul en format PPTX. Pour exporter le classeur en PPTX, passez [**SaveFormat.Pptx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) comme second paramètre de la méthode [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). Vous pouvez également utiliser la classe [**PptxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pptxsaveoptions/) pour spécifier des paramètres supplémentaires pour l’exportation de la feuille en PPTX.

L'exemple de code suivant démontre l'exportation de la feuille de calcul active vers PPTX en utilisant le membre d'énumération [**SaveFormat.Pptx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/). Veuillez consulter le [fichier PPTX de sortie](Book1.pptx) généré par le code pour référence.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output PowerPoint file
    U16String outputFilePath = outDir + u"Book1.pptx";

    // Create workbook from the input Excel file
    Workbook workbook(inputFilePath);

    // Save the workbook as a PowerPoint file
    workbook.Save(outputFilePath, SaveFormat::Pptx);

    std::cout << "Workbook saved as PowerPoint successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Convertir le classeur Excel en EPUB**

L'API Aspose.Cells prend en charge la conversion de feuilles de calcul au format EPUB. Pour exporter le classeur au format EPUB, passez [**SaveFormat.Epub**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) en tant que deuxième paramètre de la méthode [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). Vous pouvez également utiliser la classe [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/) pour spécifier des paramètres supplémentaires lors de l'exportation de la feuille de calcul en EPUB.

L'exemple de code suivant démontre l'exportation de la feuille de calcul active en EPUB en utilisant le membre d'énumération [**SaveFormat.Epub**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/).

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"sample.xlsx";

    // Path of output EPUB file
    U16String outputFilePath = outDir + u"ConvertingToEPUBFiles_out.epub";

    // Load the sample excel file into a workbook object
    Workbook wb(filePath);

    // Save the workbook in EPUB format
    wb.Save(outputFilePath, SaveFormat::Epub);

    std::cout << "File converted to EPUB format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Convertir le classeur Excel en AZW3**

L'API Aspose.Cells prend en charge la conversion de feuilles de calcul au format AZW3. Pour exporter le classeur en AZW3, passez [**SaveFormat.Azw3**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) en tant que deuxième paramètre de la méthode [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). Vous pouvez également utiliser la classe [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/) pour définir des paramètres supplémentaires pour l'exportation de la feuille de calcul en AZW3.

L'exemple de code suivant démontre l'exportation de la feuille de calcul active en AZW3 en utilisant le membre d'énumération [**SaveFormat.Azw3**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"sample.xlsx";

    // Path of output AZW3 file
    U16String outputFilePath = outDir + u"ConvertingToEPUBFiles_out.azw3";

    // Load the sample excel file into a workbook object
    Workbook wb(filePath);

    // Save the workbook in AZW3 format
    wb.Save(outputFilePath, SaveFormat::Azw3);

    std::cout << "File converted to AZW3 format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sujets avancés**
- [Convertir la révision de XLSB en XLSM](/cells/fr/cpp/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/fr/cpp/convert-excel-to-html/)
- [Image](/cells/fr/cpp/convert-excel-to-image/)
- [Json](/cells/fr/cpp/convert-workbook-to-json/)
- [Convertir le classeur Excel en Ods, Sxc et Fods (OpenOffice / LibreOffice calc).](/cells/fr/cpp/convert-excel-to-ods/)
- [Pdf](/cells/fr/cpp/convert-excel-workbook-to-pdf/)
- [Convertir Excel en CSV, TSV et Txt](/cells/fr/cpp/convert-excel-to-csv-tsv-and-txt/)
- [Suivre la progression de la conversion des documents](/cells/fr/cpp/track-document-conversion-progress/)
- [Convertir CSV, TSV et TXT en Excel](/cells/fr/cpp/convert-csv-tsv-and-txt-to-excel/)
{{< app/cells/assistant language="cpp" >}}
