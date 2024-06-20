---
title: Creare Workbook (Global) e Worksheet Scoped Named Ranges
type: docs
weight: 10
url: /it/java/create-workbook-global-and-worksheet-scoped-named-ranges/
---

{{% alert color="primary" %}}

Microsoft Excel consente agli utenti di definire intervalli nominati con due ambiti diversi: cartella di lavoro (noto anche come ambito globale) e foglio di lavoro.

- I nomi definiti con un ambito a livello di cartella di lavoro possono essere accessibili da qualsiasi foglio di calcolo all'interno di quella cartella di lavoro semplicemente usando il suo nome.
- I nomi definiti con ambito a livello di foglio di lavoro sono accessibili con il riferimento al foglio di lavoro particolare in cui sono stati creati.

Aspose.Cells fornisce la stessa funzionalità di Microsoft Excel per l'aggiunta di intervalli con nome a livello di cartella di lavoro e di foglio di lavoro. Quando si crea un intervallo con nome a livello di foglio di lavoro, deve essere utilizzato il riferimento del foglio di lavoro nell'intervallo con nome per specificarlo come intervallo con nome a livello di foglio di lavoro.

{{% /alert %}}

I seguenti esempi di codice mostrano come creare intervalli di nomi con ambito di lavoro e di foglio di lavoro utilizzando la classe [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range).

## **Aggiunta di un intervallo denominato con ambito di lavoro**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorkbookScope-AddNamedRangeWithWorkbookScope.java" >}}

## **Aggiunta di un intervallo con nome a livello di foglio di lavoro**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorksheetScope-AddNamedRangeWithWorkbookScope.java" >}}
