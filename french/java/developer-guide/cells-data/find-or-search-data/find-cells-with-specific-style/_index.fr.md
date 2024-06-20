---
title: Trouver des cellules avec un style spécifique
type: docs
weight: 80
url: /fr/java/find-cells-with-specific-style/
description: Cet article démontre comment trouver des cellules avec un style spécifique en utilisant MS Excel et Aspose.Cells for Java API.
keywords: trouver des cellules avec un style spécifique, trouver des cellules avec un style spécifique excel, trouver des cellules avec un style spécifique excel java, rechercher des cellules avec un style spécifique, rechercher des cellules avec un style spécifique excel, rechercher des cellules avec un style spécifique excel java, comment trouver des cellules avec un style spécifique, comment trouver des cellules avec un style spécifique excel, comment trouver des cellules avec un style spécifique excel java
---

{{% alert color="primary" %}}

Parfois, vous devez trouver des cellules avec un style particulier. Cet article démontre comment y parvenir en utilisant Microsoft Excel ainsi que l'API Aspose.Cells for Java.

{{% /alert %}}

## Utiliser Microsoft Excel

Voici les étapes requises pour rechercher des cellules avec des styles spécifiques dans MS Excel.

1. Sélectionnez **Rechercher et sélectionner** dans l'onglet **Accueil**.
1. Sélectionnez **Rechercher**.
1. Cliquez sur **Options** si les options avancées ne sont pas visibles.
1. Sélectionnez **Choisir le format à partir de la cellule...** dans le menu déroulant **Format**.
1. Sélectionnez la cellule avec le style que vous souhaitez rechercher.
1. Cliquez sur **Trouver tout** pour trouver toutes les cellules avec un style similaire à votre cellule sélectionnée.

## Utiliser Aspose.Cells for Java

Aspose.Cells for Java propose la fonctionnalité de trouver des cellules dans la feuille de calcul avec un style spécifique. Pour cela, l'API fournit la propriété [**FindOptions.setStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#Style).

### Code d'exemple

Le code suivant trouve toutes les cellules qui ont le même style que la cellule **A1** et modifie le texte à l'intérieur de ces cellules. Veuillez consulter la capture d'écran des fichiers source et de sortie pour analyser la sortie du code d'exemple.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindCellsWithSpecificStyle-FindCellsWithSpecificStyle.java" >}}

Après l'exécution du code, toutes les cellules qui ont le même style que la cellule A1 auront un texte "Trouvé".

### Captures d'écran

![todo:image_alt_text](find-cells-with-specific-style_1.png)

**Figure :** Fichier source avec des cellules ayant des styles

Voici le fichier de sortie généré par le code suivant. Vous pouvez voir toutes les cellules qui ont le même style que la cellule **A1** a un texte "Trouvé"

![todo:image_alt_text](find-cells-with-specific-style_2.png)

**Figure :** Fichier de sortie avec les cellules trouvées après la recherche par le style **A1**
