---
title: Crea grafici dinamici
type: docs
weight: 200
url: /it/java/create-dynamic-charts/
---
{{% alert color="primary" %}}

grafici dinamici (o interattivi) possono cambiare quando si modifica l'ambito dei dati. In altre parole, i grafici dinamici possono riflettere automaticamente le modifiche quando l'origine dati viene modificata. Per attivare la modifica dell'origine dati, è possibile utilizzare l'opzione di filtro delle tabelle di Excel o utilizzare un controllo come ComboBox o elenco a discesa.

Questo articolo illustra l'utilizzo delle API Aspose.Cells for Java per creare grafici dinamici utilizzando entrambi gli approcci sopra menzionati.

{{% /alert %}}

## **Utilizzo delle tabelle Excel**

{{% alert color="primary" %}}

 Le tabelle di Excel sono indicate come ListObjects nella prospettiva Aspose.Cells, pertanto per maggiore chiarezza utilizzeremo il termine "ListObject" invece di "Table". Si prega di leggere in dettaglio su come[creare ListObject](/cells/it/java/creating-a-list-object/) con Aspose.Cells for .NET API.

{{% /alert %}}

ListObjects fornisce la funzionalità integrata per ordinare e filtrare i dati in base all'interazione dell'utente. Entrambe le opzioni di ordinamento e filtraggio vengono fornite tramite gli elenchi a discesa che vengono aggiunti automaticamente alla riga di intestazione di ListObject. A causa di queste funzionalità (ordinamento e filtraggio), ListObject sembra essere il candidato perfetto per fungere da origine dati per un grafico dinamico perché quando l'ordinamento o il filtro viene modificato, la rappresentazione dei dati nel grafico verrà modificata per riflettere l'attuale stato del ListObject.

Per mantenere la dimostrazione semplice da capire, creeremo la cartella di lavoro da zero e procederemo passo dopo passo come descritto di seguito.

1. Crea una cartella di lavoro vuota.
1. Accedi allo Cells del primo foglio di lavoro nella cartella di lavoro.
1. Inserisci alcuni dati nelle celle.
1. Crea ListObject in base ai dati inseriti.
1. Crea un grafico basato sull'intervallo di dati di ListObject.
1. Salva risultato su disco.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingExcelTables-UsingExcelTables.java" >}}

## **Utilizzo di formule dinamiche**

Nel caso in cui non desideri utilizzare ListObjects come origine dati per il grafico dinamico, l'altra opzione è utilizzare le funzioni (o le formule) di Excel per creare un intervallo dinamico di dati e un controllo (come ComboBox) per attivare la modifica nei dati. In questo scenario, utilizzeremo la funzione CERCA.VERT per recuperare i valori appropriati in base alla selezione di ComboBox. Quando la selezione viene modificata, la funzione CERCA.VERT aggiornerà il valore della cella. Se un intervallo di celle utilizza la funzione VLOOKUP, l'intero intervallo può essere aggiornato all'interazione dell'utente, quindi può essere utilizzato come origine per il grafico dinamico.

Per mantenere la dimostrazione semplice da capire, creeremo la cartella di lavoro da zero e procederemo passo dopo passo come descritto di seguito.

1. Crea una cartella di lavoro vuota.
1. Accedi allo Cells del primo foglio di lavoro nella cartella di lavoro.
1. Inserisci alcuni dati nelle celle creando un intervallo denominato. Questi dati serviranno come serie per il grafico dinamico.
1. Crea ComboBox in base all'intervallo denominato creato nel passaggio precedente.
1. Inserisci altri dati nelle celle che fungeranno da origine per la funzione CERCA.VERT.
1. Inserisci la funzione CERCA.VERT (con i parametri appropriati) in un intervallo di celle. Questo intervallo servirà come fonte per il grafico dinamico.
1. Crea grafico basato sull'intervallo creato nel passaggio precedente.
1. Salva risultato su disco.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDynamicFormulas-UsingDynamicFormulas.java" >}}
