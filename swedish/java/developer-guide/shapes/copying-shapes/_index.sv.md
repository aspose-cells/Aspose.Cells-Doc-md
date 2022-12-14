---
title: Kopiera former mellan kalkylblad
type: docs
weight: 250
url: /sv/java/copy-shapes-between-worksheets/
---
{{% alert color="primary" %}}

Ibland behöver du kopiera olika bilder, diagram och andra ritobjekt till olika kalkylblad enligt dina krav. Aspose.Cells stöder kopiering av former mellan kalkylblad. Sjökorten, bilderna och andra objekt kopieras med högsta precision.

Du kan prova Office Automation men det har sina egna nackdelar. Det finns flera orsaker och problem inblandade: till exempel säkerhet, stabilitet, skalbarhet, hastighet, pris och funktioner. Kort sagt, det finns många anledningar, med den främsta är att Microsoft själva starkt rekommenderar Office-automation från mjukvarulösningar.

I den här artikeln skapar vi en konsolapplikation, utför kopiering av bilder, diagram och andra ritobjekt mellan kalkylblad i en arbetsbok med några få och enklaste rader kod med hjälp av Aspose.Cells.

Detta dokument är utformat för att ge utvecklarna en detaljerad förståelse för hur man kopierar former (bilder, diagram, kontroller och andra ritobjekt) mellan kalkylblad.

{{% /alert %}}

## **Kopiera former**

Den här artikeln förklarar hur du:

- [Kopiera en bild från ett kalkylblad till ett annat](/cells/sv/java/copy-shapes-between-worksheets/#copying-a-picture-from-one-worksheet-to-another).
- [Kopiera ett diagram från ett kalkylblad till ett annat](/cells/sv/java/copy-shapes-between-worksheets/#task-2-copying-a-chart-from-one-worksheet-to-another).
- [Kopiera kontroller och andra ritobjekt från ett kalkylblad till ett annat](/cells/sv/java/copy-shapes-between-worksheets/#task-3-copying-controls-and-other-drawing-objects-from-one-worksheet-to-another).

### **Kopiera en bild från ett arbetsblad till ett annat**

#### **Steg 1: Skapa en arbetsbok med bild och diagram i Microsoft Excel**

1. Skapat en ny arbetsbok i Microsoft Excel.
1. Lägg till en bild på det första kalkylbladet och ett diagram på det andra kalkylbladet.

 Följande skärmdumpar visar de två mallar som skapats i Microsoft Excel.

   **Arbetsblad "Diagram" med diagram**

![todo:image_alt_text](copy-shapes-between-worksheets_1.png)

**Arbetsblad "Bild" med bild**

![todo:image_alt_text](copy-shapes-between-worksheets_2.png)

Kopiera nu bilden i kalkylbladet med namnet "Bild" till det sista kalkylbladet "Resultat".

#### **Steg 2: Ladda ner Aspose.Cells.Zip**

1. [Ladda ner Aspose.Cells för Java](https://downloads.aspose.com/cells/java).
1. Packa upp det på din utvecklingsdator.

 Allt[Aspose](http://www.aspose.com/) komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och det injicerar bara vattenstämplar i producerade dokument.

#### **Steg 3: Skapa ett projekt**

Du kan antingen skapa ett projekt med hjälp av någon Java-redigerare, till exempel Eclipse eller skapa ett enkelt program med hjälp av en NotePad.

#### **Steg 4: Lägg till klasssökväg**

För att ställa in en klassväg med Eclipse, utför följande steg:

1. Extrahera Aspose.Cells.jar och dom4j_1.6.1.jar från Aspose.Cells.zip.
1. Ställ in klassvägen för projektet i Eclipse:
1. Välj ditt projekt i Eclipse och klicka sedan på menyerna Projekt-egenskaper.
1. Välj "Java Build Path" till vänster i popup-fönstret, välj sedan fliken "Libraries", klicka på "Add JARs" eller "Add External JARs" för att välja Aspose.Cells.jar och dom4j_1.6.1.jar och lägga till dem i build vägar.
1. Skriv applikation för att anropa API:er för Aspose:s komponenter.

Eller så kan du ställa in den vid körning vid DOS-prompt i Windows. Till exempel:

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; Klassnamn

#### **Steg 5: Kopiera en bild från ett kalkylblad till ett annat**

Följande är koden för att utföra uppgiften. Den kopierar en bild från arbetsbladet med namnet "Bild" till arbetsbladet "Resultat".

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyPicturefromOneWorksheetToAnother-CopyPicturefromOneWorksheetToAnother.java" >}}

#### **Resultatuppgift 1:**

Efter exekvering av ovanstående kod kopieras nu bilden från kalkylbladet "Bild" till det sista kalkylbladet "Resultat"

**Arbetsblad "Resultat" med kopierad bild**

![todo:image_alt_text](copy-shapes-between-worksheets_3.png)

### **Uppgift 2: Kopiera ett diagram från ett arbetsblad till ett annat**

#### **Steg 1: Kopiera ett diagram från ett kalkylblad till ett annat**

Följande är den faktiska koden som används av komponenten för att utföra uppgiften.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyChartFromOneWorksheetToAnother-CopyChartFromOneWorksheetToAnother.java" >}}

#### **Resultat Uppgift 2**

Efter exekvering av ovanstående kod kopieras diagrammet från kalkylbladet "Diagram" till kalkylbladet "Resultat". Se följande ögonblicksbild av det resulterande arbetsbladet.

**Arbetsblad "Resultat" med kopierad bild och diagram**

![todo:image_alt_text](copy-shapes-between-worksheets_4.png)

### **Uppgift 3: Kopiera kontroller och andra ritobjekt från ett arbetsblad till ett annat**

**Arbetsblad "Kontroll" med textruta och oval**

![todo:image_alt_text](copy-shapes-between-worksheets_5.png)

Se följande enkla steg som du måste utföra för att få önskat resultat.

#### **Steg 1: Kopiera ett kalkylblad mellan arbetsböcker**

Följande är koden som används av komponenten för att utföra uppgiften.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyWorksheetBetweenWorkbooks-CopyWorksheetBetweenWorkbooks.java" >}}

#### **Resultat Uppgift 3**

Efter exekvering av ovanstående kod kopieras nu kontrollerna från arbetsbladet "Kontroll" till arbetsbladet "Resultat". Se följande ögonblicksbild av "Resultat".

**Arbetsblad "Resultat" med kopierad textruta och oval**

![todo:image_alt_text](copy-shapes-between-worksheets_6.png)

## **Slutsats**

Den här artikeln har visat hur du kopierar olika former som bilder, diagram och andra ritobjekt mellan att använda Aspose.Cells. Förhoppningsvis kommer det att ge dig lite insikt och du kommer att kunna använda dessa alternativ enligt dina olika scenarier.

Aspose.Cells kan erbjuda mer flexibilitet än andra för lösningar och ger enastående hastighet, effektivitet och tillförlitlighet för att möta specifika affärsapplikationskrav. Resultaten visar att Aspose.Cells har dragit nytta av år av forskning, design och noggrann justering.

 Vi välkomnar hjärtligt dina frågor, kommentarer och förslag i[Aspose.Cells Forum](https://forum.aspose.com/c/cells/9).
