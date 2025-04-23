---
title: Verbergen von überlagertem Inhalt mit CrossHideRight beim Speichern als HTML
type: docs
weight: 100
url: /de/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/
---

## **Mögliche Verwendungsszenarien**

Wenn Sie Ihre Excel-Datei in HTML speichern, können Sie verschiedene Kreuzarten für Zellzeichenfolgen angeben. Standardmäßig generiert Aspose.Cells HTML gemäß Microsoft Excel, aber wenn Sie  [**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType) ändern in [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS-HIDE-RIGHT), dann werden alle Zeichenfolgen auf der rechten Seite der Zelle verborgen, die mit der Zellzeichenfolge überlagert sind oder mit ihr überlappen.

## **Überlagerter Inhalt mit CrossHideRight beim Speichern in HTML ausblenden**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](64716916.xlsx) und speichert sie als [Ausgabe-HTML](64716915.zip), nachdem das [**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType) als [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS-HIDE-RIGHT) festgelegt wurde. Der Screenshot erklärt, wie [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS-HIDE-RIGHT) den Ausgabe-HTML von der Standardausgabe beeinflusst.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.java" >}}
{{< app/cells/assistant language="java" >}}
