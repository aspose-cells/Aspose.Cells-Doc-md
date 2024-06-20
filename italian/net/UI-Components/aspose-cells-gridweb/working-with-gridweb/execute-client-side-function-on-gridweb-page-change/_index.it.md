---
title: Eseguire la funzione lato client al cambiamento della pagina di GridWeb
type: docs
weight: 140
url: /it/net/aspose-cells-gridweb/execute-client-side-function-on-gridweb-page-change/
keywords: GridWeb,client,js,javascript,function
description: Questo articolo introduce come lavorare con la funzione client js in GridWeb.
---

## **Possibili Scenari di Utilizzo**
A volte è necessario eseguire la funzione lato client quando cambia la pagina di GridWeb. Aspose.Cells.GridWeb fornisce la proprietà OnPageChangeClientFunction a tale scopo. Si prega di impostare questa proprietà con la funzione lato client che si desidera eseguire.
## **Eseguire la funzione lato client al cambiamento della pagina di GridWeb**
Il markup aspx seguente spiega come utilizzare la proprietà OnPageChangeClientFunction. Imposta la proprietà con la funzione lato client chiamata MyOnPageChange. Si noti che questa proprietà è valida solo se si è abilitata la paginazione cioè EnablePaging="true". Ora, ogni volta che si cambierà la pagina di GridWeb, chiamerà la funzione lato client MyOnPageChange che stamperà il **indice della pagina corrente** sulla **console** come mostrato in questa schermata.

![todo:image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
## **Codice di Esempio**
Questo è il codice della funzione lato client MyOnPageChange che verrà eseguita a causa dell'impostazione della proprietà OnPageChangeClientFunction="MyOnPageChange" in GridWeb. Questo è il markup completo della pagina aspx.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples.GridWeb-CSharp-GridWebBasics-CallClientsideScriptforGridWeb.aspx-CallClientsideScriptforGridWeb.cs" >}}
