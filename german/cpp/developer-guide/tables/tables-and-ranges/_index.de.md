---
title: Tabellen und Bereiche
type: docs
weight: 30
url: /de/cpp/tables-and-ranges/
---

## **Einführung**
Manchmal erstellen Sie in Microsoft Excel eine Tabelle und möchten nicht mit der Tabellenfunktionalität arbeiten, die sie mitbringt. Stattdessen möchten Sie etwas, das wie eine Tabelle aussieht. Um Daten in einer Tabelle zu behalten, ohne die Formatierung zu verlieren, wandeln Sie die Tabelle in einen regulären Datenbereich um. Aspose.Cells unterstützt diese Funktion von Microsoft Excel für Tabellen und Listenobjekte.
## **Verwendung von Microsoft Excel**
Verwenden Sie die **In Bereich konvertieren** -Funktion, um eine Tabelle ohne Formatierung schnell in einen Bereich zu konvertieren. In Microsoft Excel 2007/2010:

1. Klicken Sie irgendwo in der Tabelle, um sicherzustellen, dass die aktive Zelle in einer Tabellenspalte liegt.
1. Auf dem Register **Entwurf** klicken Sie in der Gruppe **Tools** auf **In Bereich konvertieren**.

{{% alert color="primary" %}} 

Die Tabellenfunktionen sind nicht mehr verfügbar, nachdem die Tabelle in einen Bereich konvertiert wurde. Beispielsweise enthalten die Zeilenüberschriften nicht mehr die Sortier- und Filterpfeile, und strukturierte Verweise (Verweise, die Tabellennamen verwenden), die in Formeln verwendet wurden, werden in normale Zellverweise umgewandelt.

{{% /alert %}} 
## **Verwendung von Aspose.Cells**
Der folgende Codeausschnitt zeigt die gleiche Funktionalität unter Verwendung von Aspose.Cells.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-ConvertTableToRange-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
