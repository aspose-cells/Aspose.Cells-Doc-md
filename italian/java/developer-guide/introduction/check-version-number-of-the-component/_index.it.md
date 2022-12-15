---
title: Controllare il numero di versione del componente
type: docs
weight: 70
url: /it/java/check-version-number-of-the-component/
---
{{% alert color="primary" %}} 

In alcuni casi, potresti chiederti quale versione del prodotto possiedi. Spesso creiamo nuove correzioni (correzioni di bug per gli scenari utente che segnalano) e le pubblichiamo nei forum contro le loro necessità con urgenza. Il numero di versione è costituito dal numero di versione principale, dal numero di versione secondaria e dal numero di versione dell'aggiornamento rapido. Tutti i componenti definiti devono essere numeri interi maggiori o uguali a 0. Il formato del numero di versione è il seguente:

major.minor.hotfix , potremmo aumentare una parte di 1 e creare una nuova versione. Normalmente, aumentiamo l'ultima parte di 1 e creiamo una nuova correzione per pubblicarla nei forum per gli utenti.

Questo documento descrive alcuni modi per controllare quale versione del componente è installata sul tuo sistema.

{{% /alert %}} 
## **Controllo del numero di versione**
### **1) Modo manuale**
Se si dispone della versione/correzione di Java (Aspose.Cells for Java), è possibile decomprimere il file jar della libreria Aspose.Cells, aprire il file MANIFEST con il blocco note e cercare la stringa, ad esempio "Specification-Version: " per verificarne il valore.

![cose da fare:immagine_alt_testo](check-version-number-of-the-component_1.png)


**Figura:** Controllo del numero di versione della correzione Java
### **2) Utilizzo delle API**
Puoi anche utilizzare le seguenti API per ottenere il numero di versione del prodotto.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-CheckVersionNumberOfComponent-CheckVersionNumberOfComponent.java" >}}

