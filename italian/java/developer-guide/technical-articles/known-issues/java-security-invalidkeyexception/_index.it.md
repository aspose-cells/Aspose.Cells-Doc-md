---
title: java.security.InvalidKeyException
type: docs
weight: 10
url: /it/java/java-security-invalidkeyexception/
---

## **Sommario**
Per impostazione predefinita, AES supporta una chiave di 128 bit, se si prevede di utilizzare una chiave di 192 o 256 bit, il compilatore Java restituirà un'eccezione di dimensione chiave non consentita. Questo non è dovuto a un errore dell'API Aspose.Cells, ma piuttosto alla funzionalità limitata per JDK/JRE stesso. I file di policy predefiniti di JDK/JRE sono limitati a causa di restrizioni all'importazione in alcuni paesi. Gli utenti devono ottenere i file di policy "Unlimited Strength" e installarli nel loro JRE per utilizzare funzionalità di crittografia avanzate per crittografia/decrittografia.
## **Sintomi**
Potresti ricevere java.security.InvalidKeyException: dimensione chiave non consentita o parametri predefiniti o java.security.InvalidKeyException: dimensione chiave non consentita durante il caricamento di un foglio di calcolo protetto. 
## **Soluzione**
La soluzione è molto semplice come dettagliato di seguito.

1. Scarica i file di politica di giurisdizione di estensione di crittografia Java (JCE) con forza illimitata.
1. Estrarre i file JAR dall'archivio scaricato e inserirli nella directory ${java.home}/jre/lib/security/.
1. Esegui nuovamente il programma.
## **Link per il download**
Si prega di utilizzare il link per il download che corrisponde alla tua versione di JDK/JRE.

- [Estensione di crittografia Java (JCE) File di politica di giurisdizione di forza illimitata 6](https://www.oracle.com/java/technologies/jce-6-download.html)
- [Estensione di crittografia Java (JCE) File di politica di giurisdizione di forza illimitata 7](https://www.oracle.com/java/technologies/jce-7-download.html)
- [Estensione di crittografia Java (JCE) File di politica di giurisdizione di forza illimitata 8](https://www.oracle.com/java/technologies/javase-jce8-downloads.html)
{{< app/cells/assistant language="java" >}}
