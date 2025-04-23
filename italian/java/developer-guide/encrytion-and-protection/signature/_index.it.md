---
title: Assegnare e convalidare le firme digitali
linktitle: Firma
type: docs
weight: 100
url: /it/java/assign-and-validate-digital-signatures/
description: Firma digitale del file Excel, verifica. Per proteggere l autenticità del contenuto di una cartella di lavoro del file Excel, è possibile aggiungere una firma digitale utilizzando i codici C# con Aspose.Cells per .Net.
---

{{% alert color="primary" %}}

Una firma digitale fornisce l'assicurazione che un file di cartella di lavoro è valido e che nessuno lo ha alterato. È possibile creare una firma digitale personale utilizzando lo strumento SELFCERT incluso nella suite Microsoft Office o qualsiasi altro strumento. È anche possibile acquistare una firma digitale. Dopo aver creato o acquisito una firma digitale, è necessario allegarla alla cartella di lavoro. Allegare una firma digitale è simile a sigillare una busta. Se una busta arriva sigillata, si ha un certo livello di assicurazione che nessuno ha manomesso il suo contenuto.

L'API Aspose.Cells for Java fornisce le classi [**com.aspose.cells.DigitalSignatureCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignatureCollection) e [**com.aspose.cells.DigitalSignature**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignature) per firmare le cartelle di lavoro e convalidarle.

{{% /alert %}}

## **Firmare le cartelle di lavoro**

Il processo di firma richiede un certificato come discusso in precedenza. Insieme al certificato, è necessario avere anche la relativa password per firmare correttamente le cartelle di lavoro utilizzando l'API Aspose.Cells.

Il seguente frammento di codice dimostra l'uso dell'API Aspose.Cells for Java per firmare una cartella di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SigningSpreadsheets-SigningSpreadsheets.java" >}}

{{% alert color="primary" %}}

Nel caso in cui la password specificata non corrisponda a quella del certificato, verrà generata un'eccezione di tipo *javax.crypto.BadPaddingException*.

{{% /alert %}}

## **Convalidare le cartelle di lavoro**

Il seguente frammento di codice dimostra l'uso dell'API Aspose.Cells for Java per convalidare la cartella di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ValidatingSpreadsheets-ValidatingSpreadsheets.java" >}}
{{< app/cells/assistant language="java" >}}
