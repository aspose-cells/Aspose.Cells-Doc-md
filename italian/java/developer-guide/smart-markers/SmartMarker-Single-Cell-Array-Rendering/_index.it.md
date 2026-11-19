---
title: Rendering di un array in una singola cella con SmartMarker | Aspose.Cells for Java
description: Scopri come eseguire il rendering dei dati di un array in un'unica cella utilizzando gli attributi Smart Marker arrayassingle e arraydelimiter in Aspose.Cells for Java.
linktitle: Rendering di array in singola cella | Aspose.Cells
url: /it/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, libreria Java, foglio di lavoro, Smart Marker, arrayassingle, arraydelimiter, array a singola cella, rendering di array, modello
type: docs
weight: 195
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells può eseguire il rendering di un'origine dati di tipo array in un'unica cella tramite gli Smart Marker. L'attributo `arrayassingle` disattiva l'espansione predefinita elemento per elemento, mentre l'attributo `arraydelimiter` determina il separatore inserito tra gli elementi uniti — una virgola per impostazione predefinita, oppure un singolo carattere o una stringa di più caratteri tra virgolette a scelta.
{{% /alert %}}

## **Introduzione**

Gli Smart Marker di Aspose.Cells sono una funzionalità basata su modelli che popola dinamicamente i dati del foglio di lavoro tramite espressioni marker come `&=DataSource.Field`. Il marker viene inserito in una cartella di lavoro di progettazione e, quando il modello viene elaborato da `WorkbookDesigner`, i marker vengono sostituiti dai valori dell'origine dati fornita.
Per impostazione predefinita, quando uno Smart Marker fa riferimento a una proprietà di tipo array (ad esempio, `&=Product.Tags` associato a un `String[]` di quattro valori), il motore espande l'array e inserisce ogni elemento in una cella separata, distribuendo i valori verticalmente nella colonna sotto il marker. Sebbene questo comportamento sia comodo in molti scenari, in alcune situazioni è preferibile eseguire il rendering dell'intero array in un'unica cella, con gli elementi concatenati e separati da un delimitatore a scelta.
Gli attributi `arrayassingle` e `arraydelimiter`, scritti tra le parentesi di uno Smart Marker nel formato `name:value`, soddisfano esattamente questa esigenza. Consentono di mantenere layout dei report compatti e prevedibili, continuando a utilizzare in modo nativo origini dati di tipo array.

## **Perché questa funzionalità è necessaria**

### **Comportamento predefinito di espansione degli array**

Quando uno Smart Marker fa riferimento a una proprietà di tipo array, Aspose.Cells espande l'array su più celle per impostazione predefinita. Ad esempio, un marker come `&=Product.Tags` associato a un `String[]` contenente quattro valori inserisce ciascun valore in una cella separata sotto il marker, spostando gli altri contenuti del modello verso il basso e potenzialmente compromettendo layout di report progettati con cura.

### **Limiti dei casi d'uso**

In molti scenari pratici, il comportamento predefinito di espansione non è opportuno:
- **Report di riepilogo** che richiedono un layout compatto con una sola riga per record.
- **Elenchi di tag, etichette o parole chiave** che devono essere visualizzati come valori separati da virgole o barre verticali all'interno di un'unica cella.
- **Chip di filtro o indicatori di stato** che raggruppano più valori in un unico punto per migliorare la leggibilità.
- **Flussi di elaborazione successivi** (esportazione CSV, rendering PDF, stampa unione) che richiedono un singolo valore consolidato per cella anziché un intervallo espanso.
- **Compatibilità multipiattaforma**, quando alcuni destinatari non tollerano array che si estendono su più celle.

### **La lacuna che colma**

Senza un meccanismo integrato, gli sviluppatori sarebbero costretti a pre-elaborare i dati in Java — unendo gli array in stringhe delimitate prima di associarli alla cartella di lavoro di progettazione. Ciò duplica la logica, complica i modelli dati e aumenta la probabilità di errori. Gli attributi `arrayassingle` e `arraydelimiter` eliminano questa soluzione alternativa gestendo la formattazione in modo dichiarativo direttamente nello Smart Marker.

## **Vantaggi della funzionalità**

L'utilizzo degli attributi `arrayassingle` e `arraydelimiter` negli Smart Marker offre diversi vantaggi:
- **Contenimento in un'unica cella**: Tutti gli elementi dell'array vengono visualizzati in esattamente una cella, mantenendo layout compatti e prevedibili.
- **Controllo del delimitatore personalizzato**: Specificare il separatore desiderato — la virgola predefinita, un punto e virgola, un trattino, una barra verticale o una stringa di più caratteri tra virgolette come `" | "`.
- **Formattazione guidata dal modello**: Non è necessario codice aggiuntivo per pre-elaborare i dati; le regole di formattazione risiedono nel tag Smart Marker.
- **Report più puliti**: I dati di tipo array non spostano più il contenuto circostante del modello in righe o colonne diverse.
- **Tipi di dati versatili**: Funziona con array di stringhe e con valori numerici convertiti in stringa provenienti da origini dati bean.
- **Compatibilità con le versioni precedenti**: Quando gli attributi vengono omessi, viene preservato il comportamento originale di espansione, così i modelli esistenti continuano a funzionare senza modifiche.

## **Come utilizzare questa funzionalità**

### **Sintassi dello Smart Marker**

Gli attributi `arrayassingle` e `arraydelimiter` utilizzano la grammatica degli attributi `name:value` di Aspose.Cells all'interno delle parentesi di uno Smart Marker standard. La sintassi generale è:

```
&=DataSource.ArrayProperty(arrayassingle:true,arraydelimiter:;)
```

Lo Smart Marker è composto dalle seguenti parti:
- `&=DataSource.ArrayProperty` — lo Smart Marker standard che fa riferimento alla proprietà di tipo array dell'origine dati associata.
- `arrayassingle:true` — indica al motore di eseguire il rendering dell'intero array in un'unica cella anziché espandere gli elementi.
- `arraydelimiter:;` — opzionale; definisce il separatore inserito tra gli elementi dell'array. Se viene omesso, viene utilizzata una virgola.

{{% alert color="warning" %}}
Scrivere gli attributi nel formato `name:value` (due punti, non un segno uguale) e separare più attributi con una virgola **senza spazi**. Uno spazio dopo la virgola sposta di un carattere il valore analizzato — `(arrayassingle:true, arraydelimiter:;)` unirebbe gli elementi con il separatore errato `:;` anziché `;`.
{{% /alert %}}

### **Forme del delimitatore**

- Un carattere singolo segue direttamente i due punti: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- Un separatore di più caratteri viene scritto tra doppi apici: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Flusso di lavoro dettagliato**

Il flusso seguente descrive come eseguire il rendering di un array in un'unica cella utilizzando gli Smart Marker.
1. **Preparare l'origine dati**: Creare una classe bean `public` con un getter che restituisca l'array, come `String[] getTags()`, e associare un `java.util.List` di bean in modo che il motore legga un record per ogni riga. I soli campi pubblici non vengono associati: il motore legge i getter JavaBean.
2. **Creare una cartella di lavoro di progettazione**: Creare un nuovo `Workbook`, aggiungere una riga di intestazione e inserire in una cella uno Smart Marker che faccia riferimento alla proprietà dell'array con l'attributo `arrayassingle` (e `arraydelimiter` quando è necessario un separatore personalizzato).
3. **Istanziare `WorkbookDesigner`**: Creare un `WorkbookDesigner` per la cartella di lavoro e associare l'elenco con `setDataSource`.
4. **Elaborare i marker**: Chiamare il metodo `WorkbookDesigner.process()` per espandere gli Smart Marker e popolare la cartella di lavoro con i dati effettivi.
5. **Salvare il risultato**: Salvare la cartella di lavoro risultante su disco in XLSX o in qualsiasi altro formato di file supportato.

### **Esempio di codice 1 — Rendering di base di un array di stringhe**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    // The bean must be public and expose a getter; public fields bind nothing
    public static class Product {
        private String[] tags;
        public String[] getTags() { return tags; }
        public void setTags(String[] tags) { this.tags = tags; }
    }

    public static void main(String[] args) throws Exception {
        Product product = new Product();
        product.setTags(new String[] { "C#", "Aspose", "SmartMarker", "Excel" });
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        worksheet.getCells().get("A1").putValue("Tags");
        // No spaces inside the parentheses: attributes are name:value pairs
        worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Product", Arrays.asList(product));
        designer.process();
        System.out.println(worksheet.getCells().get("A2").getStringValue());
        workbook.save("output-array-single.xlsx");
    }
}
```

L'esempio stampa il valore concatenato dell'intero array. I quattro tag finiscono in un'unica cella, separati dalla virgola predefinita:

```
C#,Aspose,SmartMarker,Excel
```

### **Esempio di codice 2 — Valori numerici con un delimitatore personalizzato**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    public static class Student {
        private String[] scores;
        public String[] getScores() { return scores; }
        public void setScores(String[] scores) { this.scores = scores; }
    }

    public static void main(String[] args) throws Exception {
        Student student = new Student();
        student.setScores(new String[] { "95", "88", "76", "100", "67" });
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        worksheet.getCells().get("A1").putValue("Scores");
        // arraydelimiter:- joins the values with a hyphen
        worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Student", Arrays.asList(student));
        designer.process();
        System.out.println(worksheet.getCells().get("A2").getStringValue());
        workbook.save("output-array-numeric.xlsx");
    }
}
```

I valori numerici vengono uniti esattamente come le stringhe quando la proprietà dell'array restituisce `String[]`:

```
95-88-76-100-67
```

{{% alert color="note" %}}
Mantenere in Java la proprietà dell'array come `String[]`. Una proprietà `int[]` primitiva, quando viene unita in un'unica cella, esegue il rendering del testo restituito da `toString` per l'oggetto array (ad esempio `[I@1a2b3c4d`) anziché dei numeri, perché l'unione opera sulla forma testuale di ciascun elemento e un array primitivo è un unico elemento opaco.
{{% /alert %}}

### **Esempio di codice 3 — Confronto tra rendering predefinito e rendering in singola cella**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    public static class Order {
        private String[] items;
        public String[] getItems() { return items; }
        public void setItems(String[] items) { this.items = items; }
    }

    public static void main(String[] args) throws Exception {
        Order order = new Order();
        order.setItems(new String[] { "Apple", "Banana", "Cherry", "Date" });
        Workbook workbook = new Workbook();
        Cells cells = workbook.getWorksheets().get(0).getCells();
        // Column B: default marker — values spread vertically down the column
        cells.get("B1").putValue("Default");
        cells.get("B2").putValue("&=Order.Items");
        // Column C: single-cell rendering — the whole array joins into one cell
        cells.get("C1").putValue("Single cell");
        cells.get("C2").putValue("&=Order.Items(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Order", Arrays.asList(order));
        designer.process();
        for (int row = 1; row <= 5; row++) {
            String b = cells.get(row, 1).getStringValue();
            String c = cells.get(row, 2).getStringValue();
            if (b != null && !b.isEmpty() || c != null && !c.isEmpty())
                System.out.println("B" + (row + 1) + "=[" + b + "]  C" + (row + 1) + "=[" + c + "]");
        }
        workbook.save("output-array-comparison.xlsx");
    }
}
```

Il marker predefinito riempie una cella per elemento lungo la colonna B, mentre il marker `arrayassingle` raccoglie lo stesso array in un'unica cella della colonna C:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Note e procedure consigliate**

Tenere presenti i seguenti aspetti quando si lavora con gli attributi `arrayassingle` e `arraydelimiter`:
- I valori degli attributi usano il formato `name:value`. Il formato con segno uguale, come `arrayassingle=true`, non viene riconosciuto e il sistema ricade senza avviso nel comportamento predefinito di espansione.
- Separare gli attributi con una virgola e senza spazi; uno spazio dopo la virgola sposta di un carattere il valore del delimitatore (vedere l'avviso precedente).
- Il valore `arraydelimiter` può essere un singolo carattere scritto direttamente dopo i due punti oppure una stringa di più caratteri racchiusa tra doppi apici.
- Quando `arraydelimiter` viene omesso, gli elementi vengono uniti con una virgola.
- Associare un `java.util.List` di JavaBean pubblici dotati di getter che restituiscono array. Un singolo oggetto bean o i soli campi pubblici non permettono la risoluzione dei marker.
- Mantenere le proprietà dell'array come `String[]`; un `int[]` primitivo esegue il rendering del proprio testo restituito da `toString` quando viene unito (vedere la nota precedente).
- Posizionare lo Smart Marker in una cella con larghezza sufficiente per visualizzare la stringa concatenata risultante; in caso contrario, il contenuto può riversarsi visivamente nelle celle adiacenti, a seconda del formato.

## **Articoli correlati**
- [Aggiungere campi filtro a una tabella pivot in Aspose.Cells for Java](/cells/it/java/add-page-field-in-pivot-table/)
- [Applica stili alle tabelle pivot in Aspose.Cells for Java](/cells/it/java/apply-style-to-pivot-table/)
- [Modificare il layout del campo pagina in una tabella pivot](/cells/it/java/change-page-field-layout/)
- [Converti lo Sparkline in immagine e HTML con Aspose.Cells for Java](/cells/it/java/convert-sparkline-to-image-and-html/)
- [Conversione di Excel in formato OFD](/cells/it/java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="java" >}}