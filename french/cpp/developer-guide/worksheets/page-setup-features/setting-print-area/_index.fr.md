---
title: Comment définir la zone d impression avec C++
linktitle: Comment définir une zone d impression
type: docs
weight: 200
url: /fr/cpp/how-to-set-print-area/
description: Cet article vous montre du code expliquant comment définir la zone d impression en utilisant la bibliothèque Aspose.Cells avec C++.
keywords: Limiter la plage d impression, définir la plage d impression, effacer la plage d impression, définir et effacer la plage d impression en utilisant C++, Comment définir la zone d impression en C++, Définir et effacer la zone d impression en C++, Comment effacer la zone d impression en C++, Comment ajouter une zone d impression en C++, Comment supprimer une zone d impression en C++, Comment définir la zone d impression dans Excel, Comment effacer la zone d impression dans Excel.
---

## **Scénarios d'utilisation possibles**

La définition d'une zone d'impression dans un document, comme une feuille de calcul Excel, permet de contrôler le contenu inclus lors de l'impression. Voici quelques raisons de définir une zone d'impression :

1. Se concentrer sur des données spécifiques : vous pouvez imprimer uniquement les sections les plus pertinentes, en évitant le contenu inutile.
1. Amélioration de la disposition : cela aide à organiser et à faire en sorte que le contenu s'adapte proprement sur les pages imprimées, évitant les coupures ou les sauts de page indésirables.
1. Économiser des ressources : en limitant la zone d'impression, vous pouvez réduire la quantité de papier et d'encre utilisée.
1. Présentation professionnelle : cela garantit que seule la version finalisée et soignée des données est imprimée, ce qui est particulièrement important pour les rapports ou présentations.
1. Cohérence : lors de l'impression du même document plusieurs fois, avoir une zone d'impression définie assure une cohérence dans le résultat.

<br>
La définition d'une zone d'impression est particulièrement utile dans les grands documents où seule une partie doit être partagée ou examinée sous forme imprimée.

## **Comment définir une zone d'impression dans Excel**

Pour définir une zone d'impression dans Excel, suivez ces étapes :

1. Sélectionnez les cellules : cliquez et faites glisser pour sélectionner la plage de cellules que vous souhaitez définir comme zone d'impression.
1. Ouvrez l'onglet Mise en page : allez à l'onglet "Mise en page" dans le ruban en haut de la fenêtre Excel.
1. Définir la zone d'impression : dans le groupe Mise en page, cliquez sur "Zone d'impression". Dans le menu déroulant, sélectionnez "Définir la zone d'impression".
<br>
<img src="3.png" width=60% />

1. Ajouter à la zone d'impression : si vous souhaitez ajouter plus de cellules à la zone d'impression existante, sélectionnez les cellules supplémentaires, allez dans "Zone d'impression" dans l'onglet Mise en page, et choisissez "Ajouter à la zone d'impression".

<br>
Cette action définira les cellules sélectionnées comme zone d'impression. Lorsque vous imprimez la feuille de calcul, seule cette zone définie sera imprimée.

## **Comment effacer la zone d'impression dans Excel**

Pour effacer la zone d'impression dans Excel, suivez ces étapes :

1. Ouvrir l'onglet Mise en Page : Cliquez sur l'onglet « Mise en Page » dans le ruban en haut de la fenêtre Excel.
1. Effacer la zone d'impression : Dans le groupe "Mise en page", cliquez sur "Zone d'impression". Dans le menu déroulant, sélectionnez "Effacer la zone d'impression".
<br>
<img src="4.png" width=60% />

<br>
Cette action supprimera toute zone d'impression précédemment définie, permettant l'impression de la feuille entière.

## **Que se passe-t-il après avoir effacé la zone d'impression**

Effacer la zone d'impression dans une application de feuille de calcul comme Excel avec Aspose.Cells entraînera l'inclusion de toute la feuille lors de l'impression. Si une zone d'impression est définie, seule la plage de cellules spécifiée sera imprimée. En effaçant la zone d'impression, vous vous assurez qu'aucune plage spécifique n'est définie, et le comportement d'impression par défaut, qui inclut toute la feuille, sera appliqué.

1. Comportement d'impression par défaut : Toute la feuille sera considérée pour l'impression. Cela signifie que toutes les cellules avec des données ou une mise en forme seront imprimées.
1. Limites de la zone d'impression absentes : Les limites de la zone d'impression précédemment définies seront supprimées. Si des lignes et colonnes spécifiques étaient désignées pour l'impression, elles ne seront plus contraintes par ces limites.
1. Impression de tout le contenu : Tout le contenu, y compris les en-têtes, pieds de page et autres données de la feuille, sera inclus dans l'impression.

## **Comment définir la zone d'impression avec Aspose.Cells**

Pour définir la zone d'impression dans une feuille spécifiée : d'abord, chargez le [fichier exemple](input.xlsx), puis modifiez la propriété [**Worksheet.GetPrintArea()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintarea/) de l'objet [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) pour la feuille souhaitée. La définition de cette propriété à une chaîne de plage fixera la zone d'impression.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the workbook
    U16String inputFilePath(u"input.xlsx");
    Workbook workbook(inputFilePath);

    // Access the desired worksheet
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet worksheet = sheets.Get(0);

    // Set the print area - specify the range you want to print
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintArea(u"A1:D10");

    // Save the workbook
    U16String outputFilePath(u"set_print_area.pdf");
    workbook.Save(outputFilePath);

    std::cout << "Print area set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Le résultat en sortie :
<br>
<img src="1.png" width=60% />

## **Comment effacer la zone d'impression avec Aspose.Cells**

Pour effacer la zone d'impression dans une feuille spécifiée : d'abord, chargez le [fichier exemple](input.xlsx), puis modifiez la propriété [**Worksheet.GetPrintArea()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintarea/) de l'objet [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) pour la feuille souhaitée. La définition de cette propriété à une chaîne vide effacera la zone d'impression.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the workbook
    U16String inputFilePath(u"input.xlsx");
    Workbook workbook(inputFilePath);

    // Access the desired worksheet
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet worksheet = sheets.Get(0);

    // Clear the print area
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintArea(u"");

    // Save the workbook
    U16String outputFilePath(u"clear_print_area.pdf");
    workbook.Save(outputFilePath);

    std::cout << "Print area cleared and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Le résultat en sortie :
<br>
<img src="2.png" width=60% />
{{< app/cells/assistant language="cpp" >}}
