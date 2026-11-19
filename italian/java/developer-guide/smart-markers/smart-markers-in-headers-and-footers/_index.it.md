---
title: Smart Marker nelle intestazioni e nei piè di pagina | Aspose.Cells for Java
description: Inserisci segnaposti Smart Marker nelle intestazioni e nei piè di pagina delle pagine con la sintassi a doppio segno di maggiore e l'interruttore WorkbookDesigner.setEnableHeaderFooterMarkers utilizzando elenchi di bean getter o fonti di dati JSON, e associa immagini tramite URI dei dati, in Aspose.Cells for Java.
linktitle: Smart Marker intestazione e piè di pagina | Aspose.Cells
keywords: Aspose.Cells for Java, Smart Marker, intestazioni, piè di pagina, segnaposti intestazione piè di pagina, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, setDataSource, bean getter, origine dati JSON, associazione dati, immagine, URI dati, Java
type: docs
weight: 196
url: /it/java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
Le intestazioni e i piè di pagina contengono spesso metadati del report, come il titolo del report, il periodo di riferimento, l'autore e il dipartimento. Quando queste informazioni sono già presenti nella fonte dati usata per popolare la cartella di lavoro, ripeterle manualmente crea duplicazioni inutili.  
La sintassi classica di Smart Marker, `&=Source.Field`, viene elaborata nelle celle del corpo del foglio di lavoro. Se si inserisce un marcatore classico in un'intestazione o in un piè di pagina tramite `PageSetup.setHeader` o `PageSetup.setFooter`, rimane testo letterale perché le stringhe di intestazione e piè di pagina non fanno parte della griglia di celle scansionata da `WorkbookDesigner.process()`.  
A partire da **Aspose.Cells for Java 26.11**, l'opzione dei segnaposti intestazione/piè di pagina di `WorkbookDesigner` è `false` per impostazione predefinita. Chiamare `designer.setEnableHeaderFooterMarkers(true)` prima di `designer.process()` consente di risolvere i segnaposti scritti come `<<Source.Field>>` nelle stringhe di intestazione e piè di pagina. I segnaposti intestazione e piè di pagina utilizzano la stessa fonte dati dei marcatori del corpo.  
Ogni intestazione e piè di pagina contiene tre sezioni indirizzabili:
- La sezione `0` è la sezione sinistra.
- La sezione `1` è la sezione centrale.
- La sezione `2` è la sezione destra.  
Utilizzare `PageSetup.setHeader(int section, String value)` e `PageSetup.setFooter(int section, String value)` per scrivere queste sezioni. Dopo l'elaborazione, utilizzare `PageSetup.getHeader(int section)` e `PageSetup.getFooter(int section)` per recuperare il testo completato.

{{% alert color="primary" %}}
Un segnaposto come `<<Source.Field>>` inserisce il valore del campo come testo nella stringa della sezione. Le immagini vengono associate con il suffisso `(picture)` e un valore data-URI.
{{% /alert %}}

## **Abilitare i segnaposti intestazione/piè di pagina con un elenco bean getter**
Utilizzare la seguente sequenza per risolvere i segnaposti intestazione e piè di pagina con un elenco bean getter in **Aspose.Cells for Java 26.11**:
1. Creare un `Workbook` e ottenere il suo primo `Worksheet` all'indice `0`, ad esempio con `workbook.getWorksheets().get(0)`.
2. Scrivere segnaposti `<<Source.Field>>` nelle sezioni di intestazione e piè di pagina desiderate con `PageSetup.setHeader` e `PageSetup.setFooter`.
3. Definire una piccola classe PUBLIC bean con un getter (ad esempio, `getName()`) per ogni campo segnaposto, e scegliere un nome di sorgente che corrisponda al prefisso sorgente usato dai segnaposti. Per esempio, una sorgente denominata `node` supporta segnaposti come `<<node.Name>>`. Due regole di associazione sono verificate su questa piattaforma: un bean con campi PUBLIC non associa nulla (il motore legge i getter, non i campi), e una classe PACKAGE-PRIVATE non associa nulla — l'introspezione vede solo le classi pubbliche, e un bean non pubblico provoca un `NullPointerException` durante `process()`.
4. Creare un `WorkbookDesigner` per la cartella di lavoro.
5. Chiamare `designer.setEnableHeaderFooterMarkers(true)` prima dell'elaborazione.
6. Allegare l'elenco e il relativo nome di sorgente con `designer.setDataSource("node", table)`.
7. Chiamare `designer.process()`.
8. Dopo l'elaborazione, i segnaposti non sono più presenti nel testo dell'intestazione o del piè di pagina. Utilizzare `PageSetup.getHeader` e `PageSetup.getFooter` per recuperare le stringhe di sezione completate.

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

## **Utilizzare una fonte dati JSON**
È possibile usare JSON anziché un elenco bean getter quando i dati del report sono già disponibili in formato JSON. Chiamare `WorkbookDesigner.setJsonDataSource(String name, String json)` per allegare la sorgente.  
L'argomento `name` è il nome di sorgente usato dai segnaposti. Per esempio, il nome `node` supporta segnaposti come `<<node.Company>>` e `<<node.Title>>`.  
Passare i dati di riga direttamente a `setJsonDataSource`:
- È supportato un array di righe, ad esempio un array JSON contenente uno o più oggetti riga.
- È anche possibile passare direttamente un singolo oggetto riga.
- Non avvolgere le righe sotto una chiave di livello superiore denominata, ad esempio `{"rows":[...]}`. Questo wrapper non corrisponde alla forma di input orientata alle righe prevista per questo flusso di lavoro.  
Una singola fonte JSON può popolare entrambi gli stili di marcatore durante la stessa chiamata `designer.process()`. Può risolvere un marcatore classico `&=` in una cella del corpo del foglio e segnaposti a doppio segno di maggiore `<<>>` nelle sezioni di intestazione e piè di pagina. È comunque necessario abilitare `EnableHeaderFooterMarkers` affinché i segnaposti intestazione/piè di pagina vengano risolti.

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

## **Semantica dell'interruttore e della fonte multi-riga**
L'impostazione `EnableHeaderFooterMarkers` è `false` per impostazione predefinita, e l'interruttore controlla solo i segnaposti `<<Source.Field>>` di intestazione e piè di pagina. Quando l'interruttore è disattivato, `designer.process()` continua a risolvere i marcatori classici `&=` nel corpo, ma un segnaposto `<<Source.Field>>` in intestazione o piè di pagina rimane testo letterale.  
Una sezione di intestazione o piè di pagina è una singola stringa, non una banda ripetitiva. Se la fonte dati contiene più righe, la prima riga fornisce i valori per intestazione e piè di pagina. Una volta risolti, i valori diventano testo ordinario di intestazione o piè di pagina. Restano nella cartella di lavoro dopo aver chiamato `workbook.save(...)` e sono presenti quando si carica nuovamente la cartella di lavoro salvata.  
L'esempio seguente crea due cartelle di lavoro sulla stessa lista bean multi-riga per confrontare il comportamento disabilitato e quello abilitato. Il `plainDesigner` lascia il segnaposto invariato, mentre il `enabledDesigner` lo risolve usando la prima riga.

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

## **Associa un'immagine a un'intestazione o a un piè di pagina**
Il suffisso `(picture)` associa un'immagine a una sezione di intestazione o piè di pagina. Scrivere `<<node.logo(picture)>>` dove deve apparire l'immagine e fornire il valore del campo come data URI — il prefisso `data:image/png;base64,` seguito dal testo Base64 dei byte dell'immagine. Una stringa Base64 senza il prefisso `data:` non incorpora un'immagine.  
Dopo `designer.process()`:
1. Il segnaposto viene sostituito da `&G`, il codice standard per immagini di intestazione e piè di pagina. Poiché il marcatore diventa un codice all'interno della stringa di sezione, può trovarsi all'interno di testo più lungo, ad esempio `Logo: <<node.logo(picture)>>`.
2. I byte dell'immagine vengono incorporati nella cartella di lavoro come parte multimediale allegata al livello di disegno intestazione/piè di pagina di quel foglio, quindi l'immagine stampa con l'intestazione o il piè di pagina.

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

Il codice `&G` stampato è il codice immagine che Excel interpreta durante il rendering dell'intestazione — i byte di `logo.png` ora vivono all'interno di `HeaderFooterPicture.xlsx`, e l'immagine stampa al posto del codice.  
Per utilizzare i Smart Marker in intestazioni e piè di pagina, scrivere segnaposti `<<Source.Field>>` nelle sezioni sinistra, centrale e destra con `PageSetup.setHeader` e `PageSetup.setFooter`. Chiamare `designer.setEnableHeaderFooterMarkers(true)` sul `WorkbookDesigner` prima di `designer.process()`, e fornire i valori tramite `designer.setDataSource(name, list)` con un elenco bean getter oppure `designer.setJsonDataSource(name, json)`. Leggere le sezioni completate con `PageSetup.getHeader` e `PageSetup.getFooter`. La stessa fonte dati può popolare marcatori del corpo e segnaposti di intestazione o piè di pagina in un unico passaggio di elaborazione. Aggiungere il suffisso `(picture)` con un valore data-URI per associare un'immagine a una sezione.

## Articoli correlati
- [Rendering di SmartMarker per array a singola cella](/cells/it/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="java" >}}