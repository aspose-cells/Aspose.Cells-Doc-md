---
title: Impostazione del tipo di crittografia forte
type: docs
weight: 10
url: /it/java/setting-strong-encryption-type/
---
{{% alert color="primary" %}}

Microsoft Excel (97-2007/2010) consente di crittografare e proteggere con password i fogli di calcolo. Utilizza algoritmi forniti da un fornitore di servizi di crittografia. Un Crypto Service Provider (o CSP) è un insieme di algoritmi crittografici con diverse proprietà. Il CSP predefinito è "Compatibile con Office 97/2000". Questo è un CSP con alcuni problemi di sicurezza noti al pubblico. I fogli di calcolo protetti con la "crittografia debole (XOR)" o con il tipo di crittografia "Compatibile con Office 97/2000" possono essere violati facilmente.

Per ovviare a questo problema, utilizzare uno dei tipi di crittografia avanzata forniti da Microsoft Excel. È possibile modificare il tipo di crittografia impostandolo sul CSP più potente disponibile. Per la crittografia avanzata, è richiesta una lunghezza minima della chiave di 128 bit, ad esempio "Microsoft Strong Cryptographic Provider".

Puoi anche crittografare e proteggere con password i file Excel con un tipo di crittografia avanzata utilizzando Aspose.Cells API.

{{% /alert %}}

## **Applicazione della crittografia con Microsoft Excel**

Per implementare la crittografia dei file in Microsoft Excel (ad esempio 2007):

1.  Dal**Utensili** menù, selezionare**Opzioni**.
1.  Seleziona il**Sicurezza** scheda.
1.  Immettere un valore per il**Password per aprire** campo.
1.  Clic**Avanzate**.
1. Scegli il tipo di crittografia e conferma la password.

   **Impostazione della crittografia in Microsoft Excel**

![cose da fare:immagine_alt_testo](setting-strong-encryption-type_1.png)

## **Applicazione della crittografia con Aspose.Cells**

L'esempio di codice seguente applica una crittografia avanzata a un file e imposta una password.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyingEncryption-ApplyingEncryption.java" >}}
