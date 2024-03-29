﻿---
title: Ausblenden von überlagerten Inhalten mit CrossHideRight beim Speichern unter HTML
type: docs
weight: 100
url: /de/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/
---
## **Mögliche Nutzungsszenarien**

Wenn Sie Ihre Excel-Datei unter HTML speichern, können Sie verschiedene Kreuztypen für Zellstrings angeben. Standardmäßig generiert Aspose.Cells HTML gemäß Microsoft Excel, aber wenn Sie die ändern[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType)zu[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)dann werden alle Zeichenfolgen auf der rechten Seite der Zelle ausgeblendet, die mit der Zellzeichenfolge überlagert oder überlappt sind.

## **Ausblenden von überlagerten Inhalten mit CrossHideRight beim Speichern unter HTML**

Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](64716916.xlsx)und speichert es ab[Ausgang HTML](64716915.zip)nach dem Einstellen der[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType)als[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT). Der Screenshot erklärt wie[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)beeinflusst die Ausgabe HTML von der Standardausgabe.

![todo: Bild_alt_Text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.java" >}}
