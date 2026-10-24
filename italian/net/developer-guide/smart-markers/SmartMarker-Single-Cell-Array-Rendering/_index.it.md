---
title: Rendering di un array in una singola cella con SmartMarker | Aspose.Cells .NET
linktitle: Rendering di un array in una singola cella con SmartMarker | Aspose.Cells .NET
description: Impara a eseguire il rendering dei dati di array in una singola cella utilizzando gli attributi ArrayAsSingle ed ExtraDelimiter negli Smart Marker con Aspose.Cells for .Net.
keywords: Aspose.Cells, libreria .NET, foglio di calcolo, marcatori intelligenti, ArrayAsSingle, ExtraDelimiter, array in singola cella, rendering di array, modello
type: docs
weight: 195
url: /it/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta il rendering di dati di array in una singola cella tramite Smart Marker. Utilizzando l'attributo `ArrayAsSingle` insieme all'attributo `ExtraDelimiter`, gli sviluppatori possono controllare come gli elementi dell'array vengono separati all'interno di una singola cella, offrendo una formattazione flessibile per report e modelli.
{{% /alert %}}

## **Introduction**
Gli Smart Marker di Aspose.Cells sono una potente funzionalità basata su modelli che consente di popolare dinamicamente i dati di un foglio di calcolo utilizzando espressioni di marcatori come `&=DataSource.Field`. Il marcatore viene inserito in una cartella di lavoro creata con il designer e, quando il modello viene elaborato da `WorkbookDesigner`, i marcatori vengono sostituiti con i valori provenienti dall'origine dati fornita.
Per impostazione predefinita, quando uno Smart Marker fa riferimento a una proprietà di array (ad esempio, `&=DataSource.Numbers`), il motore espande l'array e inserisce ogni elemento in una cella adiacente distinta, orizzontalmente lungo una riga o verticalmente lungo una colonna. Sebbene questo comportamento sia comodo in molti scenari, in alcuni casi è preferibile eseguire il rendering dell'intero array in un'unica cella, con gli elementi concatenati e separati da un delimitatore a scelta.
Gli attributi `ArrayAsSingle` ed `ExtraDelimiter`, utilizzati insieme all'interno di un tag Smart Marker, rispondono esattamente a questa esigenza. Consentono di mantenere layout compatti e prevedibili nei report, preservando al contempo il supporto nativo per origini dati di tipo array.

## **Why This Feature Is Needed**

### **Default Array Spreading Behavior**
Quando uno Smart Marker fa riferimento a una proprietà di array, Aspose.Cells distribuisce l'array su più celle per impostazione predefinita. Ad esempio, un marcatore come `&=Product.Tags` associato a un `string[]` contenente quattro valori inserisce ciascun valore in una cella separata, spostando gli altri elementi del modello verso l'esterno e potenzialmente compromettendo layout di report progettati con cura.

### **Use Case Limitations**
Esistono numerosi scenari pratici in cui il comportamento predefinito di distribuzione non è desiderabile:
- **Report di riepilogo** che richiedono un layout compatto con una riga per ogni record.
- **Elenchi di tag, etichette o parole chiave** che devono essere visualizzati come valori separati da virgole o barre verticali all'interno di una singola cella.
- **Chip di filtro o indicatori di stato** che raggruppano più valori in un unico punto per migliorare la leggibilità.
- **Pipeline di elaborazione successive** (esportazione CSV, rendering PDF, stampa unione) che richiedono un unico valore consolidato per cella anziché un intervallo espanso.
- **Compatibilità multipiattaforma**, in cui alcuni componenti di destinazione non possono gestire array che si estendono su più celle.

### **The Gap It Fills**
In assenza di un meccanismo integrato, gli sviluppatori sarebbero costretti a pre-elaborare i dati in C# o VB.NET, concatenando gli array in stringhe con delimitatori prima di associarli alla cartella di lavoro tramite `WorkbookDesigner`. Questo approccio duplica la logica, complica i modelli di dati e aumenta la possibilità di errori. Gli attributi `ArrayAsSingle` ed `ExtraDelimiter` eliminano la necessità di questa soluzione alternativa gestendo la formattazione in modo dichiarativo all'interno stesso dello Smart Marker.

## **Feature Benefits**
L'utilizzo degli attributi `ArrayAsSingle` ed `ExtraDelimiter` negli Smart Marker offre diversi vantaggi:
- **Raccolta in una singola cella**: tutti gli elementi dell'array vengono renderingizzati in esattamente una cella, mantenendo layout compatti e prevedibili.
- **Controllo del delimitatore personalizzato**: consente di specificare qualsiasi stringa separatrice, ad esempio una virgola, un punto e virgola, un trattino, una barra verticale, una nuova riga o un testo personalizzato.
- **Formattazione guidata dal modello**: non è necessario alcun codice aggiuntivo per pre-elaborare i dati; le regole di formattazione sono contenute nel tag dello Smart Marker.
- **Report più puliti**: i dati di array non spostano più il contenuto circostante del modello in altre righe o colonne.
- **Tipi di dati versatili**: funziona con stringhe, numeri, date e qualsiasi altro tipo di dati che può essere concatenato mediante un delimitatore.
- **Compatibilità con le versioni precedenti**: quando gli attributi vengono omessi, viene preservato il comportamento originale di distribuzione,hausenendo i modelli esistenti continuano a funzionare senza modifiche.

## **How to Use This Feature**

### **Smart Marker Syntax**
Gli attributi `ArrayAsSingle` ed `ExtraDelimiter` vengono passati come coppie chiave-valore all'interno delle parentesi di uno Smart Marker standard. La sintassi generale è:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Il marcatore è composto dalle seguenti parti:
- `&=DataSource.ArrayProperty` — lo Smart Marker standard che fa riferimento alla proprietà di array dell'origine dati associata.
- `arrayasSingle=true` — indica al motore di eseguire il rendering dell'intero array in una singola cella. Solo il valore `true` attiva il comportamento su singola cella.
- `extraDelimiter=", "` — definisce il separatore inserito tra gli elementi dell'array. Il valore è un letterale di stringa e può essere vuoto, contenere un singolo carattere o essere una stringa di più caratteri.

{{% alert color="primary" %}}
L'attributo `extraDelimiter` accetta qualsiasi letterale di stringa, inclusi delimitatori di più caratteri, testo personalizzato o sequenze di escape come `\n` per un output separato da nuove righe. Se l'array è vuoto, la cella risultante viene lasciata vuota.
{{% /alert %}}

### **Step-by-Step Workflow**
Il seguente flusso di lavoro descrive come eseguire il rendering di un array in una singola cella utilizzando gli Smart Marker.
1. **Preparare l'origine dati**: creare una classe o una struttura di dati che esponga una proprietà che restituisce un array. La proprietà può restituire `string[]`, `int[]` o qualsiasi altro tipo di array supportato.
2. **Creare una cartella di lavoro con il designer**: creare un nuovo `Workbook`, aggiungere una riga di intestazione e inserire in una cella uno Smart Marker che faccia riferimento alla proprietà di array con gli attributi `arrayasSingle` ed `extraDelimiter`.
3. **Creare l'oggetto `WorkbookDesigner`**: creare un oggetto `WorkbookDesigner`, assegnargli la cartella di lavoro di progettazione e associare l'origine dati utilizzando il metodo `SetDataSource`.
4. **Elaborare i marcatori**: chiamare il metodo `WorkbookDesigner.Process()` per espandere gli Smart Marker e popolare la cartella di lavoro con i dati reali.
5. **Salvare il risultato**: salvare la cartella di lavoro risultante su disco in XLSX o in qualsiasi altro formato di file supportato.

### **Code Example 1 — Basic String Array Rendering**

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

### **Code Example 2 — Numeric Array with Custom Delimiter**

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

### **Code Example 3 — Comparing Default vs. ArrayAsSingle Behavior**

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
        // Section 1: Default Smart Marker - values spread horizontally across cells
        cells["A1"].PutValue("Default Spreading Behavior:");
        cells["A2"].PutValue("&=Order.Items");
        // Section 2: New single-cell rendering using arrayasSingle and extraDelimiter
        cells["A4"].PutValue("Single Cell Rendering (arrayasSingle=true):");
        cells["A5"].PutValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");
        // Bind the data source and process Smart Markers
        var designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Order", order);
        designer.Process();
        // Save the resulting workbook
        workbook.Save("output_comparison.xlsx");
    }
}
public class Order
{
    public string[] Items { get; set; }
}
```

### **Notes & Best Practices**
Tenere presenti i seguenti aspetti quando si utilizzano gli attributi `ArrayAsSingle` ed `ExtraDelimiter`:
- Il valore `extraDelimiter` viene trattato come un letterale di stringa; eseguire l'escape di eventuali caratteri speciali che il processore del modello potrebbe interpretare.
- L'attributo `arrayasSingle` accetta un valore booleano (`true` / `false`). Solo `true` attiva il comportamento su singola cella; qualsiasi altro valore ricade nel comportamento predefinito di distribuzione.
- Se l'array è vuoto o null, la cella viene lasciata vuota oppure contiene una stringa vuota, a seconda del tipo di dati.
- La funzionalità supporta origini dati di tipo object, `DataSet` e `DataTable`, in cui una colonna può essere suddivisa in array.
- Per un output separato da nuove righe, è possibile utilizzare `\n` o `Environment.NewLine` come valore del delimitatore.

## Related Articles
- [Aggiungi campi filtro a una tabella pivot in Aspose.Cells for .NET](/cells/it/net/add-page-field-in-pivot-table/)
- [Applica stili alle tabelle pivot in Aspose.Cells for .NET](/cells/it/net/apply-style-to-pivot-table/)
- [Modifica il layout dei campi pagina nella tabella pivot](/cells/it/net/change-page-field-layout/)
- [Converti Sparkline in immagine e HTML in Aspose.Cells for .NET](/cells/it/net/convert-sparkline-to-image-and-html/)
- [Conversione di Excel nel formato OFD](/cells/it/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}