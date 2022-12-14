---
title: Festlegen der ScaleCrop- und LinksUpToDate-Eigenschaften der integrierten Dokumenteigenschaften
type: docs
weight: 1050
url: /de/java/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---
## **Mögliche Nutzungsszenarien**
[ScaleCrop](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop) und[LinksUpToDate](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate)sind zwei erweiterte integrierte Dokumenteigenschaften, die im OpenXml-Format definiert sind. Der Zweck dieser Eigenschaften ist der folgende
## **1) ScaleCrop**
 Dieses Element gibt den Anzeigemodus des Miniaturbilds des Dokuments an. Setzen Sie dieses Element auf**Stimmt** um die Miniaturansicht des Dokuments auf die Anzeige zu skalieren. Setzen Sie dieses Element auf**FALSCH** , um das Zuschneiden der Miniaturansicht des Dokuments zu aktivieren, damit nur Abschnitte angezeigt werden, die in die Anzeige passen.

Die möglichen Werte für dieses Element werden durch den booleschen Datentyp des W3C-XML-Schemas definiert.
## **2) LinksUpToDate**
 Dieses Element gibt an, ob Hyperlinks in einem Dokument aktuell sind. Setzen Sie dieses Element auf**Stimmt** um anzuzeigen, dass Hyperlinks aktualisiert werden. Setzen Sie dieses Element auf**FALSCH**um anzuzeigen, dass Hyperlinks veraltet sind.

Die möglichen Werte für dieses Element werden durch den booleschen Datentyp des W3C-XML-Schemas definiert.
## **Screenshot, der diese Eigenschaften in der Datei „app.xml“ zeigt**
![todo: Bild_alt_Text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Festlegen der ScaleCrop- und LinksUpToDate-Eigenschaften der integrierten Dokumenteigenschaften**
 Der folgende Beispielcode legt die[ScaleCrop](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop)und[LinksUpToDate](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate) erweiterte integrierte Dokumenteigenschaften der Arbeitsmappe. Bitte überprüfen Sie die[Excel-Datei ausgeben](5472494.xlsx)die mit diesem Code generiert wurde, ändern Sie ihre Erweiterung in .zip und extrahieren Sie ihren Inhalt und sehen Sie sich die aap.xml an, wie im obigen Screenshot gezeigt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingScaleCropLinksUpToDate-SettingScaleCropLinksUpToDate.java" >}}
