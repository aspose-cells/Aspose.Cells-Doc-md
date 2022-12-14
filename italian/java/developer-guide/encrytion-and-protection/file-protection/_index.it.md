---
title: Crittografare e decrittografare i file Excel
type: docs
weight: 40
url: /it/java/encrypt-and-decrypt-excel-files/
description: Come crittografare e decrittografare i file excel utilizzando java. Blocca e sblocca i file Excel.
---
{{% alert color="primary" %}}
Microsoft Excel (97 - 365 ) consente di crittografare/proteggere con password i fogli di calcolo. Utilizza algoritmi forniti da Crypto Service Provider. Un Crypto Service Provider o CSP è un insieme di algoritmi crittografici con diverse proprietà. Il CSP predefinito è "Compatibile con Office 97/2000" o "Crittografia settimanale (XOR)". È anche importante scegliere una lunghezza della chiave di crittografia adeguata. Alcuni dei provider di servizi di crittografia non supportano più di 40 o 56 bit. Questo è considerato un tipo di crittografia debole. Tuttavia, per un tipo di crittografia forte, è richiesta una lunghezza minima della chiave di 128 bit. Microsoft Windows contiene provider di servizi di crittografia che offrono anche tipi di crittografia avanzata, ad esempio "Microsoft Strong Cryptographic Provider". Per dare un'idea, la crittografia a 128 bit è ciò che le banche utilizzano per crittografare la connessione con i loro sistemi di Internet Banking. Aspose.Cells consente di crittografare/proteggere con password i file excel con il tipo di crittografia desiderato.

{{% /alert %}}

## **Utilizzo di Microsoft Excel**

In MS Excel (ad esempio MS Excel 2003), per implementare le impostazioni di crittografia dei file, puoi provare:

-  Dal**Strumenti** menù, selezionare**Opzioni** , quindi selezionare il**Sicurezza** scheda.
-  Ingresso**Password per aprire** e fare clic su**Avanzate** pulsante.
- Scegli il tipo di crittografia e conferma la password.

![cose da fare:immagine_alt_testo](encrypting-excel-files_1.png)

**Figura: finestra di dialogo Opzioni**

![cose da fare:immagine_alt_testo](encrypting-excel-files_2.png)

**Figura: finestra di dialogo Tipo di crittografia**

## **Crittografia file Excel**
L'esempio seguente mostra come è possibile crittografare/proteggere con password un file excel utilizzando Aspose.Cells API.

### **Codice di esempio:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingFiles-EncryptingFiles.java" >}}


## **Decrittografia file Excel con Aspose.Cells**
È molto utile aprire il file excel protetto da password e decrittografarlo utilizzando Aspose.Cells API come i seguenti codici:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Decrypt-Excel-File.java" >}}



