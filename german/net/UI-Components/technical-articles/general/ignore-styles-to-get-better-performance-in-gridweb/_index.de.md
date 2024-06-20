---
title: Ignorieren von Stilen für bessere Leistung in GridWeb
type: docs
weight: 1060
url: /de/net/aspose-cells-gridweb/ignorestylewithnodata
description: Dieser Artikel beschreibt, wie die IgnoreStyleWithNoData Eigenschaft verwendet wird, um eine bessere Leistung in GridWeb zu erzielen.
keywords: GridWeb,performance
---

## **Mögliche Verwendungsszenarien**
Bitte verwenden Sie die Eigenschaft [GridWeb.IgnoreStyleWithNoData](https://reference.aspose.com/cells/net/aspose.cells.gridweb/mainweb/ignorestylewithnodata), um weniger erforderliche Zeilen/Spalten aus der Arbeitsmappe zu laden.

## **Bessere Leistung beim Laden der Arbeitsmappe**
Bitte überprüfen Sie die [Beispiel-Excel-Datei](largerowswithstyle.xlsx) 

Wenn IgnoreStyleWithNoData = true festgelegt ist;

Wie Sie sehen können, werden Zeilen (bis 15) und Spalten (bis L) angezeigt. Die letzten durchgehenden Zeilen und Spalten ohne Daten in den Zellen werden nicht angezeigt. Die Ladezeit wird somit verkürzt.

![Arbeitsmappe mit ignorierten Stilen](ignorestyletrue.png)


Wenn IgnoreStyleWithNoData = false festgelegt ist (der Standardwert ist false);

Wie Sie sehen können, werden viel mehr Zeilen (bis 500) und Spalten (bis CZ) angezeigt

Von Zeile 16 bis Zeile 500 haben einige Zellen den Rahmenstil erhalten, enthalten jedoch keine Daten.

Von Spalte M bis Spalte CZ wurden einige Zellen mit dem Randstil versehen, jedoch enthalten die Zellen keine Daten.

![Arbeitsmappe ohne ignorierten Stil](ignorestylefalse.png)



