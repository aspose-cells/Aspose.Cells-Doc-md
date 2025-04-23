---
title: Ohal Report Canvas Component
type: docs
weight: 30
url: /de/net/ohal-report-canvas-component/
---

{{% alert color="primary" %}}

[Bericht PDF](https://blog.aspose.com/2008/03/17/complete-excel-export-capabilities-using-apis/)

**Verwendung von Aspose.Cells im Bericht-Canvas-Komponente**

Robert Chilvers, 17. März 2008

{{% /alert %}}

## **Produkt-Hintergrund**

Die Bericht-Canvas-Komponente ermöglicht es dem Benutzer, visuelle Berichte auf der Basis eines vorab geladenen Datensatzes zu erstellen. Der Benutzer kann verschiedene Komponenten zu seiner Leinwand hinzufügen, einschließlich Bilder, Textfelder, Diagramme und Tabellen. Anschließend gibt er die Daten und deren Aggregation an. Der Benutzer kann dann die Objekte neu anordnen und ihre Größe anpassen, um auf seine Seite zu passen. Der Benutzer kann Farbpaletten festlegen und Vorlagen für die zukünftige Verwendung speichern. Aspose.Cells wird verwendet, um alle Objekte auf der Leinwand mit den korrekten Daten nach Excel zu exportieren. Die Komponente ist in VB.Net in Visual Studio 2008 geschrieben.

## **Anforderungsszenario**

Wir haben Aspose.Cells aufgrund seiner nahezu vollständigen Exportfähigkeiten für Microsoft Excel ausgewählt. Für uns ist besonders wichtig, dass die Fähigkeit zum Exportieren von Diagrammen und Tabellen, insbesondere in Microsoft Excel 2007, vorhanden war - diese fehlten bei anderen Drittanbieterkomponenten.

## **Lösungsimplementierung**

Jedes Objekt auf dem Bericht-Canvas verfügt über eine Funktion, die eine Instanz des Aspose.Cells-Arbeitsblatts erhält und sich selbst dem Arbeitsblatt hinzufügt. Wenn der Benutzer einen Export anfordert, werden das Arbeitsbuch und die Arbeitsblätter initialisiert und diese Funktion für jedes Objekt auf dem Bericht-Canvas aufgerufen.

## **Vorteile**

Aspose.Cells ermöglichte es uns, das Excel-Arbeitsbuch vollständig unabhängig von Excel aufzubauen und dann das Arbeitsbuch im vom Benutzer ausgewählten Format zu speichern. Dies ersparte stundenlanges Debugging bei der Interaktion bei Verwendung der Excel-Interop und der Implementierung unterschiedlicher Routinen zum Speichern in verschiedenen Excel-Versionen.

## **Zukünftige Implementierung**

Wir werden voraussichtlich Aspose.Cells für das Laden und Speichern aller Excel-Dateien verwenden. Dies umfasst das Laden von Datenvorlagen und das Exportieren von Ergebnissen.

## **Fazit**

{{% alert color="primary" %}}

Bisher haben wir keine Probleme bei der Verwendung der Aspose.Cells-Komponenten gehabt und die Komponente sollte uns bei der Entwicklung sowohl kurz- als auch langfristig Zeit sparen. Support- und Verkaufsfragen wurden schnell und hilfreich beantwortet.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
