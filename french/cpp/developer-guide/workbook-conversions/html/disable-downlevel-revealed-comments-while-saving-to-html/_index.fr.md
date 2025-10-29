---
title: Désactiver les commentaires révélés en mode dégradé lors de l’enregistrement en HTML avec C++
linktitle: Désactiver les commentaires révélés en mode dégradé
type: docs
weight: 20
url: /fr/cpp/disable-downlevel-revealed-comments-while-saving-to/
description: Éliminer les commentaires révélés en mode dégradé lors de l’enregistrement de fichiers Excel en HTML avec Aspose.Cells en C++.
---

## **Scénarios d'utilisation possibles**

 Lorsque vous enregistrez votre fichier Excel en HTML, Aspose.Cells révèle les commentaires conditionnels en mode dégradé. Ces commentaires conditionnels concernent principalement les anciennes versions d’Internet Explorer et sont sans intérêt pour les navigateurs Web modernes. Vous pouvez en savoir plus en détail via le lien suivant.

- [Commentaire conditionnel - Commentaire conditionnel révélé de niveau inférieur](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

 Aspose.Cells vous permet d’éliminer ces commentaires révélés en mode dégradé en réglant la propriété [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisabledownlevelrevealedcomments/) à **true**.

## **Désactiver les commentaires révélés de niveau inférieur lors de l'enregistrement en HTML**

 Le code d'exemple ci-dessous montre l’utilisation de la propriété [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisabledownlevelrevealedcomments/). La capture d'écran montre l'effet de cette propriété lorsqu'elle n'est pas réglée à true. Veuillez télécharger le [fichier Excel d'exemple](50528257.xlsx) utilisé dans ce code ainsi que le [HTML généré](50528258.zip) pour référence.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Code d'exemple**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample workbook
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(sourceDir + u"sampleDisableDownlevelRevealedComments.xlsx");

    // Disable DisableDownlevelRevealedComments
    HtmlSaveOptions opts;
    opts.SetDisableDownlevelRevealedComments(true);

    // Save the workbook in html
    wb.Save(outputDir + u"outputDisableDownlevelRevealedComments_true.html", opts);

    std::cout << "Workbook saved successfully with DisableDownlevelRevealedComments enabled!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
