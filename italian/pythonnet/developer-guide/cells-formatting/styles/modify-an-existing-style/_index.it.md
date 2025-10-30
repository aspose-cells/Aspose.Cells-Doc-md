---
title: Modificare uno stile esistente
description: Aspose.Cells è una libreria Python per lavorare con file di fogli di calcolo che permette agli utenti di modificare gli stili delle celle esistenti. Questo articolo introdurrà come modificare uno stile di cella esistente con l API Aspose.Cells per Python via .NET, in modo che gli utenti possano cambiare l aspetto delle celle secondo le proprie esigenze.
keywords: Modificare stili esistenti, personalizzare l aspetto e la sensazione della tua applicazione, guide, tutorial, documentazione di aiuto, documentazione di sviluppo, riferimenti API, codice di esempio, download, supporto.
type: docs
weight: 90
url: /it/python-net/modify-an-existing-style/
---

{{% alert color="primary" %}}

Per applicare le stesse opzioni di formattazione alle celle, creare un nuovo oggetto di stile di formattazione. Un oggetto di stile di formattazione è una combinazione di caratteristiche di formattazione, come font, dimensione del font, rientro, numero, bordo, pattern, ecc., denominati e memorizzati come un insieme. Quando applicato, tutte le formattazioni in quel formato vengono applicate.

È anche possibile utilizzare uno stile esistente, salvarlo con il foglio di lavoro e utilizzarlo per formattare le informazioni con gli stessi attributi.

Quando le celle non sono esplicitamente formattate, viene applicato lo stile **Normale** (lo stile predefinito del foglio di lavoro). Microsoft Excel predefinisce diversi stili oltre allo stile Normale, tra cui Virgola, Valuta e Percentuale.

Aspose.Cells per Python via .NET consente di modificare uno qualsiasi di questi stili o altri stili definiti con i propri attributi desiderati.

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

## **Usando Aspose.Cells per Python via .NET**

Gli esempi seguenti mostrano come utilizzare il metodo [**Style.update**](https://reference.aspose.com/cells/python-net/aspose.cells/style/update).

### **Creazione e modifica di uno stile**

Questo esempio crea un oggetto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style), lo applica a un intervallo di celle e ne modifica l'oggetto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style). Le modifiche vengono applicate automaticamente alla cella e all'intervallo a cui è stato applicato lo stile.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ModifyThroughStyleObject-1.py" >}}

### **Modifica di uno stile esistente**

Questo esempio utilizza un semplice file di modello Excel in cui è già stato applicato uno stile chiamato Percentuale a un intervallo. L'esempio:

1. ottiene lo stile,
1. crea un oggetto stile e
1. modifica la formattazione dello stile.

Le modifiche vengono applicate automaticamente all'intervallo a cui è stato applicato lo stile.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ModifyThroughSampleExcelFile-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
