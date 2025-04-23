---
title: Din första Aspose.Cells applikation  Hej världen
type: docs
weight: 30
url: /sv/net/your-first-aspose-cells-application-hello-world/
description: Skapa, redigera och spara din första excel fil i valfria format som stöds med Aspose.Cells for .NET för att uppleva dess enkelhet och kraft i C#.
keywords: C# Hej världen, Aspose.Cells for .NET Hej världen, Den första applikationen som använder Aspose.Cells for .NET, Det första programmet via Aspose.Cells for .NET.
---

{{% alert color="primary" %}}

I den här handledningen visas hur man skapar en mycket enkel applikation (Hej världen) med Aspose.Cells' enkla API. Denna enkla applikation skapar en Microsoft Excel-fil med texten 'Hej världen' i en angiven kalkylarks cell.

{{% /alert %}}

## **Hur man skapar applikationen Hej världen**

Följande steg skapar Hello World-applikationen med Aspose.Cells API:

1. Skapa en instans av [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)-klassen.
1. Om du har en licens, [ansök om den](/cells/sv/net/licensing/).
   Om du använder utvärderingsversionen, hoppa över licensrelaterade kodrader.
1. Skapa en ny Excel-fil, eller öppna en befintlig Excel-fil.
1. Åtkomst till valfri cell i ett kalkylblad i Excel-filen.
1. Infoga orden **Hello World!** i en åtkomstcell.
1. Generera den modifierade Microsoft Excel-filen.

Implementeringen av ovanstående steg visas i exemplen nedan.

### **Hur man skapar en ny arbetsbok**

Följande exempel skapar en ny arbetsbok från grunden, skriver Hej världen! i cell A1 på det första kalkylarket och sparar Excel-filen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **Hur man öppnar en befintlig fil**

Följande exempel öppnar en befintlig Microsoft Excel-mallfil vid namn "Sample.xlsx", matar in texten "Hej världen!" i cell A1 i det första kalkylarket och sparar arbetsboken.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
