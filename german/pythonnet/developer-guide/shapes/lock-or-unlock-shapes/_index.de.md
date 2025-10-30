---
title: Formen sperren oder freigeben
linktitle: Formen sperren oder freigeben
type: docs
weight: 200
url: /de/python-net/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

Manchmal müssen Sie alle Formen in bestimmten Tabellenblättern schützen, um zu verhindern, dass sie durch unerwünschte Situationen zerstört werden. In diesem Fall müssen Sie alle Formen im angegebenen Tabellenblatt sperren.

Manchmal müssen Sie in bestimmten geschützten Tabellenblättern bestimmte Formen bearbeiten können. In diesem Fall müssen Sie diese Formen freischalten.

Dieser Artikel wird ausführlich einführen, wie man bestimmte Formen sperrt und freischaltet.

{{% /alert %}}

## **Alle Formen in einem bestimmten Tabellenblatt schützen**

Verwenden Sie zum Schutz aller Formen in einem bestimmten Tabellenblatt die [Worksheet.Protect(type)](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protect/#aspose.cells.ProtectionType) Methode, wie im folgenden Beispielcode gezeigt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Lock-Or-Unlock-Shapes-1.py" >}}

## **Bestimmte Formen in einem geschützten Tabellenblatt freischalten**

Um eine bestimmte Form in einem geschützten Tabellenblatt freizuschalten, verwenden Sie [shape.is_locked](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/is_locked/), wie im folgenden Beispielcode gezeigt.

Hinweis: [shape.is_locked](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/is_locked/) ist nur sinnvoll, wenn das Arbeitsblatt geschützt ist.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Lock-Or-Unlock-Shapes-2.py" >}}

{{< app/cells/assistant language="python-net" >}}
