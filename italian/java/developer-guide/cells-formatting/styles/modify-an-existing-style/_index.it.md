---
title: Modificare uno stile esistente
type: docs
weight: 50
url: /it/java/modify-an-existing-style/
description: Scopri come cambiare gli stili in Excel con Microsoft Excel e con l API Aspose.Cells for Java.
keywords: modificare un foglio stile esistente excel, modificare un foglio stile esistente excel java, modificare foglio stile esistente excel, modificare foglio stile esistente excel java, modificare foglio stile esistente in excel, modificare foglio stile esistente in excel java, come cambiare lo stile in excel, come cambiare lo stile in excel con java, come cambiare lo stile in excel con java, come cambiare lo stile in excel usando java, cambiare stile esistente in excel java, cambiare stile esistente in excel
---

{{% alert color="primary" %}}

Per applicare le stesse opzioni di formattazione alle celle, creare un nuovo oggetto stile di formattazione. Un oggetto stile di formattazione è una combinazione di caratteristiche di formattazione, come carattere, dimensione carattere, rientro, numero, bordo, modelli, ecc., denominati e memorizzati come insieme. Quando applicati, tutte le formattazioni in tale stile vengono applicate.

Puoi anche utilizzare uno stile esistente, salvarlo con il foglio di lavoro e usarlo per formattare le informazioni con le stesse attribuzioni.

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

Aspose.Cells fornisce il metodo [**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update--) per aggiornare uno stile esistente.

Per cambiare uno stile nominato, creato dinamicamente utilizzando Aspose.Cells o predefinito, chiamare il metodo [**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update--) per riflettere eventuali modifiche nello stile applicato a una cella o a un intervallo.

Il metodo [**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update--) si comporta come il pulsante **OK** nella finestra di dialogo Stile: dopo aver apportato modifiche a uno stile esistente, chiamare per implementare il cambiamento. Se hai già applicato uno stile a un intervallo di celle, modifica gli attributi dello stile e chiama il metodo, la formattazione di quelle celle viene aggiornata automaticamente

### **Creazione e modifica di uno stile**

Questo esempio crea un oggetto stile, lo applica a un intervallo di celle e modifica l'oggetto stile. Le modifiche vengono applicate automaticamente alla cella e all'intervallo a cui è stato applicato lo stile.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatingStyle-CreatingStyle.java" >}}

### **Modifica di uno stile esistente**

Questo esempio utilizza un semplice file di modello Excel in cui è già stato applicato uno stile chiamato Percentuale a un intervallo. L'esempio:

1. ottiene lo stile,
1. crea un oggetto stile e
1. modifica la formattazione dello stile.

Le modifiche vengono applicate automaticamente all'intervallo a cui è stato applicato lo stile.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyExistingStyle-ModifyExistingStyle.java" >}}
