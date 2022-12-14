---
title: Suivre la progression de la conversion d'Excel en TIFF
type: docs
weight: 190
url: /fr/net/track-conversion-progress-of-excel-to-tiff/
---
## **Scénarios d'utilisation possibles**

 Parfois, la conversion de gros fichiers Excel peut prendre un certain temps. Pendant ce temps, vous souhaiterez peut-être afficher la progression de la conversion du document au lieu d'un simple écran de chargement pour améliorer la convivialité de votre application. Aspose.Cells prend en charge le processus de conversion de documents de suivi en fournissant le**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)** interface. La**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)**l'interface fournit**[PageStartSaving](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pagestartsaving)**et**[PageEndSaving](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pageendsaving)**méthodes que vous pouvez implémenter dans votre classe personnalisée. Vous pouvez également contrôler quelles pages sont rendues comme indiqué dans le T*estPageSavingCallback*classe personnalisée.

## **Suivre la progression de la conversion d'Excel en TIFF**

 L'exemple de code suivant charge le[fichier excel source](95584311.xlsx) et imprime sa progression de conversion dans la console en utilisant le*TestPageSavingCallback* classe personnalisée qui implémente**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)**interface. Le fichier de sortie généré est joint pour votre référence.

[Fichier de sortie](95584312.tiff)

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.cs" >}}

Voici le code pour le*TestTiffPageSavingCallback*classe personnalisée.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.cs" >}}

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
Fin de l'enregistrement page index 8 des pages 10</br>

