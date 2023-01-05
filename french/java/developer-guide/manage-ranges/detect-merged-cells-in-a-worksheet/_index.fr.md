---
title: Détecter fusionné Cells dans une feuille de calcul
type: docs
weight: 3000
url: /fr/java/detect-merged-cells-in-a-worksheet/
---
{{% alert color="primary" %}}

Dans Microsoft Excel, plusieurs cellules peuvent être fusionnées en une seule. Ceci est souvent utilisé pour créer des tableaux complexes ou pour créer une cellule contenant un en-tête qui s'étend sur plusieurs colonnes.

Aspose.Cells vous permet d'identifier les zones de cellules fusionnées dans une feuille de calcul. Vous pouvez également les dissocier. Cet article fournit les lignes de code les plus simples pour effectuer la tâche à l'aide de Aspose.Cells.

Cet article fournit des instructions compactes sur la façon de rechercher puis de dissocier des cellules fusionnées dans une feuille de calcul.

{{% /alert %}}

## **Manifestation**

 Cet exemple utilise un modèle de fichier Excel Microsoft appelé**MergeTrial**. Il comporte des zones de cellules fusionnées dans une feuille également appelée Merge Trial.

**Le fichier modèle**

![tâche : image_autre_texte](detect-merged-cells-in-a-worksheet_1.png)

 Aspose.Cells fournit le[**Cells.getMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MergedCells)méthode utilisée pour obtenir une ArrayList de zones de cellules fusionnées.

Lorsque le code ci-dessous est exécuté, il efface le contenu de la feuille et dissocie toutes les zones de cellules avant de réenregistrer le fichier.

**Le fichier de sortie**

![tâche : image_autre_texte](detect-merged-cells-in-a-worksheet_2.png)

## **Exemple de code**

Veuillez consulter l'exemple de code suivant pour savoir comment identifier les zones de cellules fusionnées dans une feuille de calcul et les dissocier.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectMergedCells-DetectMergedCells.java" >}}

## **Articles Liés**

- [Fusionner et diviser des cellules](/cells/fr/java/merging-and-unmerging-cells/).
