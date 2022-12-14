---
title: Exportieren Sie einen ähnlichen Rahmenstil, wenn der Rahmenstil nicht von Webbrowsern unterstützt wird
type: docs
weight: 70
url: /de/net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---
## **Mögliche Nutzungsszenarien**

Microsoft Excel unterstützt einige Arten von gestrichelten Rahmen, die von Webbrowsern nicht unterstützt werden. Wenn Sie eine solche Excel-Datei mit Aspose.Cells in HTML konvertieren, werden solche Rahmen entfernt. Aspose.Cells kann aber auch unterstützen, solche Grenzen mit anzuzeigen[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle) Eigentum. Bitte setzen Sie den Wert auf**Stimmt**und die nicht unterstützten Ränder werden ebenfalls in eine HTML-Datei exportiert.

## **Exportieren Sie einen ähnlichen Rahmenstil, wenn der Rahmenstil nicht von Webbrowsern unterstützt wird**

Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](64716806.xlsx) das einige nicht unterstützte Rahmen enthält, wie im folgenden Screenshot gezeigt. Der Screenshot veranschaulicht weiter die Wirkung von[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle)Eigentum innerhalb der[HTML ausgeben](64716804.zip).

![todo: Bild_alt_Text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportSimilarBorderStyle.cs" >}}
