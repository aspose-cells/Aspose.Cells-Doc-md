---
title: Angewendete Validierung auf einer Zelle erhalten.
type: docs
weight: 80
url: /de/java/get-validation-applied-on-a-cell/
description: In diesem Artikel wird erläutert, wie Sie mit Java die Validierung auf einer Zelle anwenden können.
keywords: Zellvalidierung in Excel mit Java anwenden, Validierung auf einer Zelle in Excel mit Java anwenden, Validierung in Excel mit Java anwenden, Zellvalidierung in Excel mit Java, Java Zellvalidierung in Excel anwenden, Java Validierung auf einer Zelle in Excel anwenden, Java Zellvalidierung in Excel, Java Zellvalidierung
---

{{% alert color="primary" %}}

Sie können die Aspose.Cells API verwenden, um die Validierung an einer Zelle anzuwenden. Aspose.Cells bietet die Methode [**Cell.getValidation()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidation--) für diesen Zweck. Wenn keine Validierung an der Zelle vorliegt, gibt sie null zurück. Ebenso können Sie die Methode [**Worksheet.getValidations().getValidationInCell(int row, int column)**](https://reference.aspose.com/cells/java/com.aspose.cells/validationcollection#getValidationInCell(int,%20int)) verwenden, um die validierung an einer Zelle zu erhalten, indem Sie ihre Zeilen- und Spaltenindizes bereitstellen.

{{% /alert %}}

Die folgende Momentaufnahme zeigt die Beispiel-Microsoft-Excel-Datei, die im folgenden Beispielcode verwendet wird. Die Zelle **C1** hat eine **Dezimalvalidierung** und kann nur Werte **zwischen 10 und 20** annehmen.

**Eine Zelle mit Validierung**

![todo:image_alt_text](get-validation-applied-on-a-cell_1.png)

Der folgende Beispielcode erhält die Validierung, die auf C1 angewendet wird, und liest ihre verschiedenen Eigenschaften.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetValidationAppliedonCell-GetValidationAppliedonCell.java" >}}

Hier ist die Konsolenausgabe des Beispielcodes, der mit der oben gezeigten Beispieldatei ausgeführt wurde.

{{< highlight java >}}

Reading Properties of Validation

\--------------------------------

Type: 2

Operator: 0

Formula1: =10

Formula2: =20

Ignore blank: true

{{< /highlight >}}

## Verwandte Artikel

- [Datenüberprüfung](/cells/de/java/data-validation/)
