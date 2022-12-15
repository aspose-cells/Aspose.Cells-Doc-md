---
title: java.security.InvalidKeyException
type: docs
weight: 10
url: /it/java/java-security-invalidkeyexception/
---
## **Riepilogo**
Per impostazione predefinita, AES supporta una chiave a 128 bit, se si prevede di utilizzare una chiave a 192 bit o 256 bit, il compilatore java genererà un'eccezione di dimensione della chiave illegale. Ciò non è dovuto a qualche bug dell'API Aspose.Cells piuttosto a causa della funzionalità limitata per JDK/JRE stesso. I file dei criteri predefiniti di JDK/JRE sono danneggiati a causa delle restrizioni all'importazione in alcuni paesi. Gli utenti devono ottenere i file dei criteri "Unlimited Strength" e installarli nel proprio JRE per utilizzare la funzionalità di crittografia avanzata per la crittografia/decrittografia.
## **Sintomi**
 È possibile ottenere java.security.InvalidKeyException: Illegal key size or default parameters o java.security.InvalidKeyException: Illegal key size durante il caricamento di un foglio di calcolo protetto.
## **Soluzione**
La soluzione è in realtà molto semplice come descritto di seguito.

1. Scarica i file dei criteri di giurisdizione a resistenza illimitata JCE (Java Cryptography Extension).
1. Estrarre i file JAR dall'archivio scaricato e posizionarli nella directory ${java.home}/jre/lib/security/.
1. Eseguire nuovamente il programma.
## **Link per il download**
Utilizzare il collegamento per il download corrispondente alla versione JDK/JRE in uso.

- [Java Cryptography Extension (JCE) File dei criteri di giurisdizione a forza illimitata 6](https://www.oracle.com/java/technologies/jce-6-download.html)
- [Java Cryptography Extension (JCE) File dei criteri di giurisdizione a forza illimitata 7](https://www.oracle.com/java/technologies/jce-7-download.html)
- [Java Cryptography Extension (JCE) File dei criteri di giurisdizione a forza illimitata 8](https://www.oracle.com/java/technologies/javase-jce8-downloads.html)
