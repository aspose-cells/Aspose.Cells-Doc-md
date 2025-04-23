---
title: Rückgabe eines Wertebereichs unter Verwendung von ICustomFunction
type: docs
weight: 270
url: /de/java/returning-a-range-of-values-using-icustomfunction/
---

{{% alert color="primary" %}}

Das [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) ist seit der Veröffentlichung von Aspose.Cells for Java 20.8 veraltet. Bitte verwenden Sie die Klasse [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine). Die Verwendung der Klasse [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) wird in folgendem Artikel beschrieben.

[Rückgabe eines Wertebereichs unter Verwendung von AbstractCalculationEngine](/cells/de/java/rueckgabe-eines-wertebereichs-unter-verwendung-von-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cells bietet die Schnittstelle [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction), die verwendet wird, um benutzerdefinierte Funktionen zu implementieren, die nicht von Microsoft Excel als integrierte Funktionen unterstützt werden.

Meistens, wenn Sie die Methode der Schnittstelle [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) implementieren, müssen Sie einen einzelnen Zellwert zurückgeben. Manchmal müssen jedoch Wertebereiche zurückgegeben werden. Dieser Artikel erläutert, wie der Wertebereich von [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) zurückgegeben wird.

{{% /alert %}}

## **Rückgabe eines Wertebereichs mit ICustomFunction**

Der folgende Code implementiert [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) und gibt den Wertebereich über seine Methode zurück. Überprüfen Sie die [erstellte Exceldatei](5472922.xlsx) und das [pdf](5472925.pdf), die mit dem Code generiert wurden, als Referenz.

Erstellen Sie eine Klasse mit einer Funktion *CalculateCustomFunction*. Diese Klasse implementiert [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

Verwenden Sie die obige Funktion jetzt in Ihrem Programm.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReturningRangeOfValues-ReturningRangeOfValues.java" >}}
{{< app/cells/assistant language="java" >}}
