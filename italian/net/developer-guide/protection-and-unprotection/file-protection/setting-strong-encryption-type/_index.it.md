---
title: Impostazione del tipo di crittografia avanzata
type: docs
weight: 60
url: /it/net/setting-strong-encryption-type/
---
{{% alert color="primary" %}} 

Microsoft Excel (97-2007/2010) consente di crittografare e proteggere con password i fogli di calcolo. Utilizza algoritmi forniti da un fornitore di servizi di crittografia. Un Crypto Service Provider (o CSP) è un insieme di algoritmi crittografici con diverse proprietà. Il CSP predefinito è "Compatibile con Office 97/2000". Questo è un CSP con alcuni problemi di sicurezza noti pubblicamente. I fogli di calcolo protetti con la "crittografia debole (XOR)" o con il tipo di crittografia "Compatibile con Office 97/2000" possono essere violati facilmente.

Per superare questo problema, utilizzare uno dei tipi di crittografia avanzata forniti da Microsoft Excel. È possibile modificare il tipo di crittografia impostandolo sul CSP più potente disponibile. Per la crittografia avanzata, è richiesta una lunghezza minima della chiave di 128 bit, ad esempio "Microsoft Strong Cryptographic Provider".

Puoi anche crittografare e proteggere con password i file Excel con un tipo di crittografia avanzata utilizzando l'API Aspose.Cells.

{{% /alert %}} 
## **Applicazione della crittografia con Microsoft Excel**
Per implementare la crittografia dei file in Microsoft Excel (ad esempio 2007):

1.  Dal**Strumenti** menù, selezionare**Opzioni**.
1.  Seleziona il**Sicurezza** scheda.
1.  Immettere un valore per il**Password per aprire** campo.
1.  Clic**Avanzate**.
1. Scegli il tipo di crittografia e conferma la password.
## **Applicazione della crittografia con Aspose.Cells**
Gli esempi di codice seguenti applicano una crittografia avanzata a un file e impostano una password.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingStrongEncryptionType-1.cs" >}}
