---
title: Convertir le graphique en image localisée
linktitle: Définir la région localisée
type: docs
weight: 50
url: /fr/net/convert-chart-to-localized-image/
alias: [/net/how-to-set-globalization-configuration-for-chart/]
---
{{% alert color="primary" %}}

Dans cette rubrique, nous vous montrerons comment convertir un graphique en image localisée, vous saurez comment définir une région localisée pour un graphique.

{{% /alert %}}

##  **Scénario**

Dans quel scénario aurions-nous besoin de définir une région localisée pour un graphique ?

 Lorsque vous ouvrez un fichier xlsx avec un graphique dans Excel, dans ce cas, supposons que vous l'ouvriez avec un paramètre régional espagnol dans Excel, vous pouvez voir les éléments dans la zone du graphique, tels que le titre du graphique, la longueur, ils sont traduits en espagnol. Mais lorsque vous enregistrez ce graphique en tant qu'image avec Aspose.Cells, vous pouvez rencontrer le problème suivant :

**![Global Issue](GlobalIssue.png)**

Dans ce scénario, la longueur du graphique dans l'image de sortie n'est pas la même que dans Excel, elle reste affichée en anglais par défaut. Vous pouvez maintenant résoudre ce problème en définissant une région localisée pour le graphique. Avec les paramètres corrects, les éléments suivants seront rendus en fonction de vos paramètres de localisation.

##  **Éléments pris en charge**

Les éléments suivants du graphique peuvent être rendus en fonction de vos paramètres de localisation.

|**Éléments pris en charge**|**valeur par défaut dans l'environnement anglais**|
| :- | :- |
|Nom du titre de l'axe|Titre de l'axe|
|Nom de l'unité de l'axe|Des centaines, des milliers...|
|Nom du titre du graphique|Titre du graphique|
|Légende Augmenter le nom|Augmenter|
|Légende Réduire le nom|Diminuer|
|Légende Total Nom|Total|
|Autre nom|Autre|
|Nom de la série|Série|

##  **Étapes de fonctionnement**

L'exemple suivant vous montrera en détail comment définir une région localisée pour obtenir l'effet souhaité.

- [Comment définir la région chinoise pour le graphique](/cells/fr/net/convert-chart-to-image-for-chinese-region/)
- [Comment définir la région japonaise pour le graphique](/cells/fr/net/convert-chart-to-image-for-japanese-region/)

