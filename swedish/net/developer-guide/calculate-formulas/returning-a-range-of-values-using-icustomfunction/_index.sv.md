---
title: Returnera ett värdeintervall med ICustomFunction
type: docs
weight: 50
url: /sv/net/returning-a-range-of-values-using-icustomfunction/
---
{{% alert color="primary" %}}

 De[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) är utfasad sedan lanseringen av Aspose.Cells för Java 20.8. Vänligen använd[**AbstractCalculation Engine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) klass. Användningen av[**AbstractCalculation Engine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) klass beskrivs i följande artikel.

[Returnera ett värdeintervall med AbstractCalculationEngine](/cells/sv/net/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

 Aspose.Cells tillhandahåller[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)gränssnitt som används för att implementera användardefinierade eller anpassade funktioner som inte stöds av Microsoft Excel som inbyggda funktioner.

 Mest när du implementerar[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) gränssnittsmetod måste du returnera ett enskilt cellvärde. Men ibland måste du returnera en rad värden. Den här artikeln kommer att förklara hur du returnerar värdeintervallet från[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{% /alert %}}

 Följande kod implementerar[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)och returnerar värdeintervallet via sin metod.

Skapa en klass med en funktion*CalculateCustomFunction*. Denna klass implementerar[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-CustomFunctionStaticValue.cs" >}}

Använd nu ovanstående funktion i ditt program

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-1.cs" >}}
