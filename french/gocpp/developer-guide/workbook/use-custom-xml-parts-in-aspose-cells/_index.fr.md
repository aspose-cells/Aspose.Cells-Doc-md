---
title: Utiliser des parties XML personnalisées dans Aspose.Cells avec Golang via C++
linktitle: Utiliser des parties XML personnalisées
type: docs
weight: 390
url: /fr/go-cpp/use-custom-xml-parts-in-aspose-cells/
description: Apprenez comment utiliser des parties XML personnalisées dans les fichiers Excel de manière programmatique avec Aspose.Cells et Golang via C++.
---

## Utilisation de parties XML personnalisées dans Aspose.Cells

Les parties XML personnalisées sont des données XML stockées par différentes applications comme SharePoint à l'intérieur d'un fichier Excel. Ces données sont consommées par diverses applications qui en ont besoin. Microsoft Excel n'utilise pas ces données, il n'y a donc pas d'interface graphique pour les ajouter. Vous pouvez voir ces données en changeant l'extension de **.xlsx** en **.zip** puis en l'ouvrant avec **WinZip**. Vous pouvez également ouvrir le fichier ZIP avec tout utilitaire tiers comme WinRAR ou WinZip. Les données se trouvent dans le dossier **customXml**.

Vous pouvez ajouter des parties XML personnalisées en utilisant Aspose.Cells via la méthode [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/go-cpp/contenttypepropertycollection/add_string_string/).

Le code d'exemple suivant utilise la méthode [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/go-cpp/contenttypepropertycollection/add_string_string/) pour ajouter le **Book Catalog XML**, dont le nom est **BookStore**. L'image suivante montre le résultat de ce code. Comme vous pouvez le voir, le Book Catalog XML est ajouté à l'intérieur du nœud BookStore, qui est le nom de cette propriété.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## Code C++ pour utiliser les parties XML personnalisées

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UseCustomXmlPartsInAsposeCells.go" >}}
## Article connexe

- [Ajout de propriétés personnalisées visibles dans le panneau d'informations du document](/cells/fr/cpp/adding-custom-properties-visible-inside-document-information-panel/)
