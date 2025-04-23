---
title: Suivre la progression de la conversion d Excel en TIFF
type: docs
weight: 190
url: /fr/net/track-conversion-progress-of-excel-to-tiff/
---

## **Scénarios d'utilisation possibles**

Parfois, la conversion de grands fichiers Excel peut prendre du temps. Pendant ce temps, vous voudrez peut-être afficher la progression de conversion du document au lieu d'un simple écran de chargement pour améliorer la convivialité de votre application. Aspose.Cells prend en charge le suivi du processus de conversion de document en fournissant l'interface [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback). L'interface [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback) fournit les méthodes [**PageStartSaving**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pagestartsaving) et [**PageEndSaving**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pageendsaving) que vous pouvez implémenter dans votre classe personnalisée. Vous pouvez également contrôler quelles pages sont rendues, comme le démontre la classe personnalisée *TestPageSavingCallback*.

## **Suivre la progression de la conversion d'Excel en TIFF**

Le code d'exemple suivant charge le [fichier Excel source](95584311.xlsx) et imprime sa progression de conversion dans la console en utilisant la classe personnalisée *TestPageSavingCallback* qui implémente l'interface [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback). Le fichier de sortie généré est joint à titre de référence.

[Output File](95584312.tiff)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.cs" >}}

Ce qui suit est le code de la classe personnalisée *TestTiffPageSavingCallback*.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.cs" >}}

## **Sortie console**

{{< highlight java >}}

Start saving page index 0 of pages 10</br>
End saving page index 0 of pages 10</br>
Start saving page index 1 of pages 10</br>
End saving page index 1 of pages 10</br>
Start saving page index 2 of pages 10</br>
End saving page index 2 of pages 10</br>
Start saving page index 3 of pages 10</br>
End saving page index 3 of pages 10</br>
Start saving page index 4 of pages 10</br>
End saving page index 4 of pages 10</br>
Start saving page index 5 of pages 10</br>
End saving page index 5 of pages 10</br>
Start saving page index 6 of pages 10</br>
End saving page index 6 of pages 10</br>
Start saving page index 7 of pages 10</br>
End saving page index 7 of pages 10</br>
Start saving page index 8 of pages 10</br>
End saving page index 8 of pages 10</br>

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
