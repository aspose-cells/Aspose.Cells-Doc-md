---
title: Ignorieren Sie Stile, um eine bessere Leistung in GridWeb zu erzielen
type: docs
weight: 1060
url: /de/net/aspose-cells-gridweb/ignorestylewithnodata
description: In diesem Artikel wird beschrieben, wie IgnoreStyleWithNoData verwendet wird, um eine bessere Leistung für die Aspose.Cells.GridWeb-Bibliothek zu erzielen.
keywords: performance
---
## **Mögliche Nutzungsszenarien**
 Bitte verwende[GridWeb.IgnoreStyleWithNoData](https://reference.aspose.com/cells/net/aspose.cells.gridweb/mainweb/ignorestylewithnodata)-Eigenschaft, um weniger benötigte Zeilen/Spalten aus der Arbeitsmappe zu laden.
 
## **Bessere Leistung beim Laden der Arbeitsmappe**
 Bitte überprüfen Sie die[Excel-Beispieldatei](largerowswithstyle.xlsx) 

Wenn gesetzt IgnoreStyleWithNoData = true;

Wie Sie sehen können, werden Zeilen (bis 15) und Spalten (bis L) angezeigt. Die letzten fortlaufenden Zeilen und Spalten werden nicht ohne Daten in Zellen angezeigt. Daher ist die Ladezeit kürzer.

![Arbeitsmappe mit Stil ignorieren](ignorestyletrue.png)


Wenn gesetzt IgnoreStyleWithNoData = false;(der Standardwert ist false)

Wie Sie sehen können, zeigt es viel mehr Zeilen (bis 500) und Spalten (bis CZ)

Von Zeile 16 bis Zeile 500 haben einige der Zellen den Rahmenstil festgelegt, die Zellen enthalten jedoch keine Daten.

Von Spalte M bis Spalte CZ haben einige der Zellen den Randstil festgelegt, die Zellen enthalten jedoch keine Daten.

![Arbeitsmappe ohne Stil zu ignorieren](ignorestylefalse.png)
 
 
 