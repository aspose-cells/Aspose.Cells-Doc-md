﻿---
title: Festlegen der ScaleCrop- und LinksUpToDate-Eigenschaften der integrierten Dokumenteigenschaften
type: docs
weight: 320
url: /de/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---
## **Mögliche Nutzungsszenarien**
[ScaleCrop](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop) und[LinksUpToDate](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate)sind zwei erweiterte integrierte Dokumenteigenschaften, die im OpenXml-Format definiert sind. Der Zweck dieser Eigenschaften ist der folgende
## **1) ScaleCrop**
 Dieses Element gibt den Anzeigemodus des Miniaturbilds des Dokuments an. Setzen Sie dieses Element auf**WAHR** um die Miniaturansicht des Dokuments auf die Anzeige zu skalieren. Setzen Sie dieses Element auf**FALSCH** , um das Zuschneiden der Miniaturansicht des Dokuments zu aktivieren, damit nur Abschnitte angezeigt werden, die in die Anzeige passen.

Die möglichen Werte für dieses Element werden durch den booleschen Datentyp des W3C-XML-Schemas definiert.
## **2) LinksUpToDate**
 Dieses Element gibt an, ob Hyperlinks in einem Dokument aktuell sind. Setzen Sie dieses Element auf**WAHR** um anzuzeigen, dass Hyperlinks aktualisiert werden. Setzen Sie dieses Element auf**FALSCH** um anzuzeigen, dass Hyperlinks veraltet sind.

Die möglichen Werte für dieses Element werden durch den booleschen Datentyp des W3C-XML-Schemas definiert.
## **Screenshot, der diese Eigenschaften in der Datei „app.xml“ zeigt**
![todo: Bild_alt_Text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Festlegen der ScaleCrop- und LinksUpToDate-Eigenschaften der integrierten Dokumenteigenschaften**
 Der folgende Beispielcode legt die[ScaleCrop](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop) und[LinksUpToDate](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate) erweiterte integrierte Dokumenteigenschaften der Arbeitsmappe. Bitte überprüfen Sie die[Excel-Datei ausgeben](5115500.xlsx)die mit diesem Code generiert wurde, ändern Sie ihre Erweiterung in .zip und extrahieren Sie ihren Inhalt und sehen Sie sich die app.xml an, wie im obigen Screenshot gezeigt.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingScaleCropAndLinksUpToDateProperties.cs" >}}
