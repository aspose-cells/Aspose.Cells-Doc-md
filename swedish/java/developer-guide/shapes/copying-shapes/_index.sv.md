---
title: Kopiera former mellan arkmallar
type: docs
weight: 250
url: /sv/java/copy-shapes-between-worksheets/
---

{{% alert color="primary" %}}

Ibland behöver du kopiera olika bilder, diagram och andra ritobjekt till olika kalkylblad enligt dina behov. Aspose.Cells stöder att kopiera former mellan kalkylblad. Diagram, bilder och andra objekt kopieras med högsta precision.

Du kan försöka Office Automation men det har sina egna nackdelar. Det finns flera skäl och problem involverade: till exempel säkerhet, stabilitet, skalbarhet, hastighet, pris och funktioner. Kort sagt finns det många skäl, det främsta är att Microsoft själva starkt avråder från Office automation från programvarulösningar.

I den här artikeln skapar vi en konsolapplikation, utför kopiering av bilder, diagram och andra ritobjekt mellan kalkylblad i en arbetsbok med några och enklaste kodrader med hjälp av Aspose.Cells.

Det här dokumentet är utformat för att ge utvecklarna en detaljerad förståelse för hur man kopierar former (bilder, diagram, kontroller och andra ritobjekt) mellan kalkylblad.

{{% /alert %}}

## **Kopiera former**

Den här artikeln förklarar hur man:

- [Kopiera en bild från ett kalkylblad till ett annat](/cells/sv/java/copy-shapes-between-worksheets/#copying-a-picture-from-one-worksheet-to-another).
- [Kopiera ett diagram från ett kalkylblad till ett annat](/cells/sv/java/copy-shapes-between-worksheets/#task-2-copying-a-chart-from-one-worksheet-to-another).
- [Kopiera kontroller och andra ritobjekt från ett kalkylblad till ett annat](/cells/sv/java/copy-shapes-between-worksheets/#task-3-copying-controls-and-other-drawing-objects-from-one-worksheet-to-another).

### **Kopiera en bild från ett ark till ett annat**

#### **Steg 1: Skapa en arbetsbok med bild och diagram i Microsoft Excel**

1. Skapat en ny arbetsbok i Microsoft Excel.
1. Lägg till en bild på första kalkylbladet och ett diagram på andra kalkylbladet.

   Följande skärmbilder visar de två mallkalkylbladen skapade i Microsoft Excel.

   **Kalkylblad "Diagram" med diagram**

![todo:image_alt_text](copy-shapes-between-worksheets_1.png)

**Kalkylblad "Bild" med bild**

![todo:image_alt_text](copy-shapes-between-worksheets_2.png)

Nu, kopiera bilden i kalkylbladet med namnet "Bild" till det sista kalkylbladet "Resultat".

#### **Steg 2: Ladda ner Aspose.Cells.Zip**

1. [Ladda ner Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. Packa upp det på din utvecklingsdator.

   Alla [Aspose](http://www.aspose.com/) -komponenter fungerar i utvärderingsläge när de är installerade. Utvärderingsläget har ingen tidsbegränsning och det lägger bara till vattenstämplar i producerade dokument.

#### **Steg 3: Skapa ett projekt**

Du kan antingen skapa ett projekt med någon Java-editor, till exempel Eclipse, eller skapa ett enkelt program med en Notepad.

#### **Steg 4: Lägg till Class Path**

För att ange en klass sökväg med Eclipse, utför följande steg:

1. Extrahera Aspose.Cells.jar och dom4j_1.6.1.jar från Aspose.Cells.zip.
1. Ange klassens sökväg i Eclipse:
1. Välj ditt projekt i Eclipse och klicka sedan menyn Projekt-Egenskaper.
1. Välj "Java Build Path" på den vänstra sidan av popup-fönstret, välj sedan fliken "Libraries", klicka på "Add JARs" eller "Add External JARs" för att välja Aspose.Cells.jar och dom4j_1.6.1.jar och lägg till dem i bygg sökvägar.
1. Skriv applikation för att anropa API:er för Asposes komponenter.

Eller så kan du ställa in det vid körning vid DOS-prompten i Windows. Till exempel:

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

#### **Steg 5: Kopiera en bild från en arbetsbok till en annan**

Följande är koden för att utföra uppgiften. Den kopierar en bild från arbetsboken med namnet "Bild" till arbetsboken "Resultat".

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyPicturefromOneWorksheetToAnother-CopyPicturefromOneWorksheetToAnother.java" >}}

#### **Resultat Uppgift 1:**

Efter att ha kört ovanstående kod har bilden från arbetsboken "Bild" nu kopierats till den sista arbetsboken "Resultat"

**Arbetsbok "Resultat" med kopierad bild**

![todo:image_alt_text](copy-shapes-between-worksheets_3.png)

### **Uppgift 2: Kopiera ett diagram från en arbetsbok till en annan**

#### **Steg 1: Kopiera ett diagram från en arbetsbok till en annan**

Följande är den faktiska koden som används av komponenten för att utföra uppgiften.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyChartFromOneWorksheetToAnother-CopyChartFromOneWorksheetToAnother.java" >}}

#### **Resultat Uppgift 2**

Efter att ha kört ovanstående kod har diagrammet från arbetsboken "Diagram" kopierats till arbetsboken "Resultat". Se följande skärmbild av resultatet.

**Arbetsbok "Resultat" med kopierad bild och diagram**

![todo:image_alt_text](copy-shapes-between-worksheets_4.png)

### **Uppgift 3: Kopiera kontroller och andra ritobjekt från en arbetsbok till en annan**

**Arbetsbok "Kontroll" med textruta och oval**

![todo:image_alt_text](copy-shapes-between-worksheets_5.png)

Se följande enkla steg som du behöver utföra för att få önskade resultat.

#### **Steg 1: Kopiera en arbetsbok mellan arbetsböcker**

Följande är koden som används av komponenten för att utföra uppgiften.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyWorksheetBetweenWorkbooks-CopyWorksheetBetweenWorkbooks.java" >}}

#### **Resultat Uppgift 3**

Efter att ha kört ovanstående kod har kontrollerna från arbetsboken "Kontroll" nu kopierats till arbetsboken "Resultat". Se följande skärmbild av "Resultat".

**Arbetsbok "Resultat" med kopierad textruta och oval**

![todo:image_alt_text](copy-shapes-between-worksheets_6.png)

## **Slutsats**

Den här artikeln har visat hur man kopierar olika former som bilder, diagram och andra ritobjekt mellan användning av Aspose.Cells. Förhoppningsvis kommer den att ge dig en inblick, och du kommer att kunna utnyttja dessa alternativ enligt dina olika scenarier.

Aspose.Cells kan erbjuda mer flexibilitet än andra för lösningar och ger enastående hastighet, effektivitet och tillförlitlighet för att uppfylla specifika affärsapplikationskrav. Resultaten visar faktiskt att Aspose.Cells har gynnats av års forskning, design och noggrant justering.

Vi välkomnar varmt dina frågor, kommentarer och förslag i [Aspose.Cells Forum](https://forum.aspose.com/c/cells/9).
{{< app/cells/assistant language="java" >}}
