---
title: Ottieni e imposta lo stile delle celle con C++
linktitle: Stili
type: docs
weight: 50
url: /it/cpp/styling-and-data-formatting/
description: Scopri come eseguire la formattazione e lo stile dei dati in Aspose.Cells for C++, inclusa la formattazione del testo, la formattazione dei numeri, la formattazione delle date e altre opzioni di stile. La nostra guida ti aiuterà a creare fogli di calcolo dall aspetto professionale con una formattazione attraente.
keywords: Aspose.Cells for C++, formattazione dei dati, styling, formattazione del testo, formattazione dei numeri, formattazione delle date, opzioni di styling, fogli di calcolo, formattazione attraente, dall aspetto professionale.
---

{{% alert color="primary" %}}

Aspose.Cells for C++ ha introdotto due nuovi metodi per formattare le celle: `Cell.GetStyle` e `Cell.SetStyle`. Questo articolo esamina l’approccio `Cell.GetStyle`/`SetStyle` per aiutarti a giudicare quale tecnica si adatta meglio a te.

{{% /alert %}}

## **Formattazione celle**
Ci sono due modi per formattare una cella, illustrati di seguito.

### **Utilizzando GetStyle()**
Con il seguente pezzo di codice, viene inizializzato un oggetto `Style` per ogni cella durante la formattazione. Se molte celle vengono formattate, viene consumata una grande quantità di memoria perché l’oggetto `Style` è grande. Questi oggetti `Style` non verranno liberati fino a quando il metodo `Workbook.Save` non viene chiamato.

**C++**

```cpp
cell.GetStyle()->GetFont()->SetIsBold(true);
```

### **Utilizzare SetStyle()**
Il primo approccio è semplice e diretto, allora perché abbiamo aggiunto il secondo approccio?

Abbiamo aggiunto il secondo approccio per ottimizzare l’uso della memoria. Dopo aver utilizzato il metodo `Cell.GetStyle` per recuperare un oggetto `Style`, modificalo e usalo di nuovo con il metodo `Cell.SetStyle`. Questo oggetto `Style` non verrà conservato, e il runtime C++ lo raccoglierà quando non sarà più referenziato.

Quando si chiama il metodo `Cell.SetStyle`, l’oggetto `Style` non viene salvato per ogni cella. Invece, confrontiamo questo oggetto `Style` con un pool interno di oggetti `Style` per vedere se può essere riutilizzato. Solo gli oggetti `Style` che differiscono da quelli esistenti vengono mantenuti per ogni oggetto `Workbook`. Ciò significa che ci sono solo alcune centinaia di oggetti `Style` per ogni file Excel invece di migliaia. Per ogni cella, viene conservato solo un indice al pool di oggetti `Style`.

**C++**

```cpp
auto style = cell.GetStyle();
style->GetFont()->SetIsBold(true);
cell.SetStyle(style);
```

## **Argomenti avanzati**
- [Crea un oggetto Style utilizzando la classe CellsFactory](/cells/it/cpp/create-style-object-using-cellsfactory-class/)
- [Modifica un Style esistente](/cells/it/cpp/modify-an-existing-style/)
- [Riutilizzo degli oggetti Style](/cells/it/cpp/reusing-style-objects/)
- [Utilizzo degli stili incorporati](/cells/it/cpp/using-built-in-styles/)
