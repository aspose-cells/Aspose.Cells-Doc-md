---
title: Assegna e convalida le firme digitali
linktitle: Firma
type: docs
weight: 140
url: /it/net/assign-and-validate-digital-signatures/
description: Firma digitale del file Excel, verifica. Per proteggere l'autenticità del contenuto di una cartella di lavoro del file Excel, è possibile aggiungere una firma digitale utilizzando i codici C# con Aspose.Cells per .Net.
---
{{% alert color="primary" %}}

 Una firma digitale garantisce che un file della cartella di lavoro sia valido e che nessuno lo abbia modificato. È possibile creare una firma digitale personale utilizzando il file**Microsoft Selfcert.exe** o qualsiasi altro strumento, oppure puoi acquistare una firma digitale. Dopo aver creato una firma digitale, è necessario allegarla alla cartella di lavoro. Allegare una firma digitale è simile a sigillare una busta. Se una busta arriva sigillata, hai un certo livello di sicurezza che nessuno ha manomesso il suo contenuto.

{{% /alert %}}

## **introduzione**

 Utilizzare la finestra di dialogo Firma digitale per allegare una firma digitale. La finestra di dialogo Firma digitale elenca i certificati validi. È possibile utilizzare la finestra di dialogo Firma digitale per visualizzare i certificati e selezionare quello che si desidera utilizzare. Se una cartella di lavoro ha una firma digitale, il nome della firma viene visualizzato nel file**Nome certificato** campo. Se fai clic sul**Rimuovere** pulsante nella finestra di dialogo Firma digitale, Microsoft Excel rimuove anche la firma digitale.

Aspose.Cells fornisce il[**Aspose.Cells.DigitalSignatures**](https://reference.aspose.com/cells/net/aspose.cells.digitalsignatures/digitalsignature)spazio dei nomi per eseguire il lavoro (assegnare e convalidare le firme digitali). Lo spazio dei nomi ha alcune funzioni utili per l'aggiunta e la convalida delle firme digitali.

Vedere il seguente codice di esempio che descrive come eseguire l'attività utilizzando Aspose.Cells for .NET API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-AssignAndValidateDigitalSignatures-AssignAndValidateDigitalSignatures.cs" >}}



## **Argomenti avanzati**
- [Aggiungi la firma digitale a un file Excel già firmato](/cells/it/net/add-digital-signature-to-an-already-signed-excel-file/)
- [Aggiungi la riga della firma al foglio di lavoro](/cells/it/net/add-signature-line/)
- [Supporto per la firma XAdES](/cells/it/net/support-for-xades-signature/)
