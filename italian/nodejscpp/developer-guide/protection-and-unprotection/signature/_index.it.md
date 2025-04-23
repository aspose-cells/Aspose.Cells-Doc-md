---  
title: Assegna e convalida firme digitali con Node.js tramite C++  
linktitle: Firma  
type: docs  
weight: 140  
url: /it/nodejs-cpp/assign-and-validate-digital-signatures/  
description: Firma digitale e verifica del file Excel usando Aspose.Cells for Node.js via C++. Proteggi l autenticità del contenuto del workbook con firme digitali.  
keywords: Firma digitale del file Excel, Aggiungi firma digitale per Excel Node.js tramite C++, Come convalidare la firma digitale Node.js tramite C++  
---  

{{% alert color="primary" %}}  
Una firma digitale garantisce che un file di cartella di lavoro sia valido e che nessuno lo abbia alterato. È possibile creare una firma digitale personale utilizzando **Microsoft Selfcert.exe** o qualsiasi altro strumento, oppure è possibile acquistare una firma digitale. Dopo aver creato una firma digitale, è necessario allegarla alla cartella di lavoro. Allegare una firma digitale è simile a sigillare una busta. Se una busta arriva sigillata, si ha un certo livello di garanzia che nessuno abbia manomesso i suoi contenuti.  
{{% /alert %}}  

## **Introduzione**  

Utilizzare il dialogo Firma digitale per allegare una firma digitale. Il dialogo Firma digitale elenca certificati validi. È possibile utilizzare il dialogo Firma digitale per visualizzare i certificati e selezionare quello che si desidera utilizzare. Se una cartella di lavoro ha una firma digitale, il nome della firma appare nel campo **Nome certificato**. Se si fa clic sul pulsante **Rimuovi** nel dialogo Firma digitale, Microsoft Excel rimuove anche la firma digitale.  

## **Come aggiungere una firma digitale per Excel**  

Aspose.Cells fornisce il modulo [**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature/) per eseguire il lavoro (assegnare e convalidare firme digitali). Il modulo ha alcune caratteristiche utili per aggiungere e validare firme digitali.  

Consulta il seguente esempio di codice che descrive come puoi eseguire il compito usando l'API Aspose.Cells for Node.js via C++.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const certPassword = "aa";

// dsc is signature collection that contains one or more signatures needed to sign
const dsc = new AsposeCells.DigitalSignatureCollection();

// Cert must contain a private key, it can be constructed from a cert file or Windows certificate collection.
const cert = new AsposeCells.DigitalSignature(dataDir + "mykey2.pfx", certPassword, "test for sign", new Date());
dsc.add(cert);

const wb = new AsposeCells.Workbook();

// wb.setDigitalSignature signs all signatures in dsc
wb.setDigitalSignature(dsc);
wb.save(path.join(dataDir, "newfile_out.xlsx"));

// open the file
const wb2 = new AsposeCells.Workbook(path.join(dataDir, "newfile_out.xlsx"));
console.log(wb2.isDigitallySigned);

// Get digitalSignature collection from workbook
const dsc2 = wb2.getDigitalSignature();
const digitalSignatures = dsc2.getEnumerator();
for (var dst of digitalSignatures)
{
    console.log(dst.getComments()); // test for sign - OK
    console.log(dst.getSignTime()); // 11/25/2010 1:22:01 PM - OK
    console.log(dst.isValid()); // True - OK
}

```  

## **Argomenti avanzati**  
- [Aggiungi firma digitale a un file Excel già firmato](/cells/it/nodejs-cpp/add-digital-signature-to-an-already-signed-excel-file/)  
- [Aggiungi linea di firma al foglio di calcolo](/cells/it/nodejs-cpp/add-signature-line/)  
- [Supporto per la firma XAdES](/cells/it/nodejs-cpp/support-for-xades-signature/)  

