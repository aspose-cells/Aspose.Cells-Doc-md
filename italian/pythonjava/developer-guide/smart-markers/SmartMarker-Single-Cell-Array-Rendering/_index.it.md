---
title: Rendering di un array in singola cella con SmartMarker | Aspose.Cells Python via Java
description: Scopri come rendere i dati di un array in una singola cella utilizzando gli attributi Smart Marker `arrayassingle` e `arraydelimiter` in Aspose.Cells for Python via Java.
linktitle: Rendering di un array in singola cella | Aspose.Cells
url: /it/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, libreria Python via Java, foglio di calcolo, Smart Marker, arrayassingle, arraydelimiter, array a singola cella, rendering di array, modello
type: docs
weight: 195
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells può rendere un'origine dati di tipo array in un'unica cella tramite gli Smart Marker. L'attributo `arrayassingle` disattiva la distribuzione predefinita degli elementi uno alla volta, mentre l'attributo `arraydelimiter` determina il separatore inserito tra gli elementi concatenati: una virgola per impostazione predefinita oppure un singolo carattere o una stringa di più caratteri tra virgolette, a seconda di quanto specificato.
{{% /alert %}}

## **Introduzione**

Gli Smart Marker di Aspose.Cells sono una funzione basata su modelli che popola dinamicamente i dati del foglio di calcolo mediante espressioni come `&=DataSource.Field`. Il marcatore viene inserito in una cartella di lavoro di progettazione e, quando il modello viene elaborato da `WorkbookDesigner`, i marcatori vengono sostituiti con i valori dell'origine dati fornita.
Per impostazione predefinita, quando uno Smart Marker fa riferimento a un campo di tipo array, ad esempio `&=Product.Tags` associato a un elenco di quattro valori, il motore espande l'array e colloca ogni elemento in una cella separata, distribuendo i valori verticalmente lungo la colonna sotto il marcatore. Sebbene questo comportamento sia comodo in molti scenari, in alcuni casi si preferisce rendere l'intero array in un'unica cella, con gli elementi concatenati e separati da un delimitatore a scelta.
Gli attributi `arrayassingle` e `arraydelimiter`, scritti tra parentesi di uno Smart Marker nella forma `name:value`, soddisfano esattamente questa esigenza. Consentono di mantenere layout dei report compatti e prevedibili, continuando a utilizzare in modo nativo le origini dati di tipo array.

## **Perché è necessaria questa funzione**

### **Comportamento predefinito di distribuzione degli array**

Quando uno Smart Marker fa riferimento a un campo di tipo array, Aspose.Cells espande l'array su più celle per impostazione predefinita. Ad esempio, un marcatore come `&=Product.Tags` utilizzato con un elenco contenente quattro valori colloca ciascun valore in una cella separata sotto il marcatore, spostando gli altri contenuti del modello verso l'esterno e potenzialmente compromettendo layout di report progettati con cura.

### **Limitazioni dei casi d'uso**

Sono presenti molti scenari pratici in cui il comportamento predefinito di distribuzione non è desiderabile:
- **Report riepilogativi** che richiedono un layout compatto con una riga per ogni record.
- **Elenchi di etichette o parole chiave** che devono essere visualizzati come valori separati da virgole o barre verticali all'interno di una singola cella.
- **Etichette di filtro o indicatori di stato** che riuniscono più valori in un unico punto per migliorarne la leggibilità.
- **Flussi di elaborazione successivi** (esportazione CSV, rendering PDF, stampa unione) che richiedono un singolo valore consolidato per cella anziché un intervallo espanso.
- **Compatibilità multipiattaforma**, in cui alcune applicazioni di destinazione non tollerano array estesi su più celle.

### **La lacuna che colma**

Senza un meccanismo integrato, gli sviluppatori sarebbero costretti a preelaborare i dati in Python, unendo le liste in stringhe delimitate prima di associarle alla cartella di lavoro di progettazione. Ciò duplicherebbe la logica, complicherebbe i modelli di dati e aumenterebbe la probabilità di errori. Gli attributi `arrayassingle` e `arraydelimiter` eliminano questa soluzione alternativa gestendo la formattazione in modo dichiarativo all'interno dello stesso Smart Marker.

## **Vantaggi della funzione**

L'utilizzo degli attributi `arrayassingle` e `arraydelimiter` negli Smart Marker offre diversi vantaggi:
- **Contenimento in una singola cella**: tutti gli elementi dell'array vengono renderizzati in esattamente una cella, mantenendo layout compatti e prevedibili.
- **Controllo del delimitatore personalizzato**: specifica il separatore preferito, ovvero la virgola predefinita, un punto e virgola, un trattino, una barra verticale o una stringa di più caratteri tra virgolette come `" | "`.
- **Formattazione guidata dal modello**: non è necessario codice aggiuntivo per preelaborare i dati; le regole di formattazione sono definite all'interno dello Smart Marker.
- **Report più puliti**: i dati di tipo array non spostano più il contenuto adiacente del modello in righe o colonne diverse.
- **Tipi di dati versatile**: funziona con array di stringhe forniti come righe JSON, inclusi i valori numerici resi come stringhe.
- **Compatibilità con le versioni precedenti**: quando gli attributi vengono omessi, il comportamento di distribuzione originale viene mantenuto, pertanto i modelli esistenti continuano a funzionare senza modifiche.

## **Come utilizzare questa funzione**

### **Sintassi dello Smart Marker**

Gli attributi `arrayassingle` e `arraydelimiter` utilizzano la grammatica `name:value` degli attributi di Aspose.Cells all'interno delle parentesi di uno Smart Marker standard. La sintassi generale è:

```
&=DataSource.ArrayField(arrayassingle:true,arraydelimiter:;)
```

Il marcatore è costituito dalle seguenti parti:
- `&=DataSource.ArrayField` — lo Smart Marker standard che fa riferimento al campo di tipo array dell'origine dati associata.
- `arrayassingle:true` — indica al motore di rendere l'intero array in un'unica cella anziché distribuirne gli elementi.
- `arraydelimiter:;` — facoltativo; definisce il separatore inserito tra gli elementi dell'array. Se viene omesso, viene utilizzata una virgola.

{{% alert color="warning" %}}
Scrivi gli attributi nella forma `name:value` (due punti, non un segno uguale) e separa più attributi con una virgola **senza spazi**. Uno spazio dopo la virgola sposta di un carattere il valore analizzato: `(arrayassingle:true, arraydelimiter:;)` produrrebbe la concatenazione con il separatore errato `:;` anziché `;`.
{{% /alert %}}

### **Forme del delimitatore**

- Un singolo carattere viene scritto direttamente dopo i due punti: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- Un separatore di più caratteri viene scritto tra virgolette doppie: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Flusso di lavoro passo per passo**

Il seguente flusso di lavoro descrive come rendere un array in una singola cella utilizzando gli Smart Marker.
1. **Preparare l'origine dati**: organizza ogni record come un oggetto JSON il cui campo contiene un array, ad esempio `{"Tags": ["C#", "Aspose"]}`. Le normali istanze di classi Python e i dizionari passati a `setDataSource` non vengono associati su questa piattaforma; le righe JSON sono il formato tabulare supportato.
2. **Creare una cartella di lavoro di progettazione**: crea una nuova istanza di `Workbook`, aggiungi una riga di intestazione e inserisci in una cella uno Smart Marker che faccia riferimento al campo di tipo array con l'attributo `arrayassingle` e, quando è necessario un separatore personalizzato, con `arraydelimiter`.
3. **Istanziare `WorkbookDesigner`**: crea un'istanza di `WorkbookDesigner` associata alla cartella di lavoro e allega le righe JSON con `setJsonDataSource`.
4. **Elaborare i marcatori**: chiama il metodo `WorkbookDesigner.process()` per espandere gli Smart Marker e popolare la cartella di lavoro con i dati effettivi.
5. **Salvare il risultato**: salva la cartella di lavoro risultante su disco in formato XLSX o in qualsiasi altro formato di file supportato.

### **Esempio di codice 1 — Rendering di base di un array di stringhe**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Tags")
# No spaces inside the parentheses: attributes are name:value pairs
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)")
designer = WorkbookDesigner(workbook)
designer.setJsonDataSource(
    "Product",
    '[{"Tags": ["C#", "Aspose", "SmartMarker", "Excel"]}]')
designer.process()
print(worksheet.getCells().get("A2").getStringValue())
workbook.save("output-array-single.xlsx")
```

L'esempio stampa il valore ottenuto concatenando l'intero array. Le quattro etichette finiscono in una cella, separate dalla virgola predefinita:

```
C#,Aspose,SmartMarker,Excel
```

### **Esempio di codice 2 — Valori numerici con un delimitatore personalizzato**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Scores")
# arraydelimiter:- joins the values with a hyphen
worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)")
designer = WorkbookDesigner(workbook)
designer.setJsonDataSource(
    "Student",
    '[{"Scores": ["95", "88", "76", "100", "67"]}]')
designer.process()
print(worksheet.getCells().get("A2").getStringValue())
workbook.save("output-array-numeric.xlsx")
```

Con i punteggi forniti come stringhe JSON, il risultato della concatenazione conserva i numeri così come sono:

```
95-88-76-100-67
```

{{% alert color="note" %}}
I numeri JSON passati attraverso il motore Java arrivano come numeri in virgola mobile, pertanto l'array `[95, 88]` verrebbe concatenato come `95.0-88.0`. Metti tra virgolette i numeri nelle righe JSON se desideri che la cella concatenata contenga il testo esatto dell'intero.
{{% /alert %}}

### **Esempio di codice 3 — Confronto tra il rendering predefinito e quello in singola cella**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner

workbook = Workbook()
cells = workbook.getWorksheets().get(0).getCells()
# Column B: default marker — values spread vertically down the column
cells.get("B1").putValue("Default")
cells.get("B2").putValue("&=Order.Items")
# Column C: single-cell rendering — the whole array joins into one cell
cells.get("C1").putValue("Single cell")
cells.get("C2").putValue("&=Order.Items(arrayassingle:true)")
designer = WorkbookDesigner(workbook)
designer.setJsonDataSource(
    "Order",
    '[{"Items": ["Apple", "Banana", "Cherry", "Date"]}]')
designer.process()
for row in range(1, 6):
    b = cells.get(row, 1).getStringValue() or ""
    c = cells.get(row, 2).getStringValue() or ""
    if b or c:
        print(f"B{row + 1}=[{b}]  C{row + 1}=[{c}]")
workbook.save("output-array-comparison.xlsx")
```

Il marcatore predefinito riempie una cella per ogni elemento scendendo lungo la colonna B, mentre il marcatore `arrayassingle` compatta lo stesso array in un'unica cella della colonna C:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Note e best practice**

Quando lavori con gli attributi `arrayassingle` e `arraydelimiter`, tieni presenti i punti seguenti:
- I valori degli attributi utilizzano la forma `name:value`. La forma con il segno uguale, come `arrayassingle=true`, non viene riconosciuta e ricade silenziosamente nel comportamento predefinito di distribuzione.
- Separa gli attributi con una virgola e senza spazi; uno spazio dopo la virgola sposta di un carattere il valore del delimitatore, come indicato nell'avviso precedente.
- Il valore `arraydelimiter` può essere un singolo carattere scritto direttamente dopo i due punti oppure una stringa di più caratteri racchiusa tra virgolette doppie.
- Quando `arraydelimiter` viene omesso, gli elementi vengono concatenati con una virgola.
- Fornisci i campi di tipo array tramite gli oggetti riga di `setJsonDataSource`; gli oggetti Python semplici e i dizionari passati a `setDataSource` non vengono associati su questa piattaforma.
- I numeri JSON arrivano come numeri in virgola mobile attraverso il motore Java (`95` viene concatenato come `95.0`); metti tra virgolette i valori numerici nelle righe JSON quando è importante che il testo dell'intero sia esatto.
- Colloca lo Smart Marker in una cella con una larghezza sufficiente per visualizzare la stringa finale ottenuta concatenando gli elementi; in caso contrario, il contenuto può traboccare visivamente nelle celle adiacenti, a seconda del formato.

## **Articoli correlati**
- [Aggiungere campi filtro a una tabella pivot in Aspose.Cells for Python via Java](/cells/it/python-java/add-page-field-in-pivot-table/)
- [Applica stili alle tabelle pivot in Aspose.Cells for Python via Java](/cells/it/python-java/apply-style-to-pivot-table/)
- [Modificare il layout del campo pagina in una tabella pivot](/cells/it/python-java/change-page-field-layout/)
- [Convertire Sparkline in Immagine e HTML in Aspose.Cells for Python via Java](/cells/it/python-java/convert-sparkline-to-image-and-html/)
- [Conversione di Excel in formato OFD](/cells/it/python-java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="python" >}}