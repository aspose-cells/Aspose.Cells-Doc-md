---
title: Ottenere e impostare lo stile per le celle
description: Scopri come eseguire la formattazione dei dati e lo stile in Aspose.Cells per Python via .NET, inclusa la formattazione del testo, la formattazione dei numeri, la formattazione delle date e altre opzioni di stile. La nostra guida ti aiuterà a creare fogli di calcolo dall aspetto professionale con una formattazione accattivante.
keywords: Aspose.Cells per Python via .NET, formattazione dei dati, stile, formattazione del testo, formattazione dei numeri, formattazione delle date, opzioni di stile, fogli di calcolo, formattazione attraente, dall aspetto professionale.
linktitle: Stili
type: docs
weight: 50
url: /it/python-net/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells per Python via .NET ha introdotto due nuovi metodi per la formattazione delle celle: Cell.GetStyle e Cell.SetStyle. Questo articolo esamina l'approccio Cell.GetStyle/SetStyle per aiutarti a valutare quale tecnica si adatta meglio alle tue esigenze.

{{% /alert %}} 

## **Formattazione celle**
Ci sono due modi per formattare una cella, illustrati di seguito.

### **Utilizzando GetStyle()**
Con il seguente pezzo di codice, viene inizializzato un oggetto Style per ogni cella durante la formattazione. Se viene formattato un gran numero di celle, viene consumata una grande quantità di memoria perché l'oggetto Style è un oggetto grande. Questi oggetti Style non verranno liberati fino a quando non viene chiamato il metodo Workbook.Save.


**Python**

{{< highlight python >}}

cell.get_style().font.is_bold = True

{{< /highlight >}}

### **Utilizzare SetStyle()**
Il primo approccio è semplice e diretto, quindi perché abbiamo aggiunto il secondo approccio?

Abbiamo aggiunto il secondo approccio per ottimizzare l'uso della memoria. Dopo aver utilizzato il metodo Cell.GetStyle per recuperare un oggetto Style, modificarlo e utilizzare il metodo Cell.SetStyle per impostarlo di nuovo su questa cella. Questo oggetto Style non verrà preservato e sarà raccolto dal .NET GC quando non è referenziato.

Quando si chiama il metodo Cell.SetStyle, l'oggetto Style non viene salvato per ogni cella. Invece, confrontiamo questo oggetto Style con un pool interno di oggetti Style per vedere se può essere riutilizzato. Solo gli oggetti Style che differiscono da quelli esistenti vengono mantenuti per ogni oggetto Workbook. Questo significa che ci sono solo diversi centinaia di oggetti Style per ogni file Excel invece di migliaia. Per ogni cella, viene preservato solo un indice al pool di oggetti Style.



**Python**

{{< highlight python >}}

style = cell.get_style()
style.font.is_bold = True
cell.set_style(style)

{{< /highlight >}}

## **Argomenti avanzati**
- [Crea un oggetto Style utilizzando la classe CellsFactory](/cells/it/python-net/create-style-object-using-cellsfactory-class/)
- [Modifica un Style esistente](/cells/it/python-net/modify-an-existing-style/)
- [Riutilizzo degli oggetti Style](/cells/it/python-net/reusing-style-objects/)
- [Utilizzo degli stili incorporati](/cells/it/python-net/using-built-in-styles/)


