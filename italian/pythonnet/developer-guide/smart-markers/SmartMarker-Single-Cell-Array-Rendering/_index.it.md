---
title: Rendering di array SmartMarker in una singola cella | Aspose.Cells for Python via .NET
description: Scopri come eseguire il rendering di dati array in una singola cella utilizzando gli attributi Smart Marker arrayassingle e arraydelimiter in Aspose.Cells for Python via .NET.
linktitle: Rendering di array SmartMarker in singola cella | Aspose.Cells
url: /it/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, libreria Python via .NET, foglio di calcolo, Smart Marker, arrayassingle, arraydelimiter, array in singola cella, rendering degli array, modello
type: docs
weight: 195
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells può eseguire il rendering di un'origine dati array in un'unica cella tramite gli Smart Marker. L'attributo `arrayassingle` disattiva l'espansione predefinita elemento per elemento, mentre l'attributo `arraydelimiter` determina il separatore inserito tra gli elementi uniti — una virgola per impostazione predefinita, oppure il singolo carattere o la stringa di più caratteri tra virgolette che si desidera specificare.
{{% /alert %}}

## **Introduzione**

Gli Smart Marker di Aspose.Cells sono una funzionalità basata su modelli che popola dinamicamente i dati del foglio di calcolo utilizzando espressioni come `&=DataSource.Field`. Il marcatore viene collocato in una cartella di lavoro di progettazione e, quando il modello viene elaborato da `WorkbookDesigner`, i marcatori vengono sostituiti dai valori provenienti dall'origine dati fornita.
Per impostazione predefinita, quando uno Smart Marker fa riferimento a un campo array (ad esempio, `&=Product.Tags` associato a un elenco di quattro valori), il motore espande l'array e inserisce ogni elemento in una cella separata, distribuendo i valori verticalmente nella colonna sotto il marcatore. Sebbene questo comportamento sia comodo in molti scenari, in alcuni casi si preferisce eseguire il rendering dell'intero array in un'unica cella, con gli elementi concatenati e separati da un separatore a scelta.
Gli attributi `arrayassingle` e `arraydelimiter`, scritti all'interno delle parentesi di uno Smart Marker nella forma `name:value`, rispondono esattamente a questa esigenza. Consentono di mantenere layout dei report compatti e prevedibili, continuando a utilizzare in modo nativo le origini dati di tipo array.

## **Perché questa funzione è necessaria**

### **Comportamento predefinito di espansione degli array**

Quando uno Smart Marker fa riferimento a un campo array, Aspose.Cells espande l'array su più celle per impostazione predefinita. Ad esempio, un marcatore come `&=Product.Tags` associato a un elenco contenente quattro valori inserisce ogni valore in una cella separata sotto il marcatore, spostando gli altri contenuti del modello verso l'esterno e potenzialmente compromettendo layout di report progettati con cura.

### **Limitazioni dei casi d'uso**

Esistono numerosi scenari pratici in cui il comportamento predefinito di espansione non è desiderabile:
- **Report riepilogativi** che richiedono un layout compatto con una riga per ogni record.
- **Elenchi di tag, etichette o parole chiave** che devono essere visualizzati come valori separati da virgole o barre verticali all'interno di una singola cella.
- **Chip di filtro o indicatori di stato** che raggruppano più valori in un unico punto per migliorare la leggibilità.
- **Pipeline a valle** (esportazione CSV, rendering PDF, stampa unione) che richiedono un singolo valore consolidato per cella anziché un intervallo espanso.
- **Compatibilità multipiattaforma**, dove alcuni sistemi consumatori non tollerano array che si estendono su più celle.

### **La lacuna che colma**

Senza un meccanismo integrato, gli sviluppatori sarebbero costretti a pre-elaborare i dati in Python, unendo gli elenchi in stringhe delimitate prima di associarli al designer della cartella di lavoro. Ciò duplicherebbe la logica, complicherebbe i modelli di dati e aumenterebbe la probabilità di errori. Gli attributi `arrayassingle` e `arraydelimiter` eliminano questa soluzione alternativa gestendo la formattazione in modo dichiarativo all'interno dello stesso Smart Marker.

## **Vantaggi della funzione**

L'utilizzo degli attributi `arrayassingle` e `arraydelimiter` negli Smart Marker offre diversi vantaggi:
- **Contenimento in una singola cella**: tutti gli elementi dell'array vengono rappresentati in una sola cella, mantenendo layout compatti e prevedibili.
- **Controllo personalizzato del separatore**: specificare il separatore desiderato — la virgola predefinita, un punto e virgola, un trattino, una barra verticale o una stringa di più caratteri tra virgolette come `" | "`.
- **Formattazione guidata dal modello**: non è necessario scrivere codice aggiuntivo per pre-elaborare i dati; le regole di formattazione sono definite nel tag Smart Marker.
- **Report più puliti**: i dati array non spostano più i contenuti adiacenti del modello in righe o colonne diverse.
- **Tipi di dati versatili**: funziona con elenchi di stringhe ed elenchi numerici forniti come righe JSON.
- **Compatibilità con le versioni precedenti**: quando gli attributi vengono omessi, viene preservato il comportamento di espansione originale, pertanto i modelli esistenti continuano a funzionare senza modifiche.

## **Come utilizzare questa funzione**

### **Sintassi degli Smart Marker**

Gli attributi `arrayassingle` e `arraydelimiter` utilizzano la grammatica degli attributi `name:value` di Aspose.Cells all'interno delle parentesi di uno Smart Marker standard. La sintassi generale è:

```
&=DataSource.ArrayField(arrayassingle:true,arraydelimiter:;)
```

Il marcatore è composto dalle seguenti parti:
- `&=DataSource.ArrayField` — lo Smart Marker standard che fa riferimento al campo array dell'origine dati associata.
- `arrayassingle:true` — indica al motore di eseguire il rendering dell'intero array in un'unica cella anziché espandere gli elementi.
- `arraydelimiter:;` — facoltativo; definisce il separatore inserito tra gli elementi dell'array. Quando viene omesso, viene utilizzata una virgola.

{{% alert color="warning" %}}
Scrivere gli attributi nella forma `name:value` (due punti, non il segno di uguaglianza) e separare più attributi con una virgola **senza spazi**. Uno spazio dopo la virgola fa scorrere di un carattere il valore analizzato: `(arrayassingle:true, arraydelimiter:;)` unirebbe gli elementi usando il separatore errato `:;` anziché `;`.
{{% /alert %}}

### **Forme del separatore**

- Un singolo carattere segue direttamente i due punti: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- Un separatore di più caratteri viene scritto tra virgolette doppie: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Flusso di lavoro passo per passo**

Il flusso di lavoro seguente descrive come eseguire il rendering di un array in una singola cella utilizzando gli Smart Marker.
1. **Prepara l'origine dati**: organizza ogni record come oggetto JSON il cui campo contiene un array, ad esempio `{"Tags": ["C#", "Aspose"]}}. Le istanze di classi Python, i dizionari e gli elenchi passati a `set_data_source` non associano i campi array su questa piattaforma; le righe JSON sono la forma tabulare supportata.
2. **Crea una cartella di lavoro di progettazione**: crea un nuovo `Workbook`, aggiungi una riga di intestazione e inserisci in una cella uno Smart Marker che faccia riferimento al campo array, con l'attributo `arrayassingle` e con `arraydelimiter` quando è necessario un separatore personalizzato.
3. **Istanzia `WorkbookDesigner`**: crea un'istanza di `WorkbookDesigner` per la cartella di lavoro e associa le righe JSON tramite `set_json_data_source`.
4. **Elabora i marcatori**: chiama il metodo `WorkbookDesigner.process()` per espandere gli Smart Marker e popolare la cartella di lavoro con i dati effettivi.
5. **Salva il risultato**: salva la cartella di lavoro risultante su disco in XLSX o in qualsiasi altro formato di file supportato.

### **Esempio di codice 1 — Rendering di array di stringhe**

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Tags")
# No spaces inside the parentheses: attributes are name:value pairs
worksheet.cells.get("A2").put_value("&=Product.Tags(arrayassingle:true)")
designer = ac.WorkbookDesigner(workbook)
designer.set_json_data_source(
    "Product",
    '[{"Tags": ["C#", "Aspose", "SmartMarker", "Excel"]}]')
designer.process()
print(worksheet.cells.get("A2").string_value)
workbook.save("output-array-single.xlsx")
```

L'esempio stampa il valore concatenato dell'intero array. I quattro tag finiscono in una singola cella, separati dalla virgola predefinita:

```
C#,Aspose,SmartMarker,Excel
```

### **Esempio di codice 2 — Array numerico con un separatore personalizzato**

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Scores")
# arraydelimiter:- joins the numbers with a hyphen
worksheet.cells.get("A2").put_value("&=Student.Scores(arrayassingle:true,arraydelimiter:-)")
designer = ac.WorkbookDesigner(workbook)
designer.set_json_data_source(
    "Student",
    '[{"Scores": [95, 88, 76, 100, 67]}]')
designer.process()
print(worksheet.cells.get("A2").string_value)
workbook.save("output-array-numeric.xlsx")
```

I numeri JSON vengono uniti esattamente come le stringhe: ogni elemento mantiene la propria rappresentazione numerica semplice:

```
95-88-76-100-67
```

### **Esempio di codice 3 — Confronto tra il rendering predefinito e quello in singola cella**

```python
import aspose.cells as ac

workbook = ac.Workbook()
cells = workbook.worksheets[0].cells
# Column B: default marker — values spread vertically down the column
cells.get("B1").put_value("Default")
cells.get("B2").put_value("&=Order.Items")
# Column C: single-cell rendering — the whole array joins into one cell
cells.get("C1").put_value("Single cell")
cells.get("C2").put_value("&=Order.Items(arrayassingle:true)")
designer = ac.WorkbookDesigner(workbook)
designer.set_json_data_source(
    "Order",
    '[{"Items": ["Apple", "Banana", "Cherry", "Date"]}]')
designer.process()
for row in range(1, 6):
    b = cells.get(row, 1).string_value or ""
    c = cells.get(row, 2).string_value or ""
    if b or c:
        print(f"B{row + 1}=[{b}]  C{row + 1}=[{c}]")
workbook.save("output-array-comparison.xlsx")
```

Il marcatore predefinito riempie una cella per ogni elemento, procedendo verso il basso nella colonna B, mentre il marcatore `arrayassingle` compatta lo stesso array in un'unica cella nella colonna C:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Note e buone pratiche**

Quando si lavora con gli attributi `arrayassingle` e `arraydelimiter`, tenere presenti i punti seguenti:
- I valori degli attributi usano la forma `name:value`. Una forma con il segno di uguaglianza, come `arrayassingle=true`, non viene riconosciuta e ricade silenziosamente nel comportamento predefinito di espansione.
- Separare gli attributi con una virgola e senza spazi; uno spazio dopo la virgola sposta di un carattere il valore del separatore (consultare l'avviso precedente).
- Il valore `arraydelimiter` può essere un singolo carattere scritto direttamente dopo i due punti oppure una stringa di più caratteri racchiusa tra virgolette doppie.
- Quando `arraydelimiter` viene omesso, gli elementi vengono uniti con una virgola.
- Fornire i campi array tramite gli oggetti riga di `set_json_data_source`. Gli oggetti Python e i dizionari passati a `set_data_source` non vengono associati su questa piattaforma, mentre una `ICellsDataTable` personalizzata la cui colonna restituisce un elenco Python visualizza la rappresentazione testuale del contenitore dell'elenco anziché unirne gli elementi.
- I numeri JSON mantengono la propria forma di intero semplice nell'output unito.

## **Articoli correlati**
- [Aggiungere campi filtro a una tabella pivot in Aspose.Cells per .NET](/cells/it/python-net/add-page-field-in-pivot-table/)
- [Applicare stili alle tabelle pivot in Aspose.Cells for Python via .NET](/cells/it/python-net/apply-style-to-pivot-table/)
- [Modificare il layout del campo pagina in una tabella pivot](/cells/it/python-net/change-page-field-layout/)
- [Convertire Sparkline in Immagine e HTML in Aspose.Cells for Python via .NET](/cells/it/python-net/convert-sparkline-to-image-and-html/)
- [Conversione di Excel in formato OFD](/cells/it/python-net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="python-net" >}}