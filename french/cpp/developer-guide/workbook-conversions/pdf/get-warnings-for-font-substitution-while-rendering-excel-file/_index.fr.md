---
title: Obtenir des avertissements pour la substitution de police lors du rendu d’un fichier Excel en PDF avec C++
linktitle: Obtenir des avertissements pour la substitution de police
type: docs
weight: 230
url: /fr/cpp/get-warnings-for-font-substitution-while-rendering-excel-file/
description: Apprenez comment obtenir des avertissements pour la substitution de police lors du rendu de fichiers Excel en PDF en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Parfois, lors du rendu d'un fichier Microsoft Excel en PDF, Aspose.Cells substitue des polices. Aspose.Cells propose une fonctionnalité qui permet aux développeurs de savoir quelle police particulière a été substituée en déclenchant un avertissement. Il s'agit d'une fonctionnalité utile qui peut vous aider à identifier pourquoi un PDF créé par Aspose.Cells semble différent du fichier Excel d'origine afin que vous puissiez prendre des mesures appropriées. Par exemple, installer les polices manquantes pour que les résultats du rendu soient identiques.

{{% /alert %}}

Pour obtenir des avertissements pour la substitution de police lors du rendu de fichiers Excel en PDF, implémentez l’interface `IWarningCallback` et définissez la propriété `PdfSaveOptions.WarningCallback` avec votre interface implémentée.

La capture d'écran ci-dessous montre un fichier Excel source que nous utiliserons dans le code suivant. Il contient du texte dans les cellules A6 et A7 dans des polices qui ne sont pas rendues correctement par Microsoft Excel.

|**Toutes les polices ne sont pas rendues correctement**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|

Aspose.Cells va substituer les polices dans les cellules A6 et A7 par des polices appropriées comme indiqué ci-dessous.

|**Polices substituées**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|

## **Télécharger le fichier source et le PDF de sortie**
Vous pouvez télécharger le fichier Excel source et le PDF de sortie via les liens suivants :

- [source.xlsx](5112611.xlsx)
- [output.pdf](5112616.pdf)

## **Code**
Le code suivant implémente `IWarningCallback` et définit la propriété `PdfSaveOptions.WarningCallback` avec l’interface implémentée. Désormais, chaque fois qu’une police sera substituée dans une cellule, Aspose.Cells déclenchera un avertissement dans la méthode `WarningCallback.Warning()`.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class GetWarningsForFontSubstitution : public IWarningCallback
{
public:
    void Warning(WarningInfo& info) override
    {
        if (info.GetType() == ExceptionType::FontSubstitution)
        {
            std::cout << "WARNING INFO: " << info.GetDescription().ToUtf8() << std::endl;
        }
    }

    static void Run()
    {
        U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
        U16String outDir(u"..\\Data\\02_OutputDirectory\\");
        Workbook workbook(srcDir + u"source.xlsx");
        PdfSaveOptions options;
        auto callback = std::make_shared<GetWarningsForFontSubstitution>();
        options.SetWarningCallback(callback.get());
        workbook.Save(outDir + u"output_out.pdf", options);
        std::cout << "PDF saved successfully with font substitution warnings!" << std::endl;
    }
};

int main()
{
    Aspose::Cells::Startup();
    GetWarningsForFontSubstitution::Run();
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sortie**
Après avoir converti le fichier Excel source en PDF, les avertissements sont affichés dans la console de débogage comme ceci :

{{< highlight java >}}
WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].
WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].
{{< /highlight >}}

{{% alert color="primary" %}}

Si votre feuille de calcul contient des formules, il est préférable d’appeler la méthode `Workbook.CalculateFormula` juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
