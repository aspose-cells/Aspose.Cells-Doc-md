---
title: Assegna e convalida le firme digitali
linktitle: Firma
type: docs
weight: 100
url: /it/java/assign-and-validate-digital-signatures/
description: Firma digitale del file Excel, verifica. Per proteggere l'autenticità del contenuto di una cartella di lavoro del file Excel, è possibile aggiungere una firma digitale utilizzando i codici C# con Aspose.Cells per .Net.
---
{{% alert color="primary" %}}

 Una firma digitale garantisce che un file della cartella di lavoro sia valido e che nessuno lo abbia modificato. È possibile creare una firma digitale personale utilizzando il file**AUTOCERT** strumento fornito con la suite Microsoft Office o qualsiasi altro strumento. Puoi persino acquistare una firma digitale. Dopo aver creato o acquisito una firma digitale, è necessario allegarla alla cartella di lavoro. Allegare una firma digitale è simile a sigillare una busta. Se una busta arriva sigillata, hai un certo livello di sicurezza che nessuno ha manomesso il suo contenuto.

 Aspose.Cells for Java API forniscono il[**com.aspose.cells.DigitalSignatureCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignatureCollection) & [**com.aspose.cells.DigitalSignature**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignature) classi per firmare i fogli di calcolo e convalidarli.

{{% /alert %}}

## **Firmare i fogli di calcolo**

Il processo di firma richiede un certificato come discusso sopra. Insieme al certificato, si dovrebbe avere anche la propria password per firmare correttamente i fogli di calcolo utilizzando l'API Aspose.Cells.

Il seguente frammento di codice illustra l'utilizzo dell'API Aspose.Cells for Java per firmare un foglio di calcolo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SigningSpreadsheets-SigningSpreadsheets.java" >}}

{{% alert color="primary" %}}

 Nel caso in cui la password specificata non corrisponda alla password del certificato allora un'eccezione di tipo*javax.crypto.BadPaddingException* verrà lanciato.

{{% /alert %}}

## **Convalida dei fogli di calcolo**

Il seguente frammento di codice illustra l'utilizzo dell'API Aspose.Cells for Java per convalidare il foglio di calcolo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ValidatingSpreadsheets-ValidatingSpreadsheets.java" >}}
