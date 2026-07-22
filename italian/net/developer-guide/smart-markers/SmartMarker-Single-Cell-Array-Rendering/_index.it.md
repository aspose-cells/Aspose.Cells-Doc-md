---
title: Rendering di Array in Cella Singola con SmartMarker | Aspose.Cells .NET
linktitle: Rendering di Array
description: Scopri come eseguire il rendering dei dati di array in una singola cella utilizzando gli attributi ArrayAsSingle e ExtraDelimiter negli Smart Markers con Aspose.Cells for .NET.
keywords: Aspose.Cells, libreria .NET, foglio di calcolo, Smart Markers, ArrayAsSingle, ExtraDelimiter, array in cella singola, rendering di array, modello
type: docs
weight: 195
url: /it/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells supporta il rendering dei dati di array in una singola cella tramite Smart Markers. Utilizzando l'attributo `ArrayAsSingle` insieme all'attributo `ExtraDelimiter`, gli sviluppatori possono controllare come gli elementi dell'array vengono separati all'interno di una singola cella, fornendo una formattazione flessibile per report e modelli.

{{% /alert %}}

## **Introduzione**

Gli Smart Markers in Aspose.Cells sono una potente funzionalità basata su modelli che consente di popolare dinamicamente i dati del foglio di calcolo utilizzando espressioni marker come `&=DataSource.Field`. Il marker viene inserito in una cartella di lavoro di progettazione e, quando il modello viene elaborato dal `WorkbookDesigner`, i marker vengono sostituiti con i valori provenienti dall'origine dati fornita.

Per impostazione predefinita, quando uno Smart Marker fa riferimento a una proprietà di array (ad esempio, `&=DataSource.Numbers`), il motore espande l'array e inserisce ciascun elemento in una cella adiacente separata, orizzontalmente lungo una riga o verticalmente lungo una colonna. Sebbene questo comportamento sia comodo in molti scenari, ci sono situazioni in cui si preferisce eseguire il rendering dell'intero array in un'unica cella, con gli elementi concatenati e separati da un delimitatore a scelta.

Gli attributi `ArrayAsSingle` e `ExtraDelimiter`, utilizzati insieme all'interno di un tag Smart Marker, soddisfano esattamente questo requisito. Consentono di mantenere i layout dei report compatti e prevedibili lavorando comunque in modo nativo con origini dati di tipo array.

## **Perché Questa Funzionalità È Necessaria**

### **Comportamento Predefinito di Espansione dell'Array**

Quando uno Smart Marker fa riferimento a una proprietà di array, Aspose.Cells espande l'array su più celle per impostazione predefinita. Ad esempio, un marker come `&=Product.Tags` applicato a un `string[]` contenente quattro valori inserirà ciascun valore nella propria cella, spingendo il resto del contenuto del modello verso l'esterno e potenzialmente compromettendo layout di report progettati con cura.

### **Limitazioni dei Casi d'Uso**

Esistono molti scenari pratici in cui il comportamento predefinito di espansione è indesiderabile:

- **Report in stile riepilogo** che richiedono un layout compatto con una riga per record.
- **Elenchi di tag, etichette o parole chiave** che devono essere visualizzati come valori separati da virgola o pipe all'interno di una singola cella.
- **Chip di filtro o indicatori di stato** che raggruppano più valori in un unico punto per una migliore leggibilità.
- **Pipeline a valle** (esportazione CSV, rendering PDF, mail merge) che si aspettano un singolo valore consolidato per cella anziché un intervallo espanso.
- **Compatibilità multipiattaforma**, in cui alcuni consumer non tollerano array che si estendono su più celle.

### **Il Gap che Colma**

Senza un meccanismo integrato, gli sviluppatori sarebbero costretti a pre-elaborare i dati in C# o VB.NET, unendo gli array in stringhe delimitate prima di associarle al progettista della cartella di lavoro. Ciò duplica la logica, complica i modelli di dati e aumenta la probabilità di errori. Gli attributi `ArrayAsSingle` e `ExtraDelimiter` eliminano questa soluzione alternativa gestendo la formattazione in modo dichiarativo direttamente all'interno dello Smart Marker.

## **Vantaggi della Funzionalità**

L'utilizzo degli attributi `ArrayAsSingle` e `ExtraDelimiter` negli Smart Markers offre diversi vantaggi:

- **Contenimento in cella singola**: tutti gli elementi dell'array vengono renderizzati esattamente in una cella, mantenendo i layout compatti e prevedibili.
- **Controllo personalizzato del delimitatore**: specificare qualsiasi stringa separatore si preferisca, virgola, punto e virgola, trattino, pipe, nuova riga o qualsiasi testo personalizzato.
- **Formattazione guidata dal modello**: non è richiesto codice aggiuntivo per pre-elaborare i dati; le regole di formattazione risiedono all'interno del tag Smart Marker.
- **Report più puliti**: i dati di array non spingono più il contenuto adiacente del modello in righe o colonne diverse.
- **Tipi di dati versatili**: funziona con stringhe, numeri, date e qualsiasi altro tipo di dati che possa essere unito con un delimitatore.
- **Compatibilità con le versioni precedenti**: quando gli attributi vengono omessi, il comportamento originale di espansione viene preservato, quindi i modelli esistenti continuano a funzionare invariati.

## **Come Utilizzare Questa Funzionalità**

### **Sintassi dello Smart Marker**

Gli attributi `ArrayAsSingle` e `ExtraDelimiter` vengono passati come coppie chiave-valore all'interno delle parentesi di uno Smart Marker standard. La sintassi generale è:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Il marker è composto dalle seguenti parti:

- `&=DataSource.ArrayProperty` — lo Smart Marker standard che fa riferimento alla proprietà di array sull'origine dati associata.
- `arrayasSingle=true` — indica al motore di eseguire il rendering dell'intero array in una singola cella. Solo il valore `true` attiva il comportamento in cella singola.
- `extraDelimiter=", "` — definisce il separatore inserito tra gli elementi dell'array. Il valore è una stringa letterale; può essere vuoto, un singolo carattere o una stringa multi-carattere.

{{% alert color="primary" %}}

L'attributo `extraDelimiter` accetta qualsiasi stringa letterale, inclusi delimitatori multi-carattere, testo personalizzato o sequenze di escape come `\n` per output separato da nuove righe. Se l'array è vuoto, la cella risultante viene lasciata vuota.

{{% /alert %}}

### **Flusso di Lavoro Passo per Passo**

Il seguente flusso di lavoro descrive come eseguire il rendering di un array in una singola cella utilizzando gli Smart Markers.

1. **Preparare l'origine dati**: creare una classe (o struttura dati) che espone una proprietà che restituisce un array. La proprietà può restituire `string[]`, `int[]` o qualsiasi altro tipo di array supportato.
2. **Creare una cartella di lavoro di progettazione**: creare un nuovo `Workbook`, aggiungere una riga di intestazione e posizionare una cella Smart Marker che fa riferimento alla proprietà di array con gli attributi `arrayasSingle` e `extraDelimiter`.
3. **Istanziare il WorkbookDesigner**: creare un oggetto `WorkbookDesigner`, associarvi la cartella di lavoro di progettazione e collegare l'origine dati utilizzando il metodo `SetDataSource`.
4. **Elaborare i marker**: chiamare il metodo `WorkbookDesigner.Process()` per espandere gli Smart Markers e popolare la cartella di lavoro con i dati reali.
5. **Salvare il risultato**: salvare la cartella di lavoro risultante su disco in XLSX o in qualsiasi altro formato di file supportato.

### **Esempio di Codice 1 — Rendering Base di Array di Stringhe**

```csharp
using System;
using Aspose.Cells;

class Program
{
    public class Product
    {
        public string[] Tags { get; set; }
    }

    public static void Main()
    {
        Product product = new Product
        {
            Tags = new string[] { "C#", "Aspose", "SmartMarker", "Excel" }
        };

        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];

        worksheet.Cells["A1"].PutValue("Tags");
        worksheet.Cells["A2"].PutValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

        WorkbookDesigner designer = new WorkbookDesigner();
        designer.Workbook = workbook;
        designer.SetDataSource("Product", product);
        designer.Process();

        workbook.Save("output_arraySingle.xlsx");
    }
}
```

### **Esempio di Codice 2 — Array Numerico con Delimitatore Personalizzato**

```csharp
public class Student
{
    public int[] Scores { get; set; }
}

public class Program
{
    public static void Main()
    {
        var student = new Student
        {
            Scores = new int[] { 95, 88, 76, 100, 67 }
        };

        var workbook = new Workbook();
        var worksheet = workbook.Worksheets[0];

        worksheet.Cells["A1"].PutValue("Scores");
        worksheet.Cells["A2"].PutValue(string.Join(" - ", student.Scores));

        workbook.Save("output_numericArray.xlsx");
    }
}
```

### **Esempio di Codice 3 — Confronto tra Comportamento Predefinito e ArrayAsSingle**

```csharp
using System;
using Aspose.Cells;

public class Program
{
    public static void Main()
    {
        var order = new Order
        {
            Items = new string[] { "Apple", "Banana", "Cherry", "Date" }
        };

        var workbook = new Workbook();
        var sheet = workbook.Worksheets[0];
        var cells = sheet.Cells;

        // Sezione 1: Smart Marker predefinito - valori distribuiti orizzontalmente tra le celle
        cells["A1"].PutValue("Default Spreading Behavior:");
        cells["A2"].PutValue("&=Order.Items");

        // Sezione 2: Nuovo rendering a cella singola utilizzando arrayasSingle e extraDelimiter
        cells["A4"].PutValue("Single Cell Rendering (arrayasSingle=true):");
        cells["A5"].PutValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

        // Associa l'origine dati ed elabora gli Smart Marker
        var designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Order", order);
        designer.Process();

        // Salva la cartella di lavoro risultante
        workbook.Save("output_comparison.xlsx");
    }
}

public class Order
{
    public string[] Items { get; set; }
}
```

### **Note e Buone Pratiche**

Tenere presente i seguenti punti quando si lavora con gli attributi `ArrayAsSingle` e `ExtraDelimiter`:

- Il valore di `extraDelimiter` viene trattato come una stringa letterale; effettuare l'escape di eventuali caratteri speciali che il processore del modello potrebbe interpretare.
- L'attributo `arrayasSingle` accetta un valore booleano (`true` / `false`). Solo `true` attiva il comportamento in cella singola; qualsiasi altro valore ripiega sul comportamento predefinito di espansione.
- Se l'array è vuoto o null, la cella viene lasciata vuota (o contiene una stringa vuota a seconda del tipo di dati).
- La funzionalità funziona con origini dati oggetto così come con origini `DataSet` e `DataTable` in cui una colonna può essere suddivisa in array.
- Per output separato da nuove righe, è possibile utilizzare `\n` o `Environment.NewLine` come valore del delimitatore.
- Posizionare lo Smart Marker in una cella che abbia larghezza sufficiente per visualizzare la stringa concatenata risultante; in caso contrario, il contenuto potrebbe visivamente traboccare nelle celle adiacenti a seconda del formato.

## **Articoli Correlati**

- [Smart Markers](/cells/it/net/smart-markers/)
- [Unione e Separazione delle Celle](/cells/it/net/merging-and-unmerging-cells/)

{{< app/cells/assistant language="csharp" >}}