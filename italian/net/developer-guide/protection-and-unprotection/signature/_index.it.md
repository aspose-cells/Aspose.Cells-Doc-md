---
title: Assegnare e convalidare le firme digitali
linktitle: Firma
type: docs
weight: 140
url: /it/net/assign-and-validate-digital-signatures/
description: Firma digitale del file Excel, verifica. Per proteggere l autenticità del contenuto di una cartella di lavoro del file Excel, è possibile aggiungere una firma digitale utilizzando i codici C# con Aspose.Cells per .Net.
keywords: Firma digitale del file di Excel, Aggiungi firma digitale per Excel, Come convalidare la firma digitale.
---

{{% alert color="primary" %}}

Una firma digitale garantisce che un file di cartella di lavoro sia valido e che nessuno lo abbia alterato. È possibile creare una firma digitale personale utilizzando **Microsoft Selfcert.exe** o qualsiasi altro strumento, oppure è possibile acquistare una firma digitale. Dopo aver creato una firma digitale, è necessario allegarla alla cartella di lavoro. Allegare una firma digitale è simile a sigillare una busta. Se una busta arriva sigillata, si ha un certo livello di garanzia che nessuno abbia manomesso i suoi contenuti.

{{% /alert %}}

## **Introduzione**

Utilizzare il dialogo Firma digitale per allegare una firma digitale. Il dialogo Firma digitale elenca certificati validi. È possibile utilizzare il dialogo Firma digitale per visualizzare i certificati e selezionare quello che si desidera utilizzare. Se una cartella di lavoro ha una firma digitale, il nome della firma appare nel campo **Nome certificato**. Se si fa clic sul pulsante **Rimuovi** nel dialogo Firma digitale, Microsoft Excel rimuove anche la firma digitale.

## **Come aggiungere una firma digitale per Excel**

Aspose.Cells fornisce il **namespace** [**Aspose.Cells.DigitalSignatures**](https://reference.aspose.com/cells/net/aspose.cells.digitalsignatures/digitalsignature) per eseguire il lavoro (assegnare e convalidare firme digitali). Il **namespace** ha alcune funzionalità utili per aggiungere e convalidare firme digitali.

Si prega di consultare il seguente codice di esempio che descrive come è possibile eseguire il compito utilizzando l'API Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-AssignAndValidateDigitalSignatures-AssignAndValidateDigitalSignatures.cs" >}}



## **Argomenti avanzati**
- [Aggiungi firma digitale a un file Excel già firmato](/cells/it/net/add-digital-signature-to-an-already-signed-excel-file/)
- [Aggiungi linea di firma al foglio di calcolo](/cells/it/net/add-signature-line/)
- [Supporto per la firma XAdES](/cells/it/net/support-for-xades-signature/)
