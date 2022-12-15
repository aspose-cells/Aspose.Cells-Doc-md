---
title: Modifica uno stile esistente
type: docs
weight: 50
url: /it/java/modify-an-existing-style/
description: Scopri come modificare gli stili in Excel con Microsoft Excel e con l'API Aspose.Cells for Java.
keywords: modify an existing style excel, modify an existing style excel java, modify existing style excel, modify existing style excel java, change existing style in excel, change existing style in excel java, how to change style in excel, how to change style in excel with java, how to change style in excel with java, how to change style in excel using java, changing existing style in excel java, changing existing style in excel
---
{{% alert color="primary" %}}

Per applicare le stesse opzioni di formattazione alle celle, crea un nuovo oggetto stile di formattazione. Un oggetto stile di formattazione è una combinazione di caratteristiche di formattazione, come carattere, dimensione del carattere, rientro, numero, bordo, motivi e così via, denominate e memorizzate come set. Quando applicato, viene applicata tutta la formattazione in quello stile.

Puoi anche utilizzare uno stile esistente, salvarlo con la cartella di lavoro e utilizzarlo per formattare le informazioni con gli stessi attributi.

 Quando le celle non sono formattate in modo esplicito, il**Normale** style (lo stile predefinito della cartella di lavoro). Microsoft Excel predefinisce diversi stili oltre allo stile Normale, inclusi Virgola, Valuta e Percentuale.

Aspose.Cells consente di modificare uno qualsiasi di questi stili o qualsiasi altro stile definito con gli attributi desiderati.

{{% /alert %}}

## **Utilizzo di Microsoft Excel**

Per aggiornare uno stile in Microsoft Excel 97-2003:

1.  Sul**Formato** menu, fare clic**Stile**.
1.  Selezionare lo stile che si desidera modificare da**Nome dello stile** elenco.
1.  Clic**Modificare**.
1. Selezionare le opzioni di stile desiderate utilizzando le schede nella finestra di dialogo Formato Cells.
1.  Clic**OK**.
1.  Sotto**Lo stile include**, specificare le caratteristiche di stile desiderate.
1.  Clic**OK** per salvare lo stile e applicarlo all'intervallo selezionato.

## **Utilizzando Aspose.Cells**

 Aspose.Cells fornisce il[**Stile.aggiornamento**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update()) metodo per aggiornare uno stile esistente.

 Per modificare uno stile con nome, creato dinamicamente utilizzando Aspose.Cells o predefinito, chiama il file[**Stile.aggiornamento**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update()) per riflettere eventuali modifiche di stile applicate a una cella o a un intervallo.

 Il[**Stile.aggiornamento**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update() ) si comporta come il metodo**OK** pulsante nella finestra di dialogo Stile: dopo aver apportato modifiche a uno stile esistente, chiama per implementare la modifica. Se hai già applicato uno stile a un intervallo di celle, modifica gli attributi di stile e chiama il metodo, la formattazione di quelle celle viene aggiornata automaticamente

### **Creazione e modifica di uno stile**

Questo esempio crea un oggetto stile, lo applica a un intervallo di celle e modifica l'oggetto stile. Le modifiche vengono applicate automaticamente alla cella e all'intervallo a cui è stato applicato lo stile.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatingStyle-CreatingStyle.java" >}}

### **Modifica di uno stile esistente**

Questo esempio utilizza un semplice file Excel modello in cui uno stile denominato Percentuale è già stato applicato a un intervallo. L'esempio:

1. ottiene lo stile,
1. crea un oggetto di stile e
1. modifica la formattazione dello stile.

Le modifiche vengono applicate automaticamente all'intervallo a cui è stato applicato lo stile.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyExistingStyle-ModifyExistingStyle.java" >}}
