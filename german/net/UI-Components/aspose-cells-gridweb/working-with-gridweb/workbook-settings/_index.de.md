---
title: Einstellungen für Arbeitsmappe
type: docs
weight: 250
url: /de/net/aspose-cells-gridweb/aspose-cells-gridweb/workbook-settings/
description: Dieser Artikel beschreibt die Arbeitsmappeneinstellungen in GridWeb.
keywords: GridWeb,Einstellungen
---


Es gibt einige Einstellungen, die wir durch Setzen von GridWorkbookSettings festlegen können:


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/GridWorkbookSettings)

|**Name** |**Beschreibung** |
| :- | :- |
|MaxIteration |Ruft den maximalen Durchlauf zur Lösung einer Zirkelreferenz ab oder legt diesen fest. Der Standardwert ist 100.
|Iteration | Ruft ab oder legt fest, ob zur Lösung von Zirkelbezügen Iterationen verwendet werden.
|ForceFullCalculate | Ruft ab oder legt fest, ob bei jeder Auslösung einer Berechnung immer vollständig berechnet wird.
|CreateCalcChain | Ruft ab oder legt fest, ob eine berechnete Formelkette erstellt wird. Der Standardwert ist false.
|ReCalculateOnOpen | Ruft ab oder legt fest, ob alle Formeln beim Öffnen der Datei erneut berechnet werden.
|PrecisionAsDisplayed | True, wenn Berechnungen in dieser Arbeitsmappe nur mit der Genauigkeit der angezeigten Zahlen durchgeführt werden.
|Date1904 | Ruft einen Wert ab oder legt diesen fest, der angibt, ob die Arbeitsmappe das Datumsystem 1904 verwendet.
|CheckCustomNumberFormat | Ruft ab oder legt fest, ob beim Setzen von Style.Custom die benutzerdefinierte Zahlenformatüberprüfung aktiviert wird.
|Author |Ruft den Autor der Datei ab und legt ihn fest. |



Zum Beispiel setzt der folgende Code das ReCalculateOnOpen auf false, um die Berechnung beim Öffnen der Datei zu stoppen:

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-ReCalculateOnOpen.cs" >}}

 Der folgende Code setzt den Autor für die Datei:

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-Author.cs" >}}


