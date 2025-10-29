---
title: Convertir le graphique en image pour la région chinoise avec Golang via C++
linktitle: Définir la région chinoise
description: Apprenez à utiliser Aspose.Cells for C++ pour configurer la localisation chinoise pour les graphiques. Notre guide montrera comment configurer les graphiques pour supporter les caractères et formats chinois, y compris polices, tailles, orientations du texte, et plus encore.
keywords: Aspose.Cells for C++, graphiques, configuration chinoise, polices, taille de police, orientation du texte, support.
type: docs
weight: 9
url: /fr/go-cpp/convert-chart-to-image-for-chinese-region/
alias: [/cpp/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

Dans ce sujet, nous vous montrerons comment définir la région chinoise pour un graphique.

{{% /alert %}}

## **Définit une classe d'héritage**

Première étape, vous devez définir une classe "ChartChineseSetttings" qui hérite de [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/). 
Ensuite, en surchargeant les fonctions associées, vous pouvez définir le texte des éléments du graphique dans votre propre langue.

Exemple de code :
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChineseSettting.go" >}}
Ensuite, vous pouvez voir l'effet dans l'image de sortie, les éléments du graphique seront rendus selon vos paramètres.

## **Conclusion**

Dans cet exemple, si vous ne définissez pas la région chinoise pour un graphique, les éléments du graphique suivants peuvent être rendus dans la langue par défaut, telle que l'anglais.
Après l'opération ci-dessus, nous pouvons obtenir une image de graphique de sortie avec une région chinoise.

|**Éléments pris en charge**|**Valeur dans cet exemple**|**valeur par défaut dans l'environnement anglais**|
| :- | :- | :- |
|Nom du titre de l'axe|坐标轴标题|Titre de l'axe|
|Nom de l'unité de l'axe|百,千...|Centaines, Milliers...|
|Nom du titre du graphique|图表标题|Titre du graphique|
|Nom de Légende Augmentation|增加|Augmentation|
|Nom de Légende Diminution|减少|Diminution|
|Nom de Légende Total|汇总|Total|
|Autre Nom|其他|Autre|
|Nom de Série|系列|Série|
