---
title: Esegui la funzione lato client alla modifica della pagina GridWeb
type: docs
weight: 70
url: /it/java/execute-client-side-function-on-gridweb-page-change/
---
##  **Possibili scenari di utilizzo**
A volte è necessario eseguire la funzione lato client quando la pagina GridWeb cambia. Aspose.Cells.GridWeb fornisce a questo scopo la proprietà OnPageChangeClientFunction. Imposta questa proprietà con la funzione lato client che desideri eseguire.
##  **Esegui la funzione lato client alla modifica della pagina GridWeb**
 Il seguente codice Java spiega come utilizzare la proprietà GridWebBean.setOnPageChangeClientFunction(). Imposta la proprietà con la funzione lato client denominata MyOnPageChange. Tieni presente che questa proprietà è valida solo se hai abilitato il paging, ad esempio GridWebBean.setEnablePaging(true). Ora, ogni volta che cambierai la pagina GridWeb, chiamerà la funzione lato client MyOnPageChange che stamperà il file**indice della pagina corrente** sul**consolle** come mostrato in questa schermata.

![cose da fare:immagine_alt_testo](execute-client-side-function-on-gridweb-page-change_1.png)
##  **Codice d'esempio**
Questo è il codice della funzione lato client MyOnPageChange che verrà eseguita a causa di questa riga, ovvero Gridweb.setOnPageChangeClientFunction("MyOnPageChange");

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
