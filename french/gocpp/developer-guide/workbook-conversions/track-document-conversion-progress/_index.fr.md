---
title: Suivez la progression de la conversion de document avec Golang via C++
linktitle: Suivre l avancement de la conversion du document
type: docs
weight: 970
url: /fr/go-cpp/track-document-conversion-progress/
description: Apprenez comment suivre la progression de la conversion du document en C++ en utilisant Aspose.Cells pour améliorer la convivialité de l application.
---

## **Scénarios d'utilisation possibles**

Parfois, la conversion de grands fichiers Excel peut prendre du temps. Pendant ce temps, vous pouvez vouloir afficher la progression de la conversion du document au lieu d'un simple écran de chargement pour améliorer l'utilisabilité de votre application. Aspose.Cells supporte le suivi de la progression de la conversion du document en fournissant l'interface [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/). L'interface [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/) fournit [**PageStartSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pagestartsaving/) et [**PageEndSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pageendsaving/) méthodes que vous pouvez implémenter dans votre classe personnalisée. Vous pouvez également contrôler quelles pages sont rendues comme démontré dans la classe personnalisée `TestPageSavingCallback`.

## **Suivre la progression de la conversion des documents**

Le code suivant charge le fichier Excel [source](94896151.xlsx) et affiche la progression de sa conversion dans la console en utilisant la classe personnalisée `TestPageSavingCallback` qui implémente l'interface [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/).

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackDocumentConversionProgress.go" >}}
Voici le code pour la classe personnalisée `TestPageSavingCallback`.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackDocumentConversionProgress-1.go" >}}
## **Sortie console**

{{< highlight java >}}

Start saving page index 0 of pages 11</br>
End saving page index 0 of pages 11</br>
Start saving page index 1 of pages 11</br>
End saving page index 1 of pages 11</br>
Start saving page index 2 of pages 11</br>
End saving page index 2 of pages 11</br>
Start saving page index 3 of pages 11</br>
End saving page index 3 of pages 11</br>
Start saving page index 4 of pages 11</br>
End saving page index 4 of pages 11</br>
Start saving page index 5 of pages 11</br>
End saving page index 5 of pages 11</br>
Start saving page index 6 of pages 11</br>
End saving page index 6 of pages 11</br>
Start saving page index 7 of pages 11</br>
End saving page index 7 of pages 11</br>
Start saving page index 8 of pages 11</br>
End saving page index 8 of pages 11

{{< /highlight >}}
