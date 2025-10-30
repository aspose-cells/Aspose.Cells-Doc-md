---
title: Verbergen von überlagertem Inhalt mit CrossHideRight beim Speichern als HTML
type: docs
weight: 100
url: /de/python-net/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **Mögliche Verwendungsszenarien**

Beim Speichern Ihrer Excel-Datei als HTML können Sie unterschiedliche Kreuztypen für Zellstrings angeben. Standardmäßig generiert Aspose.Cells für Python via .NET HTML entsprechend Microsoft Excel, aber wenn Sie den Kreuztyp auf [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/) ändern, werden alle mit Überlagerung oder Überschneidung des Zellstrings auf der rechten Seite versehenen Strings ausgeblendet.

## **Verstecken überlagerter Inhalte mit CrossHideRight beim Speichern in Html**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](64716894.xlsx) und speichert sie im [Ausgabe-HTML](64716893.zip) nachdem der [**HtmlSaveOptions.html_cross_string_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/html_cross_string_type) als [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/) festgelegt wurde. Die Abbildung erklärt, wie [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/) den Ausgabe-HTML-Code vom Standardausgang beeinflusst.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
{{< app/cells/assistant language="python-net" >}}
