---
title: Verrouiller ou déverrouiller les formes
linktitle: Verrouiller ou déverrouiller les formes
type: docs
weight: 200
url: /fr/net/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

Parfois, vous devez protéger toutes les formes dans certaines feuilles de calcul pour les empêcher d'être détruites par des situations non désirées. Dans ce cas, vous devez verrouiller toutes les formes dans la feuille de calcul spécifiée.

Parfois, vous devez être en mesure de modifier certaines formes dans certaines feuilles de calcul protégées, auquel cas, vous devez déverrouiller ces formes.

Cet article présentera en détail comment verrouiller et déverrouiller des formes spécifiées.

{{% /alert %}}

## **Protéger toutes les formes dans une feuille de calcul spécifiée**

Pour protéger toutes les formes dans une feuille de calcul spécifiée, utilisez la méthode [Worksheet.Protect( ProtectionType.Objects)](https://reference.aspose.com/cells/net/aspose.cells/worksheet/protect/#protect), comme indiqué dans le code d'exemple suivant.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-1.cs" >}}

## **Déverrouiller les formes spécifiées dans une feuille de calcul protégée**

Pour déverrouiller une forme spécifiée dans une feuille de calcul protégée, utilisez [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/), comme indiqué dans le code d'exemple suivant.

Remarque : [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/) n'a de sens que lorsque la feuille de calcul est protégée.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-2.cs" >}}

