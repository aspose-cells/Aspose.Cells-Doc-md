---
title: Wege zur Berechnung von Formeln
type: docs
weight: 30
url: /de/go-cpp/ways-to-calculate-formulas/
---

## **Einführung**

Aspose.Cells verfügt über einen integrierten Formelberechnungsmotor. Es kann nicht nur Formeln, die aus Designer-Vorlagen importiert wurden, neu berechnen, sondern unterstützt auch das Berechnen der Ergebnisse von Formeln, die zur Laufzeit hinzugefügt wurden.

## **Hinzufügen von Formeln & Berechnen von Ergebnissen**

Aspose.Cells unterstützt die meisten Formeln oder Funktionen, die Teil von Microsoft Excel sind. Sie können über die API oder über Designer-Tabellenkalkulationstabellen verwendet werden. Aspose.Cells unterstützt eine große Menge mathematischer, string, boolescher, Datum/Uhrzeit-, statistischer, Such- und Bezugsformeln.

Verwenden Sie die Cell.SetFormula-Methode, um einer Zelle eine Formel hinzuzufügen. Beim Anwenden einer Formel auf eine Zelle sollten Sie die Zeichenfolge immer mit einem Gleichheitszeichen (=) beginnen, wie Sie es bei der Erstellung einer Formel in Microsoft Excel tun. Verwenden Sie ein Komma (,) zur Trennung der Funktionsparameter.

Um die Ergebnisse von Formeln zu berechnen, rufen Sie die Workbook.CalculateFormula()-Methode auf, die alle in einer Excel-Datei eingebetteten Formeln verarbeitet. Bitte beachten Sie den folgenden Beispielcode, der die Formel hinzufügt und ihre Ergebnisse berechnet. Bitte überprüfen Sie die [ausgegebene Excel-Datei](38109185.xlsx), die mit diesem Code generiert wurde.

**Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingFormulasAndCalculatingResults.go" >}}

## **Einmaliges Berechnen von Formeln**

Wenn Workbook.CalculateFormula() aufgerufen wird, um die Werte von Formeln in einer Arbeitsmappen-Vorlage zu berechnen, erstellt Aspose.Cells eine Berechnungskette. Dies erhöht die Leistung, wenn Formeln das zweite oder dritte Mal berechnet werden.

Wenn die Vorlage jedoch viele Formeln enthält, kann das erste Mal, wenn die Formel berechnet wird, viel CPU-Verarbeitungszeit und Speicher in Anspruch nehmen.

Aspose.Cells ermöglicht es Ihnen, das Erstellen einer Berechnungskette auszuschalten, was nützlich ist, wenn Sie Formeln nur einmal berechnen möchten.

Bitte rufen Sie Workbook.GetISettings().SetCreateCalcChain() mit dem Parameter false auf. Sie können die [bereitgestellte Excel-Datei](38109186.xlsx) verwenden, um diesen Code zu testen.

**Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculatingFormulasOnceOnly.go" >}}
