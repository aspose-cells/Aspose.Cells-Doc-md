---
title: Détecter les cellules fusionnées dans une feuille de calcul
type: docs
weight: 3000
url: /fr/java/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Dans Microsoft Excel, plusieurs cellules peuvent être fusionnées en une seule. Cela est souvent utilisé pour créer des tableaux complexes ou pour créer une cellule qui contient un en-tête qui s'étend sur plusieurs colonnes.

Aspose.Cells vous permet d'identifier les zones de cellules fusionnées dans une feuille de calcul. Vous pouvez également les dé-fusionner. Cet article fournit les lignes de code les plus simples pour effectuer la tâche avec Aspose.Cells.

Cet article fournit des instructions compactes sur la manière de trouver puis dé-fusionner les cellules fusionnées dans une feuille de calcul.

{{% /alert %}}

## **Démonstration**

Cet exemple utilise un fichier Microsoft Excel modèle appelé **MergeTrial**. Il a quelques zones de cellules fusionnées dans une feuille également appelée Fusion d'essai.

**Le fichier modèle**

![todo:image_alt_text](detect-merged-cells-in-a-worksheet_1.png)

Aspose.Cells fournit la méthode [**Cells.getMergedCells()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells/#getMergedCells--) qui permet d'obtenir toutes les cellules fusionnées.

Lorsque le code ci-dessous est exécuté, il efface le contenu de la feuille et dé-fusionne toutes les zones de cellules avant d'enregistrer à nouveau le fichier.

**Le fichier de sortie**

![todo:image_alt_text](detect-merged-cells-in-a-worksheet_2.png)

## **Exemple de code**

Veuillez consulter le code d'exemple suivant pour savoir comment identifier les zones de cellules fusionnées dans une feuille de calcul et les dé-fusionner.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectMergedCells-DetectMergedCells.java" >}}

## **Articles connexes**

- [Fusionner et scinder des cellules](/cells/fr/java/fusionner-et-separer-des-cellules/).
{{< app/cells/assistant language="java" >}}
