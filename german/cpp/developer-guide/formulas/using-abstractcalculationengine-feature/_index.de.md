---
title: Verwendung der AbstractCalculationEngine Funktion
type: docs
weight: 20
url: /de/cpp/using-abstractcalculationengine-feature/
---


## **Einführung**
Dieser Artikel bietet ein Verständnis dafür, wie Sie die [AbstractCalculationEngine](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/) Funktion verwenden können, um benutzerdefinierte Funktionen mit den Aspose.Cells APIs zu implementieren.

Die AbstractCalculationEngine-Schnittstelle ermöglicht es Ihnen, benutzerdefinierte Formelberechnungsfunktionen hinzuzufügen, um den Aspose.Cells-Kernberechnungsmotor zu erweitern, um bestimmte Anforderungen zu erfüllen. Diese Funktion ist nützlich, um benutzerdefinierte Funktionen in einer Vorlagendatei oder in einem Code zu definieren, in dem die benutzerdefinierte Funktion mit Aspose.Cells APIs implementiert und bewertet werden kann, wie eine andere Standard-Microsoft Excel-Funktion.

## **Verwendung der AbstractCalculationEngine-Funktion - 1**

Der folgende Beispielcode implementiert die AbstractCalculationEngine-Schnittstelle, die die Werte der beiden benutzerdefinierten Funktionen MySampleFunc() und YourSampleFunc() bewertet und zurückgibt. Diese benutzerdefinierten Funktionen sind in den Zellen A1 und A2 enthalten. Dann ruft es die Workbook.CalculateFormula(const CalculationOptions& options) Methode auf, um die Implementierung der AbstractCalculationEngine .Calculate(CalculationData& data) Methode aufzurufen. Dann druckt es die Werte von A1 und A2 auf der Konsole aus. Bitte beachten Sie die Konsolenausgabe des Beispielcodes unten für mehr Hilfe.

## **Beispielcode**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingAbstractCalculationEngine.cpp" >}}


## **Konsolenausgabe**
{{< highlight java >}}

MySampleFunc-Test called successfully.
YourSampleFunc-Test called successfully.
Value of A1 is : 1
Value of A2 is : 2

{{< /highlight >}}

## **Verwendung der AbstractCalculationEngine-Funktion - 2**

Der folgende Beispielcode liest eine benutzerdefinierte Funktion aus einer Beispiel-Datei und ruft die Methode Workbook.CalculateFormula(const CalculationOptions& options) auf, um die Methode AbstractCalculationEngine .Calculate(CalculationData& data) für die weitere Verarbeitung aufzurufen.

Beispiel-Datei: [sample-file.xlsx](sample-file.xlsx)

## **Beispielcode**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingAbstractCalculationEngine2.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
