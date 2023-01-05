---
title: Öffentlich API Änderungen in Aspose.Cells 8.2.0
type: docs
weight: 70
url: /de/net/public-api-changes-in-aspose-cells-8-2-0/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt Änderungen an Aspose.Cells API von Version 8.1.2 zu 8.2.0, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **MultiThreadReading-Eigenschaft für Klasse Cells hinzugefügt**
Mit Aspose.Cells for .NET 8.2.0 wurde die Eigenschaft MultiThreadReading zur Klasse Cells hinzugefügt, um einen robusteren Mechanismus zum gleichzeitigen Lesen von Zellenwerten mit mehreren Threads bereitzustellen. Durch Festlegen der Boolean-Typeneigenschaft in der Multithread-Anwendung auf true wird sichergestellt, dass jeder Thread den richtigen Zellenwert erhält.

{{% alert color="primary" %}} 

 Bitte lesen Sie den ausführlichen Artikel auf[Lesen Sie gleichzeitig Cells-Werte in einer Multithread-Umgebung](http://aspose.com/docs/display/cellsnet/Reading+Cells+Values+in+Multiple+Threads+Simultaneously) für mehr Informationen.

{{% /alert %}}
## **Überladungen für AutoFitRows- und AutoFitColumns-Methoden hinzugefügt**
 Der Worksheet-Klasse wurden neue Überladungen für AutoFitRows und AutoFitColumns hinzugefügt, die es den Entwicklern ermöglichen, die Zeilen und Spalten basierend auf ihren jeweiligen Bereichen automatisch anzupassen, während sie eine Instanz der AutoFitterOptions-Klasse übergeben.

Die Signaturen der oben genannten Methoden sind wie folgt:

1. AutoFitRows(int startRow, int endRow, AutoFitterOptions-Optionen)
1. AutoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions-Optionen)

{{% alert color="primary" %}} 

 Bitte lesen Sie den ausführlichen Artikel auf[Zeilen und Spalten automatisch anpassen](http://aspose.com/docs/display/cellsnet/AutoFit+Rows+and+Columns).

{{% /alert %}}
