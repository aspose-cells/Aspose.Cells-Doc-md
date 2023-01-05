---
title: Skapa, manipulera eller ta bort scenarier från arbetsblad
linktitle: Hantera scenarier
type: docs
weight: 190
url: /sv/net/create-manipulate-or-remove-scenarios-from-worksheets/
---
{{% alert color="primary" %}}

Ibland behöver du skapa, manipulera eller ta bort scenarier i kalkylblad. Ett scenario är ett namngivet "tänk om?" modell som inkluderar variabla indataceller länkade med en eller flera formler. Innan du skapar ett scenario, utforma kalkylbladet så att det innehåller minst en formel som beror på celler som olika värden kan infogas i. Följande exempel visar hur du skapar och tar bort scenarier från ett kalkylblad i en arbetsbok via Aspose.Cells API:er.

{{% /alert %}}

Aspose.Cells tillhandahåller några användbara klasser, till exempel,[**ScenarioCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenariocollection), [**Scenario**](https://reference.aspose.com/cells/net/aspose.cells/scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcellcollection) , och[**ScenarioInputCell**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcell) klasser. Det ger också[**Arbetsblad. Scenarier**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/scenarios)fast egendom. Exempelkoden nedan öppnar en XLSX Excel-fil som innehåller några scenarier och tar bort ett befintligt scenario. Det lägger också till ett nytt scenario i kalkylbladet innan Excel-filen sparas. Exemplet använder en mycket enkel mallfil som innehåller ett scenario.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateManipulateRemoveScenarios-1.cs" >}}
