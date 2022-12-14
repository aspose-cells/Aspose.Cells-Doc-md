---
title: Spara varje kalkylblad till en annan PDF-fil
type: docs
weight: 130
url: /sv/net/save-each-worksheet-to-a-different-pdf-file/
---
{{% alert color="primary" %}} 

Aspose.Cells stöder konvertering av XLS-filer (som innehåller bilder, diagram, etc.) till PDF-dokument. Aspose.Cells för .NET kan arbeta oberoende för att konvertera ett kalkylblad till PDF och du behöver inte använda Aspose.PDF för .NET för konverteringen. Konverteringen kräver inte att programvaran skapar eller använder några temporära filer eftersom hela processen kan göras i minnet.

{{% /alert %}} 
## **Spara varje kalkylblad till en annan PDF-fil**
Om du behöver spara varje kalkylblad i din Excel-mall för att generera olika PDF-filer kan du enkelt uppnå detta. Du kan försöka gömma ark i filen och göra ett ark synligt i taget för att rendera till PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SaveEachWorksheetToDifferentPDF-1.cs" >}}

{{% alert color="primary" %}} 

 Om ditt kalkylblad innehåller formler är det bäst att ringa[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) precis innan du renderar kalkylarket till PDF-format. Om du gör det säkerställer du att de formelberoende värdena räknas om och att de korrekta värdena återges i PDF-filen.

{{% /alert %}}
