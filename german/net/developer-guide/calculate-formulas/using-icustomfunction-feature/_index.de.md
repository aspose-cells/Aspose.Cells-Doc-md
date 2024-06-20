---
title: Verwendung der ICustomFunction Funktion
description: Dieser Artikel beschreibt, wie man eine benutzerdefinierte Funktion in Microsoft Excel mithilfe des ICustomFunction Features in der Aspose.Cells Bibliothek erstellt. Durch Laden einer vorhandenen Excel Datei oder Erstellen einer neuen Excel Datei können wir die von Aspose.Cells bereitgestellten Methoden verwenden, um benutzerdefinierte Funktionen zu definieren und zu registrieren und die Ergebnisse zu erhalten. Schließlich speichern wir die modifizierte Excel Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, ICustomFunction Features, benutzerdefinierte Funktionen
type: docs
weight: 30
url: /de/net/using-icustomfunction-feature/
---

{{% alert color="primary" %}} 

Dieser Artikel bietet eine ausführliche Erklärung zur Verwendung des ICustomFunction-Features zur Implementierung benutzerdefinierter Funktionen mit Aspose.Cells-APIs.

Die ICustomFunction-Schnittstelle ermöglicht die Hinzufügung benutzerdefinierter Formelberechnungsfunktionen, um den Kernberechnungsmotor von Aspose.Cells zu erweitern, um bestimmte Anforderungen zu erfüllen. Diese Funktion ist nützlich, um benutzerdefinierte Funktionen in einer Vorlagendatei oder im Code zu definieren, wo die benutzerdefinierte Funktion mit Aspose.Cells-APIs wie jede andere Standard-Microsoft Excel-Funktion implementiert und ausgewertet werden kann.

Bitte beachten Sie, dass diese Schnittstelle durch [AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/) ersetzt wurde und in Zukunft entfernt wird. Einige technische Artikel/Beispiele zu der neuen API: [hier](/cells/de/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) und [hier](/cells/de/net/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} 
## **Erstellen und Auswerten einer benutzerdefinierten Funktion**
Dieser Artikel demonstriert die Implementierung der ICustomFunction-Schnittstelle, um eine benutzerdefinierte Funktion zu schreiben und sie in der Tabellenkalkulation zu verwenden, um die Ergebnisse zu erhalten. Wir definieren eine benutzerdefinierte Funktion namens **MyFunc**, die 2 Parameter mit folgenden Details akzeptiert.

- Der erste Parameter bezieht sich auf eine einzelne Zelle
- Der zweite Parameter bezieht sich auf einen Zellenbereich

Die benutzerdefinierte Funktion wird alle Werte aus dem als 2. Parameter angegebenen Zellbereich addieren und das Ergebnis durch den Wert im 1. Parameter dividieren.

Hier ist, wie wir die Methode CalculateCustomFunction implementiert haben.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


So verwenden Sie die neu definierte Funktion in einer Tabellenkalkulation



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
## **Übersicht**
Die Aspose.Cells-APIs legen den ReferredArea-Objekt in die "paramsList", wenn der entsprechende Parameter eine Referenz ist oder sein berechnetes Ergebnis eine Referenz ist. Wenn Sie die Referenz selbst benötigen, können Sie direkt die ReferredArea verwenden. Wenn Sie den Wert einer einzelnen Zelle aus der Referenz benötigen, die der Position der Formel entspricht, können Sie die Methode ReferredArea.GetValue(rowOffset, int colOffset) verwenden. Wenn Sie die Zellwerte für den gesamten Bereich benötigen, können Sie die Methode ReferredArea.GetValues verwenden.

Da die Aspose.Cells-APIs die ReferredArea in "paramsList" erhalten, wird die ReferredAreaCollection in "contextObjects" nicht mehr benötigt (in älteren Versionen konnte sie nicht immer eine eins-zu-eins-Mapping zu den Parametern der benutzerdefinierten Funktion erstellen), daher wurde sie aus den "contextObjects" entfernt.

{{< highlight java >}}

 public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    object o = paramsList[i];

    if(o is ReferredArea) //fetch data from reference

    {

        ReferredArea ra = (ReferredArea)o;

        if(ra.IsArea)

        {

            o = ra.GetValues();

        }

        else

        {

            o = ra.GetValue(0, 0);

        }

    }

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}
