---
title: Formen sperren oder freigeben
linktitle: Formen sperren oder freigeben
type: docs
weight: 200
url: /de/cpp/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

Manchmal müssen Sie alle Formen in bestimmten Tabellenblättern schützen, um zu verhindern, dass sie durch unerwünschte Situationen zerstört werden. In diesem Fall müssen Sie alle Formen im angegebenen Tabellenblatt sperren.

Manchmal müssen Sie in bestimmten geschützten Tabellenblättern bestimmte Formen bearbeiten können. In diesem Fall müssen Sie diese Formen freischalten.

Dieser Artikel wird ausführlich einführen, wie man bestimmte Formen sperrt und freischaltet.

{{% /alert %}}

## **Alle Formen in einem bestimmten Tabellenblatt schützen**

Um alle Formen in einem bestimmten Arbeitsblatt zu schützen, verwenden Sie die [Worksheet.Protect(ProtectionType)](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/) Methode, wie im folgenden Beispielcode gezeigt.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Lock-Or-Unlock-Shapes-1.cpp" >}}

## **Bestimmte Formen in einem geschützten Tabellenblatt freischalten**

Um eine bestimmte Form in einem geschützten Arbeitsblatt zu entsperren, verwenden Sie [shape.IsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/islocked/) und [shape.SetIsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setislocked/), wie im folgenden Beispielcode gezeigt.

Hinweis: [shape.IsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/islocked/) und [shape.SetIsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setislocked/) sind nur sinnvoll, wenn das Arbeitsblatt geschützt ist.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Lock-Or-Unlock-Shapes-2.cpp" >}}

