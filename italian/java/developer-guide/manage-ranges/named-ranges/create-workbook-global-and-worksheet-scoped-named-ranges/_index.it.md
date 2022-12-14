---
title: Crea cartella di lavoro (globale) e intervalli denominati con ambito del foglio di lavoro
type: docs
weight: 10
url: /it/java/create-workbook-global-and-worksheet-scoped-named-ranges/
---
{{% alert color="primary" %}}

Microsoft Excel consente agli utenti di definire intervalli denominati con due ambiti diversi: cartella di lavoro (nota anche come ambito globale) e foglio di lavoro.

- È possibile accedere agli intervalli denominati con un ambito di cartella di lavoro da qualsiasi foglio di lavoro all'interno di quella cartella di lavoro semplicemente usando il suo nome.
- È possibile accedere agli intervalli denominati nell'ambito del foglio di lavoro con il riferimento del particolare foglio di lavoro in cui è stato creato.

Aspose.Cells fornisce la stessa funzionalità di Microsoft Excel per l'aggiunta di intervalli denominati con ambito cartella di lavoro e foglio di lavoro. Quando si crea un intervallo denominato con ambito del foglio di lavoro, il riferimento al foglio di lavoro deve essere utilizzato nell'intervallo denominato per specificarlo come intervallo denominato con ambito del foglio di lavoro.

{{% /alert %}}

 Gli esempi di codice seguenti mostrano come creare intervalli di nomi con ambito di cartella di lavoro e foglio di lavoro usando il[**Gamma**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) classe.

## **Aggiunta di un intervallo denominato con ambito della cartella di lavoro**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorkbookScope-AddNamedRangeWithWorkbookScope.java" >}}

## **Aggiunta di un intervallo denominato con ambito del foglio di lavoro**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorksheetScope-AddNamedRangeWithWorkbookScope.java" >}}
