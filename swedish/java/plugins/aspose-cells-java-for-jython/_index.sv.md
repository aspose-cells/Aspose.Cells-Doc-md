---
title: Aspose.Cells Java for Jython
type: docs
weight: 70
url: /sv/java/aspose-cells-java-for-jython/
---

## **Introduktion**

### **Vad är Jython?**

Jython är en Java-implementering av Python som kombinerar uttrycksfull kraft med tydlighet. Jython är fritt tillgänglig för både kommersiellt och icke-kommersiellt bruk och distribueras med källkod. Jython är kompletterande till Java och är särskilt lämpad för följande uppgifter:

- **Inbäddad skriptning** - Java-programmerare kan lägga till Jython-biblioteken till sitt system för att låta slutanvändare skriva enkla eller komplicerade script som lägger till funktionalitet i applikationen.
- **Interaktiv experimentation** - Jython tillhandahåller en interaktiv tolk som kan användas för att interagera med Java-paket eller med körande Java-applikationer. Detta gör att programmerare kan experimentera och felsöka vilket Java-system som helst med Jython.
- **Snabb applikationsutveckling** - Python-program är vanligtvis 2-10 ggr kortare än det motsvarande Java-programmet. Detta översätts direkt till ökad programmerarproduktivitet. Den sömlösa interaktionen mellan Python och Java gör att utvecklare fritt kan blanda de två språken både under utveckling och i leverans av produkter.

### **Aspose.Cells for Java**

Aspose.Cells for Java är ett avancerat klassbibliotek för Java som gör att du kan utföra ett brett utbud av dokumenthanteringsuppgifter direkt inom din Java-applikation.
applikationer.

Aspose.Cells for Java stödjer bearbetning av celler (DOC, DOCX, OOXML, RTF) HTML, OpenDocument, PDF, EPUB, XPS, SWF och alla bildformat. Med Aspose.Cells kan du skapa, modifiera och konvertera dokument utan att använda Microsoft Cells.
generera, modifiera och konvertera dokument utan att använda Microsoft Cells.

### **Aspose.Cells Java for Jython**

Aspose.Cells Java för Jython är ett projekt som demonstrerar / tillhandahåller Aspose.Cells for Java API-användningsexempel i Jython.

## **Systemkrav och stödda plattformar**

### **Systemkrav**

**Följande är systemkraven för att använda Aspose.Cells Java för Jython:**

- Java 1.5 eller senare installerat
- Nerladdad Aspose.Cells-komponent
- Jython 2.7.0

### **Stödda plattformar**

**Följande plattformar stöds:**

- Aspose.Cells 15.4 och senare.
- Java IDE (Eclipse, NetBeans...)

## **Hämta Installation och Användning**

### **Nedladdning**

**Hämta exempel från sociala kodningswebbplatser**

Följande versioner av körnings exempel är tillgängliga för nedladdning på alla nedan angivna sociala kodningssajter:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)

**Ladda ner Aspose.Cells for Java-komponenten**

- [Aspose.Cells for Java](https://releases.aspose.com/cells/java/)

### **Installation**

- Placera den nedladdade Aspose.Cells for Java-jar-filen i "lib"-mappen.
- Ersätt "din-lib" med den nedladdade jar-filens namn i _* init* _.py-filen.

### **Användning**

Du kan skapa ett HelloWorld-dokument med hjälp av följande exempelkod:

{{< highlight java >}}

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

## **Support, Utvidga och Bidra**

### **Support**

Från allra första början av Aspose visste vi att det inte bara skulle räcka med att ge våra kunder bra produkter. Vi behövde också leverera en bra service. Vi är själva utvecklare och förstår hur frustrerande det är när en teknisk fråga eller en egenhet i programvaran hindrar dig från att göra det du behöver göra. Vi är här för att lösa problem, inte skapa dem. 

Detta är anledningen till att vi erbjuder kostnadsfri support. Alla som använder våra produkter, vare sig de har köpt dem eller använder en utvärdering, förtjänar vår fulla uppmärksamhet och respekt.

Du kan logga alla frågor eller förslag relaterade till Aspose.Cells Java för Jython med hjälp av någon av följande plattformar:

- [Github](https://github.com/aspose-words/Aspose.Words-for-Java/issues)

### **Utvidga och Bidra**

Aspose.Cells Java för Jython är öppen källkod och dess källkod finns tillgänglig på de stora sociala kodningswebbplatserna som listas nedan. Utvecklare uppmanas att ladda ner källkoden och bidra genom att föreslå eller lägga till nya funktioner eller förbättra befintliga, så att andra också kan dra nytta av det.

### **Källkod**

Du kan få den senaste källkoden från någon av följande platser

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)
