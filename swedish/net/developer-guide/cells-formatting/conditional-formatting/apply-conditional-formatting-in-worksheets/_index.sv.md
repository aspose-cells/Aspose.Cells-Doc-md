---
title: Använd villkorlig formatering i kalkylblad
type: docs
weight: 130
url: /sv/net/apply-conditional-formatting-in-worksheets/
---
{{% alert color="primary" %}}

Den här artikeln är utformad för att ge en detaljerad förståelse för hur man lägger till villkorlig formatering till ett antal celler i ett kalkylblad.

Villkorlig formatering är en avancerad funktion i Microsoft Excel som låter dig tillämpa format på en rad celler och ändra formateringen beroende på cellens värde eller värdet på en formel. Till exempel kan bakgrunden i en cell vara röd för att markera ett negativt värde, eller så kan textfärgen vara grön för ett positivt värde. När cellens värde uppfyller formatvillkoret tillämpas formatet. Om cellens värde inte uppfyller formatvillkoret används cellens standardformatering.

Det är möjligt att tillämpa villkorlig formatering med Microsoft Office Automation men det har sina nackdelar. Det finns flera orsaker och frågor inblandade: till exempel säkerhet, stabilitet, skalbarhet och hastighet. Den främsta anledningen till att hitta en annan lösning är att Microsoft själva starkt avråder från Office Automation för mjukvarulösningar.

Den här artikeln visar hur man skapar en konsolapplikation, lägger till villkorlig formatering på celler med några enklaste rader kod med hjälp av Aspose.Cells API.

{{% /alert %}}

## **Använda Aspose.Cells för att tillämpa villkorlig formatering baserat på Cell-värde**

1. **Ladda ner och installera Aspose.Cells**.
 1. Ladda ner Aspose.Cells för .NET.
1. Installera det på din utvecklingsdator.
Alla Aspose-komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och det injicerar bara vattenstämplar i producerade dokument.
1. **Skapa ett projekt**.
 Starta Visual Studio.NET och skapa en ny konsolapplikation. Det här exemplet skapar en C#-konsolapplikation, men du kan också använda VB.NET.
1. **Lägg till referenser**.
 Lägg till en referens till Aspose.Cells till ditt projekt, till exempel lägg till en referens till ….\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. *Använd villkorlig formatering baserat på cellvärde.
 Nedan finns koden som används för att utföra uppgiften. Jag tillämpar villkorlig formatering på en cell.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingCellValue-1.cs" >}}

När ovanstående kod exekveras, tillämpas villkorlig formatering på cell "A1" i det första kalkylbladet i utdatafilen (output.xls). Den villkorliga formateringen som tillämpas på A1 beror på cellvärdet. Om cellvärdet för A1 är mellan 50 och 100 är bakgrundsfärgen röd på grund av den villkorliga formateringen som tillämpats.

## **Använda Aspose.Cells för att tillämpa villkorlig formatering baserad på formel**

1. Tillämpa villkorlig formatering beroende på formel (kodavsnitt)
 Nedan finns koden för att utföra uppgiften. Den tillämpar villkorlig formatering på B3.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingFormula-1.cs" >}}

När ovanstående kod exekveras, tillämpas villkorlig formatering på cell "B3" i det första kalkylbladet i utdatafilen (output.xls). Den villkorliga formateringen som tillämpas beror på formeln som beräknar värdet på "B3" som summan av B1 & B2.
