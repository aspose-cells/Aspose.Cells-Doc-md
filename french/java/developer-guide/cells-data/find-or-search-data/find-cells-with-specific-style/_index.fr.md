---
title: Trouver des cellules avec un style spécifique
type: docs
weight: 80
url: /fr/java/find-cells-with-specific-style/
description: Cet article montre comment rechercher des cellules avec un style spécifique à l'aide de MS Excel et Aspose.Cells for Java API.
keywords: find cells with specific style, find cells with specific style excel, find cells with specific style excel java, search cells with specific style, search cells with specific style excel, search cells with specific style excel java, how to find cells with specific style, how to find cells with specific style excel, how to find cells with specific style excel java
---
{{% alert color="primary" %}}

Parfois, vous devez trouver les cellules avec un style particulier. Cet article montre comment y parvenir en utilisant Microsoft Excel ainsi que Aspose.Cells for Java API.

{{% /alert %}}

## Utilisation d'Excel Microsoft

Ce sont les étapes nécessaires pour rechercher des cellules avec des styles spécifiques dans MS Excel.

1.  Sélectionner**Rechercher et sélectionner** dans le**Onglet Accueil**.
1.  Sélectionner**Trouver**.
1.  Cliquez sur**Choix**si les options avancées ne sont pas visibles.
1.  Sélectionner**Choisissez le format de Cell...** du**Format** menu déroulant.
1. Sélectionnez la cellule avec le style que vous souhaitez rechercher.
1.  Cliquez sur**Trouver tout** pour trouver toutes les cellules avec un style similaire à la cellule sélectionnée.

## En utilisant Aspose.Cells for Java

 Aspose.Cells for Java fournit la fonctionnalité permettant de rechercher des cellules dans une feuille de calcul avec un style spécifique. Pour cela, le API fournit[**FindOptions.setStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#Style) la propriété.

### Exemple de code

 L'extrait de code suivant trouve toutes les cellules qui ont le même style que celui de cellule**A1** et modifie le texte à l'intérieur de ces cellules. Veuillez consulter la capture d'écran des fichiers source et de sortie pour analyser la sortie de l'exemple de code.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindCellsWithSpecificStyle-FindCellsWithSpecificStyle.java" >}}

Après l'exécution du code, toutes les cellules qui ont le même style que la cellule A1 auront un texte "Trouvé".

### Captures d'écran

![tâche : image_autre_texte](find-cells-with-specific-style_1.png)

**Chiffre:** Fichier source avec des cellules ayant des styles

 Voici le fichier de sortie généré par le code suivant. Vous pouvez voir toutes les cellules qui ont le même style que la cellule**A1** a un texte "Trouvé"

![tâche : image_autre_texte](find-cells-with-specific-style_2.png)

**Chiffre:**Fichier de sortie avec les cellules trouvées après une recherche par**A1** style
