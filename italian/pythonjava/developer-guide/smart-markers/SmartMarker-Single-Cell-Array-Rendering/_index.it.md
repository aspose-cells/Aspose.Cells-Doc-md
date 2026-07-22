---
title: Rendering di Array in Cella Singola con SmartMarker | Aspose.Cells Python via Java
linktitle: Rendering di Array
description: Scopri come eseguire il rendering dei dati di un array in una singola cella utilizzando gli attributi ArrayAsSingle e ExtraDelimiter negli Smart Markers con Aspose.Cells for Python via Java.
keywords: Aspose.Cells, libreria Python via Java, foglio di calcolo, Smart Markers, ArrayAsSingle, ExtraDelimiter, array in cella singola, rendering di array, modello
type: docs
weight: 195
url: /it/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells supporta il rendering dei dati di un array in una singola cella tramite gli Smart Markers. Utilizzando l'attributo `ArrayAsSingle` insieme all'attributo `ExtraDelimiter`, gli sviluppatori possono controllare come gli elementi dell'array vengono separati all'interno di una singola cella, fornendo una formattazione flessibile per report e modelli.

{{% /alert %}}

## **Introduzione**

Gli Smart Markers in Aspose.Cells sono una potente funzionalità basata su modelli che consente di popolare dinamicamente i dati del foglio di calcolo utilizzando espressioni marker come `&=DataSource.Field`. Il marker viene posizionato in una cartella di lavoro designer e, quando il modello viene elaborato dal `WorkbookDesigner`, i marker vengono sostituiti con i valori provenienti dall'origine dati fornita.

Per impostazione predefinita, quando uno Smart Marker fa riferimento a una proprietà di array (ad esempio, `&=DataSource.Numbers`), il motore espande l'array e posiziona ciascun elemento in una cella adiacente separata — orizzontalmente su una riga o verticalmente lungo una colonna. Sebbene questo comportamento sia comodo in molti scenari, ci sono situazioni in cui si preferisce eseguire il rendering dell'intero array in un'unica cella, con gli elementi concatenati e separati da un delimitatore a scelta.

Gli attributi `ArrayAsSingle` e `ExtraDelimiter`, utilizzati insieme all'interno di un tag Smart Marker, soddisfano esattamente questo requisito. Consentono di mantenere i layout dei report compatti e prevedibili, lavorando comunque in modo nativo con origini dati di tipo array.

## **Perché Questa Funzionalità È Necessaria**

### **Comportamento Predefinito di Espansione dell'Array**

Quando uno Smart Marker fa riferimento a una proprietà di array, Aspose.Cells espande l'array su più celle per impostazione predefinita. Ad esempio, un marker come `&=Product.Tags` applicato a un `string[]` contenente quattro valori posizionerà ciascun valore nella propria cella, spingendo gli altri contenuti del modello verso l'esterno e potenzialmente rompendo layout di report accuratamente progettati.

### **Limitazioni dei Casi d'Uso**

Esistono molti scenari pratici in cui il comportamento di espansione predefinito è indesiderabile:

- **Report in stile riepilogo** che necessitano di un layout compatto con una riga per record.
- **Elenchi di tag, etichette o parole chiave** che devono essere visualizzati come valori separati da virgola o da pipe all'interno di una singola cella.
- **Chip di filtro o indicatori di stato** che raggruppano più valori in un unico punto per una migliore leggibilità.
- **Pipeline a valle** (esportazione CSV, rendering PDF, stampa unione) che si aspettano un singolo valore consolidato per cella anziché un intervallo espanso.
- **Compatibilità multipiattaforma**, dove alcuni consumatori non tollerano array che si estendono su più celle.

### **Il Gap che Colma**

Senza un meccanismo integrato, gli sviluppatori sarebbero costretti a pre-elaborare i dati in Python — unendo gli array in stringhe delimitate prima di associarle alla cartella di lavoro designer. Ciò duplica la logica, complica i modelli di dati e aumenta la probabilità di errori. Gli attributi `ArrayAsSingle` e `ExtraDelimiter` eliminano questa soluzione alternativa gestendo la formattazione in modo dichiarativo all'interno dello Smart Marker stesso.

## **Vantaggi della Funzionalità**

L'utilizzo degli attributi `ArrayAsSingle` e `ExtraDelimiter` nei tuoi Smart Markers offre diversi vantaggi:

- **Contenimento in cella singola**: tutti gli elementi dell'array vengono renderizzati in esattamente una cella, mantenendo i layout compatti e prevedibili.
- **Controllo personalizzato del delimitatore**: specifica qualsiasi stringa separatore desideri — virgola, punto e virgola, trattino, pipe, nuova riga o qualsiasi testo personalizzato.
- **Formattazione guidata dal modello**: non è richiesto codice aggiuntivo per pre-elaborare i dati; le regole di formattazione risiedono all'interno del tag Smart Marker.
- **Report più puliti**: i dati dell'array non spingono più il contenuto del modello adiacente in righe o colonne diverse.
- **Tipi di dati versatili**: funziona con stringhe, numeri, date e qualsiasi altro tipo di dati che può essere unito con un delimitatore.
- **Compatibilità con le versioni precedenti**: quando gli attributi vengono omessi, viene mantenuto il comportamento di espansione originale, quindi i modelli esistenti continuano a funzionare senza modifiche.

## **Come Utilizzare Questa Funzionalità**

### **Sintassi degli Smart Markers**

Gli attributi `ArrayAsSingle` e `ExtraDelimiter` vengono passati come coppie chiave-valore all'interno delle parentesi di uno Smart Marker standard. La sintassi generale è:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Il marker è composto dalle seguenti parti:

- `&=DataSource.ArrayProperty` — lo Smart Marker standard che fa riferimento alla proprietà array sull'origine dati associata.
- `arrayasSingle=true` — indica al motore di eseguire il rendering dell'intero array in una singola cella. Solo il valore `true` attiva il comportamento in cella singola.
- `extraDelimiter=", "` — definisce il separatore posizionato tra gli elementi dell'array. Il valore è una stringa letterale; può essere vuoto, un singolo carattere o una stringa multi-carattere.

{{% alert color="primary" %}}

L'attributo `extraDelimiter` accetta qualsiasi stringa letterale, inclusi delimitatori multi-carattere, testo personalizzato o sequenze di escape come `\n` per output separati da nuova riga. Se l'array è vuoto, la cella risultante viene lasciata vuota.

{{% /alert %}}

### **Flusso di Lavoro Passo per Passo**

Il seguente flusso di lavoro descrive come eseguire il rendering di un array in una singola cella utilizzando gli Smart Markers.

1. **Prepara l'origine dati**: crea una classe (o struttura dati) che espone una proprietà che restituisce un array. La proprietà può restituire `string[]`, `int[]` o qualsiasi altro tipo di array supportato.
2. **Crea una cartella di lavoro designer**: crea un nuovo `Workbook`, aggiungi una riga di intestazione e posiziona una cella Smart Marker che fa riferimento alla proprietà array con gli attributi `arrayasSingle` e `extraDelimiter`.
3. **Istanzia il WorkbookDesigner**: crea un oggetto `WorkbookDesigner`, associa la cartella di lavoro designer ad esso e associa la tua origine dati utilizzando il metodo `set_data_source`.
4. **Elabora i marker**: chiama il metodo `WorkbookDesigner.process()` per espandere gli Smart Markers e popolare la cartella di lavoro con i dati reali.
5. **Salva il risultato**: salva la cartella di lavoro risultante su disco in formato XLSX o in qualsiasi altro formato di file supportato.

### **Esempio di Codice 1 — Rendering Base di Array di Stringhe**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, WorkbookDesigner

class Product:
    def __init__(self, tags):
        self._tags = tags
    
    def getTags(self):
        return self._tags

product = Product(["C#", "Aspose", "SmartMarker", "Excel"])

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

worksheet.getCells().get("A1").putValue("Tags")
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")")

designer = WorkbookDesigner()
designer.setWorkbook(workbook)
designer.setDataSource("Product", product)
designer.process()

workbook.save("output_arraySingle.xlsx")

jpype.shutdownJVM()
```

### **Esempio di Codice 2 — Array Numerico con Delimitatore Personalizzato**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook

# Definizione della classe Student
class Student:
    def __init__(self):
        self.Scores = []

student = Student()
student.Scores = [95, 88, 76, 100, 67]

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

worksheet.getCells().get("A1").putValue("Scores")
worksheet.getCells().get("A2").putValue(" - ".join(str(s) for s in student.Scores))

workbook.save("output_numericArray.xlsx")

jpype.shutdownJVM()
```

### **Esempio di Codice 3 — Confronto tra Comportamento Predefinito e ArrayAsSingle**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, WorkbookDesigner

# Definire l'origine dati come dizionario (equivalente alla classe Order)
order = {"Items": ["Apple", "Banana", "Cherry", "Date"]}

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Sezione 1: Smart Marker predefinito - valori distribuiti orizzontalmente tra le celle
cells.get("A1").putValue("Default Spreading Behavior:")
cells.get("A2").putValue("&=Order.Items")

# Sezione 2: Nuovo rendering a cella singola utilizzando arrayasSingle e extraDelimiter
cells.get("A4").putValue("Single Cell Rendering (arrayasSingle=true):")
cells.get("A5").putValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")")

# Associare l'origine dati ed elaborare gli Smart Marker
designer = WorkbookDesigner(workbook)
designer.setDataSource("Order", order)
designer.process()

# Salvare la cartella di lavoro risultante
workbook.save("output_comparison.xlsx")

jpype.shutdownJVM()
```

### **Note e Best Practices**

Tieni presente i seguenti punti quando lavori con gli attributi `ArrayAsSingle` e `ExtraDelimiter`:

- Il valore di `extraDelimiter` viene trattato come una stringa letterale; esegui l'escape di eventuali caratteri speciali che il tuo processore di modelli potrebbe interpretare.
- L'attributo `arrayasSingle` accetta un valore booleano (`true` / `false`). Solo `true` attiva il comportamento in cella singola; qualsiasi altro valore ricade nel comportamento di espansione predefinito.
- Se l'array è vuoto o nullo, la cella viene lasciata vuota (oppure contiene una stringa vuota a seconda del tipo di dati).
- La funzionalità funziona sia con origini dati di oggetti sia con origini `DataSet` e `DataTable` in cui una colonna può essere suddivisa in array.
- Per output separati da nuova riga, puoi utilizzare `\n` o la costante di nuova riga della piattaforma come valore del delimitatore.
- Posiziona lo Smart Marker in una cella che abbia larghezza sufficiente per visualizzare la stringa concatenata risultante; altrimenti, il contenuto potrebbe traboccare visivamente nelle celle adiacenti a seconda del formato.

## **Articoli Correlati**

- [Smart Markers](/cells/it/python-java/smart-markers/)

{{< app/cells/assistant language="python" >}}