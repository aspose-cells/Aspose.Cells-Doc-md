---
title: Insérer des hyperliens dans Excel ou OpenOffice avec C++
linktitle: Gérer les liens hypertexte
type: docs
weight: 45
url: /fr/cpp/insert-hyperlinks-to-excel/
description: Comment insérer des hyperliens dans un fichier Excel avec la bibliothèque Aspose.Cells sans utiliser MS Excel avec C++.
keywords: Insérer des hyperliens dans Excel, Ajouter ou insérer des hyperliens, Ajouter ou insérer un lien vers une URL, Ajouter ou insérer un lien vers une cellule, Ajouter un lien vers un fichier externe
---

{{% alert color="primary" %}} 

Un lien hypertexte est utilisé pour créer un lien entre deux entités. Tout le monde est familier avec l'utilisation des liens hypertexte, en particulier sur les sites Internet.
En utilisant Aspose.Cells, les développeurs peuvent créer différents types de liens hypertexte dans les fichiers Microsoft Excel. Ce sujet explique quels types de liens hypertexte sont pris en charge par Aspose.Cells et comment ils peuvent être utilisés dans nos fichiers Excel.

{{% /alert %}} 

## **Ajout de liens hypertexte**
Aspose.Cells permet aux développeurs d'ajouter des hyperliens aux fichiers Excel soit via l'API, soit en utilisant des feuilles de calcul de conception (feuilles où les hyperliens sont créés manuellement et Aspose.Cells est utilisé pour les importer dans d'autres feuilles).

Aspose.Cells fournit une classe, [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) permettant d’accéder à chacune des feuilles de calcul du fichier Excel. Une feuille est représentée par la classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) offre différentes méthodes pour ajouter différents hyperliens dans les fichiers Excel.

## **Ajout de lien vers une URL**
La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) contient une collection [GetHyperlinks()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gethyperlinks/). Chaque élément de cette collection représente un [Hyperlink](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/). Ajoutez des hyperliens vers des URL en appelant la méthode [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) de la collection [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/). La méthode [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) prend les paramètres suivants :

- Nom de la cellule, le nom de la cellule à laquelle le lien hypertexte sera ajouté.
- Nombre de lignes, le nombre de lignes dans cette plage de liens hypertexte.
- Nombre de colonnes, le nombre de colonnes dans cette plage de liens hypertexte.
- URL, l'adresse URL.

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

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a hyperlink to cell "A1"
    worksheet.GetHyperlinks().Add(u"A1", 1, 1, u"http://www.aspose.com");

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

Dans l'exemple ci-dessus, un lien hypertexte est ajouté à une URL dans une cellule vide, ** A1 **. Dans de tels cas, si une cellule est vide, l'adresse URL est également ajoutée à cette cellule vide en tant que sa valeur. Si la cellule n'est pas vide et qu'un lien hypertexte est ajouté, la valeur de la cellule ressemble à du texte brut. Pour le faire ressembler à un lien hypertexte, appliquez les paramètres de formatage appropriés sur cette cellule.

{{% /alert %}} 

## **Ajouter un lien vers une cellule dans le même fichier**
Il est possible d’ajouter des hyperliens dans des cellules du même fichier Excel en appelant la méthode [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) de la collection [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/). La méthode [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) fonctionne pour les hyperliens internes et externes. Une version de la méthode surchargee prend les paramètres suivants :

- Nom de la cellule, le nom de la cellule à laquelle le lien hypertexte sera ajouté.
- Nombre de lignes, le nombre de lignes dans cette plage de liens hypertexte.
- Nombre de colonnes, le nombre de colonnes dans cette plage de liens hypertexte.
- URL, l'adresse de la cellule cible.

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    workbook.GetWorksheets().Add();

    // Obtaining the reference of the first (default) worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in
    // The same Excel file
    worksheet.GetHyperlinks().Add(u"B3", 1, 1, u"Sheet2!B9");

    // Saving the Excel file
    workbook.Save(outDir + u"output.out.xls");

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Ajouter un lien vers un fichier externe**
Il est possible d’ajouter des hyperliens vers des fichiers Excel externes en appelant la méthode [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) de la collection [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/). La méthode [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) prend les paramètres suivants :

- Nom de la cellule, le nom de la cellule à laquelle le lien hypertexte sera ajouté.
- Nombre de lignes, le nombre de lignes dans cette plage de liens hypertexte.
- Nombre de colonnes, le nombre de colonnes dans cette plage de liens hypertexte.
- URL, l'adresse de la cible, fichier Excel externe.

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Add an internal hyperlink to the "A5" cell of the other worksheet "Sheet2" in the same Excel file
    worksheet.GetHyperlinks().Add(U16String(u"A5"), 1, 1, srcDir + U16String(u"book1.xls"));

    // Save the Excel file
    workbook.Save(outDir + U16String(u"output.out.xls"));

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sujets avancés**
- [Ajouter des hyperliens d'image](/cells/fr/cpp/add-image-hyperlinks/)
- [Détecter le type de lien hypertexte](/cells/fr/cpp/detect-hyperlink-type/)
- [Modifier les hyperliens de la feuille de calcul](/cells/fr/cpp/editing-hyperlinks-of-worksheet/)
- [Obtenir des hyperliens dans la plage](/cells/fr/cpp/get-hyperlinks-in-range/)
{{< app/cells/assistant language="cpp" >}}
