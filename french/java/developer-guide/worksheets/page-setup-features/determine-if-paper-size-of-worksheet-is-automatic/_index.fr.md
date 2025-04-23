---
title: Déterminer si la taille du papier de la feuille de calcul est automatique
type: docs
weight: 20
url: /fr/java/determine-if-paper-size-of-worksheet-is-automatic/
---

## **Scénarios d'utilisation possibles**

La plupart du temps, la taille du papier de la feuille de calcul est automatique. Lorsqu'elle est automatique, elle est souvent définie comme *Letter*. Parfois, l'utilisateur définit la taille du papier de la feuille de calcul selon ses besoins. Dans ce cas, la taille du papier n'est pas automatique. Vous pouvez vérifier si la taille du papier de la feuille de calcul est automatique ou non en utilisant la méthode [**Worksheet.getPageSetup().isAutomaticPaperSize()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#IsAutomaticPaperSize).

## **Déterminer si la taille du papier de la feuille de calcul est automatique**

Le code d'exemple ci-dessous charge les deux fichiers Excel suivants

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496700.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496701.xlsx)

et détermine si la taille du papier de leur première feuille de calcul est automatique ou non. Dans Microsoft Excel, vous pouvez vérifier si la taille du papier est automatique ou non via la fenêtre de configuration de la page comme indiqué dans cette capture d'écran.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.java" >}}

## **Sortie console**

Voici la sortie console du code d'exemple ci-dessus lorsqu'il est exécuté avec les fichiers Excel d'exemple donnés.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: false

First Worksheet of Second Workbook - IsAutomaticPaperSize: true

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
