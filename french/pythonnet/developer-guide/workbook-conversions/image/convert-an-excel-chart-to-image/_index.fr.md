---
title: Convertir un graphique Excel en image
type: docs
weight: 20
url: /fr/python-net/convert-an-excel-chart-to-image/
description: Convertissez un graphique Excel en image en utilisant Aspose.Cells for Python via .NET API.
keywords: Python Convert an Excel Chart to Image, Export an Excel Chart to Image in Python via NET, Python Save an Excel Chart to Image.
---
{{% alert color="primary" %}}

Les graphiques sont visuellement attrayants et permettent aux utilisateurs de voir facilement les comparaisons, les modèles et les tendances des données. Par exemple, plutôt que d’analyser les colonnes des numéros d’une feuille de calcul, un graphique montre d’un coup d’œil si les ventes sont en baisse ou en hausse, ou comment les ventes réelles se comparent aux ventes projetées. Il est fréquemment demandé aux gens de présenter des informations statistiques et graphiques d’une manière facile à comprendre et à gérer. Une image aide.

Parfois, des graphiques sont nécessaires dans une application ou des pages Web. Ou cela peut être nécessaire pour un document Word, un fichier PDF, une présentation PowerPoint ou une autre application. Dans chaque cas, vous souhaitez restituer le graphique sous forme d’image afin de pouvoir l’utiliser ailleurs.

{{% /alert %}}

##  **Conversion de graphiques en images**

Dans les exemples ici, un diagramme circulaire et un caractère de colonne sont convertis en images.

###  **Conversion d'un graphique à secteurs en fichier image**

Tout d’abord, créez un diagramme circulaire dans Microsoft Excel, puis convertissez-le en fichier image avec Aspose.Cells for Python via .NET. Le code de cet exemple crée une image EMF basée sur le diagramme circulaire du modèle de fichier Excel Microsoft.

|**Résultat : image de diagramme circulaire**|
| :- |
|![tâche : image_alt_text](convert-an-excel-chart-to-image_1.png)|

1. Créez un diagramme circulaire dans Excel Microsoft :
 1. Ouverture d'un nouveau classeur dans Excel Microsoft.
 1. Saisissez quelques données dans une feuille de calcul.
 1. Création d'un diagramme circulaire basé sur les données.
 1. Enregistrez le fichier.

|**Le fichier d'entrée.**|
| :- |
|![tâche : image_alt_text](convert-an-excel-chart-to-image_2.png)|

Nous hébergeons nos packages Python dans des référentiels PyPi.

Installez Aspose.Cells for Python à partir de pypi, utilisez la commande comme : $ pip install aspose-cells-python.

Et vous pouvez également suivre les instructions étape par étape pour installer « Aspose.Cells for Python via .NET » dans votre environnement de développeur.
1. Téléchargez et installez Aspose.Cells for Python via .NET :
 1. Installez Aspose.Cells for Python via .NET à partir de[Pypi](https://pypi.org/project/aspose-cells-python/)utilisez la commande comme : $ pip install aspose-cells-python.
 1. Et vous pouvez également suivre le[instructions étape par étape](https://docs.aspose.com/cells/python-net/getting-started/)sur la façon d'installer "Aspose.Cells for Python via .NET" dans votre environnement de développeur.

 Tous[Aspose](http://www.aspose.com/) les composants fonctionnent en mode évaluation lors de leur première installation. Le mode d'évaluation n'a pas de limite de temps et injecte uniquement des filigranes dans les documents de sortie.

1. Créez un projet :
 1. Démarrez Visual Studio.
 1. Ajoutez une référence de bibliothèque (importez la bibliothèque) à votre projet Python.
 1. Écrivez le code qui recherche et convertit le graphique. Vous trouverez ci-dessous le code utilisé par le composant pour accomplir la tâche. Très peu de lignes de code sont utilisées.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ConvertingPieChartToImageFile-1.py" >}}

###  **Conversion d'un histogramme en fichier image**

Créez d’abord un histogramme dans Excel Microsoft et convertissez-le en fichier image, comme ci-dessus. Après avoir exécuté l'exemple de code, un fichier JPEG est créé sur la base de l'histogramme du modèle de fichier Excel.

|**Fichier de sortie : une image de diagramme à colonnes.**|
| :- |
|![tâche : image_alt_text](convert-an-excel-chart-to-image_3.png)|

1. Créez un histogramme dans Microsoft Excel :
 1. Ouvrez un nouveau classeur dans Microsoft Excel.
 1. Saisissez quelques données dans une feuille de calcul.
 1. Créez un histogramme basé sur les données.
 1. Enregistrez le fichier.

|**Fichier d'entrée.**|
| :- |
|![tâche : image_alt_text](convert-an-excel-chart-to-image_4.png)|

1. Mettez en place un projet, avec des références, comme décrit ci-dessus.
1. Convertissez le graphique en image de manière dynamique. Voici le code utilisé par le composant pour accomplir la tâche. Le code est similaire au précédent :

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ConvertingColumnChartToImage-1.py" >}}
