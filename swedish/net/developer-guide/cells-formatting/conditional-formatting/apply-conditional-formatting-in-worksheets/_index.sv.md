---
title: Tillämpa villkorlig formatering i arbetsblad
description: Hur man använder Aspose.Cells biblioteket i C# för att tillämpa villkorlig formatering i arbetsblad. Genom att justera dessa kriterier har du mer kontroll över hur celler ser ut och visas.
keywords: Aspose.Cells, Villkorlig formatering, C#, Arbetsblad, Formattering
type: docs
weight: 130
url: /sv/net/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Den här artikeln syftar till att ge en detaljerad förståelse för hur man lägger till villkorlig formatering till en rad celler i ett arbetsblad.

Villkorlig formatering är en avancerad funktion i Microsoft Excel som gör det möjligt att tillämpa format på en rad celler och ha den formateringen ändras beroende på cellens värde eller värdet på en formel. Till exempel kan bakgrunden för en cell vara röd för att markera ett negativt värde eller textfärgen kan vara grön för ett positivt värde. När cellens värde uppfyller formatvillkoret tillämpas formatet. Om cellens värde inte uppfyller formatvillkoret används cellens standardformatering.

Det är möjligt att tillämpa villkorlig formatering med Microsoft Office Automation men det har sina nackdelar. Det finns flera skäl och problem involverade: till exempel säkerhet, stabilitet, skalbarhet och hastighet. Det främsta skälet till att hitta en annan lösning är att Microsoft själva starkt avråder från Office Automation för programvarulösningar.

Den här artikeln visar hur du skapar en konsolapplikation, lägger till villkorlig formatering på celler med några få enklaste kodrader med hjälp av Aspose.Cells API.

{{% /alert %}}

## **Använda Aspose.Cells för att tillämpa villkorlig formatering baserat på cellvärde**

1. **Ladda ner och installera Aspose.Cells**.
   1. Ladda ner Aspose.Cells for .NET.
1. Installera det på din utvecklingsdator.
   Alla Aspose-komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och det injicerar endast vattenstämplar i producerade dokument.
1. **Skapa ett projekt**.
   Starta Visual Studio.NET och skapa en ny konsolapplikation. Detta exempel skapar en C#-konsolapplikation, men du kan också använda VB.NET.
1. **Lägg till referenser**.
   Lägg till en referens till Aspose.Cells i ditt projekt, till exempel en referens till ….\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. *Tillämpa villkorlig formatering baserat på cellvärde.
   Nedan är koden som används för att utföra uppgiften. Jag tillämpar villkorlig formatering på en cell.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingCellValue-1.cs" >}}

När ovanstående kod körs, tillämpas villkorlig formatering på cellen ”A1” i den första arbetsboken i utdatafilen (output.xls). Den villkorliga formateringen som tillämpas på A1 beror på cellens värde. Om cellvärdet i A1 ligger mellan 50 och 100 är bakgrundsfärgen röd på grund av den villkorliga formateringen som tillämpas.

## **Använd Aspose.Cells för att tillämpa villkorlig formatering baserat på formel**

1. Tillämpa villkorlig formatering beroende på formel (kodsöndag)
   Nedan är koden för att utföra uppgiften. Den tillämpar villkorlig formatering på B3.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingFormula-1.cs" >}}

När ovanstående kod körs, tillämpas villkorlig formatering på cellen ”B3” i den första arbetsboken i utdatafilen (output.xls). Den villkorliga formateringen som tillämpas beror på formeln som beräknar värdet av “B3” som summan av B1 & B2.
