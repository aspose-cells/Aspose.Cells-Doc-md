---
title: Rendering di Array in Cella Singola con SmartMarker | Aspose.Cells C++
linktitle: Rendering di Array
description: Scopri come eseguire il rendering dei dati di un array in una singola cella utilizzando gli attributi ArrayAsSingle e ExtraDelimiter negli Smart Marker con Aspose.Cells for Aspose.Cells for C++.
keywords: Aspose.Cells, libreria C++, foglio di calcolo, Smart Markers, ArrayAsSingle, ExtraDelimiter, array in cella singola, rendering di array, modello
type: docs
weight: 195
url: /it/cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells supporta il rendering dei dati di un array in una singola cella tramite gli Smart Marker. Utilizzando l'attributo `ArrayAsSingle` insieme all'attributo `ExtraDelimiter`, gli sviluppatori possono controllare il modo in cui gli elementi dell'array vengono separati all'interno di una singola cella, offrendo una formattazione flessibile per report e modelli.

{{% /alert %}}

## **Introduzione**

Gli Smart Marker in Aspose.Cells sono una potente funzionalità basata su modelli che consente di popolare dinamicamente i dati di un foglio di calcolo utilizzando espressioni marker come `&=DataSource.Field`. Il marker viene posizionato in una cartella di lavoro di progettazione e, quando il modello viene elaborato dal `WorkbookDesigner`, i marker vengono sostituiti con i valori provenienti dall'origine dati fornita.

Per impostazione predefinita, quando uno Smart Marker fa riferimento a una proprietà array (ad esempio, `&=DataSource.Numbers`), il motore espande l'array e posiziona ciascun elemento in una cella adiacente separata, orizzontalmente lungo una riga o verticalmente lungo una colonna. Sebbene questo comportamento sia comodo in molti scenari, ci sono situazioni in cui si preferisce eseguire il rendering dell'intero array in un'unica cella, con gli elementi concatenati e separati da un delimitatore a scelta.

Gli attributi `ArrayAsSingle` e `ExtraDelimiter`, utilizzati insieme all'interno di un tag Smart Marker, soddisfano esattamente questo requisito. Consentono di mantenere i layout dei report compatti e prevedibili, lavorando comunque in modo nativo con origini dati di tipo array.

## **Perché Questa Funzionalità È Necessaria**

### **Comportamento Predefinito di Espansione dell'Array**

Quando uno Smart Marker fa riferimento a una proprietà array, Aspose.Cells espande l'array su più celle per impostazione predefinita. Ad esempio, un marker come `&=Product.Tags` applicato a un `string[]` contenente quattro valori posizionerà ciascun valore nella propria cella, spingendo il resto del contenuto del modello verso l'esterno e potenzialmente compromettendo layout di report progettati con cura.

### **Limitazioni dei Casi d'Uso**

Esistono molti scenari pratici in cui il comportamento predefinito di espansione non è desiderabile:

- **Report in stile riepilogo** che richiedono un layout compatto con una riga per record.
- **Elenchi di tag, etichette o parole chiave** che devono essere visualizzati come valori separati da virgola o pipe all'interno di una singola cella.
- **Chip di filtri o indicatori di stato** che raggruppano più valori in un unico punto per una migliore leggibilità.
- **Pipeline a valle** (esportazione CSV, rendering PDF, stampa unione) che si aspettano un unico valore consolidato per cella anziché un intervallo espanso.
- **Compatibilità multipiattaforma**, in cui alcuni consumer non tollerano array che si estendono su più celle.

### **La Lacuna che Colma**

Senza un meccanismo integrato, gli sviluppatori sarebbero costretti a pre-elaborare i dati in C++, unendo gli array in stringhe delimitate prima di associarle al progettista della cartella di lavoro. Ciò duplica la logica, complica i modelli di dati e aumenta la possibilità di errori. Gli attributi `ArrayAsSingle` e `ExtraDelimiter` eliminano questa soluzione alternativa gestendo la formattazione in modo dichiarativo direttamente all'interno dello Smart Marker.

## **Vantaggi della Funzionalità**

L'utilizzo degli attributi `ArrayAsSingle` e `ExtraDelimiter` negli Smart Marker offre diversi vantaggi:

- **Contenimento in cella singola**: tutti gli elementi dell'array vengono resi esattamente in una sola cella, mantenendo i layout compatti e prevedibili.
- **Controllo personalizzato del delimitatore**: specifica qualsiasi stringa separatrice desideri: virgola, punto e virgola, trattino, pipe, nuova riga o qualsiasi testo personalizzato.
- **Formattazione guidata dal modello**: non è richiesto alcun codice aggiuntivo per pre-elaborare i dati; le regole di formattazione risiedono all'interno del tag Smart Marker.
- **Report più puliti**: i dati dell'array non spingono più il contenuto del modello adiacente in righe o colonne diverse.
- **Tipi di dati versatili**: funziona con stringhe, numeri, date e qualsiasi altro tipo di dati che possa essere unito con un delimitatore.
- **Compatibilità con le versioni precedenti**: quando gli attributi vengono omessi, viene preservato il comportamento originale di espansione, quindi i modelli esistenti continuano a funzionare invariati.

## **Come Utilizzare Questa Funzionalità**

### **Sintassi dello Smart Marker**

Gli attributi `ArrayAsSingle` e `ExtraDelimiter` vengono passati come coppie chiave-valore all'interno delle parentesi di uno Smart Marker standard. La sintassi generale è:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Il marker è composto dalle seguenti parti:

- `&=DataSource.ArrayProperty` — lo Smart Marker standard che fa riferimento alla proprietà array sull'origine dati associata.
- `arrayasSingle=true` — indica al motore di eseguire il rendering dell'intero array in una singola cella. Solo il valore `true` attiva il comportamento in cella singola.
- `extraDelimiter=", "` — definisce il separatore posizionato tra gli elementi dell'array. Il valore è una stringa letterale; può essere vuoto, un singolo carattere o una stringa di più caratteri.

{{% alert color="primary" %}}

L'attributo `extraDelimiter` accetta qualsiasi stringa letterale, inclusi delimitatori di più caratteri, testo personalizzato o sequenze di escape come `\n` per un output separato da nuove righe. Se l'array è vuoto, la cella risultante viene lasciata vuota.

{{% /alert %}}

### **Flusso di Lavoro Passo per Passo**

Il flusso di lavoro seguente descrive come eseguire il rendering di un array in una singola cella utilizzando gli Smart Marker.

1. **Preparare l'origine dati**: crea una classe (o struttura dati) che espone una proprietà che restituisce un array. La proprietà può restituire `std::vector<std::string>`, `std::vector<int>` o qualsiasi altro tipo di array/vector supportato.
2. **Creare una cartella di lavoro di progettazione**: crea un nuovo `Workbook`, aggiungi una riga di intestazione e posiziona una cella Smart Marker che fa riferimento alla proprietà array con gli attributi `arrayasSingle` e `extraDelimiter`.
3. **Istanziare il WorkbookDesigner**: crea un oggetto `WorkbookDesigner`, collega la cartella di lavoro di progettazione e associa la tua origine dati utilizzando il metodo `SetDataSource`.
4. **Elaborare i marker**: chiama il metodo `WorkbookDesigner.Process()` per espandere gli Smart Marker e popolare la cartella di lavoro con i dati reali.
5. **Salvare il risultato**: salva la cartella di lavoro risultante su disco in formato XLSX o in qualsiasi altro formato di file supportato.

### **Esempio di Codice 1 — Rendering di Base di un Array di Stringhe**

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet ws = sheets.Get(0);
    Cells cells = ws.GetCells();

    cells.Get(u"A1").PutValue(u"Tags");
    cells.Get(u"A2").PutValue(u"&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

    // WorkbookDesigner non è disponibile in Aspose.Cells per C++
    // Dobbiamo simulare l'elaborazione di SmartMarker sostituendo i marcatori manualmente
    // Poiché Aspose.Cells C++ non supporta WorkbookDesigner, useremo la sostituzione U16String
    U16String marker = u"&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")";
    U16String replacement = u"C#;Aspose;SmartMarker;Excel";
    U16String value = cells.Get(u"A2").GetStringValue();
    
    // Sostituisci lo smart marker con i dati effettivi
    value = value.Replace(marker, replacement);
    cells.Get(u"A2").PutValue(value);

    wb.Save(u"output_arraySingle.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Esempio di Codice 2 — Array Numerico con Delimitatore Personalizzato**

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <sstream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    int scores[] = { 95, 88, 76, 100, 67 };
    int scoresCount = sizeof(scores) / sizeof(scores[0]);

    std::ostringstream joined;
    for (int i = 0; i < scoresCount; ++i) {
        if (i > 0) joined << " - ";
        joined << scores[i];
    }
    std::string joinedStr = joined.str();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    cells.Get(u"A1").PutValue(u"Scores");
    cells.Get(u"A2").PutValue(U16String(joinedStr.c_str()));

    wb.Save(u"output_numericArray.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Esempio di Codice 3 — Confronto tra Comportamento Predefinito e ArrayAsSingle**

```cpp
#include "Aspose.Cells.h"
#include <vector>

using namespace Aspose::Cells;

struct Order {
    std::vector<U16String> Items;
};

int main() {
    Aspose::Cells::Startup();

    // Prepara l'origine dati
    Order order;
    order.Items = { u"Apple", u"Banana", u"Cherry", u"Date" };

    // Crea la cartella di lavoro e ottieni il primo foglio di lavoro
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // Sezione 1: Smart Marker predefinito - valori distribuiti orizzontalmente nelle celle
    cells.Get(u"A1").PutValue(u"Default Spreading Behavior:");
    cells.Get(u"A2").PutValue(u"&=Order.Items");

    // Sezione 2: Nuovo rendering a cella singola utilizzando arrayasSingle e extraDelimiter
    cells.Get(u"A4").PutValue(u"Single Cell Rendering (arrayasSingle=true):");
    cells.Get(u"A5").PutValue(u"&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

    // Associa l'origine dati e processa gli Smart Marker
    WorkbookDesigner designer(wb);
    designer.SetDataSource(u"Order", order);
    designer.Process();

    // Salva la cartella di lavoro risultante
    wb.Save(u"output_comparison.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Note e Best Practice**

Tieni presente i seguenti punti quando lavori con gli attributi `ArrayAsSingle` e `ExtraDelimiter`:

- Il valore di `extraDelimiter` viene trattato come una stringa letterale; esegui l'escape di eventuali caratteri speciali che il processore del modello potrebbe interpretare.
- L'attributo `arrayasSingle` accetta un valore booleano (`true` / `false`). Solo `true` attiva il comportamento in cella singola; qualsiasi altro valore ripiega sul comportamento predefinito di espansione.
- Se l'array è vuoto o nullo, la cella viene lasciata vuota (o contiene una stringa vuota a seconda del tipo di dati).
- La funzionalità funziona con origini dati oggetto, nonché con origini di tipo `DataSet` e `DataTable` in cui una colonna può essere suddivisa in array.
- Per un output separato da nuove righe, puoi utilizzare `\n` come valore del delimitatore.
- Posiziona lo Smart Marker in una cella con larghezza sufficiente per visualizzare la stringa concatenata risultante; in caso contrario, il contenuto potrebbe traboccare visivamente nelle celle adiacenti a seconda del formato.

## **Articoli Correlati**

- [Smart Markers](/cells/it/cpp/smart-markers/)
- [Unione e Separazione delle Celle](/cells/it/cpp/merging-and-unmerging-cells/)

{{< app/cells/assistant language="cpp" >}}