---
title: Formen sperren oder freigeben
linktitle: Formen sperren oder freigeben
type: docs
weight: 200
url: /de/net/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

Manchmal müssen Sie alle Formen in bestimmten Tabellenblättern schützen, um zu verhindern, dass sie durch unerwünschte Situationen zerstört werden. In diesem Fall müssen Sie alle Formen im angegebenen Tabellenblatt sperren.

Manchmal müssen Sie in bestimmten geschützten Tabellenblättern bestimmte Formen bearbeiten können. In diesem Fall müssen Sie diese Formen freischalten.

Dieser Artikel wird ausführlich einführen, wie man bestimmte Formen sperrt und freischaltet.

{{% /alert %}}

## **Alle Formen in einem bestimmten Tabellenblatt schützen**

Um alle Formen in einem angegebenen Arbeitsblatt zu schützen, verwenden Sie die Methode [Worksheet.Protect( ProtectionType.Objects)](https://reference.aspose.com/cells/net/aspose.cells/worksheet/protect/#protect), wie im folgenden Beispielcode gezeigt.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-1.cs" >}}

## **Bestimmte Formen in einem geschützten Tabellenblatt freischalten**

Um eine bestimmte Form in einem geschützten Arbeitsblatt zu entsperren, verwenden Sie [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/), wie im folgenden Beispielcode gezeigt.

Hinweis: [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/) ist nur sinnvoll, wenn das Arbeitsblatt geschützt ist.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-2.cs" >}}

