---
title: Ähnlichen Rahmenstil exportieren, wenn der Rahmenstil von Webbrowsern nicht unterstützt wird
type: docs
weight: 70
url: /de/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **Mögliche Verwendungsszenarien**

Microsoft Excel unterstützt einige Arten von gestrichelten Rahmen, die von Webbrowsern nicht unterstützt werden. Wenn Sie eine solche Excel-Datei unter Verwendung von Aspose.Cells in HTML konvertieren, werden solche Rahmen entfernt. Aspose.Cells kann jedoch auch unterstützen, ähnliche Rahmen mit der Eigenschaft [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle) anzuzeigen. Bitte setzen Sie ihren Wert als **true** und die nicht unterstützten Rahmen werden ebenfalls in die HTML-Datei exportiert.

## **Ähnlichen Randstil exportieren, wenn der Randstil von Webbrowsern nicht unterstützt wird**

Der folgende Beispielscode lädt die [sample Excel-Datei](64716832.xlsx) die einige nicht unterstützte Rahmen enthält, wie in folgendem Screenshot gezeigt. Der Screenshot veranschaulicht weiterhin die Wirkung der [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle) Eigenschaft innerhalb des [ausgegebenen HTMLs](64716831.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportSimilarBorderStyle.java" >}}
{{< app/cells/assistant language="java" >}}
