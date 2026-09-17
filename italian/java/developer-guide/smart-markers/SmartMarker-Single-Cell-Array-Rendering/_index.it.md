---
title: Rendering di array in cella singola con SmartMarker | Aspose.Cells Java
linktitle: Rendering di array in cella singola con SmartMarker | Aspose.Cells Java
description: Scopri come eseguire il rendering dei dati di array in una singola cella utilizzando gli attributi ArrayAsSingle ed ExtraDelimiter in Smart Markers con Aspose.Cells for Java.
keywords: Aspose.Cells, libreria Java, foglio di calcolo, Smart Markers, ArrayAsSingle, ExtraDelimiter, array in cella singola, rendering di array, modello
type: docs
weight: 195
url: /it/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta il rendering dei dati di array in una singola cella tramite Smart Markers. Utilizzando l'attributo `ArrayAsSingle` insieme all'attributo `ExtraDelimiter`, gli sviluppatori possono controllare il modo in cui gli elementi dell'array vengono separati all'interno di una singola cella, offrendo una formattazione flessibile per report e modelli.

## **Introduction**
Gli Smart Markers in Aspose.Cells sono una potente funzionalità basata su modelli che consente di popolare dinamicamente i dati del foglio di calcolo utilizzando espressioni marker come `&=DataSource.Field`. Il marker viene inserito in una cartella di lavoro designer e, quando il modello viene elaborato dal `WorkbookDesigner`, i marker vengono sostituiti con i valori provenienti dall'origine dati fornita.
Per impostazione predefinita, quando uno Smart Marker fa riferimento a una proprietà array (ad esempio, `&=DataSource.Numbers`), il motore espande l'array e posiziona ciascun elemento in una cella adiacente separata, orizzontalmente su una riga o verticalmente lungo una colonna. Sebbene questo comportamento sia comodo in molti scenari, esistono situazioni in cui è preferibile eseguire il rendering dell'intero array in un'unica cella, con gli elementi concatenati e separati da un delimitatore a scelta.
Gli attributi `ArrayAsSingle` e `ExtraDelimiter`, utilizzati insieme all'interno di un tag Smart Marker, soddisfano esattamente questo requisito. Consentono di mantenere i layout dei report compatti e prevedibili, lavorando comunque in modo nativo con origini dati di tipo array.

## **Why This Feature Is Needed**

### **Default Array Spreading Behavior**
Quando uno Smart Marker fa riferimento a una proprietà array, Aspose.Cells espande l'array su più celle per impostazione predefinita. Ad esempio, un marker come `&=Product.Tags` riferito a un `string[]` contenente quattro valori posizionerà ciascun valore nella propria cella, spingendo il resto del contenuto del modello verso l'esterno e potenzialmente compromettendo layout di report progettati con cura.

### **Use Case Limitations**
Esistono molti scenari pratici in cui il comportamento di espansione predefinito è indesiderato:
- **Report in stile riepilogo** che richiedono un layout compatto di una riga per record.
- **Elenchi di tag, etichette o parole chiave** che devono essere visualizzati come valori separati da virgola o da pipe all'interno di una singola cella.
- **Chip di filtro o indicatori di stato** che raggruppano più valori in un unico punto per una migliore leggibilità.
- **Pipeline a valle** (esportazione CSV, rendering PDF, stampa unione) che si aspettano un singolo valore consolidato per cella anziché un intervallo espanso.
- **Compatibilità multipiattaforma**, in cui alcuni consumer non tollerano array che si estendono su più celle.

### **The Gap It Fills**
Senza un meccanismo integrato, gli sviluppatori sarebbero costretti a pre-elaborare i dati in Java, unendo gli array in stringhe delimitate prima di associarle al workbook designer. Ciò duplica la logica, complica i modelli di dati e aumenta la possibilità di errori. Gli attributi `ArrayAsSingle` e `ExtraDelimiter` eliminano questa soluzione alternativa gestendo la formattazione in modo dichiarativo direttamente all'interno dello Smart Marker.

## **Feature Benefits**
L'utilizzo degli attributi `ArrayAsSingle` e `ExtraDelimiter` negli Smart Markers offre diversi vantaggi:
- **Contenimento in cella singola**: tutti gli elementi dell'array vengono renderizzati esattamente in una sola cella, mantenendo layout compatti e prevedibili.
- **Controllo personalizzato del delimitatore**: specificare qualsiasi stringa separatore desiderata, virgola, punto e virgola, trattino, pipe, nuova riga o qualsiasi testo personalizzato.
- **Formattazione guidata dal modello**: non è richiesto alcun codice aggiuntivo per pre-elaborare i dati; le regole di formattazione risiedono all'interno del tag Smart Marker.
- **Report più puliti**: i dati di array non spostano più il contenuto adiacente del modello in righe o colonne diverse.
- **Tipi di dati versatili**: funziona con stringhe, numeri, date e qualsiasi altro tipo di dati che possa essere unito con un delimitatore.
- **Retrocompatibilità**: quando gli attributi vengono omessi, viene preservato il comportamento di espansione originale, quindi i modelli esistenti continuano a funzionare senza modifiche.

## **How to Use This Feature**

### **Smart Marker Syntax**
Gli attributi `ArrayAsSingle` e `ExtraDelimiter` vengono passati come coppie chiave-valore all'interno delle parentesi di uno Smart Marker standard. La sintassi generale è:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Il marker è composto dalle seguenti parti:
- `&=DataSource.ArrayProperty`: lo Smart Marker standard che fa riferimento alla proprietà array sull'origine dati associata.
- `arrayasSingle=true`: indica al motore di eseguire il rendering dell'intero array in una singola cella. Solo il valore `true` attiva il comportamento in cella singola.
- `extraDelimiter=", "`: definisce il separatore inserito tra gli elementi dell'array. Il valore è una stringa letterale; può essere vuoto, un singolo carattere o una stringa multi-carattere.

{{% alert color="primary" %}}
L'attributo `extraDelimiter` accetta qualsiasi stringa letterale, inclusi delimitatori multi-carattere, testo personalizzato o sequenze di escape come `\n` per output separati da nuova riga. Se l'array è vuoto, la cella risultante viene lasciata vuota.

### **Step-by-Step Workflow**
Il flusso di lavoro seguente descrive come eseguire il rendering di un array in una singola cella utilizzando gli Smart Markers.
1. **Preparare l'origine dati**: creare una classe (o struttura dati) che espone una proprietà che restituisce un array. La proprietà può restituire `String[]`, `int[]` o qualsiasi altro tipo di array supportato.
2. **Creare una cartella di lavoro designer**: creare un nuovo `Workbook`, aggiungere una riga di intestazione e inserire una cella Smart Marker che faccia riferimento alla proprietà array con gli attributi `arrayasSingle` e `extraDelimiter`.
3. **Istanziare il WorkbookDesigner**: creare un oggetto `WorkbookDesigner`, associarvi la cartella di lavoro designer e collegare l'origine dati utilizzando il metodo `setDataSource`.
4. **Elaborare i marker**: chiamare il metodo `WorkbookDesigner.process()` per espandere gli Smart Markers e popolare la cartella di lavoro con i dati reali.
5. **Salvare il risultato**: salvare la cartella di lavoro risultante su disco in formato XLSX o in qualsiasi altro formato di file supportato.

### **Code Example 1 — Basic String Array Rendering**

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

### **Code Example 2 — Numeric Array with Custom Delimiter**

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

### **Code Example 3 — Comparing Default vs. ArrayAsSingle Behavior**

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

### **Notes & Best Practices**
Tenere presenti i seguenti punti quando si lavora con gli attributi `ArrayAsSingle` e `ExtraDelimiter`:
- Il valore di `extraDelimiter` viene trattato come una stringa letterale; eseguire l'escape di eventuali caratteri speciali che il processore di modelli potrebbe interpretare.
- L'attributo `arrayasSingle` accetta un valore booleano (`true` / `false`). Solo `true` attiva il comportamento in cella singola; qualsiasi altro valore torna al comportamento di espansione predefinito.
- Se l'array è vuoto o null, la cella viene lasciata vuota (oppure contiene una stringa vuota a seconda del tipo di dati).
- La funzionalità funziona sia con origini dati di oggetti sia con origini `DataSet` e `DataTable` in cui una colonna può essere suddivisa in array.
- Per output separati da nuova riga, è possibile utilizzare `\n` o `System.lineSeparator()` come valore del delimitatore.
- Posizionare lo Smart Marker in una cella che abbia larghezza sufficiente per visualizzare la stringa concatenata risultante; in caso contrario, il contenuto potrebbe visivamente traboccare nelle celle adiacenti a seconda del formato.
{{% /alert %}}

{{% /alert %}}

## Related Articles
- [Aggiungere Campi Filtro a una Tabella Pivot in Aspose.Cells for Java](/cells/it/java/add-page-field-in-pivot-table/)
- [Applicare Stili alle Tabelle Pivot in Aspose.Cells for Java](/cells/it/java/apply-style-to-pivot-table/)
- [Modificare il Layout dei Campi Pagina nella Tabella Pivot](/cells/it/java/change-page-field-layout/)
- [Convertire Sparkline in Immagine e HTML in Aspose.Cells for Java](/cells/it/java/convert-sparkline-to-image-and-html/)
- [Conversione di Excel in Formato OFD](/cells/it/java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="java" >}}