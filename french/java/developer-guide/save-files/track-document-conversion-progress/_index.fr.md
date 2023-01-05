---
title: Suivre la progression de la conversion des documents
type: docs
weight: 120
url: /fr/java/track-document-conversion-progress/
---
## **Scénarios d'utilisation possibles**

Parfois, la conversion de gros fichiers Excel peut prendre un certain temps. Pendant ce temps, vous souhaiterez peut-être afficher la progression de la conversion du document au lieu d'un simple écran de chargement pour améliorer la convivialité de votre application. Aspose.Cells prend en charge le processus de conversion de documents de suivi en fournissant le**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**interface. Le**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**l'interface fournit**[PageStartSaving](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving(com.aspose.cells.PageStartSavingArgs))**et**[PageEndSaving](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving(com.aspose.cells.PageEndSavingArgs))** méthodes que vous pouvez implémenter dans votre classe personnalisée. Vous pouvez également contrôler quelles pages sont rendues comme indiqué dans le*TestPageSavingCallback*classe personnalisée.

## **Suivre la progression de la conversion des documents**

L'exemple de code suivant charge le[fichier excel source](PagesBook1.xlsx)et imprime sa progression de conversion dans la console en utilisant le*TestPageSavingCallback*classe personnalisée qui implémente**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**interface.

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.java" >}}

Voici le code pour le*TestPageSavingCallback*classe personnalisée.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.java" >}}

## **Sortie console**

Commencer à enregistrer l'index de page 0 des pages 11</br>
Fin de l'enregistrement de l'index de page 0 des pages 11</br>
Commencer à enregistrer l'index de la page 1 des pages 11</br>
Fin de l'enregistrement page index 1 des pages 11</br>
Commencer à enregistrer l'index de la page 2 des pages 11</br>
Fin de l'enregistrement page index 2 des pages 11</br>
Commencer à enregistrer l'index de la page 3 des pages 11</br>
Fin de l'enregistrement page index 3 des pages 11</br>
Commencer à enregistrer l'index de la page 4 des pages 11</br>
Fin de l'enregistrement page index 4 des pages 11</br>
Commencer à enregistrer l'index de la page 5 des pages 11</br>
Fin de l'enregistrement page index 5 des pages 11</br>
Commencer à enregistrer l'index de la page 6 des pages 11</br>
Fin de l'enregistrement page index 6 des pages 11</br>
Commencer à enregistrer l'index de la page 7 des pages 11</br>
Fin de l'enregistrement page index 7 des pages 11</br>
Commencer à enregistrer l'index de la page 8 des pages 11</br>
Fin de l'enregistrement page index 8 des pages 11
