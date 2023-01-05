---
title: Controllare la password da modificare utilizzando Aspose.Cells
type: docs
weight: 190
url: /it/java/check-password-to-modify-using-aspose-cells/
---
{{% alert color="primary" %}}

 Puoi assegnare un**Password per aprire** e un**Password da modificare** durante la creazione delle cartelle di lavoro in Microsoft Excel. Si prega di vedere questo screenshot che mostra l'interfaccia Microsoft fornita da Excel per specificare queste password.

![cose da fare:immagine_alt_testo](check-password-to-modify-using-aspose-cells_1.png)

 A volte, è necessario verificare se la password fornita corrisponde al file**Password da modificare** programmaticamente. Aspose.Cells fornisce[**cartella di lavoro.getSettings().getWriteProtection().validatePassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/writeprotection#validatePassword(java.lang.String)) metodo che puoi usare per verificare se la password data da modificare è corretta o meno.

{{% /alert %}}

## Java codice da controllare Password da modificare utilizzando Aspose.Cells

 I seguenti codici di esempio caricano il file[fonte Excel](5473057.xlsx) file. Ha una password per aprire come*1234* e password da modificare come*5678* . Il codice prima controlla se*567* è la password corretta da modificare e ritorna**falso** e poi controlla se*5678* è la password da modificare e ritorna**VERO**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckPassword-CheckPassword.java" >}}

## Console Output generato dal codice Java

 Ecco l'output della console del codice di esempio precedente dopo aver caricato il file[fonte Excel](5473057.xlsx) file.

{{< highlight "java" >}}

Is 567 correct Password to modify: false

Is 5678 correct Password to modify: true

{{< /highlight >}}
