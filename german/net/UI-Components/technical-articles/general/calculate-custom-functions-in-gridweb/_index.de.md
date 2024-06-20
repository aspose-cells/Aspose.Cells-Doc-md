---
title: Benutzerdefinierte Funktionen in GridWeb berechnen
type: docs
weight: 90
url: /de/net/aspose-cells-gridweb/calculate-custom-functions-in-gridweb/
keywords: GridWeb,custom functions,custom,function
description: Dieser Artikel stellt Funktionen benutzerdefinierter Funktionen in GridWeb vor.
---


## **Mögliche Verwendungsszenarien**
Aspose.Cells.GridWeb unterstützt die Berechnung von benutzerdefinierten Funktionen mit der Eigenschaft GridWeb.CustomCalculationEngine. Diese Eigenschaft nimmt die Instanz des GridAbstractCalculationEngine-Interfaces. Bitte implementieren Sie das GridAbstractCalculationEngine-Interface und berechnen Sie Ihre benutzerdefinierten Funktionen mit Ihrer eigenen Logik.
## **Berechnen von benutzerdefinierten Funktionen in GridWeb**
Der folgende Beispielcode fügt eine benutzerdefinierte Funktion mit dem Namen MYTESTFUNC() in Zelle B3 hinzu. Dann berechnen wir den Wert dieser Funktion, indem wir das GridAbstractCalculationEngine-Interface implementieren. Wir berechnen MYTESTFUNC() so, dass es seinen Parameter mit 2 multipliziert und das Ergebnis zurückgibt. Wenn sein Parameter also 9 ist, wird es 2*9 = 18 zurückgeben.
### **Beispielcode**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-CalculateCustomFunction.aspx-CalculateCustomFunction.cs" >}}
