---
title: Bloccare o sbloccare forme
linktitle: Bloccare o sbloccare forme
type: docs
weight: 200
url: /it/python-net/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

A volte è necessario proteggere tutte le forme in determinati fogli di lavoro per evitare che vengano distrutte da situazioni indesiderate. In questo caso, è necessario bloccare tutte le forme nel foglio di lavoro specificato.

A volte è necessario essere in grado di modificare determinate forme in determinati fogli di lavoro protetti, in tal caso, è necessario sbloccare queste forme.

Questo articolo illustrerà dettagliatamente come bloccare e sbloccare forme specificate.

{{% /alert %}}

## **Proteggere tutte le forme in un foglio di lavoro specificato**

Per proteggere tutte le forme in una tabella specificata, utilizza il metodo [Worksheet.Protect(type)](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protect/#aspose.cells.ProtectionType), come mostrato nel seguente codice di esempio.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Lock-Or-Unlock-Shapes-1.py" >}}

## **Sbloccare forme specificate in un foglio di lavoro protetto**

Per sbloccare una forma specificata in una tabella protetta, utilizza [shape.is_locked](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/is_locked/), come mostrato nel seguente codice di esempio.

Nota: [shape.is_locked](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/is_locked/) ha significato solo quando la tabella è protetta.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Lock-Or-Unlock-Shapes-2.py" >}}

