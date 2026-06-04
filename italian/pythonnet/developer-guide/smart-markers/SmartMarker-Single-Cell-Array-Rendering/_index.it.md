---
title: Rendering di array in singola cella con SmartMarker | Aspose.Cells for Python via .NET
description: Scopri come eseguire il rendering dei dati di array in una singola cella utilizzando gli attributi ArrayAsSingle ed ExtraDelimiter negli Smart Marker con Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, libreria Python via .NET, foglio di calcolo, Smart Markers, ArrayAsSingle, ExtraDelimiter, array in singola cella, rendering di array, modello
type: docs
weight: 195
url: /it/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

Aspose.Cells supporta il rendering dei dati di array in una singola cella tramite Smart Markers. Utilizzando l'attributo `ArrayAsSingle` insieme all'attributo `ExtraDelimiter`, gli sviluppatori possono controllare come gli elementi dell'array vengono separati all'interno di una singola cella, fornendo una formattazione flessibile per report e modelli.

{{% /alert %}}

## **Introduzione**

Gli Smart Markers in Aspose.Cells sono una funzionalità potente basata su modelli che consente di popolare dinamicamente i dati del foglio di calcolo utilizzando espressioni di marker come `&=DataSource.Field`. Il marker viene posizionato in una cartella di lavoro del designer e, quando il modello viene elaborato dal `WorkbookDesigner`, i marker vengono sostituiti con i valori provenienti dall'origine dati fornita.

Per impostazione predefinita, quando uno Smart Marker fa riferimento a una proprietà array (ad esempio, `&=DataSource.Numbers`), il motore espande l'array e posiziona ciascun elemento in una cella adiacente separata, sia orizzontalmente lungo una riga sia verticalmente lungo una colonna. Sebbene questo comportamento sia comodo in molti scenari, esistono situazioni in cui si preferisce eseguire il rendering dell'intero array in un'unica cella, con gli elementi concatenati e separati da un delimitatore a scelta.

Gli attributi `ArrayAsSingle` ed `ExtraDelimiter`, utilizzati insieme all'interno di un tag Smart Marker, soddisfano esattamente questo requisito. Consentono di mantenere layout di report compatti e prevedibili, lavorando comunque in modo nativo con origini dati di tipo array.

## **Perché questa funzionalità è necessaria**

### **Comportamento predefinito di espansione dell'array**

Quando uno Smart Marker fa riferimento a una proprietà array, Aspose.Cells espande l'array su più celle per impostazione predefinita. Ad esempio, un marker come `&=Product.Tags` applicato a un `string[]` contenente quattro valori posizionerà ciascun valore nella propria cella, spingendo il resto del contenuto del modello verso l'esterno e potenzialmente compromettendo layout di report accuratamente progettati.

### **Limitazioni dei casi d'uso**

Esistono molti scenari pratici in cui il comportamento di espansione predefinito è indesiderabile:

- **Report in stile riepilogo** che richiedono un layout compatto con una riga per record.
- **Elenchi di tag, etichette o parole chiave** che devono essere visualizzati come valori separati da virgola o da pipe all'interno di una singola cella.
- **Chip di filtro o indicatori di stato** che raggruppano più valori in un unico punto per migliorare la leggibilità.
- **Pipeline a valle** (esportazione CSV, rendering PDF, mail merge) che si aspettano un singolo valore consolidato per cella anziché un intervallo espanso.
- **Compatibilità multipiattaforma**, in cui alcuni consumatori non tollerano array che si estendono su più celle.

### **Il gap che colma**

Senza un meccanismo integrato, gli sviluppatori sarebbero costretti a pre-elaborare i dati in Python, unendo gli array in stringhe delimitate prima di associarle al designer della cartella di lavoro. Ciò duplica la logica, complica i modelli di dati e aumenta la probabilità di errori. Gli attributi `ArrayAsSingle` ed `ExtraDelimiter` eliminano questa soluzione alternativa gestendo la formattazione in modo dichiarativo all'interno dello Smart Marker stesso.

## **Vantaggi della funzionalità**

L'utilizzo degli attributi `ArrayAsSingle` ed `ExtraDelimiter` nei propri Smart Marker offre diversi vantaggi:

- **Contenimento in una singola cella**: tutti gli elementi dell'array vengono resi esattamente in una cella, mantenendo layout compatti e prevedibili.
- **Controllo personalizzato del delimitatore**: specificare qualsiasi stringa separatore si desideri, ad esempio virgola, punto e virgola, trattino, pipe, nuova riga o qualsiasi testo personalizzato.
- **Formattazione guidata dal modello**: non è richiesto codice aggiuntivo per pre-elaborare i dati; le regole di formattazione risiedono all'interno del tag Smart Marker.
- **Report più puliti**: i dati di array non spingono più il contenuto adiacente del modello in righe o colonne diverse.
- **Tipi di dati versatili**: funziona con stringhe, numeri, date e qualsiasi altro tipo di dati che possa essere unito con un delimitatore.
- **Compatibilità con le versioni precedenti**: quando gli attributi vengono omessi, viene mantenuto il comportamento di espansione originale, quindi i modelli esistenti continuano a funzionare invariati.

## **Come utilizzare questa funzionalità**

### **Sintassi degli Smart Marker**

Gli attributi `ArrayAsSingle` ed `ExtraDelimiter` vengono passati come coppie chiave-valore all'interno delle parentesi di uno Smart Marker standard. La sintassi generale è:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Il marker è composto dalle seguenti parti:

- `&=DataSource.ArrayProperty` — lo Smart Marker standard che fa riferimento alla proprietà array sull'origine dati associata.
- `arrayasSingle=true` — indica al motore di eseguire il rendering dell'intero array in una singola cella. Solo il valore `true` attiva il comportamento in singola cella.
- `extraDelimiter=", "` — definisce il separatore inserito tra gli elementi dell'array. Il valore è una stringa letterale; può essere vuoto, un singolo carattere o una stringa multi-carattere.

{{% alert color="primary" %}}

L'attributo `extraDelimiter` accetta qualsiasi stringa letterale, inclusi delimitatori multi-carattere, testo personalizzato o sequenze di escape come `\n` per output separati da nuova riga. Se l'array è vuoto, la cella risultante viene lasciata vuota.

{{% /alert %}}

### **Flusso di lavoro passo per passo**

Il seguente flusso di lavoro descrive come eseguire il rendering di un array in una singola cella utilizzando gli Smart Marker.

1. **Preparare l'origine dati**: creare una classe (o struttura dati) che espone una proprietà che restituisce un array. La proprietà può restituire `list[str]`, `list[int]` o qualsiasi altro tipo di array supportato.
2. **Creare una cartella di lavoro del designer**: creare un nuovo `Workbook`, aggiungere una riga di intestazione e posizionare una cella Smart Marker che faccia riferimento alla proprietà array con gli attributi `arrayasSingle` e `extraDelimiter`.
3. **Istanziare il WorkbookDesigner**: creare un oggetto `WorkbookDesigner`, associarvi la cartella di lavoro del designer e associare la propria origine dati utilizzando il metodo `set_data_source`.
4. **Elaborare i marker**: chiamare il metodo `WorkbookDesigner.process()` per espandere gli Smart Marker e popolare la cartella di lavoro con i dati reali.
5. **Salvare il risultato**: salvare la cartella di lavoro risultante su disco in XLSX o in qualsiasi altro formato di file supportato.

### **Esempio di codice 1 — Rendering di base di un array di stringhe**

```python
class Product:
    def __init__(self):
        self.Tags = []

product = Product()
product.Tags = ["C#", "Aspose", "SmartMarker", "Excel"]

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

worksheet.cells["A1"].put_value("Tags")
worksheet.cells["A2"].put_value("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")")

designer = ac.WorkbookDesigner()
designer.workbook = workbook
designer.set_data_source("Product", product)
designer.process()

workbook.save("output_arraySingle.xlsx")
```

### **Esempio di codice 2 — Array numerico con delimitatore personalizzato**

```python
class Student:
    def __init__(self):
        self.scores = []


student = Student()
student.scores = [95, 88, 76, 100, 67]

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

worksheet.cells["A1"].put_value("Scores")
worksheet.cells["A2"].put_value(" - ".join(str(s) for s in student.scores))

workbook.save("output_numericArray.xlsx")
```

### **Esempio di codice 3 — Confronto tra comportamento predefinito e ArrayAsSingle**

```python
class Order:
    def __init__(self, items):
        self._items = items

    @property
    def Items(self):
        return self._items

    @Items.setter
    def Items(self, value):
        self._items = value

order = Order(["Apple", "Banana", "Cherry", "Date"])

workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells

# Sezione 1: Smart Marker predefinito - valori distribuiti orizzontalmente nelle celle
cells["A1"].put_value("Default Spreading Behavior:")
cells["A2"].put_value("&=Order.Items")

# Sezione 2: Nuovo rendering a cella singola utilizzando arrayasSingle e extraDelimiter
cells["A4"].put_value("Single Cell Rendering (arrayasSingle=true):")
cells["A5"].put_value('&=Order.Items(arrayasSingle=true, extraDelimiter="; ")')

# Collega l'origine dati ed elabora gli Smart Marker
designer = ac.WorkbookDesigner(workbook)
designer.set_data_source("Order", order)
designer.process()

# Salva la cartella di lavoro risultante
workbook.save("output_comparison.xlsx")
```

### **Note e best practice**

Tenere presente i seguenti punti quando si lavora con gli attributi `ArrayAsSingle` ed `ExtraDelimiter`:

- Il valore di `extraDelimiter` viene trattato come una stringa letterale; effettuare l'escape di eventuali caratteri speciali che il processore del modello potrebbe interpretare.
- L'attributo `arrayasSingle` accetta un valore booleano (`True` / `False`). Solo `True` attiva il comportamento in singola cella; qualsiasi altro valore ripristina il comportamento di espansione predefinito.
- Se l'array è vuoto o nullo, la cella viene lasciata vuota (oppure contiene una stringa vuota a seconda del tipo di dati).
- La funzionalità funziona con origini dati di oggetti, nonché con origini `DataSet` e `DataTable` in cui una colonna può essere suddivisa in array.
- Per output separati da nuova riga, è possibile utilizzare `\n` oppure `os.linesep` come valore del delimitatore.
- Posizionare lo Smart Marker in una cella con larghezza sufficiente per visualizzare la stringa concatenata risultante; in caso contrario, il contenuto potrebbe traboccare visivamente nelle celle adiacenti a seconda del formato.

## **Articoli correlati**

- [Smart Markers](/cells/it/python-net/smart-markers/)
- [Unione e separazione delle celle](/cells/it/python-net/merging-and-unmerging-cells/)

{{< app/cells/assistant language="python" >}}