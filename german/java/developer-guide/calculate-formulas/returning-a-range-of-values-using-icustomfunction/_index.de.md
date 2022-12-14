---
title: Zurückgeben eines Wertebereichs mit ICustomFunction
type: docs
weight: 270
url: /de/java/returning-a-range-of-values-using-icustomfunction/
---
{{% alert color="primary" %}}

 Das[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) ist seit der Veröffentlichung von Aspose.Cells veraltet for Java 20.8. Bitte verwenden Sie die[**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) Klasse. Die Verwendung der[**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) Klasse wird im folgenden Artikel beschrieben.

[Zurückgeben eines Wertebereichs mit AbstractCalculationEngine](/cells/de/java/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

 Aspose.Cells bietet[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)Schnittstelle, die verwendet wird, um benutzerdefinierte oder benutzerdefinierte Funktionen zu implementieren, die von Microsoft Excel nicht als integrierte Funktionen unterstützt werden.

 Meistens, wenn Sie die implementieren[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) -Schnittstellenmethode müssen Sie einen einzelnen Zellenwert zurückgeben. Aber manchmal müssen Sie einen Wertebereich zurückgeben. In diesem Artikel wird erläutert, wie Sie den Wertebereich zurückgeben[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{% /alert %}}

## **Zurückgeben eines Wertebereichs mit ICustomFunction**

 Der folgende Code implementiert[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) und gibt den Wertebereich über seine Methode zurück. Bitte überprüfen Sie die[Excel-Datei ausgeben](5472922.xlsx) und[pdf](5472925.pdf) generiert mit dem Code für Ihre Referenz.

Erstellen Sie eine Klasse mit einer Funktion*Benutzerdefinierte Funktion berechnen*. Diese Klasse implementiert[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

Verwenden Sie nun die obige Funktion in Ihrem Programm.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReturningRangeOfValues-ReturningRangeOfValues.java" >}}
