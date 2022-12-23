---
title: Ohal Report Canvas-Komponente
type: docs
weight: 30
url: /de/net/ohal-report-canvas-component/
---
{{% alert color="primary" %}}

[Melden Sie sich unter PDF](https://blog.aspose.com/2008/03/17/complete-excel-export-capabilities-using-apis/)

**Verwendung von Aspose.Cells in der Report Canvas-Komponente**

Robert Chilvers, 17. März 2008

{{% /alert %}}

## **Produkthintergrund**

Die Report Canvas-Komponente ermöglicht es dem Benutzer, visuelle Berichte auf der Grundlage eines vorab geladenen Datensatzes zu erstellen. Der Benutzer kann seiner Leinwand verschiedene Komponenten hinzufügen, darunter Bilder, Textfelder, Diagramme und Tabellen, und dann die Daten angeben und angeben, wie sie aggregiert werden sollen. Der Benutzer kann die Objekte dann neu anordnen und ihre Größe ändern, damit sie auf ihre Seite passen. Der Benutzer kann Farbpaletten angeben und Vorlagen für die zukünftige Verwendung speichern. Aspose.Cells wird verwendet, um alle Objekte auf der Leinwand mit den richtigen Daten nach Excel zu exportieren. Die Komponente ist mit VB.Net in Visual Studio 2008 geschrieben.

## **Anforderungsszenario**

Wir haben Aspose.Cells aufgrund seiner fast vollständigen Microsoft Excel-Exportfunktionen ausgewählt. Am wichtigsten für uns ist die Möglichkeit, Diagramme und Tabellen insbesondere in Microsoft Excel 2007 zu exportieren – diese fehlten in anderen Komponenten von Drittanbietern.

## **Lösungsimplementierung**

Jedes Objekt im Berichtsbereich hat eine Funktion, der eine Instanz des Arbeitsblatts Aspose.Cells übergeben wird und die sich selbst dem Arbeitsblatt hinzufügt. Wenn der Benutzer einen Export anfordert, werden die Arbeitsmappe und die Arbeitsblätter initialisiert, und für jedes Objekt im Berichtsbereich wird diese Funktion aufgerufen.

## **Leistungen**

Aspose.Cells ermöglichte es uns, die Excel-Arbeitsmappe völlig unabhängig von Excel aufzubauen und die Arbeitsmappe dann in dem vom Benutzer gewählten Format zu speichern. Dies sparte Stunden beim Debuggen der Interaktion, wenn die Excel-Interop verwendet und verschiedene Routinen zum Speichern in verschiedenen Excel-Versionen implementiert wurden.

## **Zukünftige Implementierung**

Wir werden wahrscheinlich Aspose.Cells für das Laden und Speichern von Excel-Dateien verwenden. Dazu gehören das Laden von Datenvorlagen und das Exportieren von Ergebnissen.

## **Fazit**

{{% alert color="primary" %}}

Bisher hatten wir keine Probleme mit den Komponenten Aspose.Cells und die Komponente sollte uns sowohl kurz- als auch langfristig Entwicklungszeit sparen. Support- und Vertriebsanfragen wurden schnell und hilfreich beantwortet.

{{% /alert %}}
