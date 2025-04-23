---
title: Obtenir des en têtes ou pieds de page avec C++
linktitle: Obtenir les en têtes ou pieds de page
type: docs
weight: 30
url: /fr/cpp/get-headers-or-footers/
description: Cet article explique comment obtenir de manière programmatique les en têtes et pieds de page des fichiers Excel ou OpenOffice en utilisant l’API ou la bibliothèque C++.
---

{{% alert color="primary" %}}

Les en-têtes et pieds de page ne s'affichent qu'en mode Mise en page, Aperçu avant impression et sur les pages imprimées. 

Vous pouvez également utiliser la boîte de dialogue Mise en page si vous souhaitez afficher les en-têtes ou pieds de page pour plus d'une feuille de calcul à la fois. 

Pour d'autres types de feuilles, tels que les feuilles de graphique ou les graphiques, vous pouvez insérer des en-têtes et pieds de page uniquement en utilisant la boîte de dialogue Mise en page.

{{% /alert %}}

## **Obtenir des en-têtes et des pieds de page dans MS Excel**
1. Cliquez sur la feuille de calcul où vous souhaitez afficher ou modifier les en-têtes ou les pieds de page.
2. Dans l’onglet Affichage, dans le groupe Vues du classeur, cliquez sur Mise en page.
  Excel affiche la feuille de calcul en mode Mise en page.
3. Pour afficher ou modifier un en-tête ou un pied de page, cliquez sur la zone de texte de l'en-tête ou du pied de page de gauche, du centre ou de droite en haut ou en bas de la page de la feuille de calcul (sous En-tête ou au-dessus de Pied de page).


## **Obtention d’en-têtes et pieds de page avec Aspose.Cells for C++**
Avec les méthodes [**Worksheet.PageSetup.GetHeader**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getheader/) et [**Worksheet.PageSetup.GetFooter**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfooter/), les développeurs C++ peuvent simplement obtenir les en-têtes ou pieds de page du fichier.

1. Construisez un classeur pour ouvrir le fichier.
2. Obtenez la feuille de calcul où vous souhaitez obtenir les en-têtes ou les pieds de page.
3. Obtenez l'en-tête ou le pied de page avec un identifiant de section spécifique.

```c++
#include <iostream>
#include <codecvt>
#include <locale>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook workbook(srcDir + u"HeaderFooter.xlsx");
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    std::cout << sheet.GetPageSetup().GetHeader(0).ToUtf8() << std::endl;
    std::cout << sheet.GetPageSetup().GetHeader(1).ToUtf8() << std::endl;
    std::cout << sheet.GetPageSetup().GetHeader(2).ToUtf8() << std::endl;
    std::cout << sheet.GetPageSetup().GetFooter(1).ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Analyser les en-têtes et les pieds de page en liste de commandes**
Le texte de l'en-tête ou du pied de page peut contenir des commandes spéciales, par exemple un espace réservé pour le numéro de page, la date actuelle ou des attributs de formatage de texte.

Les commandes spéciales sont représentées par une seule lettre précédée d'un esperluette ("&").

Les chaînes d'en-tête et de pied de page sont construites en utilisant la grammaire ABNF. Il n'est pas facile de comprendre sans un visualiseur.

Aspose.Cells for C++ fournit la méthode [**Worksheet.PageSetup.GetCommands**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcommands/) pour analyser les en-têtes et pieds de page en tant que liste de commandes.

Le code suivant montre comment analyser un en-tête ou un pied de page en tant que liste de commandes et traiter les commandes :

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"HeaderFooter.xlsx");

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get left section of header
    U16String headerSection = sheet.GetPageSetup().GetHeader(0);

    // Get commands from the header section
    Vector<HeaderFooterCommand> commands = sheet.GetPageSetup().GetCommands(headerSection);

    // Iterate through each command
    for (int i = 0; i < commands.GetLength(); ++i)
    {
        HeaderFooterCommand c = commands[i];
        switch (c.GetType())
        {
            case HeaderFooterCommandType::SheetName:
                // Embedded the name of the sheet to header or footer
                break;
            default:
                break;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
