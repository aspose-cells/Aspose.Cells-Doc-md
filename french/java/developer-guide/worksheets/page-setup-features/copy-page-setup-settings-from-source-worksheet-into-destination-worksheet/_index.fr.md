---
title: Copier les paramètres de mise en page de la feuille de calcul source dans la feuille de calcul de destination
type: docs
weight: 10
url: /fr/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
---

## **Scénarios d'utilisation possibles**

Lorsque vous ajoutez une nouvelle feuille à un classeur, elle contient les paramètres par défaut de la mise en page. Il peut arriver que vous ayez besoin de transférer les paramètres ([**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup)) d'une feuille de calcul à une autre. Ce document explique comment copier les paramètres de mise en page d'une feuille à une autre à l'aide des API Aspose.Cells.

## **Copier les paramètres de configuration de la page de la feuille source dans la feuille de destination**

Le code d'exemple suivant illustre comment copier les paramètres de configuration de la mise en page de une feuille de calcul à une autre en utilisant la méthode [**PageSetup.Copy()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#copy(com.aspose.cells.PageSetup,%20com.aspose.cells.CopyOptions)). Veuillez consulter le code d'exemple suivant et sa sortie console pour une référence.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.java" >}}

## **Sortie console**

{{< highlight java >}}

Before Paper Size: PAPER_A_3_EXTRA_TRANSVERSE

Before Paper Size: PAPER_LETTER

After Paper Size: PAPER_A_3_EXTRA_TRANSVERSE

After Paper Size: PAPER_A_3_EXTRA_TRANSVERSE

{{< /highlight >}}
