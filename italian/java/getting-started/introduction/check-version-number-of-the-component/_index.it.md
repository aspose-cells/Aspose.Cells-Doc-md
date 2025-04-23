---
title: Controllare il numero di versione del componente
type: docs
weight: 70
url: /it/java/check-version-number-of-the-component/
---

{{% alert color="primary" %}} 

In alcuni casi, potresti chiederti quale versione del prodotto hai. Spesso costruiamo nuove correzioni (correzioni di bug per gli scenari dell'utente che ci indicano) e le pubblichiamo nei forum in base alla loro necessità urgente. Il numero di versione è composto da numero di versione principale, numero di versione minore e numero di versione di hotfix. Tutti i componenti definiti devono essere numeri interi maggiori o uguali a 0. Il formato del numero di versione è il seguente:

versione principale.minore.hotfix, possiamo aumentare una parte di 1 e creare una nuova versione. Normalmente, aumentiamo l'ultima parte di 1 e creiamo una nuova correzione per pubblicarla nei forum per gli utenti.

Questo documento descrive alcuni modi per verificare quale versione del componente è installata sul tuo sistema.

{{% /alert %}} 
## **Controllo del numero di versione**
### **1) Metodo manuale**
Se hai la versione/correzione Java (Aspose.Cells for Java), puoi decomprimere il file jar della libreria Aspose.Cells, aprire il file MANIFEST con il Blocco note e cercare la stringa cioè., "Specification-Version: " per controllarne il valore.

![todo:image_alt_text](check-version-number-of-the-component_1.png)


**Figura:** Verifica del numero di versione del fix Java
### **2) Utilizzo delle API**
È anche possibile utilizzare le seguenti API per ottenere il numero di versione del prodotto.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-CheckVersionNumberOfComponent-CheckVersionNumberOfComponent.java" >}}

{{< app/cells/assistant language="java" >}}
