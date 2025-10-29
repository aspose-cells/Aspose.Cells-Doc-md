---
title: Accéder et mettre à jour les parties du texte enrichi d une cellule avec C++
linktitle: Texte enrichi avec formatage
type: docs
weight: 40
url: /fr/cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Apprenez comment accéder et mettre à jour les parties du texte enrichi d’une cellule via l’API Aspose.Cells for C++.
keywords: Accéder et mettre à jour le texte enrichi de la cellule, obtenir le texte enrichi de la cellule, modifier le texte enrichi de la cellule, accéder au texte enrichi de la cellule, mettre à jour le texte enrichi de la cellule, changer le texte enrichi de la cellule
---

{{% alert color="primary" %}}

Aspose.Cells vous permet d'accéder et de mettre à jour les différentes parties du texte enrichi de la cellule. À cette fin, vous pouvez utiliser les méthodes [**Cell->GetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcharacters/) et [**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/). Ces méthodes retourneront et accepteront un tableau d'objets [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/) que vous pouvez utiliser pour accéder et mettre à jour diverses propriétés de la police, telles que le nom de la police, la couleur de la police, le gras, etc.

{{% /alert %}}

## **Accéder et mettre à jour les parties du texte enrichi de la cellule**

 Le code ci-dessous démontre l’utilisation des méthodes [**Cell->GetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcharacters/) et [**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/) en utilisant le [fichier Excel source](5112369.xlsx). Le fichier Excel source contient un texte enrichi dans la cellule A1 avec 3 parties, chacune ayant une police différente. Le code accède à ces parties et met à jour la police de la première partie en **"Arial"**. Le classeur modifié est enregistré en tant que [fichier Excel de sortie](5112366.xlsx).

### Code C++ pour accéder et mettre à jour les parties du texte enrichi

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputPath = srcDir + u"Sample.xlsx";
    U16String outputPath = outDir + u"Output.out.xlsx";

    Workbook workbook(inputPath);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Cell cell = worksheet.GetCells().Get(U16String(u"A1"));

    std::cout << "Before updating the font settings...." << std::endl;

    Vector<FontSetting> fnts = cell.GetCharacters();

    for (int i = 0; i < fnts.GetLength(); ++i)
    {
        FontSetting& fs = fnts[i];
        std::cout << fs.GetFont().GetName().ToUtf8() << std::endl;
    }

    if (fnts.GetLength() > 0)
    {
        FontSetting& fs = fnts[0];
        fs.GetFont().SetName(u"Arial");
        cell.SetCharacters(fnts);
    }

    std::cout << std::endl << "After updating the font settings...." << std::endl;

    fnts = cell.GetCharacters();

    for (int i = 0; i < fnts.GetLength(); ++i)
    {
        FontSetting& fs = fnts[i];
        std::cout << fs.GetFont().GetName().ToUtf8() << std::endl;
    }

    workbook.Save(outputPath);

    Aspose::Cells::Cleanup();
    return 0;
}
```

### Sortie de la console générée par le code d'exemple

Voici la sortie de la console lors de l’utilisation du [fichier Excel source](5112369.xlsx):

{{< highlight java >}}

Before updating the font settings....
Century
Courier New
Verdana

After updating the font settings....
Arial
Courier New
Verdana

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
