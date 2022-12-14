---
title: Erkennen, ob das Arbeitsblatt passwortgeschützt ist
type: docs
weight: 280
url: /de/java/detect-if-worksheet-is-password-protected/
---
{{% alert color="primary" %}}

Es ist möglich, die Arbeitsmappen und Arbeitsblätter separat zu schützen. Beispielsweise kann eine Tabellenkalkulation ein oder mehrere passwortgeschützte Arbeitsblätter enthalten, die Tabellenkalkulation selbst kann jedoch geschützt sein oder nicht. Aspose.Cells APIs bieten die Möglichkeit zu erkennen, ob ein bestimmtes Arbeitsblatt passwortgeschützt ist oder nicht. Dieser Artikel demonstriert die Verwendung von Aspose.Cells for Java API, um dasselbe zu erreichen.

{{% /alert %}}

## **Erkennen, ob das Arbeitsblatt passwortgeschützt ist**

Aspose.Cells for Java 8.7.0 hat die ausgesetzt[**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) -Eigenschaft, um zu erkennen, ob ein Arbeitsblatt passwortgeschützt ist oder nicht. Boolescher Typ[**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) Feld gibt zurück**Stimmt** wenn[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) ist passwortgeschützt und**FALSCH** wenn nicht.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectWorksheetisPasswordProtected-DetectWorksheetisPasswordProtected.java" >}}
