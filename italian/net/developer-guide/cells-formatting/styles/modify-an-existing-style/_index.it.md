---
title: Modificare uno stile esistente
description: Aspose.Cells è una libreria .NET per lavorare con file di fogli elettronici che consente agli utenti di modificare gli stili delle celle esistenti. Questo articolo presenterà come modificare uno stile di cella esistente con la libreria Aspose.Cells in modo che gli utenti possano cambiare l aspetto delle celle secondo necessità.
keywords: Modificare stili esistenti, personalizzare l aspetto e la sensazione della tua applicazione, guide, tutorial, documentazione di aiuto, documentazione di sviluppo, riferimenti API, codice di esempio, download, supporto.
type: docs
weight: 90
url: /it/net/modify-an-existing-style/
---

{{% alert color="primary" %}}

Per applicare le stesse opzioni di formattazione alle celle, creare un nuovo oggetto di stile di formattazione. Un oggetto di stile di formattazione è una combinazione di caratteristiche di formattazione, come font, dimensione del font, rientro, numero, bordo, pattern, ecc., denominati e memorizzati come un insieme. Quando applicato, tutte le formattazioni in quel formato vengono applicate.

È anche possibile utilizzare uno stile esistente, salvarlo con il foglio di lavoro e utilizzarlo per formattare le informazioni con gli stessi attributi.

Quando le celle non sono esplicitamente formattate, viene applicato lo stile **Normale** (lo stile predefinito del foglio di lavoro). Microsoft Excel predefinisce diversi stili oltre allo stile Normale, tra cui Virgola, Valuta e Percentuale.

Aspose.Cells consente di modificare uno qualsiasi di questi stili o qualsiasi altro stile che si definisce con i propri attributi desiderati.

{{% /alert %}}

## **Utilizzando Microsoft Excel**

Per aggiornare uno stile in Microsoft Excel 97-2003:

1. Nel menu **Formato**, fare clic su **Stile**.
1. Selezionare lo stile che si desidera modificare dall'elenco **Nome stile**.
1. Fare clic su **Modifica**.
1. Selezionare le opzioni di stile desiderate utilizzando le schede nella finestra di dialogo Formato celle.
1. Fai clic su **OK**.
1. In **Lo stile include**, specificare le caratteristiche dello stile desiderate.
1. Fare clic su **OK** per salvare lo stile e applicarlo all'intervallo selezionato.

## **Usare Aspose.Cells**

Gli esempi seguenti mostrano come utilizzare il metodo [**Style.Update**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/update).

### **Creazione e modifica di uno stile**

Questo esempio crea un oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style), lo applica a un intervallo di celle e ne modifica l'oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style). Le modifiche vengono applicate automaticamente alla cella e all'intervallo a cui è stato applicato lo stile.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughStyleObject-1.cs" >}}

### **Modifica di uno stile esistente**

Questo esempio utilizza un semplice file di modello Excel in cui è già stato applicato uno stile chiamato Percentuale a un intervallo. L'esempio:

1. ottiene lo stile,
1. crea un oggetto stile e
1. modifica la formattazione dello stile.

Le modifiche vengono applicate automaticamente all'intervallo a cui è stato applicato lo stile.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughSampleExcelFile-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
