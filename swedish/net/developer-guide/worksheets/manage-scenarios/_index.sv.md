---
title: Skapa, manipulera eller ta bort scenarier från arbetsblad
linktitle: Hantera scenarier
type: docs
weight: 190
url: /sv/net/create-manipulate-or-remove-scenarios-from-worksheets/
description: I den här artikeln lär du dig hur man skapar, manipulerar eller tar bort scenarier från Excel ark programmatiskt med C# bibliotek med .NET API.
keywords: skapa scenario ark c#, ta bort scenario excel ark c#, manipulera scenario ark c#
---

{{% alert color="primary" %}}

Ibland behöver du skapa, manipulera eller radera scenarier i kalkylblad. Ett scenario är en namngiven 'vad om?'-modell som inkluderar variabelindataceller kopplade av en eller flera formler. Innan scenariot skapas, utforma kalkylbladet så att det innehåller minst en formel som beror på celler där olika värden kan sättas in. Följande exempel visar hur man skapar och tar bort scenarier från ett kalkylblad i en arbetsbok via Aspose.Cells-API:  

{{% /alert %}}

Aspose.Cells tillhandahåller några användbara klasser, till exempel [**ScenarioCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenariocollection), [**Scenario**](https://reference.aspose.com/cells/net/aspose.cells/scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcellcollection), och [**ScenarioInputCell**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcell) klasser. Det tillhandahåller också egenskapen [**Worksheet.Scenarios**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/scenarios). Exempelkoden nedan öppnar en XLSX Excel-fil som innehåller några scenarier och tar bort ett befintligt scenario. Det lägger också till ett nytt scenario i kalkylbladet före att spara Excel-filen. Exemplet använder en mycket enkel mallfil som innehåller ett scenario.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateManipulateRemoveScenarios-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
