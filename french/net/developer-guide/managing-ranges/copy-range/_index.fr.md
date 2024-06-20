---
title: Copier des plages d Excel
linktitle: Copier des plages
type: docs
weight: 105
url: /fr/net/copy-ranges-of-Excel/
---

## **Introduction**

Dans Excel, vous pouvez sélectionner une plage, copier la plage, puis la coller avec des options spécifiques dans la même feuille de calcul, d'autres feuilles de calcul ou d'autres fichiers.

## **Copier des plages en utilisant Aspose.Cells**

Aspose.Cells fournit quelques surcharges des méthodes [Range.Copy](https://reference.aspose.com/cells/net/aspose.cells/range/copy/#copy) pour copier la plage.
et [Range.CopyStyle](https://reference.aspose.com/cells/net/aspose.cells/range/copystyle/) copie uniquement le style de la plage ; [Range.CopyData](https://reference.aspose.com/cells/net/aspose.cells/range/copydata/) copie uniquement la valeur de la plage.

## **Copier la plage**

Création de deux plages : la plage source, la plage cible, puis copie de la plage source vers la plage cible avec la méthode Range.Copy.

Voir le code suivant :

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range.cs" >}}

## **Coller la plage avec des options**

Aspose.Cells prend en charge le collage de la plage avec un type spécifique.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Paste-Range.cs" >}}

## **Copier uniquement les données de la plage**
Vous pouvez également copier les données avec la méthode Range.CopyData comme dans les codes suivants :

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range-Data.cs" >}}

## **Sujets avancés**
- [Copier les hauteurs de ligne de la plage source vers la plage de destination](/cells/fr/net/copy-row-heights-of-source-range-to-destination-range/)


