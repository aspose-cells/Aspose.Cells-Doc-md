---
title: Hantera sidbrytningar
type: docs
weight: 30
url: /sv/cpp/managing-page-breaks/
---

{{% alert color="primary" %}} 

Enligt definitionen är en sidbrytning en plats i en textflöde där en sida slutar och den nästa börjar. Microsoft Excel låter användare lägga till sidbrytningar i valfri markerad cell i ett kalkylblad.

Platsen för den cell där sidbrytningen läggs till, sidan avslutas och resten av data efter sidbrytningen skrivs ut på nästa sida vid utskrift. Med enkla ord delar sidbrytningarna upp ditt kalkylblad i flera sidor enligt dina specifikationer. Du kan också lägga till sidbrytningar till dina kalkylblad vid körning med hjälp av Aspose.Cells. Aspose.Cells tillåter utvecklare att lägga till två typer av sidbrytningar:

- Horisontell sidbrytning
- Vertikal sidbrytning

I resten av diskussionen kommer vi att beskriva hur du kan lägga till horisontella eller vertikala sidbrytningar i dina kalkylblad med hjälp av Aspose.Cells.

{{% /alert %}} 
## **Sidbrytningar**
Aspose.Cells tillhandahåller en klass [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) som representerar en Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) innehåller en samling [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection) som tillåter åtkomst till varje kalkylblad i Excel-filen.

Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Klassen [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) tillhandahåller ett brett utbud av metoder för att hantera kalkylblad. För att lägga till sidbrytningar, använd metoden [AddPageBreaks](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/addpagebreaks) av klassen [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).
### **Lägga till sidbrytningar**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManagingPageBreaks-AddingPageBreaks-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
