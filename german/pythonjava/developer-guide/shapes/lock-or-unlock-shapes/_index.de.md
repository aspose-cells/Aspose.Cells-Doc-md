---
title: Formen sperren oder freigeben
linktitle: Formen sperren oder freigeben
type: docs
weight: 200
url: /de/python-java/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

Manchmal müssen Sie alle Formen in bestimmten Tabellenblättern schützen, um zu verhindern, dass sie durch unerwünschte Situationen zerstört werden. In diesem Fall müssen Sie alle Formen im angegebenen Tabellenblatt sperren.

Manchmal müssen Sie in bestimmten geschützten Tabellenblättern bestimmte Formen bearbeiten können. In diesem Fall müssen Sie diese Formen freischalten.

Dieser Artikel wird ausführlich einführen, wie man bestimmte Formen sperrt und freischaltet.

{{% /alert %}}

## **Alle Formen in einem bestimmten Tabellenblatt schützen**

Um alle Formen in einem bestimmten Arbeitsblatt zu schützen, verwenden Sie die Methode [Worksheet.Protect(type)](https://reference.aspose.com/cells/python-java/asposecells.api/worksheet#protect(int)), wie im folgenden Beispielcode gezeigt.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Lock-Or-Unlock-Shapes-1.py" >}}

## **Bestimmte Formen in einem geschützten Tabellenblatt freischalten**

Um eine bestimmte Form in einem geschützten Arbeitsblatt zu entsperren, verwenden Sie [shape.IsLocked](https://reference.aspose.com/cells/python-java/asposecells.api/shape#IsLocked), wie im folgenden Beispielcode gezeigt.

Hinweis: [shape.IsLocked](https://reference.aspose.com/cells/python-java/asposecells.api/shape#IsLocked) ist nur sinnvoll, wenn das Arbeitsblatt geschützt ist.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Lock-Or-Unlock-Shapes-2.py" >}}

