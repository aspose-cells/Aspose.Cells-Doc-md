---
title: Impostazione del tipo di crittografia forte
type: docs
weight: 10
url: /it/java/setting-strong-encryption-type/
---

{{% alert color="primary" %}}

Microsoft Excel (97-2007/2010) ti consente di criptare e proteggere con password i fogli di calcolo. Utilizza algoritmi forniti da un Fornitore di Servizi Crittografici. Un Fornitore di Servizi Crittografici (o CSP) è un insieme di algoritmi crittografici con diverse proprietà. Il CSP predefinito è "Office 97/2000 Compatible". Si tratta di un CSP con alcune note problematiche di sicurezza. I fogli di calcolo che sono protetti con la "crittografia debole (XOR)" o con il tipo di crittografia "Office 97/2000 Compatible" possono essere facilmente violati.

Per superare questo problema, utilizzare uno dei tipi di crittografia robusti forniti da Microsoft Excel. Puoi cambiare il tipo di crittografia con il CSP più forte disponibile. Per una crittografia robusta, è richiesta una lunghezza chiave minima di 128 bit, ad esempio 'Microsoft Strong Cryptographic Provider'.

È anche possibile crittografare e proteggere con password file di Excel con tipo di crittografia forte utilizzando l'API Aspose.Cells.

{{% /alert %}}

## **Applicare la crittografia con Microsoft Excel**

Per implementare la crittografia file in Microsoft Excel (ad esempio 2007):

1. Dal menu **Strumenti**, selezionare **Opzioni**.
1. Selezionare la scheda **Sicurezza**.
1. Immettere un valore per il campo **Password per aprire**.
1. Fare clic su **Avanzate**.
1. Scegliere il tipo di crittografia e confermare la password.

   **Impostazione della crittografia in Microsoft Excel**

![todo:image_alt_text](setting-strong-encryption-type_1.png)

## **Applicare la crittografia con Aspose.Cells**

L'esempio di codice di seguito applica una crittografia robusta a un file e imposta una password.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyingEncryption-ApplyingEncryption.java" >}}
{{< app/cells/assistant language="java" >}}
