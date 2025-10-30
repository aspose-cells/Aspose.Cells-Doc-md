---
title: Ottenere e impostare lo stile per le celle
description: Scopri come eseguire la formattazione dei dati e lo stile in Aspose.Cells for JavaScript tramite C++, inclusi formattazione del testo, formattazione numerica, formattazione delle date e altre opzioni di stile. La nostra guida ti aiuterà a creare fogli di calcolo dall aspetto professionale con una formattazione attraente.
keywords: Aspose.Cells for JavaScript tramite C++, formattazione dei dati, stile, formattazione del testo, formattazione numerica, formattazione delle date, opzioni di stile, fogli di calcolo, formattazione attraente, dall aspetto professionale.
linktitle: Stili
type: docs
weight: 50
url: /it/javascript-cpp/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells for JavaScript tramite C++ ha introdotto due nuovi metodi per la formattazione delle celle: Cell.style e Cell.style. Questo articolo esamina l'approccio Cell.style/style per aiutarti a giudicare quale tecnica si adatta meglio alle tue esigenze.

{{% /alert %}} 
## **Formattazione celle**
Ci sono due modi per formattare una cella, illustrati di seguito.
### **Utilizzo dello stile**
Con il seguente esempio di codice, viene inizializzato un oggetto Style per ogni cella durante la formattazione. Se molte celle vengono formattate, si consuma molta memoria perché l'oggetto Style è grande. Questi oggetti Style non verranno liberati fino a quando il metodo Workbook.save non viene chiamato.

**JavaScript**

{{< highlight javascript >}}
cell.style.font.isBold = true;
{{< /highlight >}}
### **Utilizzo dello stile**
Il primo approccio è semplice e diretto, quindi perché abbiamo aggiunto il secondo approccio?

Abbiamo aggiunto il secondo metodo per ottimizzare l'uso della memoria. Dopo aver usato la proprietà Cell.style per recuperare un oggetto Style, modificarlo e assegnarlo di nuovo usando la proprietà Cell.style a questa cella. Questo oggetto Style non verrà conservato e il garbage collector di JavaScript lo raccoglierà quando non sarà più referenziato.

Quando si assegna la proprietà Cell.style, l'oggetto Style non viene salvato per ogni cella. Invece, confrontiamo questo oggetto Style con un pool interno di oggetti Style per vedere se può essere riutilizzato. Solo gli oggetti Style che differiscono da quelli esistenti vengono mantenuti per ogni oggetto Workbook. Ciò significa che ci sono solo alcune centinaia di oggetti Style per ogni file Excel anziché migliaia. Per ogni cella, viene mantenuto solo un indice nel pool di oggetti Style.

**JavaScript**

{{< highlight javascript >}}
let style = cell.style;

style.font.isBold = true;

cell.style = style;
{{< /highlight >}}

## **Argomenti avanzati**
- [Crea un oggetto Style utilizzando la classe CellsFactory](/cells/it/javascript-cpp/create-style-object-using-cellsfactory-class/)
- [Modifica un Style esistente](/cells/it/javascript-cpp/modify-an-existing-style/)
- [Riutilizzo degli oggetti Style](/cells/it/javascript-cpp/reusing-style-objects/)
- [Utilizzo degli stili incorporati](/cells/it/javascript-cpp/using-built-in-styles/)
