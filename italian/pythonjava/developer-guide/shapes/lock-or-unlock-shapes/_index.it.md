---
title: Bloccare o sbloccare forme
linktitle: Bloccare o sbloccare forme
type: docs
weight: 200
url: /it/python-java/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

A volte è necessario proteggere tutte le forme in determinati fogli di lavoro per evitare che vengano distrutte da situazioni indesiderate. In questo caso, è necessario bloccare tutte le forme nel foglio di lavoro specificato.

A volte è necessario essere in grado di modificare determinate forme in determinati fogli di lavoro protetti, in tal caso, è necessario sbloccare queste forme.

Questo articolo illustrerà dettagliatamente come bloccare e sbloccare forme specificate.

{{% /alert %}}

## **Proteggere tutte le forme in un foglio di lavoro specificato**

Per proteggere tutte le forme in un foglio di lavoro specificato, utilizzare il metodo [Worksheet.Protect(type)](https://reference.aspose.com/cells/python-java/asposecells.api/worksheet#protect(int)), come mostrato nel seguente esempio di codice.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Lock-Or-Unlock-Shapes-1.py" >}}

## **Sbloccare forme specificate in un foglio di lavoro protetto**

Per sbloccare una forma specifica in un foglio di lavoro protetto, utilizzare [shape.IsLocked](https://reference.aspose.com/cells/python-java/asposecells.api/shape#IsLocked), come mostrato nel seguente esempio di codice.

Nota: [shape.IsLocked](https://reference.aspose.com/cells/python-java/asposecells.api/shape#IsLocked) ha significato solo quando il foglio di lavoro è protetto.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Lock-Or-Unlock-Shapes-2.py" >}}

