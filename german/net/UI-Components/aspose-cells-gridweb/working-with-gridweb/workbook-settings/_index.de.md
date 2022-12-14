---
title: Einstellungen für Arbeitsmappe
type: docs
weight: 250
url: /de/net/aspose-cells-gridweb/workbook-settings/
description: Dieser Artikel beschreibt die Arbeitsmappeneinstellungen für GridWeb.
keywords: settings
---
Es gibt einige Einstellungen, die wir durch set GridWorkbookSettings festlegen können:

 
- **[GridWorkbookSettings](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/GridWorkbookSettings)**

|**Name** |**Beschreibung** |
|:- |:- |
| MaxIteration| Ruft die maximale Anzahl von Iterationen zum Auflösen eines Zirkelverweises ab oder legt diese fest, der Standardwert ist 100.|
| Wiederholung| Ruft ab oder legt fest, ob eine Iteration zum Auflösen von Zirkelbezügen verwendet wird.|
| ForceFullCalculate| Ruft ab oder legt fest, ob jedes Mal, wenn eine Berechnung ausgelöst wird, vollständig berechnet wird.|
| CreateCalcChain|Ruft ab oder legt fest, ob eine berechnete Formelkette erstellt wird. Standard ist falsch.|
| Beim Öffnen neu berechnen| Ruft ab oder legt fest, ob alle Formeln beim Öffnen der Datei neu berechnet werden.|
| Präzisionwieangezeigt| True, wenn Berechnungen in dieser Arbeitsmappe nur mit der Genauigkeit der angezeigten Zahlen durchgeführt werden|
| Datum1904| Ruft einen Wert ab oder legt einen Wert fest, der angibt, ob die Arbeitsmappe das Datumssystem 1904 verwendet.|
| Überprüfen Sie CustomNumberFormat| Ruft ab oder legt fest, ob beim Festlegen von Style.Custom das benutzerdefinierte Zahlenformat überprüft wird.|
| Autor| Ruft den Autor der Datei ab und legt ihn fest.|
 


Beispielsweise setzt der folgende Code ReCalculateOnOpen auf false, um die Berechnung beim Öffnen der Datei zu stoppen:

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-ReCalculateOnOpen.cs" >}}

 Der folgende Code legt den Autor für die Datei fest:

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-Author.cs" >}}
 
 