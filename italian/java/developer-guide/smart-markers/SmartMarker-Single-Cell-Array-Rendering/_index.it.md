---
title: Rendering di array in una singola cella con SmartMarker | Aspose.Cells Java
linktitle: Rendering di array
description: Scopri come renderizzare i dati di array in una singola cella utilizzando gli attributi ArrayAsSingle e ExtraDelimiter in Smart Markers con Aspose.Cells for Aspose.Cells for Java.
keywords: Aspose.Cells, libreria Java, foglio di calcolo, Smart Markers, ArrayAsSingle, ExtraDelimiter, array in singola cella, rendering di array, modello
type: docs
weight: 195
url: /it/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells supporta il rendering dei dati di array in una singola cella tramite Smart Markers. Utilizzando l'attributo `ArrayAsSingle` insieme all'attributo `ExtraDelimiter`, gli sviluppatori possono controllare come gli elementi dell'array vengono separati all'interno di una singola cella, offrendo una formattazione flessibile per report e modelli.

{{% /alert %}}

## **Introduzione**

Gli Smart Markers in Aspose.Cells sono una potente funzionalità basata su modelli che consente di popolare dinamicamente i dati del foglio di calcolo utilizzando espressioni di marcatori come `&=DataSource.Field`. Il marcatore viene posizionato in una cartella di lavoro designer e, quando il modello viene elaborato dal `WorkbookDesigner`, i marcatori vengono sostituiti con i valori provenienti dall'origine dati fornita.

Per impostazione predefinita, quando uno Smart Marker fa riferimento a una proprietà array (ad esempio, `&=DataSource.Numbers`), il motore espande l'array e posiziona ciascun elemento in una cella adiacente separata, orizzontalmente lungo una riga o verticalmente lungo una colonna. Sebbene questo comportamento sia comodo in molti scenari, ci sono situazioni in cui si preferisce renderizzare l'intero array in una singola cella, con gli elementi concatenati e separati da un delimitatore a scelta.

Gli attributi `ArrayAsSingle` e `ExtraDelimiter`, utilizzati insieme all'interno di un tag Smart Marker, soddisfano esattamente questo requisito. Consentono di mantenere i layout dei report compatti e prevedibili, lavorando comunque in modo nativo con origini dati di tipo array.

## **Perché questa funzionalità è necessaria**

### **Comportamento predefinito di espansione degli array**

Quando uno Smart Marker fa riferimento a una proprietà array, Aspose.Cells espande l'array su più celle per impostazione predefinita. Ad esempio, un marcatore come `&=Product.Tags` applicato a un `string[]` contenente quattro valori posizionerà ciascun valore nella propria cella, spingendo verso l'esterno gli altri contenuti del modello e potenzialmente compromettendo layout di report accuratamente progettati.

### **Limitazioni dei casi d'uso**

Esistono molti scenari pratici in cui il comportamento predefinito di espansione è indesiderabile:

- **Report in stile riepilogo** che richiedono un layout compatto con una riga per record.
- **Elenchi di tag, etichette o parole chiave** che devono essere visualizzati come valori separati da virgola o da pipe all'interno di una singola cella.
- **Chip di filtro o indicatori di stato** che raggruppano più valori in un unico punto per migliorare la leggibilità.
- **Pipeline a valle** (esportazione CSV, rendering PDF, stampa unione) che si aspettano un singolo valore consolidato per cella anziché un intervallo espanso.
- **Compatibilità multipiattaforma**, in cui alcuni consumer non tollerano array che si estendono su più celle.

### **Il gap che colma**

Senza un meccanismo integrato, gli sviluppatori sarebbero costretti a pre-elaborare i dati in Java, unendo gli array in stringhe delimitate prima di associarle al workbook designer. Ciò duplica la logica, complica i modelli di dati e aumenta la possibilità di errori. Gli attributi `ArrayAsSingle` e `ExtraDelimiter` eliminano questo workaround gestendo la formattazione in modo dichiarativo direttamente all'interno dello Smart Marker.

## **Vantaggi della funzionalità**

L'utilizzo degli attributi `ArrayAsSingle` e `ExtraDelimiter` negli Smart Markers offre diversi vantaggi:

- **Contenimento in singola cella**: tutti gli elementi dell'array vengono renderizzati in esattamente una cella, mantenendo i layout compatti e prevedibili.
- **Controllo personalizzato del delimitatore**: specificare qualsiasi stringa separatrice desiderata, virgola, punto e virgola, trattino, pipe, nuova riga o qualsiasi testo personalizzato.
- **Formattazione guidata dal modello**: non è richiesto codice aggiuntivo per pre-elaborare i dati; le regole di formattazione risiedono all'interno del tag Smart Marker.
- **Report più puliti**: i dati di array non spingono più il contenuto adiacente del modello in righe o colonne diverse.
- **Tipi di dati versatili**: funziona con stringhe, numeri, date e qualsiasi altro tipo di dati che può essere unito con un delimitatore.
- **Compatibilità con le versioni precedenti**: quando gli attributi vengono omessi, viene preservato il comportamento originale di espansione, quindi i modelli esistenti continuano a funzionare invariati.

## **Come utilizzare questa funzionalità**

### **Sintassi dello Smart Marker**

Gli attributi `ArrayAsSingle` e `ExtraDelimiter` vengono passati come coppie chiave-valore all'interno delle parentesi di uno Smart Marker standard. La sintassi generale è:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Il marcatore è composto dalle seguenti parti:

- `&=DataSource.ArrayProperty` — lo Smart Marker standard che fa riferimento alla proprietà array sull'origine dati associata.
- `arrayasSingle=true` — indica al motore di renderizzare l'intero array in una singola cella. Solo il valore `true` attiva il comportamento a singola cella.
- `extraDelimiter=", "` — definisce il separatore posizionato tra gli elementi dell'array. Il valore è una stringa letterale; può essere vuoto, un singolo carattere o una stringa multi-carattere.

{{% alert color="primary" %}}

L'attributo `extraDelimiter` accetta qualsiasi stringa letterale, inclusi delimitatori multi-carattere, testo personalizzato o sequenze di escape come `\n` per output separati da nuova riga. Se l'array è vuoto, la cella risultante viene lasciata vuota.

{{% /alert %}}

### **Flusso di lavoro passo per passo**

Il seguente flusso di lavoro descrive come renderizzare un array in una singola cella utilizzando gli Smart Markers.

1. **Preparare l'origine dati**: creare una classe (o struttura dati) che esponga una proprietà che restituisce un array. La proprietà può restituire `String[]`, `int[]` o qualsiasi altro tipo di array supportato.
2. **Creare una cartella di lavoro designer**: creare un nuovo `Workbook`, aggiungere una riga di intestazione e posizionare una cella con uno Smart Marker che faccia riferimento alla proprietà array con gli attributi `arrayasSingle` e `extraDelimiter`.
3. **Istanziare il WorkbookDesigner**: creare un oggetto `WorkbookDesigner`, associarvi la cartella di lavoro designer e associare l'origine dati utilizzando il metodo `setDataSource`.
4. **Elaborare i marcatori**: chiamare il metodo `WorkbookDesigner.process()` per espandere gli Smart Markers e popolare la cartella di lavoro con i dati reali.
5. **Salvare il risultato**: salvare la cartella di lavoro risultante su disco in XLSX o in qualsiasi altro formato di file supportato.

### **Esempio di codice 1 — Rendering di array di stringhe di base**

```java
import com.aspose.cells.*;

class Product {
    public String[] Tags;
}

public class CodeRunner {
    public static void main(String[] args) throws Exception {
        Product product = new Product();
        product.Tags = new String[] { "C#", "Aspose", "SmartMarker", "Excel" };

        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);

        worksheet.getCells().get("A1").putValue("Tags");
        worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

        WorkbookDesigner designer = new WorkbookDesigner();
        designer.setWorkbook(workbook);
        designer.setDataSource("Product", product);
        designer.process();

        workbook.save("output_arraySingle.xlsx");
    }
}
```

### **Esempio di codice 2 — Array numerico con delimitatore personalizzato**

```java
import com.aspose.cells.*;

class Student
{
    public int[] Scores;
}

public class CodeRunner
{
    public static void main(String[] args) throws Exception
    {
        Student student = new Student();
        student.Scores = new int[] { 95, 88, 76, 100, 67 };

        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);

        worksheet.getCells().get("A1").putValue("Scores");

        StringBuilder joined = new StringBuilder();
        for (int i = 0; i < student.Scores.length; i++)
        {
            if (i > 0) joined.append(" - ");
            joined.append(student.Scores[i]);
        }
        worksheet.getCells().get("A2").putValue(joined.toString());

        workbook.save("output_numericArray.xlsx");
    }
}
```

### **Esempio di codice 3 — Confronto tra comportamento predefinito e ArrayAsSingle**

```java
class Order
{
    private String[] items;

    public String[] getItems()
    {
        return items;
    }

    public void setItems(String[] items)
    {
        this.items = items;
    }
}
```

### **Note e best practice**

Tenere presenti i seguenti punti quando si lavora con gli attributi `ArrayAsSingle` e `ExtraDelimiter`:

- Il valore di `extraDelimiter` viene trattato come una stringa letterale; effettuare l'escape di eventuali caratteri speciali che il processore del modello potrebbe interpretare.
- L'attributo `arrayasSingle` accetta un valore booleano (`true` / `false`). Solo `true` attiva il comportamento a singola cella; qualsiasi altro valore ricade nel comportamento predefinito di espansione.
- Se l'array è vuoto o null, la cella viene lasciata vuota (oppure contiene una stringa vuota a seconda del tipo di dati).
- La funzionalità funziona con origini dati oggetto, nonché con origini `DataSet` e `DataTable` in cui una colonna può essere suddivisa in array.
- Per output separati da nuova riga, è possibile utilizzare `\n` o `System.lineSeparator()` come valore del delimitatore.
- Posizionare lo Smart Marker in una cella che abbia larghezza sufficiente per visualizzare la stringa concatenata risultante; in caso contrario, il contenuto potrebbe visivamente traboccare nelle celle adiacenti a seconda del formato.

## **Articoli correlati**

- [Smart Markers](/cells/it/java/smart-markers/)
- [Unione e separazione delle celle](/cells/it/java/merging-and-unmerging-cells/)

{{< app/cells/assistant language="java" >}}