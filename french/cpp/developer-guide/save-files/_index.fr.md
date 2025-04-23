---
title: Différentes façons d’enregistrer des fichiers avec C++
linktitle: Enregistrer des fichiers
type: docs
weight: 40
url: /fr/cpp/different-ways-to-save-files/
description: Aspose.Cells for C++ peut enregistrer des fichiers dans différents formats. Enregistrer en PDF. Enregistrer en HTML. Enregistrer en DOCX. Enregistrer en PPTX. Enregistrer en JSON. Enregistrer en MHTML.
keywords: Aspose.Cells enregistre Excel en PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML et autres en utilisant C++, en enregistrant ou convertissant un classeur en PDF, HTML, JSON, TXT, SQL dans C++.
---

{{% alert color="primary" %}}

Aspose.Cells rend possible la création et l'enregistrement de fichiers. Cet article explique les différentes façons dont les fichiers peuvent être enregistrés.

{{% /alert %}}

## **Différentes façons d'enregistrer des fichiers**

Aspose.Cells fournit la classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Microsoft Excel et fournit les propriétés et les méthodes nécessaires pour travailler avec des fichiers Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) fournit la méthode [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) utilisée pour enregistrer des fichiers Excel. La méthode [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) a de nombreuses surcharges qui sont utilisées pour enregistrer des fichiers de différentes manières.

Le format de fichier dans lequel le fichier est enregistré est décidé par l'énumération [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)

|**Types de formats de fichier**|**Description**|
| :- | :- |
|CSV|Représente un fichier CSV|
|Excel97To2003|Représente un fichier Excel 97 - 2003|
|Xlsx|Représente un fichier Excel 2007 XLSX|
|Xlsm|Représente un fichier Excel 2007 XLSM|
|Xltx|Représente un modèle Excel 2007 XLTX|
|Xltm|Représente un modèle activé par macro Excel 2007 XLTM|
|Xlsb|Représente un fichier XLSB binaire Excel 2007|
|SpreadsheetML|Représente un fichier XML de feuille de calcul|
|TSV|Représente un fichier de valeurs séparées par des tabulations|
|TabDelimited|Représente un fichier de texte à onglets|
|ODS|Représente un fichier ODS|
|Html|Représente un fichier HTML|
|MHtml|Représente un fichier MHTML|
|Pdf|Représente un fichier PDF|
|XPS|Représente un document XPS|
|TIFF|Représente le format de fichier TIFF (Tagged Image File Format)|

## **Comment enregistrer un fichier dans différents formats**

Pour enregistrer des fichiers dans un emplacement de stockage, spécifiez le nom du fichier (complet avec le chemin de stockage) et le format de fichier souhaité (à partir de l'énumération [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)) lors de l'appel de la méthode [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) de l'objet [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/).

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
    U16String filePath = srcDir + u"Book1.xls";

    // Load your source workbook
    Workbook workbook(filePath);

    // Save in Excel 97 to 2003 format
    workbook.Save(outDir + u".output.xls");
    // OR
    XlsSaveOptions xlsSaveOptions;
    workbook.Save(outDir + u".output.xls", xlsSaveOptions);

    // Save in Excel2007 xlsx format
    workbook.Save(outDir + u".output.xlsx", SaveFormat::Xlsx);

    // Save in Excel2007 xlsb format
    workbook.Save(outDir + u".output.xlsb", SaveFormat::Xlsb);

    // Save in ODS format
    workbook.Save(outDir + u".output.ods", SaveFormat::Ods);

    // Save in Pdf format
    workbook.Save(outDir + u".output.pdf", SaveFormat::Pdf);

    // Save in Html format
    workbook.Save(outDir + u".output.html", SaveFormat::Html);

    // Save in SpreadsheetML format
    workbook.Save(outDir + u".output.xml", SaveFormat::SpreadsheetML);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Comment enregistrer un classeur au format PDF**
Le format de fichier Portable Document Format (PDF) est un type de document créé par Adobe dans les années 1990. Le but de ce format de fichier était d'introduire une norme de représentation de documents et d'autres matériels de référence dans un format indépendant du logiciel d'application, du matériel et du système d'exploitation. Le format de fichier PDF a la capacité de contenir des informations telles que du texte, des images, des hyperliens, des champs de formulaire, des médias riches, des signatures numériques, des pièces jointes, des métadonnées, des fonctionnalités géospatiales et des objets 3D qui peuvent devenir une partie du document source.

Les codes suivants montrent comment enregistrer le classeur au format fichier PDF avec Aspose.Cells:
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate the Workbook object
    Workbook workbook;

    // Set value to Cell
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").PutValue(u"Hello World!");

    // Save the workbook to PDF
    workbook.Save(u"pdf1.pdf");

    // Save as Pdf format compatible with PDFA-1a
    PdfSaveOptions saveOptions;
    saveOptions.SetCompliance(PdfCompliance::PdfA1a);

    workbook.Save(u"pdfa1a.pdf", saveOptions);

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Comment enregistrer le classeur au format texte ou CSV**

Parfois, vous souhaitez convertir ou enregistrer un classeur avec plusieurs feuilles de calcul au format texte. Pour les formats texte (par exemple TXT, TabDelim, CSV, etc.), par défaut, à la fois Microsoft Excel et Aspose.Cells enregistrent uniquement le contenu de la feuille de calcul active.

L'exemple de code suivant explique comment enregistrer un classeur entier au format texte. Chargez le classeur source qui peut être n'importe quel fichier de feuille de calcul Microsoft Excel ou OpenOffice (donc XLS, XLSX, XLSM, XLSB, ODS, etc.) avec n'importe quel nombre de feuilles de calcul

Lorsque le code est exécuté, il convertit les données de toutes les feuilles du classeur au format TXT

Vous pouvez modifier le même exemple pour enregistrer votre fichier au format CSV. Par défaut, [**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getseparator/) est la virgule, donc ne spécifiez pas de séparateur si vous enregistrez en format CSV. Veuillez noter : si vous utilisez la version d’évaluation et même si la propriété [**TxtSaveOptions.GetExportAllSheets()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getexportallsheets/) est définie à true, le programme n’exportera qu’une seule feuille de calcul.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output text file
    U16String outputFilePath = outDir + u"out.txt";

    // Load your source workbook
    Workbook workbook(inputFilePath);

    // Text save options. You can use any type of separator
    TxtSaveOptions opts;
    opts.SetSeparator(u'\t');
    opts.SetExportAllSheets(true);

    // Save entire workbook data into file
    workbook.Save(outputFilePath, opts);

    std::cout << "Workbook data saved to text file successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Comment enregistrer un fichier en fichiers de texte avec un séparateur personnalisé**

Les fichiers texte contiennent des données de feuille de calcul sans mise en forme. Le fichier est un type de fichier texte brut qui peut avoir des délimiteurs personnalisés entre ses données

```c++
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

    // Create a Workbook object and open the file from its path
    Workbook wb(filePath);

    // Instantiate Text File's Save Options
    TxtSaveOptions options;

    // Specify the separator
    options.SetSeparator(u';');

    // Save the file with the options
    wb.Save(srcDir + u"output.csv", options);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Comment enregistrer un fichier dans un flux**

Pour enregistrer des fichiers dans un flux, créez un objet *MemoryStream* ou *FileStream* et enregistrez le fichier dans cet objet flux en appelant la méthode [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) de l'objet [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). Spécifiez le format de fichier souhaité en utilisant l'énumération [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) lors de l'appel de la méthode [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/).

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Save workbook to memory stream with explicit FileFormatType
    Vector<uint8_t> data = workbook.SaveToStream();

    std::cout << "File size: " << data.GetLength() << std::endl;

    Cleanup();

    return 0;
}
```

## **Comment enregistrer un fichier Excel en fichiers Html et Mht**
Aspose.Cells peut simplement enregistrer un fichier Excel, JSON, CSV ou d'autres fichiers qui peuvent être chargés par Aspose.Cells en tant que fichiers .html et .mht.
```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath(u"Book1.xlsx");
    Workbook workbook(inputFilePath);

    // Save file to MHTML format
    U16String outputFilePath(u"out.mht");
    workbook.Save(outputFilePath);

    std::cout << "File saved successfully to MHTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```


## **Comment enregistrer un fichier Excel au format OpenOffice (ODS, SXC, FODS, OTS)**
Nous pouvons enregistrer les fichiers au format open offce : ODS, SXC, FODS, OTS, etc.

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

## **Comment enregistrer un fichier Excel en JSON ou XML**

JSON (JavaScript Object Notation) est un format de fichier standard ouvert pour le partage de données qui utilise un texte lisible par l'homme pour stocker et transmettre des données. Les fichiers JSON sont stockés avec l'extension .json. JSON nécessite moins de mise en forme et est une bonne alternative à XML. JSON est dérivé de JavaScript mais est un format de données indépendant du langage. La génération et l'analyse du JSON sont prises en charge par de nombreux langages de programmation modernes. application/json est le type de support utilisé pour JSON.

Aspose.Cells prend en charge l'enregistrement de fichiers en JSON ou XML.

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


## **Sujets avancés**
- [Ajuster le niveau de compression du classeur](/cells/fr/cpp/adjust-workbook-compression-level/)
- [Enregistrer le classeur au format strict Open XML Spreadsheet](/cells/fr/cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Enregistrer le fichier dans l'objet Response](/cells/fr/cpp/saving-file-to-response-object/)
