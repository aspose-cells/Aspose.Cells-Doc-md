---
title: Crittografa e Decrittografa file Excel
type: docs
weight: 10
url: /it/python-java/encrypt-and-decrypt-excel-files/
description: Come crittare e decriptare file Excel utilizzando Python. Blocca e sblocca file Excel.
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) ti consente di crittare e proteggere con password i tuoi fogli di calcolo. Utilizza algoritmi forniti da un fornitore di servizi crittografici, o CSP, un insieme di algoritmi crittografici con proprietà diverse. Il CSP predefinito è 'Office 97/2000 Compatible' o 'Crittografia debole (XOR)'. È importante scegliere la corretta lunghezza della chiave di crittografia. Alcuni CSP non supportano più di 40 o 56 bit. Questo è considerato una crittografia debole. Per una crittografia forte, è richiesta una lunghezza minima della chiave di 128 bit. Microsoft Windows contiene CSP che offrono tipi di crittografia forte, ad esempio il 'Microsoft Strong Cryptographic Provider'. Per darti un'idea, la crittografia a 128 bit è ciò che le banche usano per crittografare la connessione con i loro sistemi di Internet Banking.

Aspose.Cells per Python ti consente di crittare e proteggere con password file Microsoft Excel con il tuo tipo di crittografia desiderato.

{{% /alert %}}

## **Utilizzando Microsoft Excel**

Per impostare le impostazioni di crittografia del file in Microsoft Excel (qui Microsoft Excel 2003):

1. Dal menu **Strumenti**, seleziona **Opzioni**. Verrà visualizzata una finestra di dialogo.
1. Selezionare la scheda **Sicurezza**.
1. Immetti una password e clicca su **Avanzate**
1. Scegliere il tipo di crittografia e confermare la password.

## **Crittare file Excel con Aspose.Cells**

L'esempio seguente mostra come crittare e proteggere con password un file excel utilizzando l'API Aspose.Cells.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-CSharp-Files-Utility-EncryptingFiles-1.py" >}}

## **Decrittografare un file Excel con Aspose.Cells**
È molto semplice aprire un file Excel protetto da password e decifrarlo usando l'API Aspose.Cells come segue:

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Decrypt-Excel-File.py" >}}


