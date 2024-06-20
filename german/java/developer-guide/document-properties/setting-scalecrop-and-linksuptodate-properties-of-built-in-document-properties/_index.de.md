---
title: Festlegung der ScaleCrop und LinksUpToDate Eigenschaften der integrierten Dokumenteigenschaften
type: docs
weight: 1050
url: /de/java/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **Mögliche Verwendungsszenarien**
[ScaleCrop](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop) und [LinksUpToDate](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate) sind zwei erweiterte integrierte Dokumenteigenschaften, die im OpenXml-Format definiert sind. Der Zweck dieser Eigenschaften ist wie folgt
## **1) ScaleCrop**
Dieses Element zeigt den Anzeigemodus des Dokumentvorschaubilds an. Setzen Sie dieses Element auf **true**, um das Skalieren des Dokumentvorschaubilds für die Anzeige zu ermöglichen. Setzen Sie dieses Element auf **false**, um das Zuschneiden des Dokumentvorschaubilds auf nur die Bereiche zu ermöglichen, die in die Anzeige passen.

Die möglichen Werte für dieses Element sind durch den Datentyp boolean des W3C XML-Schemas definiert.
## **2) LinksUpToDate**
Dieses Element gibt an, ob Hyperlinks in einem Dokument auf dem neuesten Stand sind. Setzen Sie dieses Element auf **true**, um anzuzeigen, dass Hyperlinks aktualisiert sind. Setzen Sie dieses Element auf **false**, um anzuzeigen, dass Hyperlinks veraltet sind.

Die möglichen Werte für dieses Element sind durch den Datentyp boolean des W3C XML-Schemas definiert.
## **Screenshot, der diese Eigenschaften in der app.xml-Datei zeigt**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Festlegen der Eigenschaften ScaleCrop und LinksUpToDate der integrierten Dokumenteigenschaften**
Der folgende Beispielcode setzt die [ScaleCrop](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop) und [LinksUpToDate](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate) erweiterten integrierten Dokumenteigenschaften der Arbeitsmappe. Bitte überprüfen Sie die mit diesem Code generierte [Ausgabedatei Excel](5472494.xlsx), ändern Sie ihre Erweiterung in .zip, extrahieren Sie ihre Inhalte und betrachten Sie die aap.xml wie im obigen Screenshot gezeigt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingScaleCropLinksUpToDate-SettingScaleCropLinksUpToDate.java" >}}
