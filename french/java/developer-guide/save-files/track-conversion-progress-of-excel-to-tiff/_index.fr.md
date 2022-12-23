---
title: Suivre la progression de la conversion d'Excel vers TIFF
type: docs
weight: 140
url: /fr/java/track-conversion-progress-of-excel-to-tiff/
---
## **Scénarios d'utilisation possibles**

Parfois, la conversion de gros fichiers Excel peut prendre un certain temps. Pendant ce temps, vous souhaiterez peut-être afficher la progression de la conversion du document au lieu d'un simple écran de chargement pour améliorer la convivialité de votre application. Aspose.Cells prend en charge le processus de conversion de documents de suivi en fournissant le**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**interface. Le**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**l'interface fournit**[PageStartSaving](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving(com.aspose.cells.PageStartSavingArgs))**et**[PageEndSaving](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving(com.aspose.cells.PageEndSavingArgs))** méthodes que vous pouvez implémenter dans votre classe personnalisée. Vous pouvez également contrôler quelles pages sont rendues comme indiqué dans le*TestTiffPageSavingCallback*classe personnalisée.

## **Suivre la progression de la conversion d'Excel vers TIFF**

L'exemple de code suivant charge le[fichier excel source](sampleUseWorkbookRenderForImageConversion.xlsx) et imprime sa progression de conversion dans la console en utilisant le*TestTiffPageSavingCallback*classe personnalisée qui implémente**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**interface. Le fichier de sortie généré est joint pour votre référence.

[Fichier de sortie](DocumentConversionProgressForTiff_out.tiff)

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.java" >}}

Voici le code pour le*TestTiffPageSavingCallback*classe personnalisée.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.java" >}}

## **Sortie console**

Commencer à enregistrer l'index de page 0 des pages 10</br>
Fin de l'enregistrement de l'index de page 0 des pages 10</br>
Commencer à enregistrer l'index de page 1 des pages 10</br>
Fin de l'enregistrement page index 1 des pages 10</br>
Commencer à enregistrer l'index de page 2 des pages 10</br>
Fin de l'enregistrement page index 2 des pages 10</br>
Commencer à enregistrer l'index de la page 3 des pages 10</br>
Fin de l'enregistrement page index 3 des pages 10</br>
Commencer à enregistrer l'index de la page 4 des pages 10</br>
Fin de l'enregistrement page index 4 des pages 10</br>
Commencer à enregistrer l'index de page 5 des pages 10</br>
Fin de l'enregistrement page index 5 des pages 10</br>
Commencer à enregistrer l'index de la page 6 des pages 10</br>
Fin de l'enregistrement page index 6 des pages 10</br>
Commencer à enregistrer l'index de la page 7 des pages 10</br>
Fin de l'enregistrement page index 7 des pages 10</br>
Commencer à enregistrer l'index de la page 8 des pages 10</br>
Fin de l'enregistrement page index 8 des pages 10
