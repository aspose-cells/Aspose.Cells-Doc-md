---
title: Smart Markers i sidhuvuden och sidfötter | Aspose.Cells för Java
linktitle: Smartmarkörer i sidhuvud och sidfot | Aspose.Cells
description: Placera Smart Marker-platshållare i sidhuvuden och sidfötter med dubbelvinkelparentes-syntaxen och WorkbookDesigner.setEnableHeaderFooterMarkers-flaggan med hjälp av getter-bean-listor eller JSON-datakällor, och bind bilder via data-URI,er i Aspose.Cells för Java.
keywords: Aspose.Cells för Java, Smart Markers, sidhuvuden, sidfötter, sidhuvud sidfötter markörer, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, setDataSource, getter bean, JSON datakälla, databindning, bild, data URI, Java
type: docs
weight: 196
url: /sv/java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Eventuella användningsscenarier**
Sidhuvuden och sidfötter innehåller ofta rapportmetadata såsom rapptiteln, rapportperioden, författaren och avdelningen. När denna information redan finns i datakällan som används för att fylla arbetsboken, skapar man onödig duplicering om man anger den manuellt på nytt.
Klassisk Smart Marker-syntax, `&=Source.Field`, bearbetas i kalkylbladets celler. Om du placerar en klassisk markör i ett sidhuvud eller en sidfot via `PageSetup.setHeader` eller `PageSetup.setFooter`, förblir den som literals text eftersom sidhuvud- och sidfotsträngar inte ingår i kalkylbladscellerna som skannas av `WorkbookDesigner.process()`.
Från och med **Aspose.Cells för Java 26.11** är alternativet för sidhuvud/sidfötter med markörer `false` som standardvärde. Anropa `designer.setEnableHeaderFooterMarkers(true)` innan du anropar `designer.process()` för att resolvera platshållare som skrivs som `<<Source.Field>>` i sidhuvud- och sidfotsavsnittssträngar. Sidhuvud- och sidfotsplatshållare använder samma datakälla som kroppsmarkörer.
Varje sidhuvud och sidfot innehåller tre adresserbara avsnitt:
- Avsnitt `0` är det vänstra avsnittet.
- Avsnitt `1` är det mittersta avsnittet.
- Avsnitt `2` är det högra avsnittet.
Använd `PageSetup.setHeader(int section, String value)` och `PageSetup.setFooter(int section, String value)` för att skriva dessa avsnitt. Efter bearbetning, använd `PageSetup.getHeader(int section)` och `PageSetup.getFooter(int section)` för att hämta de färdiga texterna.

{{% alert color="primary" %}}
En platshållare som `<<Source.Field>>` infogar fältvärdet som text i avsnittssträngen. Bilder bindes med suffixet `(picture)` och ett data-URI-värde.
{{% /alert %}}

## **Aktivera markörer i sidhuvud/sidfötter med en getter-bean-lista**
Använd följande sekvens för att resolvera platshållare i sidhuvud och sidfötter med en getter-bean-lista i **Aspose.Cells för Java 26.11**:
1. Skapa en `Workbook` och erhåll dess första `Worksheet` vid index `0`, till exempel med `workbook.getWorksheets().get(0)`.
2. Skriv `<<Source.Field>>`-platshållare i de önskade sidhuvud- och sidfotsavsnitten med `PageSetup.setHeader` och `PageSetup.setFooter`.
3. Definiera en liten offentlig (PUBLIC) bean-klass med en getter (till exempel `getName()`) för varje platshållarfält, och välj ett källnamn som matchar källprefixet som används av platshållarna. Till exempel stöds platshållare som `<<node.Name>>` av en källa som heter `node`. Två bindningsregler verifieras på denna plattform: en bean med offentliga FIELDS binder ingenting (motorn läser getters, inte fält), och en paketprivat (PACKAGE-PRIVATE) klass binder inte heller — introspektionen ser endast offentliga klasser, och en icke-offentlig bean misslyckas med `process()` med en NullPointerException.
4. Skapa en `WorkbookDesigner` för arbetsboken.
5. Anropa `designer.setEnableHeaderFooterMarkers(true)` innan bearbetning.
6. Bifoga listan och dess källnamn med `designer.setDataSource("node", table)`.
7. Anropa `designer.process()`.
8. Efter bearbetning finns platshållarna inte längre i sidhuvud- eller sidfotstexten. Använd `PageSetup.getHeader` och `PageSetup.getFooter` för att hämta de färdiga avsnittssträngarna.

```java
import com.aspose.cells.*;
import java.util.*;
public class CodeRunner {
    public static class Node {
        private final String name;
        private final String author;
        public Node(String name, String author) {
            this.name = name;
            this.author = author;
        }
        public String getName() {
            return name;
        }
        public String getAuthor() {
            return author;
        }
    }
    public static void main(String[] args) throws Exception {
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        // Center header and center footer carry <<Source.Field>> placeholders
        worksheet.getPageSetup().setHeader(1, "Quarterly Report - <<node.Name>>");
        worksheet.getPageSetup().setFooter(1, "Prepared by <<node.Author>>");
        List<Node> table = Arrays.asList(new Node("Q4 2026", "Aspose.Cells"));
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setEnableHeaderFooterMarkers(true);
        designer.setDataSource("node", table);
        designer.process();
        System.out.println("Header: " + worksheet.getPageSetup().getHeader(1));
        System.out.println("Footer: " + worksheet.getPageSetup().getFooter(1));
        // This prints:
        // Header: Quarterly Report - Q4 2026
        // Footer: Prepared by Aspose.Cells
        workbook.save("HeaderFooterSmartMarkers.xlsx");
    }
}
```

## **Använda en JSON-datakälla**
Du kan använda JSON istället för en getter-bean-lista när rapportdata redan finns i JSON-format. Anropa `WorkbookDesigner.setJsonDataSource(String name, String json)` för att bifoga källan.
Argumentet `name` är källnamnet som används av platshållarna. Till exempel stöds platshållare som `<<node.Company>>` och `<<node.Title>>` av namnet `node`.
Skicka raddata direkt till `setJsonDataSource`:
- Ett radarray, till exempel ett JSON-array som innehåller ett eller flera radobjekt, stöds.
- Ett enda radobjekt kan också skickas direkt.
- Lägg inte raderna under en namngiven toppnivånyckel som `{"rows":[...]}`. Detta wrapper är inte den förväntade radorienterade indataformatet för denna arbetsflödesmetod.
En JSON-källa kan fylla båda markörstilarna under samma `designer.process()`-anrop. Den kan resolvera en klassisk `&=`-markör i en kalkylbladscell och dubbelvinkelparentes-`<<>>`-platshållare i sidhuvud- och sidfotsavsnitt. Du måste fortfarande aktivera `EnableHeaderFooterMarkers` för att sidhuvud- och sidfotsplatshållare ska resolveras.

```java
import com.aspose.cells.*;
public class CodeRunner {
    public static void main(String[] args) throws Exception {
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        // Left header, right header, and a classic body marker — one JSON source feeds all three
        worksheet.getPageSetup().setHeader(0, "<<node.Company>>");
        worksheet.getPageSetup().setHeader(2, "Page <<node.Title>>");
        worksheet.getCells().get("A1").putValue("&=node.Company");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setEnableHeaderFooterMarkers(true);
        designer.setJsonDataSource("node", "[{\"Company\":\"Aspose Pty Ltd\",\"Title\":\"Half-Year Report\"}]");
        designer.process();
        System.out.println("Left: " + worksheet.getPageSetup().getHeader(0));
        System.out.println("Right: " + worksheet.getPageSetup().getHeader(2));
        System.out.println("Body: " + worksheet.getCells().get("A1").getStringValue());
        // This prints:
        // Left: Aspose Pty Ltd
        // Right: Page Half-Year Report
        // Body: Aspose Pty Ltd
        workbook.save("HeaderFooterJsonMarkers.xlsx");
    }
}
```

## **Switch och flerradsdatakällsemantik**
Inställningen `EnableHeaderFooterMarkers` är `false` som standard, och inställningen styr endast sidhuvud- och sidfotsplatshållarna `<<Source.Field>>`. När inställningen är avstängd, resolverar `designer.process()` fortfarande klassiska `&=`-kroppsmarkörer, men en `<<Source.Field>>`-platshållare i ett sidhuvud eller en sidfot förblir literals text.
Ett sidhuvud eller en sidfotsavsnitt är en sträng, inte ett upprepande band. Om datakällan innehåller flera rader, ger den första raden värdena för sidhuvud och sidfot. Efter resolvering blir värdena vanlig sidhuvud- eller sidfotstext. De finns kvar i arbetsboken efter att du anropar `workbook.save(...)` och finns när du laddar den sparade arbetsboken igen.
Följande exempel skapar två arbetsböcker över samma flerradsbean-lista för att jämföra beteendet med avstängd och aktiverad inställning. `plainDesigner` lämnar platshållaren oförändrad, medan `enabledDesigner` resolverar den med hjälp av den första raden.

```java
import com.aspose.cells.*;
import java.util.*;
public class CodeRunner {
    public static class Node {
        private final String name;
        public Node(String name) {
            this.name = name;
        }
        public String getName() {
            return name;
        }
    }
    public static void main(String[] args) throws Exception {
        List<Node> table = Arrays.asList(
                new Node("First Row"),
                new Node("Second Row")
        );
        // Without the switch the placeholder stays literal text
        Workbook plainWorkbook = new Workbook();
        Worksheet plainSheet = plainWorkbook.getWorksheets().get(0);
        plainSheet.getPageSetup().setHeader(1, "<<node.Name>>");
        WorkbookDesigner plainDesigner = new WorkbookDesigner(plainWorkbook);
        plainDesigner.setDataSource("node", table);
        plainDesigner.process();
        // With the switch on, the FIRST row of a multi-row source wins
        Workbook enabledWorkbook = new Workbook();
        Worksheet enabledSheet = enabledWorkbook.getWorksheets().get(0);
        enabledSheet.getPageSetup().setHeader(1, "<<node.Name>>");
        WorkbookDesigner enabledDesigner = new WorkbookDesigner(enabledWorkbook);
        enabledDesigner.setEnableHeaderFooterMarkers(true);
        enabledDesigner.setDataSource("node", table);
        enabledDesigner.process();
        System.out.println("Without switch: " + plainSheet.getPageSetup().getHeader(1));
        System.out.println("With switch: " + enabledSheet.getPageSetup().getHeader(1));
        // This prints:
        // Without switch: <<node.Name>>
        // With switch: First Row
        enabledWorkbook.save("HeaderFooterMarkersEnabled.xlsx");
    }
}
```

## **Binda en bild i ett sidhuvud eller en sidfot**
Suffixet `(picture)` binder en bild i ett sidhuvud- eller sidfotsavsnitt. Skriv `<<node.logo(picture)>>` där bilden ska visas, och ange fältvärdet som en data-URI — prefixet `data:image/png;base64,` följt av Base64-texten för bildens byter. En ren Base64-sträng utan `data:`-prefixet bäddar inte in en bild.
Efter `designer.process()`:
1. Platshållaren ersätts av `&G`, den standardiserade sidhuvud- och sidfotsbildkoden. Eftersom markören blir en kod i avsnittssträngen, kan den finnas inne i längre text som `Logo: <<node.logo(picture)>>`.
2. Bildens byter bäddas in i arbetsboken som en mediadel som är kopplad till sidhuvud/sidfotens ritlager för det kalkylbladet, så bilden skrivs ut tillsammans med sidhuvudet eller sidfoten.

```java
import com.aspose.cells.*;
import java.nio.file.*;
import java.util.*;
public class CodeRunner {
    public static class Node {
        private final String logo;
        public Node(String logo) {
            this.logo = logo;
        }
        public String getLogo() {
            return logo;
        }
    }
    public static void main(String[] args) throws Exception {
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        // The (picture) suffix binds the image named by the data-URI field into the header
        worksheet.getPageSetup().setHeader(1, "Logo: <<node.logo(picture)>>");
        String logoDataUri = "data:image/png;base64," + Base64.getEncoder().encodeToString(Files.readAllBytes(Paths.get("logo.png")));
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setEnableHeaderFooterMarkers(true);
        designer.setDataSource("node", Arrays.asList(new Node(logoDataUri)));
        designer.process();
        System.out.println("Header: " + worksheet.getPageSetup().getHeader(1));
        // This prints:
        // Header: Logo: &G
        workbook.save("HeaderFooterPicture.xlsx");
    }
}
```

Den utskrivna `&G` är bildkoden som Excel tolkar vid rendering av sidhuvudet — `logo.png`-bytarna finns nu inuti `HeaderFooterPicture.xlsx`, och bilden skrivs ut på platsen för koden.
För att använda Smart Markers i sidhuvud och sidfötter, skriv `<<Source.Field>>`-platshållare i vänstra, mittersta och högra sidhuvud- eller sidfotsavsnitt med `PageSetup.setHeader` och `PageSetup.setFooter`. Anropa `designer.setEnableHeaderFooterMarkers(true)` på `WorkbookDesigner` innan `designer.process()`, och ange värden genom `designer.setDataSource(name, list)` med en getter-bean-lista eller `designer.setJsonDataSource(name, json)`. Läs de färdiga avsnitten med `PageSetup.getHeader` och `PageSetup.getFooter`. Samma datakälla kan fylla kroppsmarkörer och sidhuvud- eller sidfotsplatshållare i ett enda bearbetningssteg. Lägg till suffixet `(picture)` med ett data-URI-värde för att binda en bild i ett avsnitt.

## Relaterade artiklar
- [SmartMarker Single Cell Array Rendering](/cells/sv/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="java" >}}