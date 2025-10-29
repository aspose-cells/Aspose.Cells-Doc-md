---
title: Obtenir une plage avec des liens externes avec Golang via C++
linktitle: Obtenir une plage avec des liens externes
type: docs
weight: 120
url: /fr/go-cpp/get-range-with-external-links/
description: Apprenez comment récupérer des plages avec des liens externes dans des fichiers Excel en utilisant Aspose.Cells avec Golang via C++.
---

## **Obtenir une plage avec des liens externes**

Souvent, les fichiers Excel accèdent à des données provenant d'autres fichiers Excel via des liens externes. Aspose.Cells offre l'option de récupérer ces liens externes en utilisant la méthode [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/). La méthode [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/) retourne un tableau de type [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/). La classe [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) fournit une propriété [**GetExternalFileName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getexternalfilename/) qui retourne le nom du fichier externe. La classe [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) expose les membres suivants.

- [**GetEndColumn()**](https://reference.aspose.com/cells/go-cpp/referredarea/getendcolumn/) : La colonne finale de la zone
- [**GetEndRow()**](https://reference.aspose.com/cells/go-cpp/referredarea/getendrow/) : La ligne finale de la zone
- [**GetExternalFileName()**](https://reference.aspose.com/cells/go-cpp/referredarea/getexternalfilename/) : Obtenir le nom du fichier externe si c'est une référence externe
- [**IsArea**](https://reference.aspose.com/cells/go-cpp/referredarea/isarea/) : Indique si c'est une zone
- [**IsExternalLink**](https://reference.aspose.com/cells/go-cpp/referredarea/isexternallink/) : Indique s'il s'agit d'un lien externe
- [**GetSheetName()**](https://reference.aspose.com/cells/go-cpp/referredarea/getsheetname/) : Indique dans quelle feuille cette référence se trouve
- [**GetStartColumn()**](https://reference.aspose.com/cells/go-cpp/referredarea/getstartcolumn/) : La colonne de départ de la zone
- [**GetStartRow()**](https://reference.aspose.com/cells/go-cpp/referredarea/getstartrow/) : La ligne de départ de la zone

Le code d'exemple ci-dessous montre l'utilisation de la méthode [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/) pour obtenir des plages avec des liens externes.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetRangeWithExternalLinks.go" >}}
