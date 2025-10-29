---
title: Convertir un graphique Excel en image avec C++
linktitle: Convertir un graphique Excel en image
type: docs
weight: 20
url: /fr/cpp/convert-an-excel-chart-to-image/
description: Apprenez comment convertir des graphiques Excel en images avec Aspose.Cells en C++.
---

{{% alert color="primary" %}}

 Les graphiques sont attrayants visuellement et permettent aux utilisateurs de voir facilement les comparaisons, les modèles et les tendances dans les données. Par exemple, plutôt que d'analyser des colonnes de numéros de feuille de calcul, un graphique montre en un coup d'œil si les ventes diminuent ou augmentent, ou comment les ventes réelles se comparent aux prévisions. Les gens doivent souvent présenter des informations statistiques et graphiques d'une manière facile à comprendre et à maintenir. Une image aide.

 Parfois, des graphiques sont nécessaires dans une application ou sur des pages Web. Ou ils peuvent être nécessaires pour un document Word, un fichier PDF, une présentation PowerPoint ou une autre application. Dans chaque cas, vous souhaitez rendre le graphique sous forme d’image afin de l’utiliser ailleurs.

{{% /alert %}}

## **Conversion des graphiques en images**

 Dans les exemples ici, un graphique en secteur et un graphique en colonnes sont convertis en images.

### **Conversion d'un graphique circulaire en fichier image**

Tout d'abord, créez un graphique circulaire dans Microsoft Excel et convertissez-le ensuite en un fichier image avec Aspose.Cells. Le code de cet exemple crée une image EMF basée sur le graphique circulaire dans le fichier de modèle Microsoft Excel.

|**Sortie : image du graphique circulaire**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|

1. Créer un graphique en secteur dans Microsoft Excel:
   1. Ouvrir un nouveau classeur dans Microsoft Excel.
   1. Entrer des données dans une feuille de calcul.
   1. Créez un graphique circulaire basé sur les données.
   1. Enregistrez le fichier.

|**Le fichier d'entrée.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|

1. Téléchargez et installez Aspose.Cells :
   1. [Télécharger Aspose.Cells for C++](https://downloads.aspose.com/cells/cpp).
   1. Installez-le sur votre ordinateur de développement.

Tous les composants [Aspose](http://www.aspose.com/) fonctionnent en mode d'évaluation lorsqu'ils sont installés pour la première fois. Le mode d'évaluation n'a pas de limite de temps et il ne fait qu'insérer des filigranes dans les documents de sortie.

1. Créer un projet :
   1. Démarrez votre environnement de développement C++ (par exemple, Visual Studio).
   1. Créez une nouvelle application console.
   1. Ajoutez une référence à Aspose.Cells. Ce projet utilise Aspose.Cells, donc ajoutez une référence à la bibliothèque Aspose.Cells.
   1. Écrire le code qui trouve et convertit le graphique. Ci-dessous se trouve le code utilisé par le composant pour accomplir la tâche. Très peu de lignes de code sont utilisées.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the existing excel file which contains the pie chart.
    Workbook workbook(srcDir + u"PieChart.xlsx");

    // Get the designer chart (first chart) in the first worksheet of the workbook.
    Chart chart = workbook.GetWorksheets().Get(0).GetCharts().Get(0);

    // Convert the chart to an image file.
    chart.ToImage(srcDir + u"PieChart.out.emf", Aspose::Cells::Drawing::ImageType::Emf);

    std::cout << "Chart converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Conversion d'un graphique à colonnes en un fichier image**

Tout d'abord, créez un graphique en colonnes dans Microsoft Excel et convertissez-le en fichier image, comme ci-dessus. Après l'exécution du code d'exemple, un fichier JPEG est créé à partir du graphique en colonnes dans le fichier Excel modèle.

|**Fichier de sortie : une image de graphique à colonnes.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|

1. Créer un graphique à colonnes dans Microsoft Excel :
   1. Ouvrir un nouveau classeur dans Microsoft Excel.
   1. Entrer des données dans une feuille de calcul.
   1. Créer un graphique à colonnes basé sur les données.
   1. Enregistrez le fichier.

|**Fichier d'entrée.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|

1. Configurer un projet, avec des références, comme décrit ci-dessus.
1. Convertir le graphique en une image dynamiquement. Voici le code utilisé par le composant pour accomplir la tâche. Le code est similaire à celui précédent :

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the existing excel file which contains the column chart.
    U16String inputFilePath = srcDir + u"ColumnChart.xlsx";
    Workbook workbook(inputFilePath);

    // Get the designer chart (first chart) in the first worksheet of the workbook.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Chart chart = worksheet.GetCharts().Get(0);

    // Convert the chart to an image file.
    U16String outputImagePath = srcDir + u"ColumnChart.out.jpeg";
    chart.ToImage(outputImagePath, ImageType::Jpeg);

    std::cout << "Chart converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
