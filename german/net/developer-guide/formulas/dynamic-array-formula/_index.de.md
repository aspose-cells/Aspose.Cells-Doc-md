---
title: Festlegen dynamischer Array-Formeln
description: So verwenden Sie die Bibliothek Aspose.Cells zum Berechnen dynamischer Array-Formeln in Microsoft Excel. Durch das Laden einer vorhandenen Excel-Datei oder das Erstellen einer neuen Excel-Datei können wir die von Aspose.Cells bereitgestellte Methode verwenden, um die dynamische Array-Formel zu berechnen und das Ergebnis zu erhalten. Abschließend speichern wir die geänderte Excel-Datei auf der Festplatte.
keywords: Dynamic Array Formulas, Dynamic Array Formulas in Excel, Set dynamic array formulas, Calculation of dynamic array formulas, operate dynamic array formulas of Excel.
type: docs
weight: 70
url: /de/net/calculation-of-dynamic-array-formulas/
---
##  **Was ist die Excel-Array-Formel?**
In Excel ist eine Array-Formel ein spezieller Formeltyp, der es Ihnen ermöglicht, Berechnungen für Arrays von Daten statt für einzelne Zellen durchzuführen. Array-Formeln können verwendet werden, um komplexe Berechnungen durchzuführen, Daten zu manipulieren und spezifische Probleme effizient zu lösen. Sie werden anders eingegeben als normale Formeln und erfordern häufig die Verwendung von Strg + Umschalt + Eingabetaste.

Hier sind einige wichtige Punkte zu Arrayformeln in Excel:
1. Syntax:
<br>
Array-Formeln werden wie reguläre Formeln geschrieben, beinhalten jedoch Operationen auf Arrays von Werten. Sie werden in geschweifte Klammern {} eingeschlossen, um anzuzeigen, dass es sich um Arrayformeln handelt. Allerdings geben Sie diese geschweiften Klammern nicht selbst ein; Excel fügt sie automatisch hinzu, wenn Sie die Formel richtig eingeben.
1. Eingeben von Array-Formeln:
<br>
Um eine Array-Formel einzugeben, geben Sie die Formel in die Bearbeitungsleiste ein. Anstatt zum Beenden die Eingabetaste zu drücken, drücken Sie Strg + Umschalt + Eingabetaste. Dies teilt Excel mit, dass es sich um eine Arrayformel handelt. Bei korrekter Eingabe zeigt Excel die Formel in geschweiften Klammern in der Formelleiste an, um anzuzeigen, dass es sich um eine Array-Formel handelt.
1. Anwendungsfälle:
<br>
Array-Formeln eignen sich für die gleichzeitige Durchführung von Berechnungen über mehrere Zellen oder Bereiche hinweg. Sie können für fortgeschrittene mathematische Berechnungen, bedingte Operationen, das Filtern von Daten und mehr verwendet werden.
1. Vorteile:
<br>
Mit Array-Formeln können Sie komplexe Berechnungen in einer einzigen Formel durchführen, was die Effizienz verbessern und Ihre Arbeitsblätter vereinfachen kann. Sie können große Datenmengen verarbeiten und Berechnungen durchführen, die sonst mehrere Zwischenschritte erfordern würden.
1. Einschränkungen:
<br>
Array-Formeln können schwieriger zu verstehen und zu beheben sein als normale Formeln. Sie können die Arbeitsblattleistung verlangsamen, insbesondere bei intensiver Verwendung oder mit großen Datensätzen.
1. Beispiele:
<br>
 Summieren der Werte in einem Bereich:**{=SUMME(A1:A5*B1:B5)}**
<br>
 Ermitteln des Maximalwerts in einem Bereich:**{=MAX(A1:A5+B1:B5)}**
<br>
<image src="1.png" width="70%" />
<br>

Denken Sie daran, dass Array-Formeln mit Bedacht verwendet werden sollten und dass es wichtig ist, ihre Funktionsweise zu verstehen, bevor Sie sie in Ihre Arbeitsblätter implementieren. Sie können leistungsstarke Werkzeuge für die Datenanalyse und -bearbeitung in Excel sein.

##  **Was ist die Excel Dynamic Array-Formel?**
Dynamische Array-Formeln sind eine neue Funktion, die in Excel 365 und Excel 2021 eingeführt wurde. Sie ermöglichen Ihnen im Vergleich zu herkömmlichen Array-Formeln eine nahtlosere und effizientere Arbeit mit Arrays von Daten. Dynamische Array-Formeln übertragen die Ergebnisse automatisch auf benachbarte Zellen, wodurch Strg + Umschalt + Eingabetaste nicht mehr erforderlich ist und die Daten einfacher bearbeitet werden können.

Wichtige Punkte zu dynamischen Array-Formeln in Excel:
1. Automatisches Verschütten:
<br>
Dynamische Array-Formeln verteilen Ergebnisse basierend auf der Größe der Ausgabedaten automatisch in benachbarte Zellen. Das bedeutet, dass Sie vor der Eingabe der Formel keinen Zellbereich auswählen oder die Formel mit Strg + Umschalt + Eingabetaste bestätigen müssen.
1. Single-Cell Eintrag:
<br>
Dynamische Array-Formeln werden in eine einzelne Zelle eingegeben und Excel füllt die benachbarten Zellen automatisch mit den Ergebnissen. Dies erleichtert die Verwaltung und das Verständnis von Formeln, da Sie die Formel nur einmal eingeben müssen.
1. Neue Funktionen:
<br>
Dynamische Array-Formeln führen neue Funktionen ein, die Arrays nativ verarbeiten können, z. B. *FILTER**, *SORT**, *UNIQUE**, *SEQUENCE**, *SORTBY** und *RANDARRAY**. Diese Funktionen können mehrere Werte zurückgeben oder Arrays direkt bearbeiten und so komplexe Berechnungen vereinfachen.
1. Flexibles Sortimentshandling:
<br>
Dynamische Array-Formeln passen die Größe des verteilten Bereichs dynamisch an, basierend auf der Größe der Eingabedaten oder der durchgeführten Berechnung. Diese Flexibilität ermöglicht eine effizientere Nutzung des Arbeitsblattplatzes und vereinfacht die Formelerstellung.
1. Verbesserte Leistung:
<br>
Dynamische Array-Formeln können die Leistung im Vergleich zu herkömmlichen Array-Formeln verbessern, insbesondere bei der Arbeit mit großen Datensätzen oder komplexen Berechnungen.
1. Kompatibilität:
<br>
Dynamische Array-Formeln sind in Excel 365 und Excel 2021 verfügbar. Sie werden in älteren Versionen von Excel möglicherweise nicht unterstützt.
1. Beispiele für dynamische Array-Formeln:
<br>
*FILTER**: Gibt ein Array von Werten zurück, die bestimmte Kriterien erfüllen.
<br>
*SORT**: Sortiert die Werte in einem Bereich oder Array.
<br>
*UNIQUE**: Gibt eindeutige Werte aus einer Liste oder einem Bereich zurück.
<br>
*SEQUENCE**: Erzeugt eine Folge von Zahlen oder Daten.
<br>
*RANDARRAY**: Erzeugt ein Array von Zufallszahlen.
<br>
<image src="2.png" width="70%" />
<br>

Dynamische Array-Formeln bieten leistungsstarke Funktionen zur Datenbearbeitung und -analyse in Excel und erleichtern die Arbeit mit Datenarrays und die effiziente Durchführung komplexer Berechnungen.

##  **Was ist der Unterschied zwischen Array-Formeln und dynamischen Array-Formeln in Excel?**
In Excel werden sowohl Array-Formeln als auch dynamische Array-Formeln verwendet, um Berechnungen für mehrere Werte gleichzeitig durchzuführen. Sie weisen jedoch einige Unterschiede hinsichtlich der Funktionalität und der Art und Weise ihrer Implementierung auf.

###  **Funktionen für Array-Formeln**
1. Array-Formeln sind herkömmliche Formeln in Excel, mit denen Berechnungen für Datenarrays durchgeführt werden können.
1. Sie werden durch Drücken von Strg + Umschalt + Eingabetaste eingegeben, nachdem Sie die Formel eingegeben haben. Dadurch wird Excel mitgeteilt, dass es sich um eine Arrayformel handelt.
1. Array-Formeln haben Einschränkungen hinsichtlich ihrer Fähigkeit, Ergebnisse in benachbarte Zellen zu übertragen. Sie geben normalerweise ein 1. einzelnes Ergebnis zurück, obwohl es sich bei diesem Ergebnis möglicherweise um ein Zellenarray handelt.
1. Sie gibt es schon seit langem und werden in allen Excel-Versionen unterstützt.

###  **Funktionen dynamischer Array-Formeln**
1. Dynamische Array-Formeln sind eine neue Funktion, die in Excel 365 (Office 365-Abonnement) und Excel 2021 eingeführt wurde.
1. Basierend auf der Größe der Eingabedaten oder der Formelberechnung werden Ergebnisse automatisch in benachbarte Zellen übertragen.
1. Dynamische Array-Formeln erfordern nicht das Drücken von Strg + Umschalt + Eingabetaste; Sie geben einfach die Formel in eine Zelle ein und Excel füllt die angrenzenden Zellen automatisch mit den Ergebnissen.
1. Diese Formeln können mehrere Ergebnisse (einen Zellbereich) direkt zurückgeben, ohne dass eine Array-Formel oder Strg + Umschalt + Eingabetaste erforderlich ist.
1. Sie verfügen über neue Funktionen wie *FILTER**, *SORT**, *UNIQUE** usw., die Arrays nativ verarbeiten und Ergebnisse in einem dynamischen Array-Format zurückgeben können.
Zusammenfassend lässt sich sagen, dass dynamische Array-Formeln eine modernere und bequemere Möglichkeit sind, mit Arrays in Excel zu arbeiten, da sie eine automatische Ausgabe von Ergebnissen ermöglichen und die Arbeit mit Arrays im Vergleich zu herkömmlichen Array-Formeln vereinfachen. Sie sind jedoch nur in den neueren Versionen von Excel verfügbar, die dynamische Arrays unterstützen.

##  **So legen Sie dynamische Array-Formeln in Excel fest und berechnen sie**
 Das Einrichten dynamischer Array-Formeln in Excel erfordert die Verwendung spezifischer Funktionen, die für die Arbeit mit Daten-Arrays konzipiert sind und es ermöglichen, dass die Ergebnisse automatisch in benachbarte Zellen übertragen werden.

Hier ist eine Schritt-für-Schritt-Anleitung zum Einrichten dynamischer Array-Formeln:
1. Wählen Sie die Cell:
<br>
Wählen Sie die Zelle aus, in der die Ergebnisse der dynamischen Array-Formel angezeigt werden sollen. Bei dynamischen Array-Formeln werden die Ergebnisse in benachbarte Zellen verteilt. Stellen Sie daher sicher, dass genügend Platz für die verschüttete Ausgabe vorhanden ist.
1. Geben Sie die Formel ein:
<br>
Geben Sie die dynamische Array-Formel in die Bearbeitungsleiste der ausgewählten Zelle ein. Verwenden Sie eine der in Excel 365 und Excel 2021 verfügbaren dynamischen Array-Funktionen, z. B. *FILTER**, *SORT**, *UNIQUE**, *SEQUENCE**, *SORTBY** oder *RANDARRAY**.
<br>
Beispielsweise könnten Sie die FILTER-Funktion verwenden, um eine Liste von Daten basierend auf bestimmten Kriterien zu filtern: *=FILTER(A2:C15,(A2:A15=F4)*(C2:C15=G4),"")**.
<br>
<image src="3.png" width="70%" />
<br>
1. Drücken Sie Enter:
<br>
Nachdem Sie die Formel eingegeben haben, drücken Sie einfach die Eingabetaste auf Ihrer Tastatur. Im Gegensatz zu herkömmlichen Array-Formeln müssen Sie nicht Strg + Umschalt + Eingabetaste drücken.
1. Beachten Sie die verschüttete Reichweite:
<br>
Excel verteilt die Ergebnisse der Formel automatisch in benachbarte Zellen. Der verschüttete Bereich passt sich dynamisch an, basierend auf der Größe der Ausgabedaten oder der von der Formel durchgeführten Berechnung. Excel hebt den verschütteten Bereich mit einem Rahmen und einem diagonalen Pfeilsymbol hervor, um anzuzeigen, dass er verschüttete Daten enthält.
1. Interagieren Sie mit der verschütteten Reichweite:
<br>
Sie können mit dem verschütteten Bereich wie mit jedem anderen Zellbereich in Excel interagieren. Verwenden Sie den verschütteten Bereich in anderen Formeln, führen Sie Berechnungen damit durch, formatieren Sie ihn oder referenzieren Sie ihn in Diagrammen oder Tabellen.
1. Aktualisieren Sie die Formel:
<br>
Wenn Sie die dynamische Array-Formel ändern müssen, bearbeiten Sie die Formel einfach in der ursprünglichen Zelle, in die sie eingegeben wurde.
Drücken Sie nach der Bearbeitung erneut die Eingabetaste, um die Änderungen zu bestätigen. Excel aktualisiert den verschütteten Bereich bei Bedarf automatisch.
1. Löschen des verschütteten Bereichs:
<br>
Wenn Sie die verschütteten Daten löschen möchten, können Sie die Formel aus der Originalzelle löschen. Excel löscht auch den übergelaufenen Bereich. Alternativ können Sie den übergelaufenen Bereich auch direkt löschen, indem Sie ihn auswählen und die Entf-Taste drücken.
<br>

Wenn Sie diese Schritte befolgen, können Sie dynamische Array-Formeln in Excel einrichten, um Arrays von Daten effizient zu analysieren und zu bearbeiten, was eine einfachere Datenanalyse und Berichtsaufgaben ermöglicht.

##  **So legen Sie dynamische Array-Formeln mit Aspose.Cells fest und aktualisieren sie**
 Bitte sehen Sie sich den folgenden Beispielcode an, der das lädt[Beispiel-Excel-Datei](dynamicArrayFormula.xlsx)die einige Dummy-Daten enthält. Rufen Sie nach dem Laden der Datei die auf[Cell.SetDynamicArrayFormula](https://reference.aspose.com/cells/net/aspose.cells/cell/setdynamicarrayformula/#setdynamicarrayformula)Funktion zum Festlegen einer dynamischen Array-Formel und[Workbook.RefreshDynamicArrayFormulas](https://reference.aspose.com/cells/net/aspose.cells/workbook/refreshdynamicarrayformulas/#refreshdynamicarrayformulas) Funktion zum Aktualisieren dynamischer Array-Formeln vor dem Aufrufen der Formelberechnung und zum abschließenden Speichern der Arbeitsmappe unter[Excel-Datei ausgeben](out.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-dynamic-array-formulas.cs" >}}

Der Ausgabe-Snapshot:
<br>
<image src="4.png" width="70%" />