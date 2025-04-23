---
title: Öffentliche API Änderungen in Aspose.Cells 8.2.0
type: docs
weight: 70
url: /de/net/public-api-changes-in-aspose-cells-8-2-0/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt Änderungen an der Aspose.Cells API von Version 8.1.2 auf 8.2.0, die für Modul-/Anwendungs-Entwickler von Interesse sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, sondern auch eine Beschreibung etwaiger Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzufügen der MultiThreadReading-Eigenschaft für die Cells-Klasse**
Mit Aspose.Cells for .NET 8.2.0 wurde die MultiThreadReading-Eigenschaft zur Cells-Klasse hinzugefügt, um einen robusteren Mechanismus zum Lesen von Zellenwerten mit mehreren Threads gleichzeitig bereitzustellen. Durch Festlegen der Eigenschaft vom Typ Boolean auf true in der Mehrfaden-Anwendung wird sichergestellt, dass jeder Thread den korrekten Zellenwert erhält.

{{% alert color="primary" %}} 

Bitte prüfen Sie den ausführlichen Artikel zu [Gleichzeitiges Lesen von Zellenwerten in einer Multi-Thread-Umgebung](http://aspose.com/docs/display/cellsnet/Reading+Cells+Values+in+Multiple+Threads+Simultaneously) für weitere Informationen.

{{% /alert %}}
## **Hinzugefügte Überladungen für die Methoden AutoFitRows & AutoFitColumns**
Der Worksheet-Klasse wurden neue Überladungen für die AutoFitRows- & AutoFitColumns-Methoden hinzugefügt, die es den Entwicklern ermöglichen, die Zeilen & Spalten basierend auf ihren jeweiligen Bereichen automatisch anzupassen, während sie eine Instanz der AutoFitterOptions-Klasse übergeben. 

Die Signaturen der genannten Methoden lauten wie folgt:

1. AutoFitRows(int startRow, int endRow, AutoFitterOptions options)
1. AutoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions options)

{{% alert color="primary" %}} 

Bitte prüfen Sie den ausführlichen Artikel zu [Automatisches Anpassen von Zeilen und Spalten](http://aspose.com/docs/display/cellsnet/AutoFit+Rows+and+Columns).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
