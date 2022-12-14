---
title: Esegui la funzione lato client al cambio di pagina GridWeb
type: docs
weight: 140
url: /it/net/execute-client-side-function-on-gridweb-page-change/
---
## **Possibili scenari di utilizzo**
A volte è necessario eseguire la funzione lato client quando la pagina GridWeb cambia. Aspose.Cells.GridWeb fornisce la proprietà OnPageChangeClientFunction per questo scopo. Impostare questa proprietà con la funzione lato client che si desidera eseguire.
## **Esegui la funzione lato client al cambio di pagina GridWeb**
Il seguente markup aspx spiega come utilizzare la proprietà OnPageChangeClientFunction. Imposta la proprietà con la funzione lato client denominata MyOnPageChange. Si noti che questa proprietà è valida solo se è stato abilitato il paging, ad esempio EnablePaging="true". Ora, ogni volta che cambierai la pagina GridWeb, chiamerà la funzione lato client MyOnPageChange che stampa il file**indice della pagina corrente** sul**consolare** come mostrato in questo screenshot.

![cose da fare:immagine_alt_testo](execute-client-side-function-on-gridweb-page-change_1.png)
## **Codice di esempio**
Questo è il codice della funzione lato client MyOnPageChange che verrà eseguita a causa dell'impostazione della proprietà OnPageChangeClientFunction ="MyOnPageChange" in GridWeb. Questo è il markup completo della pagina aspx.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples.GridWeb-CSharp-GridWebBasics-CallClientsideScriptforGridWeb.aspx-CallClientsideScriptforGridWeb.cs" >}}
