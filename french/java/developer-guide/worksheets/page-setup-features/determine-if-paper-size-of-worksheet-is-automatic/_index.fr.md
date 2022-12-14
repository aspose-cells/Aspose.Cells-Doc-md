---
title: Déterminer si la taille du papier de la feuille de calcul est automatique
type: docs
weight: 20
url: /fr/java/determine-if-paper-size-of-worksheet-is-automatic/
---
## **Scénarios d'utilisation possibles**

 La plupart du temps, le format de papier de la feuille de calcul est automatique. Lorsqu'il est automatique, il est souvent défini comme*Lettre* . Parfois, l'utilisateur définit le format de papier de la feuille de calcul en fonction de ses besoins. Dans ce cas, le format du papier n'est pas automatique. Vous pouvez savoir si le format de papier de la feuille de calcul est automatique ou non en utilisant le[**Feuille de calcul.getPageSetup().isAutomaticPaperSize()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#IsAutomaticPaperSize)méthode.

## **Déterminer si la taille du papier de la feuille de calcul est automatique**

L'exemple de code ci-dessous charge les deux fichiers Excel suivants

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496700.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496701.xlsx)

et trouver si le format de papier de leur première feuille de calcul est automatique ou non. Dans Microsoft Excel, vous pouvez vérifier si la taille du papier est automatique ou non via la fenêtre Mise en page, comme indiqué dans cette capture d'écran.

![tâche : image_autre_texte](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.java" >}}

## **Sortie console**

Voici la sortie de la console de l'exemple de code ci-dessus lorsqu'il est exécuté avec les exemples de fichiers Excel donnés.

{{< highlight "java" >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: false

First Worksheet of Second Workbook - IsAutomaticPaperSize: true

{{< /highlight >}}
