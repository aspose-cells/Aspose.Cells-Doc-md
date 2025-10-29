---
title: Obtenir des avertissements lors du chargement du fichier Excel avec C++
linktitle: Obtenir des avertissements lors du chargement du fichier Excel
type: docs
weight: 110
url: /fr/cpp/get-warnings-while-loading-excel-file/
description: Apprenez à attraper et gérer les avertissements lors du chargement de fichiers Excel en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Parfois, l’utilisateur tente de charger un classeur quelque peu corrompu mais encore chargéable. Dans de tels cas, Aspose.Cells émet des avertissements lors du chargement du classeur. Vous pouvez attraper ces avertissements en implémentant l’interface [**IWarningCallback**](https://reference.aspose.com/cells/cpp/aspose.cells/iwarningcallback/) et en réglant la propriété [**LoadOptions.GetWarningCallback()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getwarningcallback/).

## **Obtenir des avertissements lors du chargement d'un fichier Excel**

Le code d’exemple suivant explique comment obtenir des avertissements lors du chargement d’un fichier Excel. Le code charge le [fichier Excel d’exemple](sampleDuplicateDefinedName.xlsx), qui génère un avertissement [**DuplicateDefinedName**](https://reference.aspose.com/cells/cpp/aspose.cells/warningtype/) lors du chargement. Cet avertissement est ensuite capturé par la méthode [**IWarningCallback.Warning()**](https://reference.aspose.com/cells/cpp/aspose.cells/iwarningcallback/warning/), qui affiche les messages d’avertissement dans la console. Le code enregistre ensuite le classeur en tant que [fichier Excel de sortie](outputDuplicateDefinedName.xlsx). Si vous ouvrez le fichier Excel dans Microsoft Excel, cet avertissement s’affichera également, comme le montre la capture d’écran ci-dessous. Veuillez également vérifier la sortie de la console du code ci-dessous pour plus de compréhension.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Code d'exemple**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class WarningCallback : public IWarningCallback {
public:
    void Warning(WarningInfo& warningInfo) override {
        if (warningInfo.GetType() == ExceptionType::DefinedName) {
            std::cout << "Defined Name Warning: " << warningInfo.GetDescription().ToUtf8() << std::endl;
        }
    }
};

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    LoadOptions options;
    WarningCallback callback;
    options.SetWarningCallback(&callback);

    U16String inputFilePath = srcDir + u"sampleDuplicateDefinedName.xlsx";
    Workbook book(inputFilePath, options);

    U16String outputFilePath = outDir + u"outputDuplicateDefinedName.xlsx";
    book.Save(outputFilePath);

    std::cout << "Workbook saved successfully with warning handling!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sortie console**

Voici la sortie de la console du code ci-dessus lors de son exécution avec le [fichier Excel d'exemple fourni](sampleDuplicateDefinedName.xlsx).

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
