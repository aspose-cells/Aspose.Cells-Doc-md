---
title: Convertir un graphique en image localisée avec Node.js via C++
description: Apprenez à définir les configurations de globalisation pour les graphiques en utilisant Aspose.Cells for Node.js via C++. Notre guide montre comment configurer le graphique pour prendre en charge plusieurs langues et formats régionaux afin d’afficher correctement le texte, les dates et les nombres dans différentes langues.
keywords: Aspose.Cells for Node.js via C++, Graphiques, Paramètres de globalisation, Plusieurs langues, Formats régionaux, Affichage, texte, dates, nombres.
linktitle: Définir la région localisée
type: docs
weight: 50
url: /fr/nodejs-cpp/convert-chart-to-localized-image/
alias: [/nodejs-cpp/how-to-set-globalization-configuration-for-chart/]
---

{{% alert color="primary" %}}

Dans ce sujet, nous vous montrerons comment convertir un graphique en image localisée. Vous saurez comment définir la région localisée pour un graphique.

{{% /alert %}}

## **Scénario**

Dans quel scénario aurions-nous besoin de définir une région localisée pour un graphique ? 

Lorsque vous ouvrez un fichier xlsx avec un graphique dans Excel, dans ce cas, supposons que vous l’ouvrez avec un paramètre régional espagnol dans Excel, vous pouvez voir que les éléments dans la zone du graphique, tels que Titre du graphique, Légende, sont traduits en espagnol. Mais lorsque vous enregistrez ce graphique en tant qu’image avec Aspose.Cells, vous pouvez rencontrer le problème suivant : 

**![Problème global](GlobalIssue.png)**

Dans ce scénario, la légende du graphique dans l’image de sortie n’est pas identique à celle dans Excel ; elle reste affichée en anglais par défaut. Vous pouvez résoudre ce problème en définissant une région localisée pour le graphique. Avec les bons paramètres, les éléments suivants seront rendus selon vos paramètres de localisation.

## **Éléments pris en charge**

Les éléments suivants dans le graphique peuvent être rendus en fonction de vos paramètres de localisation.

|**Éléments pris en charge**|**valeur par défaut dans l'environnement anglais**|
| :- | :- |
|Nom de l'axe des ordonnées|Titre de l'axe|
|Nom de l'unité de l'axe|Centaines, Milliers...|
|Nom du titre du graphique|Titre du graphique|
|Nom de l'augmentation de la légende|Augmentation|
|Nom de la diminution de la légende|Diminution|
|Nom total de la légende|Total|
|Autre nom|Autre|
|Nom de la série|Série|

## **Étapes de l'opération**

L'exemple suivant vous montrera en détail comment définir une région localisée pour obtenir l’effet souhaité.

- [Comment définir la région chinoise pour le graphique](/cells/fr/nodejs-cpp/convert-chart-to-image-for-chinese-region/)
- [Comment définir la région japonaise pour le graphique](/cells/fr/nodejs-cpp/convert-chart-to-image-for-japanese-region/)


