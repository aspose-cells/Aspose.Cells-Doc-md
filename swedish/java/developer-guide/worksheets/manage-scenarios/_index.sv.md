---
title: Skapa, manipulera eller ta bort scenarier från arbetsblad
linktitle: Hantera scenarier
type: docs
weight: 120
url: /sv/java/create-manipulate-or-remove-scenarios-from-worksheets/
---
{{% alert color="primary" %}}

Ibland behöver du skapa, manipulera eller ta bort scenarier i kalkylblad. Ett scenario är en namngiven vad-om-modell som inkluderar variabla indataceller länkade samman av en eller flera formler. Innan du skapar ett scenario, utforma ett kalkylblad så att det innehåller minst en formel som beror på celler där olika värden kan infogas. Följande exempel visar hur du skapar och tar bort scenarier från ett kalkylblad med Aspose.Cells API:er.

{{% /alert %}}

 Aspose.Cells tillhandahåller några användbara klasser, till exempel[**ScenarioCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioCollection), [**Scenario**](https://reference.aspose.com/cells/java/com.aspose.cells/Scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCellCollection) och[**ScenarioInputCell**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCell) . Det ger också[**Arbetsblad. Scenarier**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Scenarios)fast egendom. Exempelkoden nedan öppnar en XLSX Excel-fil (som innehåller några scenarier) och tar bort ett befintligt scenario från kalkylbladet. Det lägger också till ett nytt scenario innan Excel-filen sparas. Den använder en mycket enkel mallfil som innehåller ett scenario.

Efter exekvering av koden tas ett befintligt scenario bort och ett nytt scenario läggs till i kalkylbladet.

**Utdatafilen**

![todo:image_alt_text](create-manipulate-or-remove-scenarios-from-worksheets_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateScenariosfromWorksheets-CreateScenariosfromWorksheets.java" >}}
