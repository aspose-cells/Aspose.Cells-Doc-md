---
title: Lassen Sie sich die Validierung auf Cell anwenden
type: docs
weight: 80
url: /de/java/get-validation-applied-on-a-cell/
description: Dieser Artikel zeigt, wie Sie die Validierung auf eine Cell mit Java anwenden
keywords: apply cell validation in excel with java, apply validation on a cell in excel with java, apply validation in excel with java, cell validation in excel with java, java apply cell validation in excel, java apply validation on a cell in excel, java cell validation in excel, java cell validation
---
{{% alert color="primary" %}}

 Sie können Aspose.Cells API verwenden, um die Validierung auf eine beliebige Zelle anzuwenden. Aspose.Cells bietet die[**Cell.getValidation**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidation() ) Methode zu diesem Zweck. Wenn es keine Validierung für die Zelle gibt, gibt sie null zurück. Ebenso können Sie die verwenden[**Worksheet.getValidations().getValidationInCell (int-Zeile, int-Spalte)**](https://reference.aspose.com/cells/java/com.aspose.cells/validationcollection#getValidationInCell(int,%20int))-Methode zum Erfassen der auf eine Zelle angewendeten Validierung durch Bereitstellen ihrer Zeilen- und Spaltenindizes.

{{% /alert %}}

 Der folgende Schnappschuss zeigt die Excel-Beispieldatei Microsoft, die im Beispielcode unten verwendet wird. Cell**C1** hat**dezimale Validierung** angewendet und kann nur Werte annehmen**zwischen 10 und 20**.

**Eine Zelle mit Validierung**

![todo: Bild_alt_Text](get-validation-applied-on-a-cell_1.png)

Der folgende Beispielcode ruft die auf C1 angewendete Validierung ab und liest seine verschiedenen Eigenschaften.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetValidationAppliedonCell-GetValidationAppliedonCell.java" >}}

Hier ist die Konsolenausgabe des Beispielcodes, der mit der im obigen Schnappschuss gezeigten Beispieldatei ausgeführt wird.

{{< highlight "java" >}}

Reading Properties of Validation

\--------------------------------

Type: 2

Operator: 0

Formula1: =10

Formula2: =20

Ignore blank: true

{{< /highlight >}}

## In Verbindung stehende Artikel

- [Datenvalidierung](/cells/de/java/data-validation/)
