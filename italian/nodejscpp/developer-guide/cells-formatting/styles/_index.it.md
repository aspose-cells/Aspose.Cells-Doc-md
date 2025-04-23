---
title: Ottenere e impostare lo stile per le celle
description: Scopri come eseguire il formato e lo styling dei dati in Aspose.Cells for Node.js via C++, inclusi il formato del testo, il formato numerico, il formato della data e altre opzioni di stile. La nostra guida ti aiuterà a creare fogli di calcolo dall aspetto professionale con formattazioni attraenti.
keywords: Aspose.Cells for Node.js via C++, formattazione dei dati, stile, formattazione del testo, formattazione numerica, formattazione delle date, opzioni di stile, fogli di calcolo, formattazione attraente, aspetto professionale.
linktitle: Stili
type: docs
weight: 50
url: /it/nodejs-cpp/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells for Node.js via C++ ha introdotto due nuovi metodi per la formattazione delle celle: Cell.getStyle e Cell.setStyle. Questo articolo analizza l'approccio Cell.getStyle/setStyle per aiutarti a giudicare quale tecnica si adatta meglio alle tue esigenze.

{{% /alert %}} 
## **Formattazione celle**
Ci sono due modi per formattare una cella, illustrati di seguito.
### **Utilizzo di getStyle()**
Con il seguente esempio di codice, viene inizializzato un oggetto Style per ogni cella durante la formattazione. Se molte celle vengono formattate, si consuma molta memoria perché l'oggetto Style è grande. Questi oggetti Style non verranno liberati fino a quando il metodo Workbook.save non viene chiamato.

**JavaScript**

{{< highlight javascript >}}
cell.getStyle().getFont().setIsBold(true);
{{< /highlight >}}
### **Utilizzo di setStyle()**
Il primo approccio è semplice e diretto, quindi perché abbiamo aggiunto il secondo approccio?

Abbiamo aggiunto il secondo metodo per ottimizzare l'uso della memoria. Dopo aver utilizzato il metodo Cell.getStyle per recuperare un oggetto Style, modificalo e usalo con il metodo Cell.setStyle per impostarlo di nuovo sulla cella. Questo oggetto Style non verrà preservato e il garbage collector di JavaScript lo raccoglierà quando non sarà più referenziato.

Quando si chiama il metodo Cell.setStyle, l'oggetto Style non viene salvato per ogni cella. Invece, confrontiamo questo oggetto Style con un pool interno di oggetti Style per vedere se può essere riutilizzato. Solo gli oggetti Style che differiscono da quelli esistenti vengono mantenuti per ogni oggetto Workbook. Questo significa che ci sono solo alcune centinaia di oggetti Style per ogni file Excel anziché migliaia. Per ogni cella, viene conservato solo un indice nel pool di oggetti Style.

**JavaScript**

{{< highlight javascript >}}
let style = cell.getStyle();

style.getFont().setIsBold(true);

cell.setStyle(style);
{{< /highlight >}}

## **Argomenti avanzati**
- [Crea un oggetto Style utilizzando la classe CellsFactory](/cells/it/nodejs-cpp/create-style-object-using-cellsfactory-class/)
- [Modifica un Style esistente](/cells/it/nodejs-cpp/modify-an-existing-style/)
- [Riutilizzo degli oggetti Style](/cells/it/nodejs-cpp/reusing-style-objects/)
- [Utilizzo degli stili incorporati](/cells/it/nodejs-cpp/using-built-in-styles/)

