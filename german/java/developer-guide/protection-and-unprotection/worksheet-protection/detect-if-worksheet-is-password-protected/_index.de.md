---
title: Erkennen, ob Arbeitsblatt passwortgeschützt ist
type: docs
weight: 280
url: /de/java/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

Es ist möglich, Arbeitsmappen und Arbeitsblätter getrennt zu schützen. Eine Tabellenkalkulation kann beispielsweise ein oder mehrere arbeitsblattgeschützte Arbeitsblätter enthalten, wobei die Tabelle selbst geschützt sein kann oder nicht. Aspose.Cells-APIs bieten die Möglichkeit festzustellen, ob ein bestimmtes Arbeitsblatt geschützt ist oder nicht. Dieser Artikel zeigt die Verwendung der API Aspose.Cells for Java, um dasselbe zu erreichen.

{{% /alert %}}

## **Überprüfen Sie, ob das Arbeitsblatt mit einem Kennwort geschützt ist**

Aspose.Cells for Java 8.7.0 hat die Eigenschaft [**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) freigelegt, um festzustellen, ob ein Arbeitsblatt passwortgeschützt ist. Das Feld vom Typ Boolean [**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) gibt **true** zurück, wenn [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) passwortgeschützt ist, und **false**, wenn nicht.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectWorksheetisPasswordProtected-DetectWorksheetisPasswordProtected.java" >}}
{{< app/cells/assistant language="java" >}}
