---
title: Zurückgeben eines Wertebereichs mit ICustomFunction
type: docs
weight: 50
url: /de/net/returning-a-range-of-values-using-icustomfunction/
---
{{% alert color="primary" %}}

 Das[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) ist seit der Veröffentlichung von Aspose.Cells veraltet for Java 20.8. Bitte verwenden Sie die[**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) Klasse. Die Verwendung der[**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) Klasse wird im folgenden Artikel beschrieben.

[Zurückgeben eines Wertebereichs mit AbstractCalculationEngine](/cells/de/net/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

 Aspose.Cells bietet[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)Schnittstelle, die verwendet wird, um benutzerdefinierte oder benutzerdefinierte Funktionen zu implementieren, die von Microsoft Excel nicht als integrierte Funktionen unterstützt werden.

 Meistens, wenn Sie die implementieren[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) -Schnittstellenmethode müssen Sie einen einzelnen Zellenwert zurückgeben. Aber manchmal müssen Sie einen Wertebereich zurückgeben. In diesem Artikel wird erläutert, wie Sie den Wertebereich zurückgeben[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{% /alert %}}

 Der folgende Code implementiert[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)und gibt den Wertebereich über seine Methode zurück.

 Erstellen Sie eine Klasse mit einer Funktion*Benutzerdefinierte Funktion berechnen*. Diese Klasse implementiert[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-CustomFunctionStaticValue.cs" >}}

Verwenden Sie nun obige Funktion in Ihrem Programm

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-1.cs" >}}
