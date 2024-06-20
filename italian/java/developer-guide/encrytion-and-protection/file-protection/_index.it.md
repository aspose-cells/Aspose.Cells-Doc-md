---
title: Crittografa e Decrittografa file Excel
type: docs
weight: 40
url: /it/java/encrypt-and-decrypt-excel-files/
description: Come crittografare e decrittografare file Excel utilizzando Java. Blocca e sblocca file Excel.
---

{{% alert color="primary" %}}
Microsoft Excel (97 - 365) consente di crittografare / proteggere con password i propri fogli di calcolo. Utilizza algoritmi forniti dal Crypto Service Provider. Un Crypto Service Provider o CSP è un insieme di algoritmi crittografici con diverse proprietà. Il CSP predefinito è "Office 97/2000 Compatible" o "Crittografia settimanale (XOR)". È anche importante scegliere una corretta lunghezza della chiave di crittografia. Alcuni Crypto Service Provider non supportano più di 40 o 56 bit. Questo è considerato un tipo di crittografia debole. Ma, per un tipo di crittografia forte, è richiesta una lunghezza minima della chiave di 128 bit. Microsoft Windows contiene Crypto Service Providers che offrono anche tipi di crittografia forte, ad esempio il 'Microsoft Strong Cryptographic Provider'. Per darti un'idea, la crittografia a 128 bit è quella che le banche utilizzano per crittografare la connessione con i loro sistemi di banca online. Aspose.Cells ti consente di crittografare / proteggere con password i tuoi file Excel con il tipo di crittografia desiderato.

{{% /alert %}}

## **Usare MS Excel**

In MS Excel (ad esempio MS Excel 2003), per implementare le impostazioni di crittografia del file, si può provare:

- Dal menu **Strumenti**, selezionare **Opzioni**, e quindi selezionare la scheda **Sicurezza**.
- Inserire la **Password per aprire** e fare clic sul pulsante **Avanzate**.
- Scegliere il tipo di crittografia e confermare la password.

![todo:image_alt_text](encrypting-excel-files_1.png)

**Figura: Dialogo Opzioni**

![todo:image_alt_text](encrypting-excel-files_2.png)

**Figura: Dialogo Tipo di Crittografia**

## **Crittografare il file Excel**
L'esempio seguente mostra come è possibile crittografare / proteggere con password un file Excel utilizzando l'API di Aspose.Cells.

### **Codice di Esempio:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingFiles-EncryptingFiles.java" >}}


## **Decrittografare un file Excel con Aspose.Cells**
È molto semplice aprire un file Excel protetto da password e decifrarlo usando l'API Aspose.Cells come segue:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Decrypt-Excel-File.java" >}}



