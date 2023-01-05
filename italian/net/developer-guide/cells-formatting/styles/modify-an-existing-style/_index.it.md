---
title: Modifica uno stile esistente
type: docs
weight: 90
url: /it/net/modify-an-existing-style/
---
{{% alert color="primary" %}}

Per applicare le stesse opzioni di formattazione alle celle, crea un nuovo oggetto stile di formattazione. Un oggetto stile di formattazione è una combinazione di caratteristiche di formattazione, come carattere, dimensione del carattere, indentazione, numero, bordo, motivi ecc., denominate e memorizzate come set. Quando applicato, viene applicata tutta la formattazione in quello stile.

Puoi anche utilizzare uno stile esistente, salvarlo con la cartella di lavoro e utilizzarlo per formattare le informazioni con gli stessi attributi.

 Quando le celle non sono formattate in modo esplicito, il**Normale** style (lo stile predefinito della cartella di lavoro). Microsoft Excel predefinisce diversi stili oltre allo stile Normale, tra cui Virgola, Valuta e Percentuale.

Aspose.Cells consente di modificare uno qualsiasi di questi stili o qualsiasi altro stile definito con gli attributi desiderati.

{{% /alert %}}

## **Utilizzando Microsoft Excel**

Per aggiornare uno stile in Microsoft Excel 97-2003:

1.  Sul**Formato** menu, fare clic**Stile**.
1.  Selezionare lo stile che si desidera modificare da**Nome dello stile** elenco.
1.  Clic**Modificare**.
1. Selezionare le opzioni di stile desiderate utilizzando le schede nella finestra di dialogo Formato Cells.
1.  Clic**OK**.
1.  Sotto**Lo stile include**, specificare le caratteristiche di stile desiderate.
1.  Clic**OK** per salvare lo stile e applicarlo all'intervallo selezionato.

## **Utilizzando Aspose.Cells**

 Gli esempi seguenti mostrano come utilizzare[**Stile.Aggiornamento**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/update)metodo.

### **Creazione e modifica di uno stile**

 Questo esempio crea a[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) oggetto, lo applica a un intervallo di celle e modifica il file[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style)oggetto. Le modifiche vengono applicate automaticamente alla cella e all'intervallo a cui è stato applicato lo stile.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughStyleObject-1.cs" >}}

### **Modifica di uno stile esistente**

Questo esempio utilizza un semplice file Excel modello in cui uno stile denominato Percentuale è già stato applicato a un intervallo. L'esempio:

1. ottiene lo stile,
1. crea un oggetto di stile e
1. modifica la formattazione dello stile.

Le modifiche vengono applicate automaticamente all'intervallo a cui è stato applicato lo stile.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughSampleExcelFile-1.cs" >}}
