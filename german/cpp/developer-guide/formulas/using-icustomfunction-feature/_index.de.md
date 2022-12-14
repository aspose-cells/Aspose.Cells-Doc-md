---
title: Verwenden der ICustomFunction-Funktion
type: docs
weight: 20
url: /de/cpp/using-icustomfunction-feature/
---
## **Einführung**
In diesem Artikel erfahren Sie, wie Sie das Feature ICustomFunction verwenden, um benutzerdefinierte Funktionen mit Aspose.Cells-APIs zu implementieren.

Mit der ICustomFunction-Schnittstelle können Sie benutzerdefinierte Formelberechnungsfunktionen hinzufügen, um die Kernberechnungs-Engine Aspose.Cells zu erweitern und bestimmte Anforderungen zu erfüllen. Diese Funktion ist nützlich, um benutzerdefinierte (benutzerdefinierte) Funktionen in einer Vorlagendatei oder in einem Code zu definieren, in dem die benutzerdefinierte Funktion mithilfe von Aspose.Cells-APIs wie jede andere standardmäßige Microsoft-Excel-Funktion implementiert und ausgewertet werden kann.
## **Verwenden der ICustomFunction-Funktion**
Der folgende Beispielcode implementiert die ICustomFunction-Schnittstelle, die die Werte der beiden benutzerdefinierten Funktionen, dh MySampleFunc() und YourSampleFunc(), auswertet und zurückgibt. Diese benutzerdefinierten Funktionen befinden sich jeweils in den Zellen A1 und A2. Anschließend wird die IWorkbook.CalculateFormula(false, ICustomFunction)-Methode aufgerufen, um die Implementierung der ICustomFunction.CalculateCustomFunction()-Methode aufzurufen. Dann druckt es die Werte von A1 und A2 auf der Konsole, die tatsächlich die von ICustomFunction.CalculateCustomFunction() zurückgegebenen Werte sind. Weitere Hilfe finden Sie in der Konsolenausgabe des Beispielcodes unten.
## **Beispielcode**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingICustomFunctionFeature.cpp" >}}


## **Konsolenausgabe**
{{< highlight "java" >}}

 Value of A1: MY sample function was called successfully.

Value of A2: YOUR sample function was called successfully.

{{< /highlight >}}
