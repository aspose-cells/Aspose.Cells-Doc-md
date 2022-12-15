---
title: Verwenden der ICustomFunction-Funktion
type: docs
weight: 30
url: /de/net/using-icustomfunction-feature/
---
{{% alert color="primary" %}} 

Dieser Artikel bietet ein detailliertes Verständnis der Verwendung des ICustomFunction-Features zum Implementieren benutzerdefinierter Funktionen mit Aspose.Cells-APIs.

Die ICustomFunction-Schnittstelle ermöglicht es, benutzerdefinierte Formelberechnungsfunktionen hinzuzufügen, um die Kernberechnungsmaschine von Aspose.Cells zu erweitern, um bestimmte Anforderungen zu erfüllen. Diese Funktion ist nützlich, um benutzerdefinierte (benutzerdefinierte) Funktionen in einer Vorlagendatei oder im Code zu definieren, wobei die benutzerdefinierte Funktion mithilfe von Aspose.Cells-APIs wie jede andere Microsoft-Excel-Standardfunktion implementiert und ausgewertet werden kann.

{{% /alert %}} 
## **Erstellen und Auswerten einer benutzerdefinierten Funktion**
Dieser Artikel demonstriert die Implementierung der ICustomFunction-Schnittstelle, um eine benutzerdefinierte Funktion zu schreiben und sie in der Tabelle zu verwenden, um die Ergebnisse zu erhalten. Wir definieren eine benutzerdefinierte Funktion nach Namen**MeineFunk** die 2 Parameter mit folgenden Details akzeptiert.

- 1. Parameter bezieht sich auf eine einzelne Zelle
- 2. Parameter bezieht sich auf einen Bereich von Zellen

Die benutzerdefinierte Funktion addiert alle Werte aus dem als 2. Parameter angegebenen Zellbereich und dividiert das Ergebnis durch den Wert im 1. Parameter.

So haben wir die CalculateCustomFunction-Methode implementiert.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


So verwenden Sie die neu definierte Funktion in einer Tabellenkalkulation



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
## **Überblick**
Die Aspose.Cells-APIs fügen das ReferredArea-Objekt einfach in die „paramsList“ ein, wenn der entsprechende Parameter eine Referenz ist oder sein berechnetes Ergebnis eine Referenz ist. Wenn Sie die Referenz selbst benötigen, können Sie die ReferredArea direkt verwenden. Wenn Sie den Wert einer einzelnen Zelle aus der Referenz abrufen müssen, die der Position der Formel entspricht, können Sie die Methode ReferredArea.GetValue(rowOffset, int colOffset) verwenden. Wenn Sie ein Zellwerte-Array für den gesamten Bereich benötigen, können Sie die Methode ReferredArea.GetValues verwenden.

Da die Aspose.Cells-APIs die ReferredArea in "paramsList" angeben, wird die ReferredAreaCollection in "contextObjects" nicht mehr benötigt (in alten Versionen war es nicht möglich, den Parametern der benutzerdefinierten Funktion immer eine Eins-zu-Eins-Zuordnung zu geben), daher wurde aus den "contextObjects" entfernt.

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
