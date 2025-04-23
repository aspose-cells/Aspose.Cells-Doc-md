---
title: Tillämpa villkorlig formatering i arbetsblad
type: docs
weight: 40
url: /sv/java/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Den här artikeln syftar till att ge en detaljerad förståelse för hur man lägger till villkorlig formatering till en rad celler i ett arbetsblad.

Villkorlig formatering är en avancerad funktion i Microsoft Excel som gör det möjligt att tillämpa format på en rad celler och ha den formateringen ändras beroende på cellens värde eller värdet på en formel. Till exempel kan bakgrunden för en cell vara röd för att markera ett negativt värde eller textfärgen kan vara grön för ett positivt värde. När cellens värde uppfyller formatvillkoret tillämpas formatet. Om cellens värde inte uppfyller formatvillkoret används cellens standardformatering.

Det är möjligt att tillämpa villkorlig formatering med Microsoft Office Automation men det har sina nackdelar. Det finns flera skäl och problem involverade: till exempel säkerhet, stabilitet, skalbarhet och hastighet. Det främsta skälet till att hitta en annan lösning är att Microsoft själva starkt avråder från Office Automation för programvarulösningar.

Den här artikeln visar hur du skapar en konsolapplikation, lägger till villkorlig formatering på celler med några få enklaste kodrader med hjälp av Aspose.Cells API.

{{% /alert %}}

## **Arbeta med villkorlig formatering**

Den här artikeln går igenom följande uppgifter:

1. [Använda Aspose.Cells för att tillämpa villkorlig formatering baserat på cellvärde](/cells/sv/java/apply-conditional-formatting-in-worksheets/#task-1-using-asposecells-to-apply-conditional-formatting-based-on-cell-value).
1. [Använda Aspose.Cells för att tillämpa villkorlig formatering baserat på en formel](/cells/sv/java/apply-conditional-formatting-in-worksheets/#task-2-using-asposecells-to-apply-conditional-formatting-based-on-a-formula).

### **Uppgift 1: Använda Aspose.Cells för att tillämpa villkorlig formatering baserat på cellvärde**

1. **Ladda ner och installera Aspose.Cells.zip**:
   1. [Ladda ner](https://downloads.aspose.com/cells/java) Aspose.Cells for Java.
   1. Packa upp det på din utvecklingsdator.
      Alla Aspose-komponenter fungerar i utvärderingsläge när de är installerade. Utvärderingsläget har ingen tidsbegränsning och lägger endast in vattenstämplar i genererade dokument.
1. **Skapa ett projekt**.
   Antingen skapa ett projekt med en Java-redigerare som Eclipse eller skapa ett enkelt program med en textredigerare.
1. **Lägg till class path**.
   För att ange en klass sökväg med Eclipse, utför följande steg:
   1. Extrahera Aspose.Cells.jar och dom4j_1.6.1.jar från Aspose.Cells.zip.
   1. Ange klassens sökväg i Eclipse:
      1. Välj ditt projekt i Eclipse och välj sedan **Egenskaper** från **Projekt**-menyn.
      1. Välj "Java Build Path" till vänster om dialogrutan.
      1. På fliken **Bibliotek** väljer du **Lägg till JAR-filer** eller **Lägg till externa JAR-filer** för att välja Aspose.Cells.jar och dom4j_1.6.1.jar och lägga till dem i byggvägarna.
   1. Skriv applikation för att anropa API:er för Asposes komponenter.
      Eller så kan du ange sökvägen vid körningstid i en DOS-prompt i Windows.

{{< highlight java >}}

  javac -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName  

{{< /highlight >}}

1. **Tillämpa villkorlig formatering baserat på cellvärde**.
   Nedan är koden som används av komponenten för att utföra uppgiften. Den tillämpar villkorlig formatering på en cell.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingOnCellValue-ApplyConditionalFormattingOnCellValue.java" >}}

När ovanstående kod körs tillämpas villkorlig formatering på cellen “A1” i den första kalkylbladet i utdatafilen (output.xls). Den villkorliga formateringen som tillämpas på A1 beror på cellvärdet. Om cellvärdet för A1 ligger mellan 50 och 100 blir bakgrundsfärgen röd på grund av den tillämpade villkorliga formateringen. Se följande skärmdumpar av den genererade XLS-filen.

**Utdata-excelfil med A1-värde mindre än 50**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_1.png)

**Utdata-excelfil med A1 mellan 50 och 100**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_2.png)

### **Uppgift 2: Använda Aspose.Cells för att Tillämpa Villkorlig Formatering baserat på en Formel**

1. **Tillämpa villkorlig formatering beroende på formel**.
   Nedan är den faktiska koden som används av komponenten för att utföra uppgiften. Den tillämpar villkorlig formatering på “B3”.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingBasedOnFormula-ConditionalFormattingBasedOnFormula.java" >}}

När ovanstående kod körs tillämpas villkorlig formatering på cellen “B3” i det första kalkylbladet i utdatafilen (output.xls). Den villkorliga formateringen som tillämpas beror på formeln som beräknar värdet av “B3” som summan av B1 & B2. Se följande skärmdumpar av den genererade XLS-filen.

**Utdata-excelfil med B3-värde mindre än 100**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_3.png)

**Utdata-excelfil med B3 större än 100**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_4.png)

### **Slutsats**

{{% alert color="primary" %}}

Den här artikeln visar hur man tillämpar villkorlig formatering på celler i ett kalkylblad med Aspose.Cells API. Förhoppningsvis ger den dig några insikter så att du kan använda dessa alternativ i dina egna scenarier.

Aspose.Cells erbjuder stor flexibilitet för lösningar och ger enastående hastighet, effektivitet och tillförlitlighet för att uppfylla specifika affärsapplikationskrav. Aspose.Cells drar nytta av års forskning, design och noggrann finjustering.

Vi välkomnar dina frågor, kommentarer och förslag i [Aspose.Cells Forum](https://forum.aspose.com/c/cells/9). Vi ger en snabb återkoppling.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
