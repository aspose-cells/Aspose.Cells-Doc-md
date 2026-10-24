---
title: Verificare la password per la modifica utilizzando Aspose.Cells
type: docs
weight: 190
url: /it/java/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

Puoi assegnare una **Password per l'apertura** e una **Password per la modifica** mentre crei i tuoi fogli di lavoro in Microsoft Excel. Si prega di vedere questa schermata che mostra l'interfaccia con cui Microsoft Excel consente di specificare queste password.

![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)

A volte è necessario verificare se la password fornita corrisponde alla **Password per la modifica** in modo programmatico. Aspose.Cells fornisce il metodo [**workbook.getSettings().getWriteProtection().validatePassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/writeprotection#validatePassword-java.lang.String-) che puoi utilizzare per verificare se la password fornita per la modifica è corretta o meno.

{{% /alert %}}

## Codice Java per verificare la Password per la modifica utilizzando Aspose.Cells

I seguenti codici di esempio caricano il [file Excel di origine](5473057.xlsx). Ha una password per l'apertura come *1234* e una password per la modifica come *5678*. Il codice prima controlla se *567* è la password corretta per la modifica e restituisce **false**, quindi controlla se *5678* è la password per la modifica e restituisce **true**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckPassword-CheckPassword.java" >}}

## Output della Console generato dal codice Java

Ecco l'output della Console del codice di esempio sopra dopo aver caricato il [file Excel di origine](5473057.xlsx).

{{< highlight java >}}

Is 567 correct Password to modify: false

Is 5678 correct Password to modify: true

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
