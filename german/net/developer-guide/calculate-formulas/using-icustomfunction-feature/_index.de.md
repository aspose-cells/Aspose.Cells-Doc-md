---
title: Verwenden der ICustomFunction-Funktion
description: In diesem Artikel wird beschrieben, wie Sie mithilfe der ICustomFunction-Funktion in der Aspose.Cells-Bibliothek eine benutzerdefinierte Funktion in Microsoft Excel erstellen. Durch das Laden einer vorhandenen Excel-Datei oder das Erstellen einer neuen Excel-Datei können wir die von Aspose.Cells bereitgestellten Methoden verwenden, um benutzerdefinierte Funktionen zu definieren und zu registrieren und die Ergebnisse zu erhalten. Abschließend speichern wir die geänderte Excel-Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, ICustomFunction features, custom functions
type: docs
weight: 30
url: /de/net/using-icustomfunction-feature/
---
{{% alert color="primary" %}} 

Dieser Artikel bietet detaillierte Informationen zur Verwendung der ICustomFunction-Funktion zum Implementieren benutzerdefinierter Funktionen mit Aspose.Cells-APIs.

Die ICustomFunction-Schnittstelle ermöglicht das Hinzufügen benutzerdefinierter Formelberechnungsfunktionen zur Erweiterung der Aspose.Cells'-Kernberechnungs-Engine, um bestimmte Anforderungen zu erfüllen. Diese Funktion ist nützlich, um benutzerdefinierte (benutzerdefinierte) Funktionen in einer Vorlagendatei oder in Code zu definieren, wobei die benutzerdefinierte Funktion mithilfe von Aspose.Cells-APIs wie jede andere Standard-Excel-Funktion Microsoft implementiert und ausgewertet werden kann.

 Bitte beachten Sie, dass diese Schnittstelle durch ersetzt wurde[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/) und wird in Zukunft entfernt. Einige Fachartikel/Beispiele zur neuen API:[Hier](/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) Und[Hier](/net/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} 
##  **Erstellen und Auswerten einer benutzerdefinierten Funktion**
 Dieser Artikel demonstriert die Implementierung der ICustomFunction-Schnittstelle zum Schreiben einer benutzerdefinierten Funktion und deren Verwendung in der Tabelle, um die Ergebnisse zu erhalten. Wir werden eine benutzerdefinierte Funktion nach Namen definieren**MyFunc** welches 2 Parameter mit folgenden Details akzeptiert.

- Der 1. Parameter bezieht sich auf eine einzelne Zelle
- Der 2. Parameter bezieht sich auf einen Zellbereich

Die benutzerdefinierte Funktion addiert alle Werte aus dem als 2. Parameter angegebenen Zellbereich und dividiert das Ergebnis durch den Wert im 1. Parameter.

So haben wir die CalculateCustomFunction-Methode implementiert.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


Hier erfahren Sie, wie Sie die neu definierte Funktion in einer Tabellenkalkulation verwenden



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
##  **Überblick**
Die Aspose.Cells-APIs fügen das ReferredArea-Objekt einfach in die „paramsList“ ein, wenn der entsprechende Parameter eine Referenz oder sein berechnetes Ergebnis eine Referenz ist. Wenn Sie die Referenz selbst benötigen, können Sie die ReferredArea direkt verwenden. Wenn Sie den Wert einer einzelnen Zelle aus der Referenz abrufen müssen, die der Position der Formel entspricht, können Sie die Methode ReferredArea.GetValue(rowOffset, int colOffset) verwenden. Wenn Sie ein Array mit Zellwerten für den gesamten Bereich benötigen, können Sie die Methode „ReferredArea.GetValues“ verwenden.

Da die Aspose.Cells-APIs die ReferredArea in „paramsList“ angeben, wird die ReferredAreaCollection in „contextObjects“ nicht mehr benötigt (in alten Versionen war es nicht immer möglich, den Parametern der benutzerdefinierten Funktion eine Eins-zu-eins-Zuordnung zu geben), daher ist dies der Fall wurde aus den „contextObjects“ entfernt.

{{< highlight "java" >}}

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
