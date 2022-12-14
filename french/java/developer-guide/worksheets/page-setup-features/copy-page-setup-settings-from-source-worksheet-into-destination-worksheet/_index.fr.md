---
title: Copier les paramètres de mise en page de la feuille de calcul source dans la feuille de calcul de destination
type: docs
weight: 10
url: /fr/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
---
## **Scénarios d'utilisation possibles**

Lorsque vous ajoutez une nouvelle feuille à un classeur, elle contient les paramètres de mise en page par défaut. Il peut arriver que vous deviez transférer les paramètres ([**Mise en page**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup)d'une feuille de calcul à une autre feuille de calcul. Ce document explique comment copier les paramètres de mise en page d'une feuille de calcul à une autre à l'aide des API Aspose.Cells.

## **Copier les paramètres de mise en page de la feuille de calcul source dans la feuille de calcul de destination**

L'exemple de code suivant illustre comment copier les paramètres de mise en page d'une feuille de calcul à une autre à l'aide de[**PageSetup.Copy()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#copy(com.aspose.cells.PageSetup,%20com.aspose.cells.CopyOptions)) méthode. Veuillez consulter l'exemple de code suivant et sa sortie de console pour référence.

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.java" >}}

## **Sortie console**

{{< highlight "java" >}}

Before Paper Size: PAPER_A_3_EXTRA_TRANSVERSE

Before Paper Size: PAPER_LETTER

After Paper Size: PAPER_A_3_EXTRA_TRANSVERSE

After Paper Size: PAPER_A_3_EXTRA_TRANSVERSE

{{< /highlight >}}
