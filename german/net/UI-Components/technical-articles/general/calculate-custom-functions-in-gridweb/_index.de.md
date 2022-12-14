---
title: Berechnen Sie benutzerdefinierte Funktionen in GridWeb
type: docs
weight: 90
url: /de/net/calculate-custom-functions-in-gridweb/
---
## **Mögliche Nutzungsszenarien**
Aspose.Cells. GridWeb unterstützt die Berechnung benutzerdefinierter Funktionen mit der Eigenschaft GridWeb.CustomCalculationEngine. Diese Eigenschaft übernimmt die Instanz der GridAbstractCalculationEngine-Schnittstelle. Bitte implementieren Sie die GridAbstractCalculationEngine-Schnittstelle und berechnen Sie Ihre benutzerdefinierten Funktionen mit Ihrer eigenen Logik.
## **Berechnen Sie benutzerdefinierte Funktionen in GridWeb**
Der folgende Beispielcode fügt eine benutzerdefinierte Funktion namens MYTESTFUNC() in Zelle B3 hinzu. Dann berechnen wir den Wert dieser Funktion, indem wir die Schnittstelle GridAbstractCalculationEngine implementieren. Wir berechnen MYTESTFUNC() so, dass es seinen Parameter mit 2 multipliziert und das Ergebnis zurückgibt. Wenn sein Parameter also 9 ist, wird 2*9 = 18 zurückgegeben.
### **Beispielcode**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-CalculateCustomFunction.aspx-CalculateCustomFunction.cs" >}}
