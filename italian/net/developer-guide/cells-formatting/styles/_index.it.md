---
title: Ottieni e imposta stile per le celle
linktitle: Stili
type: docs
weight: 50
url: /it/net/styling-and-data-formatting/
---
{{% alert color="primary" %}} 

Aspose.Cells for .NET 4.4.2 ha introdotto due nuovi metodi per la formattazione delle celle: Cell.GetStyle e Cell.SetStyle. Questo articolo esamina l'approccio Cell.GetStyle/SetStyle per aiutarti a giudicare la tecnica più adatta a te.

{{% /alert %}} 
## **Formattazione Cells**
Esistono due modi per formattare una cella, illustrati di seguito.
### **Utilizzo di GetStyle()**
Con il seguente pezzo di codice, viene avviato un oggetto Style per ogni cella durante la formattazione. Se vengono formattate molte celle, viene consumata una grande quantità di memoria poiché l'oggetto Style è un oggetto di grandi dimensioni. Questi oggetti Style non verranno liberati finché non viene chiamato il metodo Workbook.Save.



**C#**

{{< highlight "csharp" >}}

 cell.GetStyle().Font.IsBold = true;



{{< /highlight >}}
### **Usando SetStyle()**
Il primo approccio è semplice e diretto, quindi perché abbiamo aggiunto il secondo approccio?

Abbiamo aggiunto il secondo approccio per ottimizzare l'utilizzo della memoria. Dopo aver utilizzato il metodo Cell.GetStyle per recuperare un oggetto Style, modificarlo e utilizzare il metodo Cell.SetStyle per reimpostarlo su questa cella. Questo oggetto Style non verrà conservato e .NET GC lo raccoglierà quando non vi si fa riferimento.

Quando si chiama il metodo Cell.SetStyle, l'oggetto Style non viene salvato per ogni cella. Invece, confrontiamo questo oggetto Style con un pool di oggetti Style interno per vedere se può essere riutilizzato. Per ogni oggetto Workbook vengono mantenuti solo gli oggetti Style diversi da quelli esistenti. Ciò significa che ci sono solo diverse centinaia di oggetti Style per ogni file Excel invece di migliaia. Per ogni cella viene conservato solo un indice del pool di oggetti Style.



**C#**

{{< highlight "csharp" >}}

 Style style = cell.GetStyle();

style.Font.IsBold = vero;

cell.SetStyle(stile);


## **Argomenti avanzati**
- [Crea un oggetto Style usando la classe CellsFactory](/cells/it/net/create-style-object-using-cellsfactory-class/)
- [Modifica uno stile esistente](/cells/it/net/modify-an-existing-style/)
- [Riutilizzo degli oggetti di stile](/cells/it/net/reusing-style-objects/)
- [Utilizzo degli stili incorporati](/cells/it/net/using-built-in-styles/)


