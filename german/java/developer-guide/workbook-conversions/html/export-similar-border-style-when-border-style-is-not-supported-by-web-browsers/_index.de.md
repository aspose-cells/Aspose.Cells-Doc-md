---
title: Exportieren Sie einen ähnlichen Rahmenstil, wenn der Rahmenstil nicht von Webbrowsern unterstützt wird
type: docs
weight: 70
url: /de/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---
## **Mögliche Nutzungsszenarien**

Microsoft Excel unterstützt einige Arten von gestrichelten Rahmen, die von Webbrowsern nicht unterstützt werden. Wenn Sie eine solche Excel-Datei mit Aspose.Cells in HTML konvertieren, werden solche Rahmen entfernt. Aspose.Cells kann jedoch auch die Anzeige ähnlicher Rahmen unterstützen[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle)Eigentum. Bitte setzen Sie den Wert auf**Stimmt**und die nicht unterstützten Ränder werden ebenfalls in eine HTML-Datei exportiert.

## **Exportieren Sie einen ähnlichen Rahmenstil, wenn der Rahmenstil nicht von Webbrowsern unterstützt wird**

Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](64716832.xlsx)das einige nicht unterstützte Rahmen enthält, wie im folgenden Screenshot gezeigt. Der Screenshot veranschaulicht weiter die Wirkung von[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle)Eigentum innerhalb der[HTML ausgeben](64716831.zip).

![todo: Bild_alt_Text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportSimilarBorderStyle.java" >}}
