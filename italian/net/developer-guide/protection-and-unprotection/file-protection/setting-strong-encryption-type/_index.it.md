---
title: Impostazione del tipo di crittografia forte
type: docs
weight: 60
url: /it/net/setting-strong-encryption-type/
---

{{% alert color="primary" %}} 

Microsoft Excel (97-2007/2010) ti consente di crittografare e proteggere con password i fogli di calcolo. Utilizza algoritmi forniti da un Provider di servizi crittografici. Un Provider di servizi crittografici (o CSP) è un insieme di algoritmi crittografici con diverse proprietà. Il CSP predefinito è "Office 97/2000 Compatible". Questo è un CSP con alcuni problemi di sicurezza noti al pubblico. I fogli di calcolo che sono protetti con il tipo di crittografia "debole (XOR)" o con il tipo di crittografia "compatibile con Office 97/2000" possono essere facilmente violati.

Per superare questo problema, utilizzare uno dei tipi di crittografia forte forniti da Microsoft Excel. È possibile modificare il tipo di crittografia con il CSP più forte disponibile. Per la crittografia forte, è richiesta una lunghezza chiave minima di 128 bit, ad esempio 'Microsoft Strong Cryptographic Provider'.

È anche possibile crittografare e proteggere con password file di Excel con tipo di crittografia forte utilizzando l'API Aspose.Cells.

{{% /alert %}} 
## **Applicare la crittografia con Microsoft Excel**
Per implementare la crittografia file in Microsoft Excel (ad esempio 2007):

1. Dal menu **Strumenti**, selezionare **Opzioni**.
1. Selezionare la scheda **Sicurezza**.
1. Immettere un valore per il campo **Password per aprire**.
1. Fare clic su **Avanzate**.
1. Scegliere il tipo di crittografia e confermare la password.
## **Applicare la crittografia con Aspose.Cells**
Gli esempi di codice di seguito applicano una crittografia forte su un file e impostano una password.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingStrongEncryptionType-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
