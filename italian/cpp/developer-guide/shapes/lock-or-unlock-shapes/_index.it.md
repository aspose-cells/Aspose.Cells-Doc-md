---
title: Bloccare o sbloccare forme
linktitle: Bloccare o sbloccare forme
type: docs
weight: 200
url: /it/cpp/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

A volte è necessario proteggere tutte le forme in determinati fogli di lavoro per evitare che vengano distrutte da situazioni indesiderate. In questo caso, è necessario bloccare tutte le forme nel foglio di lavoro specificato.

A volte è necessario essere in grado di modificare determinate forme in determinati fogli di lavoro protetti, in tal caso, è necessario sbloccare queste forme.

Questo articolo illustrerà dettagliatamente come bloccare e sbloccare forme specificate.

{{% /alert %}}

## **Proteggere tutte le forme in un foglio di lavoro specificato**

Per proteggere tutte le forme in un foglio di lavoro specificato, utilizzare il metodo [Worksheet.Protect(ProtectionType)](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/), come mostrato nel seguente codice di esempio.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Lock-Or-Unlock-Shapes-1.cpp" >}}

## **Sbloccare forme specificate in un foglio di lavoro protetto**

Per sbloccare una forma specificata in un foglio di lavoro protetto, utilizzare [shape.IsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/islocked/) e [shape.SetIsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setislocked/), come mostrato nel seguente codice di esempio.

Nota: [shape.IsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/islocked/) e [shape.SetIsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setislocked/) sono significativi solo quando il foglio di lavoro è protetto.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Lock-Or-Unlock-Shapes-2.cpp" >}}

{{< app/cells/assistant language="cpp" >}}
