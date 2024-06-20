---
title: Returnera ett område av värden med hjälp av ICustomFunction
description: Den här artikeln beskriver hur du använder Aspose.Cells biblioteket för att returnera en serie värden med ICustomFunction i Microsoft Excel. Genom att ladda en befintlig Excel fil eller skapa en ny Excel fil kan vi använda metoder som tillhandahålls av Aspose.Cells för att få en serie värden och returnera resultatet. Slutligen sparar vi den modifierade Excel filen på disk.
keywords: Aspose.Cells, Excel, ICustomFunction, returnerar en serie värden
type: docs
weight: 50
url: /sv/net/returning-a-range-of-values-using-icustomfunction/
---

{{% alert color="primary" %}}

[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) klassen är nedlagd sedan versionen Aspose.Cells for Java 20.8. Använd istället [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) klassen. Användningen av [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) klassen beskrivs i följande artikel.

[Returnera ett värdeområde med hjälp av AbstractCalculationEngine](/cells/sv/net/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) gränssnitt som används för att implementera användardefinierade eller anpassade funktioner som inte stöds av Microsoft Excel som inbyggda funktioner.

Mestadels när du implementerar [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) gränssnittet metod, behöver du returnera ett enskilt cellvärde. Men ibland behöver du returnera ett område av värden. Den här artikeln kommer att förklara hur man returnerar en serie värden från [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{% /alert %}}

Följande kod implementerar [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) och returnerar värdeområdet via dess metod.

Skapa en klass med en funktion *CalculateCustomFunction*. Denna klass implementerar [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-CustomFunctionStaticValue.cs" >}}

Använd nu ovanstående funktion i ditt program.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-1.cs" >}}
