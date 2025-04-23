---
title: Formen sperren oder freigeben
linktitle: Formen sperren oder freigeben
type: docs
weight: 200
url: /de/java/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

Manchmal müssen Sie alle Formen in bestimmten Tabellenblättern schützen, um zu verhindern, dass sie durch unerwünschte Situationen zerstört werden. In diesem Fall müssen Sie alle Formen im angegebenen Tabellenblatt sperren.

Manchmal müssen Sie in bestimmten geschützten Tabellenblättern bestimmte Formen bearbeiten können. In diesem Fall müssen Sie diese Formen freischalten.

Dieser Artikel wird ausführlich einführen, wie man bestimmte Formen sperrt und freischaltet.

{{% /alert %}}

## **Alle Formen in einem bestimmten Tabellenblatt schützen**

Um alle Formen in einem bestimmten Arbeitsblatt zu schützen, verwenden Sie die Methode [Worksheet.protect(int type)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet/#protect-int-), wie im folgenden Beispielcode gezeigt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Lock-Or-Unlock-Shapes-1.java" >}}

## **Bestimmte Formen in einem geschützten Tabellenblatt freischalten**

Um eine bestimmte Form in einem geschützten Arbeitsblatt zu entsperren, verwenden Sie [shape.IsLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#isLocked--) und [shape.setLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#setLocked-boolean-), wie im folgenden Beispielcode gezeigt.

Hinweis: [shape.IsLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#isLocked--) und [shape.setLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#setLocked-boolean-) sind nur sinnvoll, wenn das Arbeitsblatt geschützt ist.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Lock-Or-Unlock-Shapes-2.java" >}}

{{< app/cells/assistant language="java" >}}
