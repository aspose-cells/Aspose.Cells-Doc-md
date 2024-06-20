---
title: Ähnlichen Rahmenstil exportieren, wenn der Rahmenstil von Webbrowsern nicht unterstützt wird
type: docs
weight: 70
url: /de/net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **Mögliche Verwendungsszenarien**

Microsoft Excel unterstützt einige Arten von gestrichelten Linien, die von Webbrowsern nicht unterstützt werden. Wenn Sie eine solche Excel-Datei in HTML mit Aspose.Cells konvertieren, werden solche Linien entfernt. Allerdings kann Aspose.Cells auch unterstützen, solche Linien mit der [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle)-Eigenschaft anzuzeigen. Bitte setzen Sie den Wert auf **true** und die nicht unterstützten Linien werden auch in der HTML-Datei exportiert.

## **Ähnlichen Randstil exportieren, wenn der Randstil von Webbrowsern nicht unterstützt wird**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](64716806.xlsx) , die einige nicht unterstützte Rahmen aufweist, wie in der folgenden Abbildung gezeigt. Die Abbildung veranschaulicht weiterhin die Wirkung der [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle)-Eigenschaft im [Ausgabe-HTML](64716804.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportSimilarBorderStyle.cs" >}}
