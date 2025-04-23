---
title: Öffentliche API Änderungen in Aspose.Cells 8.2.0
type: docs
weight: 80
url: /de/java/public-api-changes-in-aspose-cells-8-2-0/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt Änderungen an der Aspose.Cells API von Version 8.1.2 auf 8.2.0, die für Modul-/Anwendungs-Entwickler von Interesse sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, sondern auch eine Beschreibung etwaiger Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzufügen der MultiThreadReading-Eigenschaft für die Cells-Klasse**
Mit Aspose.Cells for Java 8.2.0 wurde die MultiThreadReading-Eigenschaft zur Cells-Klasse hinzugefügt, um einen robusteren Mechanismus zum Lesen von Zellenwerten mit mehreren Threads gleichzeitig bereitzustellen. Durch das Festlegen der Eigenschaft vom Typ Boolean auf true in der Mehrfadenanwendung wird sichergestellt, dass jeder Thread den korrekten Zellenwert erhält.

{{% alert color="primary" %}} 

Bitte überprüfen Sie den ausführlichen Artikel zu [Gleichzeitiges Lesen von Zellenwerten in einer mehrfädigen Umgebung](/cells/de/java/reading-cell-values-in-multiple-threads-simultaneously/) für weitere Informationen.

{{% /alert %}}
## **Hinzufügen von Überladungen für die autoFitRows- und autoFitColumns-Methoden**
Neue Überladungen für die autoFitRows- und autoFitColumns-Methoden wurden der Worksheet-Klasse hinzugefügt, um den Entwicklern das automatische Anpassen der Zeilen & Spalten basierend auf ihren jeweiligen Bereichen unter Verwendung einer Instanz der AutoFitterOptions-Klasse zu ermöglichen. 

Die Signaturen der genannten Methoden lauten wie folgt:

1. autoFitRows(int startRow, int endRow, AutoFitterOptions options)
1. autoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions options)

{{% alert color="primary" %}} 

Bitte lesen Sie den ausführlichen Artikel zu [Anpassen von Zeilen und Spalten](http://aspose.com/docs/display/cellsjava/AutoFit+Rows+and+Columns).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
