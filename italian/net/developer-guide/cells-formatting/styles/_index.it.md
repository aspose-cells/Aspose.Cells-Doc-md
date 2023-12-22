---
title: Ottieni e imposta lo stile per le celle
description: Scopri come eseguire la formattazione e lo stile dei dati in Aspose.Cells for .NET, inclusa la formattazione del testo, la formattazione dei numeri, la formattazione della data e altre opzioni di stile. La nostra guida ti aiuterà a creare fogli di calcolo dall'aspetto professionale con una formattazione accattivante.
keywords: Aspose.Cells for .NET, data formatting, styling, text formatting, number formatting, date formatting, styling options, spreadsheets, attractive formatting, professional-looking.
linktitle: Stili
type: docs
weight: 50
url: /it/net/styling-and-data-formatting/
---
{{% alert color="primary" %}} 

Aspose.Cells for .NET 4.4.2 ha introdotto due nuovi metodi per la formattazione delle celle: Cell.GetStyle e Cell.SetStyle. Questo articolo esamina l'approccio Cell.GetStyle/SetStyle per aiutarti a giudicare quale tecnica è più adatta a te.

{{% /alert %}} 
##  **Formattazione Cells**
Esistono due modi per formattare una cella, illustrati di seguito.
###  **Utilizzando GetStyle()**
Con la seguente parte di codice, viene avviato un oggetto Style per ogni cella durante la formattazione. Se vengono formattate molte celle, viene consumata una grande quantità di memoria perché l'oggetto Style è un oggetto di grandi dimensioni. Questi oggetti Style non verranno liberati finché non verrà chiamato il metodo Workbook.Save.



**C#**

{{< highlight "csharp" >}}

cell.GetStyle().Font.IsBold = true;



{{< /highlight >}}
###  **Utilizzando SetStyle()**
Il primo approccio è semplice e diretto, quindi perché abbiamo aggiunto il secondo approccio?

Abbiamo aggiunto il secondo approccio per ottimizzare l'utilizzo della memoria. Dopo aver utilizzato il metodo Cell.GetStyle per recuperare un oggetto Style, modificarlo e utilizzare il metodo Cell.SetStyle per reimpostarlo su questa cella. Questo oggetto Style non verrà conservato e .NET GC lo raccoglierà quando non viene fatto riferimento.

Quando si chiama il metodo Cell.SetStyle, l'oggetto Style non viene salvato per ogni cella. Confrontiamo invece questo oggetto Style con un pool di oggetti Style interno per vedere se può essere riutilizzato. Per ciascun oggetto Cartella di lavoro vengono mantenuti solo gli oggetti Stile che differiscono da quelli esistenti. Ciò significa che ci sono solo diverse centinaia di oggetti Stile per ciascun file Excel invece di migliaia. Per ogni cella viene conservato solo un indice del pool di oggetti Stile.



**C#**

{{< highlight "csharp" >}}

Style style = cell.GetStyle();

style.Font.IsBold = true;

cell.SetStyle(style);
{{< /highlight >}}

##  **Argomenti avanzati**
- [Crea un oggetto Style utilizzando la classe CellsFactory](/cells/it/net/create-style-object-using-cellsfactory-class/)
- [Modifica uno stile esistente](/cells/it/net/modify-an-existing-style/)
- [Riutilizzo degli oggetti di stile](/cells/it/net/reusing-style-objects/)
- [Utilizzo degli stili incorporati](/cells/it/net/using-built-in-styles/)


