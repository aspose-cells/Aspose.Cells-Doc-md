---
title: Rückgabe eines Wertebereichs unter Verwendung von AbstractCalculationEngine mit Golang über C++
linktitle: Rückgabe eines Wertebereichs unter Verwendung des abstrakten Berechnungsmotors
description: Dieser Artikel stellt eine abstrakte Berechnungs Engine vor, die in Microsoft Excel einen Wertebereich zurückgibt, mithilfe der Aspose.Cells Bibliothek mit Golang über C++. Durch das Laden einer bestehenden Excel Datei oder das Erstellen einer neuen Excel Datei können wir die von Aspose.Cells bereitgestellten Methoden verwenden, um einen Wertebereich zu erhalten und das Ergebnis zurückzugeben. Schließlich speichern wir die bearbeitete Excel Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, ein abstrakter Berechnungsmotor, der eine Reihe von Werten zurückgibt
type: docs
weight: 55
url: /de/go-cpp/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells bietet die Klasse [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/), die verwendet wird, um benutzerdefinierte Funktionen zu implementieren, die nicht von Microsoft Excel als integrierte Funktionen unterstützt werden.

In diesem Artikel wird erläutert, wie der Wertebereich von [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/) zurückgegeben wird.

{{% /alert %}}

 Der folgende Code zeigt die Verwendung der Klasse [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/) und gibt den Wertebereich über ihre Methode zurück.

 Erstellen Sie eine Klasse mit einer Funktion `CalculateCustomFunction`. Diese Klasse implementiert [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReturningARangeOfValuesUsingAbstractcalculationengine.go" >}}
 Jetzt verwenden Sie die oben genannte Funktion in Ihrem Programm.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReturningARangeOfValuesUsingAbstractcalculationengine-1.go" >}}
