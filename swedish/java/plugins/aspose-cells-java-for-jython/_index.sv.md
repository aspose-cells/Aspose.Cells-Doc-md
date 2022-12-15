---
title: Aspose.Cells Java för Jython
type: docs
weight: 70
url: /sv/java/aspose-cells-java-for-jython/
---
## **Introduktion**

### **Vad är Jython?**

Jython är en Java-implementering av Python som kombinerar uttryckskraft med klarhet. Jython är fritt tillgänglig för både kommersiell och icke-kommersiell användning och distribueras med källkod. Jython är ett komplement till Java och är speciellt lämpad för följande uppgifter:

- **Inbäddat skript** - Java programmerare kan lägga till Jython-biblioteken till sina system för att tillåta slutanvändare att skriva enkla eller komplicerade skript som lägger till funktionalitet till applikationen.
- **Interaktiva experiment** - Jython tillhandahåller en interaktiv tolk som kan användas för att interagera med Java-paket eller för att köra Java-applikationer. Detta tillåter programmerare att experimentera och felsöka vilket Java-system som helst med Jython.
- **Snabba applikationsutveckling** Python-program är vanligtvis 2-10 gånger kortare än motsvarande Java-program. Detta leder direkt till ökad programmerares produktivitet. Den sömlösa interaktionen mellan Python och Java tillåter utvecklare att fritt blanda de två språken både under utveckling och i leverans av produkter.

### **Aspose.Cells for Java**

Aspose.Cells for Java är ett avancerat klassbibliotek for Java som gör att du kan utföra ett stort antal dokumentbehandlingsuppgifter direkt i din Java
applikationer.

Aspose.Cells for Java stöder bearbetning Cells (DOC, DOCX, OOXML, RTF) HTML, OpenDocument, PDF, EPUB, XPS, SWF och alla bildformat. Med Aspose.Cells kan du
generera, ändra och konvertera dokument utan att använda Microsoft Cells.

### **Aspose.Cells Java för Jython**

Aspose.Cells Java för Jython är ett projekt som demonstrerar / tillhandahåller Aspose.Cells for Java API användningsexempel i Jython.

## **Systemkrav och plattformar som stöds**

### **Systemkrav**

**Följande är systemkraven för att använda Aspose.Cells Java för Jython:**

- Java 1,5 eller högre installerad
- Laddade ned Aspose.Cells komponent
- Jython 2.7.0

### **Plattformar som stöds**

**Följande är de plattformar som stöds:**

- Aspose.Cells 15.4 och uppåt.
- Java IDE (Eclipse, NetBeans ...)

## **Ladda ner Installation och användning**

### **Laddar ner**

**Ladda ner exempel från webbplatser för social kodning**

Följande versioner av löpande exempel finns att ladda ner på alla nedan nämnda webbplatser för social kodning:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)

**Ladda ner komponenten Aspose.Cells for Java**

- [Aspose.Cells for Java](https://releases.aspose.com/cells/java/)

### **Installerar**

- Placera den nedladdade Aspose.Cells for Java jar-filen i "lib"-katalogen.
- Ersätt "your-lib" med det nedladdade jar-filnamnet i filen _*init*_.py.

### **Använder sig av**

Du kan skapa HelloWorld-dokument med följande exempelkod:

{{< highlight "java" >}}

 from aspose-cells  import Settings

from com.aspose.Cells import Document

from com.aspose.Cells import DocumentBuilder

class HelloWorld:

    def __init__(self):

        dataDir = Settings.dataDir + 'quickstart/'



        workbook = Workbook()



        sheet = workbook.getWorksheets().get(0)



        cell = sheet.getCells().get("A1")



        cell.setValue("Hello World!")



        file_format_type = FileFormatType



        workbook.save(dataDir + "HelloWorld.xls" , file_format_type.EXCEL_97_TO_2003 )



        print "Document has been saved, please check the output file.";

if __name__ == '__main__':

    HelloWorld()

{{< /highlight >}}

## **Stödja, utöka och bidra**

### **Stöd**

Från de allra första dagarna av Aspose visste vi att det inte skulle räcka att bara ge våra kunder bra produkter. Vi behövde också leverera bra service. Vi är själva utvecklare och förstår hur frustrerande det är när ett tekniskt problem eller en egenhet i programvaran hindrar dig från att göra det du behöver göra. Vi är här för att lösa problem, inte skapa dem.

Det är därför vi erbjuder gratis support. Alla som använder vår produkt, oavsett om de har köpt dem eller använder en utvärdering, förtjänar vår fulla uppmärksamhet och respekt.

Du kan logga alla problem eller förslag relaterade till Aspose.Cells Java för Jython med någon av följande plattformar:

- [Github](https://github.com/aspose-words/Aspose.Words-for-Java/issues)

### **Utöka och bidra**

Aspose.Cells Java för Jython är öppen källkod och dess källkod är tillgänglig på de stora sociala kodningswebbplatserna nedan. Utvecklare uppmuntras att ladda ner källkoden och bidra genom att föreslå eller lägga till nya funktioner eller förbättra de befintliga, så att andra också kan dra nytta av den.

### **Källkod**

Du kan få den senaste källkoden från en av följande platser

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)
