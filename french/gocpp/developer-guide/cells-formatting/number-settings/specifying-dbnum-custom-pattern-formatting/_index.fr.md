---
title: Spécification de la mise en forme du motif personnalisé DBNum avec Golang via C++
linktitle: Spécification du Format de Motif Personnalisé DBNum
description: Aspose.Cells est une bibliothèque C++ pour travailler avec des fichiers de tableurs supportant la mise en forme des dates et des nombres à l’aide de modèles de mise en forme personnalisés. Cet article vous montrera comment utiliser la bibliothèque Aspose.Cells pour spécifier le modèle de format personnalisé dbnum pour un contrôle accru de l’affichage des nombres.
keywords: Aspose.Cells, bibliothèque C++, feuille de calcul électronique, modèle de format personnalisé, mise en forme, dbnum , contrôle de l’affichage
type: docs
weight: 110
url: /fr/go-cpp/specifying-dbnum-custom-pattern-formatting/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells prend en charge le formatage de modèle personnalisé *DBNum*. Par exemple, si la valeur de votre cellule est 123 et que vous spécifiez son format personnalisé comme [DBNum2][$-804]General, elle s’affichera comme 壹佰贰拾叁. Vous pouvez définir votre mise en forme personnalisée de la cellule en utilisant la méthode [**Cell.GetStyle()**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/) et la propriété [**Style.Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/).

## **Code d'exemple**

Le code d'exemple suivant illustre comment spécifier un motif personnalisé *DBNum*. Veuillez consulter son [PDF de sortie](43352081.pdf) pour plus d’aide.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyingDbnumCustomPatternFormatting.go" >}}
