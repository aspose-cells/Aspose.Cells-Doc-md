---
title: java.security.InvalidKeyException
type: docs
weight: 10
url: /sv/java/java-security-invalidkeyexception/
---
## **Sammanfattning**
Som standard stöder AES en 128-bitarsnyckel, om du planerar att använda 192-bitars eller 256-bitarsnyckeln kommer java-kompilatorn att ge ett undantag för illegal nyckelstorlek. Detta beror inte på någon bugg av Aspose.Cells API snarare på grund av den begränsade funktionen för JDK/JRE själv. Standardpolicyfilerna för JDK/JRE är förlamade på grund av importrestriktioner i vissa länder. Användare måste skaffa policyfilerna "Obegränsad styrka" och installera dem i sin JRE för att använda avancerad kryptografifunktion för kryptering/dekryptering.
## **Symtom**
 Du kan få java.security.InvalidKeyException: Olaglig nyckelstorlek eller standardparametrar eller java.security.InvalidKeyException: Olaglig nyckelstorlek när du laddar ett skyddat kalkylblad.
## **Lösning**
Lösningen är faktiskt väldigt enkel som beskrivs nedan.

1. Ladda ner Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files.
1. Extrahera JAR-filerna från det nedladdade arkivet och placera dem i katalogen ${java.home}/jre/lib/security/.
1. Kör programmet igen.
## **Ladda ner länkar**
Använd nedladdningslänken som motsvarar din JDK/JRE-version.

- [Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 6](https://www.oracle.com/java/technologies/jce-6-download.html)
- [Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 7](https://www.oracle.com/java/technologies/jce-7-download.html)
- [Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 8](https://www.oracle.com/java/technologies/javase-jce8-downloads.html)
