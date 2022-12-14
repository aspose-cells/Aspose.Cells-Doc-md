---
title: Copier les plages d'Excel
linktitle: Copier les plages
type: docs
weight: 105
url: /fr/net/copy-ranges-of-Excel/
---
## **Introduction**

Dans Excel, vous pouvez sélectionner une plage, copier la plage, puis la coller avec des options spécifiques dans la même feuille de calcul, d'autres feuilles de calcul ou d'autres fichiers.

## **Copier les plages à l'aide de Aspose.Cells**

 Aspose.Cells fournit une certaine surcharge[Range.Copy](https://reference.aspose.com/cells/net/aspose.cells/range/copy/#copy) méthodes pour copier la plage.
 Et[Range.CopyStyle](https://reference.aspose.com/cells/net/aspose.cells/range/copystyle/) uniquement le style de copie de la plage ;[Range.CopyData](https://reference.aspose.com/cells/net/aspose.cells/range/copydata/) uniquement la valeur de copie de la plage

## **Plage de copie**

Création de deux plages : la plage source, la plage cible, puis copie de la plage source dans la plage cible avec la méthode Range.Copy.

Voir le code suivant :

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range.cs" >}}

## **Coller la plage avec des options**

Aspose.Cells prend en charge le collage de la plage avec un type spécifique.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Paste-Range.cs" >}}

## **Copiez uniquement les données de la plage.**
Vous pouvez également copier les données avec la méthode Range.CopyData avec les codes suivants :

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range-Data.cs" >}}

## **Sujets avancés**
- [Copier les hauteurs de ligne de la plage source dans la plage de destination](/cells/fr/net/copy-row-heights-of-source-range-to-destination-range/)


