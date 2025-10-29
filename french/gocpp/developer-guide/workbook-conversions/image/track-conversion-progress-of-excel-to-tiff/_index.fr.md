---
title: Suivi de la progression de la conversion d Excel en TIFF avec Golang via C++
linktitle: Suivre la progression de la conversion d Excel en TIFF
type: docs
weight: 190
url: /fr/go-cpp/track-conversion-progress-of-excel-to-tiff/
description: Apprenez à suivre la progression de la conversion de fichiers Excel en TIFF en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Parfois, la conversion de grands fichiers Excel peut prendre du temps. Pendant cette période, vous pouvez vouloir afficher la progression de la conversion du document au lieu d’un simple écran de chargement pour améliorer l’utilisabilité de votre application. Aspose.Cells supporte le suivi de la progression de la conversion du document en fournissant l’interface [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/). L’interface [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/) fournit les méthodes [**PageStartSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pagestartsaving/) et [**PageEndSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pageendsaving/) que vous pouvez implémenter dans votre classe personnalisée. Vous pouvez également contrôler quelles pages sont rendues comme démontré dans la classe personnalisée *TestPageSavingCallback*.

## **Suivre la progression de la conversion d'Excel en TIFF**

Le code suivant charge le fichier Excel [source](95584311.xlsx) et affiche la progression de sa conversion dans la console en utilisant la classe personnalisée *TestPageSavingCallback* qui implémente l’interface [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/). Le fichier de sortie généré est joint pour votre référence.

[Output File](95584312.tiff)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackConversionProgressOfExcelToTiff.go" >}}
Ce qui suit est le code de la classe personnalisée *TestTiffPageSavingCallback*.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackConversionProgressOfExcelToTiff-1.go" >}}
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
