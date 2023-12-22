---
title: Hantera sidbrytningar
type: docs
weight: 30
url: /sv/cpp/managing-page-breaks/
---
{{% alert color="primary" %}} 

Enligt definitionen är en sidbrytning en plats i ett textflöde där en sida slutar och nästa börjar. Microsoft Excel låter användare lägga till sidbrytningar i valfri vald cell i ett kalkylblad.

Platsen för cellen där sidbrytningen läggs till, sidan är avslutad och all övrig data efter sidbrytningen skrivs ut på nästa sida under utskrift. Med enkla ord delar sidbrytningar upp ditt kalkylblad i flera sidor enligt dina specifikationer. Du kan också lägga till sidbrytningar till dina kalkylblad under körning med Aspose.Cells. Aspose.Cells tillåter utvecklare att lägga till två typer av sidbrytningar:

- Horisontell sidbrytning
- Vertikal sidbrytning

I resten av diskussionen kommer vi att beskriva hur du kan lägga till horisontella eller vertikala sidbrytningar i dina kalkylblad med Aspose.Cells.

{{% /alert %}} 
##  **Sidbrytningar**
 Aspose.Cells tillhandahåller en klass[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) som representerar en Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) klass innehåller en[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection)samling som ger åtkomst till varje kalkylblad i Excel-filen.

Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klass. De[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)klass tillhandahåller ett brett utbud av metoder som används för att hantera ett kalkylblad. För att lägga till sidbrytningar, använd[AddPageBreaks](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/addpagebreaks) metod för[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)klass.
###  **Lägga till sidbrytningar**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManagingPageBreaks-AddingPageBreaks-new.cpp" >}}
