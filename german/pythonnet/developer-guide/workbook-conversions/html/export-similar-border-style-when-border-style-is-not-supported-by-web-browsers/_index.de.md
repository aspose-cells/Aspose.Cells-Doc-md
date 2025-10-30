---
title: Ähnlichen Rahmenstil exportieren, wenn der Rahmenstil von Webbrowsern nicht unterstützt wird
type: docs
weight: 70
url: /de/python-net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **Mögliche Verwendungsszenarien**

Microsoft Excel unterstützt bestimmte Arten von gestrichelten Rahmen, die von Webbrowsern nicht unterstützt werden. Beim Konvertieren einer solchen Excel-Datei in HTML mit Aspose.Cells für Python via .NET werden diese Rahmen entfernt. Aspose.Cells für Python via .NET kann jedoch auch unterstützt werden, um solche Rahmen mit der [**HtmlSaveOptions.export_similar_border_style**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_similar_border_style)-Eigenschaft anzuzeigen. Bitte setzen Sie den Wert auf **true**, damit die nicht unterstützten Rahmen ebenfalls in die HTML-Datei exportiert werden.

## **Ähnlichen Randstil exportieren, wenn der Randstil von Webbrowsern nicht unterstützt wird**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](64716806.xlsx) , die einige nicht unterstützte Rahmen aufweist, wie in der folgenden Abbildung gezeigt. Die Abbildung veranschaulicht weiterhin die Wirkung der [**HtmlSaveOptions.export_similar_border_style**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_similar_border_style)-Eigenschaft im [Ausgabe-HTML](64716804.zip).

![todo:image_alt_text](1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportSimilarBorderStyle.py" >}}
{{< app/cells/assistant language="python-net" >}}
