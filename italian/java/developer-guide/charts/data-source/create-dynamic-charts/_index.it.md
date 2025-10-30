---
title: Creazione di grafici dinamici
type: docs
weight: 200
url: /it/java/create-dynamic-charts/
---

{{% alert color="primary" %}}

I grafici dinamici (o interattivi) hanno la capacità di cambiare quando si cambia l'ambito dei dati. In altre parole, i grafici dinamici possono riflettere automaticamente i cambiamenti quando viene modificata la fonte di dati. Per innescare il cambiamento della fonte di dati, è possibile utilizzare l'opzione di filtraggio delle tabelle di Excel o utilizzare un controllo come ComboBox o elenco a discesa.

Questo articolo dimostra l'uso delle API Aspose.Cells for Java per creare grafici dinamici utilizzando entrambi gli approcci sopra menzionati.

{{% /alert %}}

## **Utilizzo delle tabelle di Excel**

{{% alert color="primary" %}}

Le tabelle di Excel sono chiamate ListObjects nella prospettiva di Aspose.Cells, quindi useremo il termine "ListObject" invece di "Tabella" per chiarezza. Si prega di leggere attentamente come [creare ListObjects](/cells/it/java/creating-a-list-object/) con l'API Aspose.Cells for Java.

{{% /alert %}}

I ListObjects forniscono la funzionalità integrata per ordinare e filtrare i dati tramite l'interazione dell'utente. Entrambe le opzioni di ordinamento e filtraggio sono fornite tramite gli elenchi a discesa che vengono aggiunti automaticamente alla riga dell'intestazione del ListObject. Grazie a queste funzionalità (ordinamento e filtraggio), il ListObject sembra essere il candidato perfetto per servire come fonte di dati per un grafico dinamico perché quando viene modificato l'ordinamento o il filtraggio, la rappresentazione dei dati nel grafico verrà cambiata per riflettere lo stato attuale del ListObject.

Al fine di mantenere la dimostrazione semplice da comprendere, creeremo il Workbook da zero e procederemo passo dopo passo come indicato di seguito.

1. Creare un documento di lavoro vuoto.
1. Accedere alle celle del primo foglio di lavoro nel documento di lavoro.
1. Inserire alcuni dati nelle celle.
1. Creare ListObject basato sui dati inseriti.
1. Creare un grafico basato sull'intervallo di dati di ListObject.
1. Salvare il risultato su disco.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingExcelTables-UsingExcelTables.java" >}}

## **Utilizzo di Formule Dinamiche**

Nel caso in cui non si desideri utilizzare i ListObjects come origine dei dati per il grafico dinamico, l'altra opzione è utilizzare le funzioni Excel (o formule) per creare un intervallo dinamico di dati e un controllo (come ComboBox) per attivare la modifica dei dati. In questo scenario, useremo la funzione VLOOKUP per recuperare i valori appropriati in base alla selezione di ComboBox. Quando la selezione viene modificata, la funzione VLOOKUP aggiornerà il valore della cella. Se un intervallo di celle sta utilizzando la funzione VLOOKUP, l'intero intervallo può essere aggiornato tramite interazione dell'utente, quindi può essere utilizzato come origine per il grafico dinamico.

Al fine di mantenere la dimostrazione semplice da comprendere, creeremo il Workbook da zero e procederemo passo dopo passo come indicato di seguito.

1. Creare un documento di lavoro vuoto.
1. Accedere alle celle del primo foglio di lavoro nel documento di lavoro.
1. Inserire alcuni dati nelle celle creando un Named Range. Questi dati serviranno come serie per il grafico dinamico.
1. Creare ComboBox basato sul Named Range creato nel passo precedente.
1. Inserire ulteriori dati nelle celle che serviranno come origine per la funzione VLOOKUP.
1. Inserire la funzione VLOOKUP (con i parametri appropriati) in un intervallo di celle. Questo intervallo servirà come origine per il grafico dinamico.
1. Creare un grafico basato sull'intervallo creato nel passo precedente.
1. Salvare il risultato su disco.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDynamicFormulas-UsingDynamicFormulas.java" >}}
{{< app/cells/assistant language="java" >}}
