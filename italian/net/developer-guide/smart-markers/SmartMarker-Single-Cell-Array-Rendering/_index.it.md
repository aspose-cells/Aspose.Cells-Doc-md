---
title: Rendering di array a singola cella con SmartMarker | Aspose.Cells for .Net
description: Scopri come eseguire il rendering dei dati di un array in una singola cella utilizzando gli attributi Smart Marker arrayassingle e arraydelimiter in Aspose.Cells for .Net.
linktitle: Rendering di array a singola cella con SmartMarker | Aspose.Cells
url: /it/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, libreria .NET, foglio di calcolo, Smart Marker, arrayassingle, arraydelimiter, array a singola cella, rendering di array, modello
type: docs
weight: 195
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells può eseguire il rendering di una fonte dati di tipo array in una singola cella tramite gli Smart Marker. L'attributo `arrayassingle` disattiva la distribuzione predefinita elemento per elemento, mentre l'attributo `arraydelimiter` determina il separatore inserito tra gli elementi concatenati — una virgola per impostazione predefinita, oppure un qualsiasi carattere singolo o una stringa di più caratteri tra virgolette specificata dall'utente.
{{% /alert %}}

## **Introduzione**

Gli Smart Marker in Aspose.Cells sono una funzionalità basata su modelli che popola dinamicamente i dati del foglio di calcolo utilizzando espressioni di marker come `&=DataSource.Field`. Il marker viene inserito in una cartella di lavoro di progettazione e, quando il modello viene elaborato da `WorkbookDesigner`, i marker vengono sostituiti dai valori della fonte dati fornita.
Per impostazione predefinita, quando uno Smart Marker fa riferimento a una proprietà di tipo array (ad esempio, `&=Product.Tags` associata a un `string[]` di quattro valori), il motore espande l'array e inserisce ogni elemento in una cella separata, distribuendo i valori verticalmente lungo la colonna sotto il marker. Sebbene questo comportamento sia comodo in molti scenari, in alcuni casi si preferisce eseguire il rendering dell'intero array in una singola cella, con gli elementi concatenati e separati da un delimitatore a scelta.
Gli attributi `arrayassingle` e `arraydelimiter`, scritti tra parentesi di uno Smart Marker nella forma `name:value`, rispondono esattamente a questa esigenza. Consentono di mantenere compatti e prevedibili i layout dei report, utilizzando al contempo fonti dati di tipo array in modo nativo.

## **Perché è necessaria questa funzionalità**

### **Comportamento predefinito di distribuzione degli array**

Quando uno Smart Marker fa riferimento a una proprietà di tipo array, Aspose.Cells espande l'array su più celle per impostazione predefinita. Ad esempio, un marker come `&=Product.Tags` associato a un `string[]` contenente quattro valori inserisce ogni valore in una cella separata sotto il marker, spostando verso il basso gli altri contenuti del modello e potenzialmente compromettendo layout dei report progettati con cura.

### **Limitazioni dei casi d'uso**

Esistono numerosi scenari pratici in cui il comportamento predefinito di distribuzione non è desiderabile:
- **Report riepilogativi** che richiedono un layout compatto con una riga per record.
- **Elenchi di tag, etichette o parole chiave** che devono essere visualizzati come valori separati da virgole o barre verticali all'interno di una singola cella.
- **Elementi di filtro o indicatori di stato** che raggruppano più valori in un unico punto per migliorare la leggibilità.
- **Flussi di elaborazione successivi** (esportazione in CSV, rendering in PDF, stampa unione) che richiedono un singolo valore consolidato per cella anziché un intervallo espanso.
- **Compatibilità multipiattaforma**, in cui alcuni consumer non tollerano array che si estendono su più celle.

### **La lacuna che questa funzionalità colma**

In assenza di un meccanismo integrato, gli sviluppatori sarebbero costretti a preelaborare i dati in C# o VB.NET — concatenando gli array in stringhe delimitate prima di associarli al workbook designer. Questo approccio duplica la logica, complica i modelli di dati e aumenta la probabilità di errori. Gli attributi `arrayassingle` e `arraydelimiter` eliminano questa soluzione alternativa gestendo la formattazione in modo dichiarativo all'interno dello Smart Marker stesso.

## **Vantaggi della funzionalità**

L'utilizzo degli attributi `arrayassingle` e `arraydelimiter` negli Smart Marker offre diversi vantaggi:
- **Contenimento in una singola cella**: tutti gli elementi dell'array vengono renderizzati in una sola cella, mantenendo layout compatti e prevedibili.
- **Controllo del delimitatore personalizzato**: specificare il separatore desiderato — la virgola predefinita, un punto e virgola, un trattino, una barra verticale o una stringa di più caratteri tra virgolette come `" | "`.
- **Formattazione guidata dal modello**: non è necessario aggiungere codice per preelaborare i dati; le regole di formattazione sono contenute nel tag Smart Marker.
- **Report più puliti**: i dati di tipo array non spostano più i contenuti adiacenti del modello in righe o colonne diverse.
- **Tipi di dati versatili**: funziona con array di stringhe e array numerici provenienti da fonti dati di tipo oggetto.
- **Compatibilità con le versioni precedenti**: quando gli attributi vengono omessi, viene preservato il comportamento originale di distribuzione, pertanto i modelli esistenti continuano a funzionare senza modifiche.

## **Come utilizzare questa funzionalità**

### **Sintassi degli Smart Marker**

Gli attributi `arrayassingle` e `arraydelimiter` utilizzano la grammatica degli attributi `name:value` di Aspose.Cells all'interno delle parentesi di uno Smart Marker standard. La sintassi generale è:

```
&=DataSource.ArrayProperty(arrayassingle:true,arraydelimiter:;)
```

Il marker è composto dalle seguenti parti:
- `&=DataSource.ArrayProperty` — lo Smart Marker standard che fa riferimento alla proprietà di tipo array della fonte dati associata.
- `arrayassingle:true` — indica al motore di eseguire il rendering dell'intero array in una singola cella anziché distribuirne gli elementi.
- `arraydelimiter:;` — facoltativo; definisce il separatore inserito tra gli elementi dell'array. Se viene omesso, viene utilizzata una virgola.

{{% alert color="warning" %}}
Scrivere gli attributi nella forma `name:value` (un due punti, non un segno di uguale) e separare più attributi con una virgola **senza spazi**. Uno spazio dopo la virgola sposta di un carattere il valore interpretato: `(arrayassingle:true, arraydelimiter:;)` unisce gli elementi con il separatore errato `:;` anziché `;`.
{{% /alert %}}

### **Forme del delimitatore**

- Un carattere singolo segue direttamente i due punti: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- Un separatore di più caratteri viene racchiuso tra virgolette doppie: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Flusso di lavoro passo per passo**

Il flusso di lavoro seguente descrive come eseguire il rendering di un array in una singola cella utilizzando gli Smart Marker.
1. **Preparare la fonte dati**: creare una classe che esponga una proprietà che restituisce un array, ad esempio `string[]` o `int[]`, e associare un `List<T>` di tale classe in modo che il motore legga un record per riga.
2. **Creare una cartella di lavoro di progettazione**: creare un nuovo `Workbook`, aggiungere una riga di intestazione e inserire in una cella uno Smart Marker che faccia riferimento alla proprietà di tipo array con l'attributo `arrayassingle` (e `arraydelimiter` quando è necessario un separatore personalizzato).
3. **Istanziare `WorkbookDesigner`**: creare un `WorkbookDesigner` per la cartella di lavoro e associare la fonte dati con `SetDataSource`.
4. **Elaborare i marker**: chiamare il metodo `WorkbookDesigner.Process()` per espandere gli Smart Marker e popolare la cartella di lavoro con i dati reali.
5. **Salvare il risultato**: salvare la cartella di lavoro risultante su disco in XLSX o in qualsiasi altro formato di file supportato.

### **Esempio di codice 1 — Rendering di base di un array di stringhe**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Product
    {
        public string[] Tags { get; set; }
    }

    static void Main()
    {
        Product product = new Product
        {
            Tags = new string[] { "C#", "Aspose", "SmartMarker", "Excel" }
        };
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Tags");
        // No spaces inside the parentheses: attributes are name:value pairs
        worksheet.Cells["A2"].PutValue("&=Product.Tags(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Product", new List<Product> { product });
        designer.Process();
        Console.WriteLine(worksheet.Cells["A2"].StringValue);
        workbook.Save("output-array-single.xlsx");
    }
}
```

L'esempio stampa il valore concatenato dell'intero array. I quattro tag finiscono in una singola cella, separati dalla virgola predefinita:

```
C#,Aspose,SmartMarker,Excel
```

### **Esempio di codice 2 — Array numerico con delimitatore personalizzato**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Student
    {
        public int[] Scores { get; set; }
    }

    static void Main()
    {
        Student student = new Student
        {
            Scores = new int[] { 95, 88, 76, 100, 67 }
        };
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Scores");
        // arraydelimiter:- joins the numbers with a hyphen
        worksheet.Cells["A2"].PutValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Student", new List<Student> { student });
        designer.Process();
        Console.WriteLine(worksheet.Cells["A2"].StringValue);
        workbook.Save("output-array-numeric.xlsx");
    }
}
```

Gli array numerici vengono concatenati esattamente come quelli di stringhe — ogni elemento mantiene il proprio testo numerico semplice:

```
95-88-76-100-67
```

### **Esempio di codice 3 — Confronto tra rendering predefinito e rendering in singola cella**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Order
    {
        public string[] Items { get; set; }
    }

    static void Main()
    {
        Order order = new Order
        {
            Items = new string[] { "Apple", "Banana", "Cherry", "Date" }
        };
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];
        Cells cells = sheet.Cells;
        // Column B: default marker — values spread vertically down the column
        cells["B1"].PutValue("Default");
        cells["B2"].PutValue("&=Order.Items");
        // Column C: single-cell rendering — the whole array joins into one cell
        cells["C1"].PutValue("Single cell");
        cells["C2"].PutValue("&=Order.Items(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Order", new List<Order> { order });
        designer.Process();
        for (int row = 1; row <= 5; row++)
        {
            string b = cells[row, 1].StringValue;
            string c = cells[row, 2].StringValue;
            if (!string.IsNullOrEmpty(b) || !string.IsNullOrEmpty(c))
                Console.WriteLine($"B{row + 1}=[{b}]  C{row + 1}=[{c}]");
        }
        workbook.Save("output-array-comparison.xlsx");
    }
}
```

Il marker predefinito riempie una cella per elemento lungo la colonna B, mentre il marker `arrayassingle` compatta lo stesso array in una singola cella nella colonna C:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Note e pratiche consigliate**

Tenere presenti i seguenti punti quando si lavora con gli attributi `arrayassingle` e `arraydelimiter`:
- I valori degli attributi usano la forma `name:value`. Una forma con il segno di uguale, come `arrayassingle=true`, non viene riconosciuta e ricade silenziosamente nel comportamento predefinito di distribuzione.
- Separare gli attributi con una virgola e senza spazi; uno spazio dopo la virgola sposta di un carattere il valore del delimitatore (vedere l'avviso sopra).
- Il valore `arraydelimiter` può essere un carattere singolo scritto direttamente dopo i due punti oppure una stringa di più caratteri racchiusa tra virgolette doppie.
- Quando `arraydelimiter` viene omesso, gli elementi vengono concatenati con una virgola.
- La fonte dati deve consentire al motore di enumerare i record: associare un `List<T>` (o un'altra raccolta) il cui tipo di elemento esponga la proprietà di tipo array. L'associazione di un singolo oggetto fa sì che i marker del corpo non vengano risolti.
- Gli stessi attributi funzionano con array di stringhe e array numerici; ogni elemento viene renderizzato con il testo semplice del proprio valore.

## **Articoli correlati**
- [Aggiungere campi filtro a una tabella pivot in Aspose.Cells for .NET](/cells/it/net/add-page-field-in-pivot-table/)
- [Applica stili alle tabelle pivot in Aspose.Cells for .NET](/cells/it/net/apply-style-to-pivot-table/)
- [Modificare il layout del campo pagina in una tabella pivot](/cells/it/net/change-page-field-layout/)
- [Convertire Sparkline in Immagine e HTML in Aspose.Cells for .NET](/cells/it/net/convert-sparkline-to-image-and-html/)
- [Conversione di Excel in formato OFD](/cells/it/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}