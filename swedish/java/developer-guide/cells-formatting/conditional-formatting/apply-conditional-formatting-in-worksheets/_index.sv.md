---
title: Använd villkorlig formatering i kalkylblad
type: docs
weight: 40
url: /sv/java/apply-conditional-formatting-in-worksheets/
---
{{% alert color="primary" %}}

Den här artikeln är utformad för att ge en detaljerad förståelse för hur man lägger till villkorlig formatering till ett antal celler i ett kalkylblad.

Villkorlig formatering är en avancerad funktion i Microsoft Excel som låter dig tillämpa format på en rad celler och ändra formateringen beroende på cellens värde eller värdet på en formel. Till exempel kan bakgrunden i en cell vara röd för att markera ett negativt värde, eller så kan textfärgen vara grön för ett positivt värde. När cellens värde uppfyller formatvillkoret tillämpas formatet. Om cellens värde inte uppfyller formatvillkoret används cellens standardformatering.

Det är möjligt att tillämpa villkorlig formatering med Microsoft Office Automation men det har sina nackdelar. Det finns flera orsaker och frågor inblandade: till exempel säkerhet, stabilitet, skalbarhet och hastighet. Den främsta anledningen till att hitta en annan lösning är att Microsoft själva starkt avråder från Office Automation för mjukvarulösningar.

Den här artikeln visar hur man skapar en konsolapplikation, lägger till villkorlig formatering på celler med några enklaste rader kod med hjälp av Aspose.Cells API.

{{% /alert %}}

## **Arbeta med villkorlig formatering**

Den här artikeln fungerar genom följande uppgifter:

1. [Använd Aspose.Cells för att tillämpa villkorlig formatering baserat på cellvärde](/cells/sv/java/apply-conditional-formatting-in-worksheets/#task-1-using-asposecells-to-apply-conditional-formatting-based-on-cell-value).
1. [Använda Aspose.Cells för att tillämpa villkorlig formatering baserat på en formel](/cells/sv/java/apply-conditional-formatting-in-worksheets/#task-2-using-asposecells-to-apply-conditional-formatting-based-on-a-formula).

### **Uppgift 1: Använd Aspose.Cells för att tillämpa villkorlig formatering baserat på Cell-värde**

1. **Ladda ner och installera Aspose.Cells.zip**:
   1. [Ladda ner](https://downloads.aspose.com/cells/java) Aspose.Cells för Java.
 1. Packa upp det på din utvecklingsdator.
 Alla Aspose-komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och injicerar endast vattenstämplar i producerade dokument.
1. **Skapa ett projekt**.
 Skapa antingen ett projekt med en Java Editor som Eclipse eller skapa ett enkelt program med en textredigerare.
1. **Lägg till klasssökväg**.
För att ställa in en klassväg med Eclipse, utför följande steg:
 1. Extrahera Aspose.Cells.jar och dom4j_1.6.1.jar från Aspose.Cells.zip.
 1. Ställ in klassvägen för projektet i Eclipse:
 1. Välj ditt projekt i Eclipse och välj sedan**Egenskaper** från**Projekt** meny.
 1. Välj "Java Build Path" till vänster om dialogrutan.
 1. På**Bibliotek** fliken, välj**Lägg till JAR** eller**Lägg till externa JAR** för att välja Aspose.Cells.jar och dom4j_1.6.1.jar och lägga till dem i byggvägar.
 1. Skriv applikation för att anropa API:er för Aspose:s komponenter.
 Eller så kan du ställa in sökvägen vid körning på en DOS-prompt i Windows.

{{< highlight "java" >}}

  javac -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName  

{{< /highlight >}}

1. **Använd villkorlig formatering baserat på cellvärde**.
 Nedan visas koden som används av komponenten för att utföra uppgiften. Den tillämpar villkorlig formatering på en cell.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingOnCellValue-ApplyConditionalFormattingOnCellValue.java" >}}

När ovanstående kod exekveras, tillämpas villkorlig formatering på cell "A1" i det första kalkylbladet i utdatafilen (output.xls). Den villkorliga formateringen som tillämpas på A1 beror på cellvärdet. Om cellvärdet för A1 är mellan 50 och 100 är bakgrundsfärgen röd på grund av den villkorliga formateringen som tillämpats. Se följande skärmdumpar av den genererade XLS-filen.

**Utdata Excel-fil med A1-värde mindre än 50**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_1.png)

**Skriv ut Excel-fil med A1 mellan 50 och 100**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_2.png)

### **Uppgift 2: Använd Aspose.Cells för att tillämpa villkorlig formatering baserad på en formel**

1. **Använd villkorlig formatering beroende på formel**.
 Nedan visas den faktiska koden som används av komponenten för att utföra uppgiften. Den tillämpar villkorlig formatering på "B3".

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingBasedOnFormula-ConditionalFormattingBasedOnFormula.java" >}}

När ovanstående kod exekveras, tillämpas villkorlig formatering på cell "B3" i det första kalkylbladet i utdatafilen (output.xls). Den villkorliga formateringen som tillämpas beror på formeln som beräknar värdet på "B3" som summan av B1 & B2. Se följande skärmdumpar av den genererade XLS-filen.

**Utdata Excel-fil med B3-värde mindre än 100**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_3.png)

**Utdata Excel-fil med B3 större än 100**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_4.png)

### **Slutsats**

{{% alert color="primary" %}}

Den här artikeln visar hur du tillämpar villkorlig formatering på celler i ett kalkylblad med Aspose.Cells API. Förhoppningsvis kommer det att ge dig lite insikt så att du kan använda dessa alternativ i dina egna scenarier.

Aspose.Cells erbjuder stor flexibilitet för lösningar och ger enastående hastighet, effektivitet och tillförlitlighet för att möta specifika affärsapplikationskrav. Aspose.Cells drar nytta av år av forskning, design och noggrann inställning.

 Vi välkomnar dina frågor, kommentarer och förslag i[Aspose.Cells Forum](https://forum.aspose.com/c/cells/9). Vi garanterar ett snabbt svar.

{{% /alert %}}
