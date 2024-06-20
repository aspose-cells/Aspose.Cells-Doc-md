---
title: Eseguire la funzione lato client al cambiamento della pagina di GridWeb
type: docs
weight: 70
url: /it/java/execute-client-side-function-on-gridweb-page-change/
---

## **Possibili Scenari di Utilizzo**
A volte è necessario eseguire la funzione lato client quando cambia la pagina di GridWeb. Aspose.Cells.GridWeb fornisce la proprietà OnPageChangeClientFunction a tale scopo. Si prega di impostare questa proprietà con la funzione lato client che si desidera eseguire.
## **Eseguire la funzione lato client al cambiamento della pagina di GridWeb**
Il seguente codice Java spiega come utilizzare la proprietà GridWebBean.setOnPageChangeClientFunction(). Imposta la proprietà con la funzione lato client chiamata MyOnPageChange. Si prega di notare che questa proprietà è valida solo se si è abilitata la paginazione cioè GridWebBean.setEnablePaging(true). Ora, ogni volta che si cambierà la pagina di GridWeb, verrà chiamata la funzione lato client MyOnPageChange che stamperà l'**indice della pagina corrente** sulla **console** come mostrato in questa schermata.

![todo:image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
## **Codice di Esempio**
Questo è il codice della funzione lato client MyOnPageChange che verrà eseguita a causa di questa riga cioè Gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< highlight java >}}

 function MyOnPageChange(index) {

	console.log("current page is:" + (index+1));

}

{{< /highlight >}}

Il seguente codice spiega come abilitare la paginazione e impostare la proprietà OnPageChangeClientFunction.

{{< highlight java >}}

 GridWebBean gridweb=BeanManager.getBean(request);

gridweb.setEnablePaging(true);

gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< /highlight >}}
