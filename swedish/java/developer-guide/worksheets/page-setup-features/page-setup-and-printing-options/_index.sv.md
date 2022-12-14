---
title: Sidinställningar och utskriftsalternativ
type: docs
weight: 10
url: /sv/java/page-setup-and-printing-options/
---
{{% alert color="primary" %}}

Ibland måste utvecklare konfigurera sidinställningar och utskriftsinställningar för att styra utskriftsprocessen. Sidinställningar och utskriftsinställningar erbjuder olika alternativ och stöds fullt ut i Aspose.Cells.

Den här artikeln visar hur du skapar en konsolapplikation och tillämpar sidinställningar och utskriftsalternativ på ett kalkylblad med några enkla rader kod med hjälp av Aspose.Cells API.

{{% /alert %}}

## **Arbeta med sid- och utskriftsinställningar**

För det här exemplet skapade vi en arbetsbok i Microsoft Excel och använder Aspose.Cells för att ställa in sidinställningar och utskriftsalternativ.

### **Ställa in alternativ för sidinställningar**

Skapa först ett enkelt kalkylblad i Microsoft Excel. Använd sedan sidinställningar på den. Genom att köra koden ändras alternativen för sidinställningar som på skärmdumpen nedan.

**Utdatafil** 

![todo:image_alt_text](page-setup-and-printing-options_1.png)

1. Skapa ett kalkylblad med vissa data i Microsoft Excel:
 1. Öppna en ny arbetsbok i Microsoft Excel.
 1. Lägg till några data.
 Nedan finns en skärmdump av filen.

      **Indatafil**

![todo:image_alt_text](page-setup-and-printing-options_2.png)

1. Ange alternativ för sidinställningar:
 Tillämpa sidinställningar på filen. Nedan finns en skärmdump av standardalternativen, innan de nya alternativen tillämpas.

   **Standardalternativ för sidinställningar**

![todo:image_alt_text](page-setup-and-printing-options_3.png)

1. Ladda ner och installera Aspose.Cells:
   1. [Ladda ner](https://downloads.aspose.com/cells/java) Aspose.Cells för Java.
 1. Packa upp det på din utvecklingsdator.
 Allt[Aspose](http://www.aspose.com/) komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och det injicerar bara vattenstämplar i producerade dokument.
1. Skapa ett projekt.
 Skapa antingen ett projekt med en Java-redigerare, till exempel Eclipse, eller skapa ett enkelt program med en textredigerare.
1. Lägg till en klasssökväg.
 1. Extrahera Aspose.Cells.jar och dom4j_1.6.1.jar från Aspose.Cells.zip.
 1. Ställ in klassvägen för projektet i Eclipse:
 1. Välj ditt projekt i Eclipse och klicka sedan**Projekt** följd av**Egenskaper**.
 1. Välj**Java Build Path**till vänster om dialogrutan.
 1. Välj fliken Bibliotek, klicka på**Lägg till JAR** eller**Lägg till externa JAR** för att välja Aspose.Cells.jar och dom4j_1.6.1.jar och lägga till dem i byggvägarna.
 Eller så kan du ställa in det vid körning vid en DOS-prompt i Windows:

{{< highlight "java" >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

1. Skriv programmet som anropar API:er:
 Nedan visas koden som används av komponenten i detta exempel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPageSetupOptions-SettingPageSetupOptions.java" >}}

### **Ställa in utskriftsalternativ**

Inställningar för sidinställningar ger också flera utskriftsalternativ (även kallade arkalternativ) som låter användare styra hur kalkylbladssidor skrivs ut. De tillåter användare att:

- Välj ett specifikt utskriftsområde i ett kalkylblad.
- Skriv ut titlar.
- Skriv ut rutnät.
- Skriv ut rad-/kolumnrubriker.
- Uppnå dragkvalitet.
- Skriv ut kommentarer.
- Utskriftscellfel.
- Definiera sidordning.

Exemplet som följer tillämpar utskriftsalternativ på filen som skapats i exemplet ovan (PageSetup.xls). Skärmbilden nedan visar standardutskriftsalternativen innan nya alternativ tillämpas.
**Inmatningsdokument**

![todo:image_alt_text](page-setup-and-printing-options_4.png)

Genom att köra koden ändras utskriftsalternativen.
**Utdatafil**

![todo:image_alt_text](page-setup-and-printing-options_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPrintoptions-SettingPrintoptions.java" >}}

## **Sammanfattning**

{{% alert color="primary" %}}

Den här artikeln visar hur du ställer in sidinställningar och utskriftsalternativ för ark med Aspose.Cells. Förhoppningsvis kommer det att ge dig lite insikt, och du kan använda dessa alternativ i dina egna scenarier.

 Aspose.Cells drar nytta av år av forskning, design och noggrann inställning. Vi välkomnar hjärtligt dina frågor, kommentarer och förslag på[Aspose.Cells Forum](https://forum.aspose.com/c/cells/9). Vi garanterar ett snabbt svar.

{{% /alert %}}
