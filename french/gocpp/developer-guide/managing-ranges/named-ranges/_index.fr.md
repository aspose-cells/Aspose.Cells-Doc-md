---
title: Créez des plages nommées avec une portée au classeur et à la feuille de calcul avec Golang via C++
linktitle: Plage nommée
type: docs
weight: 40
url: /fr/go-cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: Apprenez à créer des plages nommées avec une portée au classeur et à la feuille de calcul avec Golang via C++ en utilisant Aspose.Cells.
---

{{% alert color="primary" %}} 

Microsoft Excel permet aux utilisateurs de définir des plages nommées avec deux portées différentes : le classeur (également appelé portée globale) et la feuille de calcul.

- Les plages nommées avec une portée de classeur peuvent être accédées à partir de n'importe quelle feuille de calcul au sein de ce classeur en utilisant simplement son nom.
- Les plages nommées avec une portée de feuille de calcul sont accessibles avec la référence de la feuille de calcul particulière dans laquelle elle a été créée.

Aspose.Cells fournit la même fonctionnalité que Microsoft Excel pour ajouter des plages nommées au niveau du classeur et de la feuille de calcul. Lors de la création d'une plage nommée au niveau de la feuille de calcul, la référence à la feuille de calcul doit être utilisée dans la plage nommée pour la spécifier comme une plage nommée au niveau de la feuille de calcul.

{{% /alert %}} 

## **Ajout d'une plage nommée au niveau du classeur**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-NamedRanges.go" >}}
## **Ajout d'une plage nommée avec une portée de feuille de calcul**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-NamedRanges-1.go" >}}
## **Sujets avancés**
- [Créer un accès et copier des plages nommées](/cells/fr/cpp/create-access-and-copy-named-ranges/)
- [Formater et modifier des plages nommées](/cells/fr/cpp/format-and-modify-named-ranges/)
- [Obtenir une plage avec des liens externes](/cells/fr/cpp/get-range-with-external-links/)
- [Mise en œuvre de plages non séquentielles](/cells/fr/cpp/implementing-non-sequential-ranges/)

