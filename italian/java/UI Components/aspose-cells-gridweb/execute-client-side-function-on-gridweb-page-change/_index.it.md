---
title: Esegui la funzione lato client al cambio di pagina GridWeb
type: docs
weight: 70
url: /it/java/execute-client-side-function-on-gridweb-page-change/
---
## **Possibili scenari di utilizzo**
A volte è necessario eseguire la funzione lato client quando la pagina GridWeb cambia. Aspose.Cells.GridWeb fornisce la proprietà OnPageChangeClientFunction per questo scopo. Impostare questa proprietà con la funzione lato client che si desidera eseguire.
## **Esegui la funzione lato client al cambio di pagina GridWeb**
Il seguente codice java spiega come utilizzare la proprietà GridWebBean.setOnPageChangeClientFunction(). Imposta la proprietà con la funzione lato client denominata MyOnPageChange. Si noti che questa proprietà è valida solo se è stato abilitato il paging, ad esempio GridWebBean.setEnablePaging(true). Ora, ogni volta che cambierai la pagina GridWeb, chiamerà la funzione lato client MyOnPageChange che stampa il file**indice della pagina corrente** sul**consolare** come mostrato in questo screenshot.

![cose da fare:immagine_alt_testo](execute-client-side-function-on-gridweb-page-change_1.png)
## **Codice di esempio**
Questo è il codice della funzione lato client MyOnPageChange che verrà eseguita a causa di questa riga, ad esempio Gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< highlight "java" >}}

 function MyOnPageChange(index) {

	console.log("current page is:" + (index+1));

}

{{< /highlight >}}

Il codice seguente spiega come abilitare il paging e impostare la proprietà OnPageChangeClientFunction.

{{< highlight "java" >}}

 GridWebBean gridweb=BeanManager.getBean(request);

gridweb.setEnablePaging(true);

gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< /highlight >}}
