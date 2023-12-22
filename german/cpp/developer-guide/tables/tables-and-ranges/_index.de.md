---
title: Tabellen und Bereiche
type: docs
weight: 30
url: /de/cpp/tables-and-ranges/
---
##  **Einführung**
Manchmal erstellen Sie eine Tabelle in Microsoft Excel und möchten nicht weiter mit der darin enthaltenen Tabellenfunktionalität arbeiten. Stattdessen möchten Sie etwas, das wie ein Tisch aussieht. Um Daten in einer Tabelle zu behalten, ohne die Formatierung zu verlieren, konvertieren Sie die Tabelle in einen regulären Datenbereich. Aspose.Cells unterstützt diese Funktion von Microsoft Excel für Tabellen und Listenobjekte.
##  **Mit Microsoft Excel**
 Benutzen Sie die**In Bereich umrechnen** Funktion zum schnellen Konvertieren einer Tabelle in einen Bereich, ohne dass die Formatierung verloren geht. In Microsoft Excel 2007/2010:

1. Klicken Sie auf eine beliebige Stelle in der Tabelle, um sicherzustellen, dass sich die aktive Zelle in einer Tabellenspalte befindet.
1.  Auf der**Design** Registerkarte, in der**Werkzeuge** Klicken Sie in der Gruppe auf *In Bereich konvertieren**.

{{% alert color="primary" %}} 

Die Tabellenfunktionen sind nicht mehr verfügbar, nachdem die Tabelle in einen Bereich konvertiert wurde. Zeilenüberschriften enthalten beispielsweise nicht mehr die Sortier- und Filterpfeile und strukturierte Referenzen (Referenzen, die Tabellennamen verwenden), die in Formeln verwendet wurden, werden zu regulären Zellreferenzen.

{{% /alert %}} 
##  **Verwenden Sie Aspose.Cells**
Der folgende Codeausschnitt demonstriert die gleiche Funktionalität mit Aspose.Cells.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-ConvertTableToRange-new.cpp" >}}
