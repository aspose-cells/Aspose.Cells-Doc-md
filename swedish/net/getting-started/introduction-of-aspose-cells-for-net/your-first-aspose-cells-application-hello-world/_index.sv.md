---
title: Din första Aspose.Cells-ansökan - Hello World
type: docs
weight: 30
url: /sv/net/your-first-aspose-cells-application-hello-world/
description: Skapa, redigera och spara din första Excel-fil i alla format som stöds med Aspose.Cells for .NET för att uppleva dess enkelhet och kraft i C#.
keywords: C# Hello World, Aspose.Cells for .NET Hello World, The first application using Aspose.Cells for .NET, The first program via Aspose.Cells for .NET.
---
{{% alert color="primary" %}}

Denna handledning visar hur man skapar en allra första applikation (Hello World) med Aspose.Cells' simple API. Denna enkla applikation skapar en Microsoft Excel-fil med texten 'Hello World' i en specificerad kalkylbladscell.

{{% /alert %}}

##  **Hur man skapar Hello World-applikationen**

Stegen nedan skapar Hello World-applikationen med hjälp av Aspose.Cells API:

1.  Skapa en instans av[Arbetsbok](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass.
1.  Om du har en licens, då[tillämpa den](/cells/sv/net/licensing/).
 Om du använder utvärderingsversionen, hoppa över de licensrelaterade kodraderna.
1. Skapa en ny Excel-fil eller öppna en befintlig Excel-fil.
1. Få åtkomst till valfri cell i ett kalkylblad i Excel-filen.
1.  Sätt in orden**Hello World!** in i en cell som nås.
1. Generera den modifierade Microsoft Excel-filen.

Implementeringen av stegen ovan visas i exemplen nedan.

###  **Hur man skapar en ny arbetsbok**

Följande exempel skapar en ny arbetsbok från början, skriver Hello World! i cell A1 på det första kalkylbladet och sparar Excel-filen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

###  **Hur man öppnar en befintlig fil**

Följande exempel öppnar en befintlig Microsoft Excel-mallfil med namnet "Sample.xlsx", matar in "Hello World!" text i A1-cellen i det första kalkylbladet och sparar arbetsboken.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
