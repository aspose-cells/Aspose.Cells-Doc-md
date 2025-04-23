---
title: Sidlayout och utskriftsalternativ
type: docs
weight: 10
url: /sv/java/page-setup-and-printing-options/
---

{{% alert color="primary" %}}

Ibland behöver utvecklare konfigurera sidlayout och utskriftsalternativ för att kontrollera utskriftsprocessen. Sidlayouts- och utskriftsalternativen erbjuder olika alternativ och stöds fullt ut i Aspose.Cells.

Denna artikel visar hur man skapar en konsolapplikation och tillämpar sidlayouts- och utskriftsalternativ på ett arbetsblad med några enkla kodrader med hjälp av Aspose.Cells API:er.

{{% /alert %}}

## **Arbeta med Sid- och Utskriftsalternativ**

För detta exempel skapade vi en arbetsbok i Microsoft Excel och använde Aspose.Cells för att ställa in sidlayouts- och utskriftsalternativ.

### **Ställa in Sidlayoutalternativ**

Skapa först ett enkelt arbetsblad i Microsoft Excel. Tillämpa sedan sidlayoutalternativ på det. När koden utförs ändras sidlayoutalternativen enligt skärmdumpen nedan.

**Utgångsfil** 

![todo:image_alt_text](page-setup-and-printing-options_1.png)

1. Skapa ett arbetsblad med viss data i Microsoft Excel:
   1. Öppna en ny arbetsbok i Microsoft Excel.
   1. Lägg till viss data.
      Här är en skärmdump av filen.

      **Ingångsfil**

![todo:image_alt_text](page-setup-and-printing-options_2.png)

1. Ange sidlayoutalternativ:
   Tillämpa sidlayoutalternativ på filen. Här är en skärmdump av de förvalda alternativen, innan de nya alternativen tillämpas.

   **Förvalda sidlayoutalternativ**

![todo:image_alt_text](page-setup-and-printing-options_3.png)

1. Ladda ner och installera Aspose.Cells:
   1. [Ladda ner](https://downloads.aspose.com/cells/java) Aspose.Cells for Java.
   1. Packa upp det på din utvecklingsdator.
      Alla [Aspose](http://www.aspose.com/) -komponenter fungerar i utvärderingsläge när de är installerade. Utvärderingsläget har ingen tidsbegränsning och det lägger bara till vattenstämplar i producerade dokument.
1. Skapa ett projekt.
   Antingen skapar du ett projekt med en Java-redigerare, till exempel Eclipse, eller skapar du ett enkelt program med en textredigerare.
1. Lägg till en klass sökväg.
   1. Extrahera Aspose.Cells.jar och dom4j_1.6.1.jar från Aspose.Cells.zip.
   1. Ange klassens sökväg i Eclipse:
   1. Välj ditt projekt i Eclipse och klicka sedan på ** Projekt ** följt av ** Egenskaper **.
   1. Välj ** Java Build Path ** till vänster om dialogrutan.
   1. Välj fliken Bibliotek, klicka på ** Lägg till JARs ** eller ** Lägg till externa JARs ** för att välja Aspose.Cells.jar och dom4j_1.6.1.jar och lägg till dem i byggvägarna.
      Eller så kan du ställa in det vid körning vid en DOS-prompt i Windows:

{{< highlight java >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

1. Skriv applikationen som anropar API: er:
   Nedan är koden som används av komponenten i detta exempel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPageSetupOptions-SettingPageSetupOptions.java" >}}

### **Inställa utskriftsalternativ**

Sidlayoutinställningar ger också flera utskriftsalternativ (även kallade bladalternativ) som låter användarna styra hur arksidor skrivs ut. De tillåter användarna att:

- Välj ett specifikt utskriftsområde av ett kalkylblad.
- Skriv ut rubriker.
- Skriv ut rutnät.
- Skriv ut rad-/kolumnrubriker.
- Uppnå utkasts kvalitet
- Skriv ut kommentarer.
- Skriv ut cellfel.
- Definiera sidordning.

Exemplet som följer tillämpar utskriftsalternativ på filen skapad i exemplet ovan (PageSetup.xls). Skärmdumpen nedan visar de standardutskriftsalternativen innan nya alternativ tillämpas.
**Ingångsdokument**

![todo:image_alt_text](page-setup-and-printing-options_4.png)

Körning av koden ändrar utskriftsalternativen.
**Utgångsfil**

![todo:image_alt_text](page-setup-and-printing-options_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPrintoptions-SettingPrintoptions.java" >}}

## **Sammanfattning**

{{% alert color="primary" %}}

Den här artikeln visar hur du ställer in sid-layout och arkutskriftsalternativ med Aspose.Cells. Förhoppningsvis ger det dig en inblick och du kan använda dessa alternativ i dina egna scenarier.

Aspose.Cells drar nytta av års forskning, design och noggrann justering. Vi välkomnar varmt dina frågor, kommentarer och förslag på [Aspose.Cells Forum](https://forum.aspose.com/c/cells/9). Vi garanti en snabb svar.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
