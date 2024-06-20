---
title: Bloccare o sbloccare forme
linktitle: Bloccare o sbloccare forme
type: docs
weight: 200
url: /it/net/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

A volte è necessario proteggere tutte le forme in determinati fogli di lavoro per evitare che vengano distrutte da situazioni indesiderate. In questo caso, è necessario bloccare tutte le forme nel foglio di lavoro specificato.

A volte è necessario essere in grado di modificare determinate forme in determinati fogli di lavoro protetti, in tal caso, è necessario sbloccare queste forme.

Questo articolo illustrerà dettagliatamente come bloccare e sbloccare forme specificate.

{{% /alert %}}

## **Proteggere tutte le forme in un foglio di lavoro specificato**

Per proteggere tutte le forme in un determinato foglio di lavoro, utilizzare il metodo [Worksheet.Protect( ProtectionType.Objects)](https://reference.aspose.com/cells/net/aspose.cells/worksheet/protect/#protect), come mostrato nel seguente codice di esempio.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-1.cs" >}}

## **Sbloccare forme specificate in un foglio di lavoro protetto**

Per sbloccare una forma specifica in un foglio di lavoro protetto, utilizzare [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/), come mostrato nel seguente codice di esempio.

Nota: [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/) ha significato solo quando il foglio di lavoro è protetto.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-2.cs" >}}

