---
title: Comment mettre à l’échelle une feuille avec C++
linktitle: Comment mettre à l échelle une feuille de calcul
type: docs
weight: 130
url: /fr/cpp/how-to-scale-a-worksheet/
description: Cet article vous montre un code expliquant comment agrandir une feuille de calcul à l aide de la bibliothèque Aspose.Cells avec C++.
keywords: Échelle en C++, Comment agrandir une feuille de calcul en C++, Agrandir une feuille en C++.
---

## **Scénarios d'utilisation possibles**
Mettre à l'échelle une feuille de calcul peut être utile pour diverses raisons, en fonction du contexte dans lequel vous travaillez. Voici quelques raisons courantes :
1. Adapter à la page : pour s'assurer que tout le contenu tient sur une seule page ou un nombre spécifique de pages lors de l'impression, ce qui facilite la lecture et la gestion sans avoir à faire défiler plusieurs pages.

1. Présentation : pour rendre la feuille de calcul plus organisée et professionnelle, notamment lorsqu'elle est partagée lors de réunions ou dans des rapports.

1. Lisibilité : pour ajuster la taille du texte et d'autres éléments pour une meilleure lisibilité, en particulier pour les personnes ayant des difficultés à lire de petites polices.

1. Gestion de l'espace : pour optimiser l'utilisation de l'espace sur une feuille de calcul, en veillant à ce qu'il n'y ait pas d'espace blanc inutile et que toutes les informations importantes soient visibles sans défilement excessif.

1. Visualisation des données : dans le cas de graphiques et de diagrammes, la mise à l'échelle peut aider à les rendre plus compréhensibles en ajustant leur taille pour s'adapter à l'espace disponible.

1. Cohérence : pour maintenir une apparence cohérente à travers plusieurs feuilles de calcul ou documents, ce qui est particulièrement important dans des contextes professionnels et éducatifs.

## **Comment mettre à l'échelle une feuille de calcul dans Excel**
Mettre à l'échelle une feuille de calcul dans Excel peut vous aider à faire tenir votre contenu sur une seule page ou un nombre spécifié de pages lors de l'impression. Voici les étapes pour mettre à l'échelle une feuille :

1. Ouvrir votre feuille de calcul : ouvrez la feuille Excel que vous souhaitez mettre à l'échelle.

1. Aller à l'onglet Mise en Page : cliquez sur l'onglet Mise en Page dans le ruban.

1. Groupe Mise à l’échelle : dans l'onglet Mise en Page, trouvez le groupe Mise à l’échelle. Vous avez ici des options pour ajuster la mise à l’échelle. Largeur : permet de spécifier le nombre de pages en largeur pour l'impression. Hauteur : permet de spécifier le nombre de pages en hauteur pour l'impression. Échelle : vous pouvez également définir un pourcentage de mise à l’échelle personnalisé.
<br>
<img src="1.png" width=60% />

1. Ajuster la largeur et la hauteur : définir la largeur et la hauteur selon le nombre de pages souhaité. Par exemple, définir les deux à 1 page si vous souhaitez que la feuille tienne sur une seule page.

1. Ajuster le pourcentage de mise à l’échelle (si nécessaire) : si vous préférez définir un pourcentage spécifique, ajustez la case Échelle. Par exemple, le réglage à 50 % réduira tout à la moitié de la taille.


## **Comment agrandir une feuille à l'aide de C++**
Aspose.Cells est une bibliothèque puissante pour travailler avec des fichiers Excel de manière programmatique. Pour agrandir une feuille avec Aspose.Cells, vous devez suivre ces étapes : charger [fichier exemple](sample.xlsx) et ajuster les paramètres d'impression pour que le contenu tienne sur le nombre de pages souhaité ou un pourcentage spécifique de la taille d'origine.

### **Exemple : Ajuster à la page**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the PageSetup object
    PageSetup pageSetup = sheet.GetPageSetup();

    // Set the worksheet to fit to 1 page wide and 1 page tall
    pageSetup.SetFitToPagesWide(1);
    pageSetup.SetFitToPagesTall(1);

    // Save the modified workbook
    workbook.Save(u"output_fit_to_page.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
<br>
<img src="3.png" width=60% />

### **Exemple : Mettre à l'échelle en pourcentage**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    // Initialize Aspose.Cells
    Aspose::Cells::Startup();

    // Load the Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the PageSetup object
    PageSetup pageSetup = sheet.GetPageSetup();

    // Set the scaling to a specific percentage (e.g., 75%)
    pageSetup.SetZoom(75);

    // Save the modified workbook
    workbook.Save(u"output_scaled_percentage.xlsx");

    // Clean up Aspose.Cells resources
    Aspose::Cells::Cleanup();

    return 0;
}
```
<br>
<img src="2.png" width=60% />
