---
title: java.security.InvalidKeyException
type: docs
weight: 10
url: /sv/java/java-security-invalidkeyexception/
---

## **Sammanfattning**
Som standard stöder AES en nyckel på 128 bitar, om du planerar att använda en nyckel på 192 bitar eller 256 bitar kastar java-kompilatorn Illegal key size-undantaget. Detta beror inte på något fel i Aspose.Cells API utan på de begränsade funktionerna för JDK/JRE själva. JDK/JRE: s standardpolicyfiler är krökta på grund av importbegränsningar i vissa länder. Användare måste skaffa "Obegränsade styrke"-policyfiler och installera dem i sin JRE för att använda avancerade kryptografifunktioner för kryptering/dekryptering.
## **Symptom**
Du kan få java.security.InvalidKeyException: Illegal key size or default parameters eller java.security.InvalidKeyException: Illegal key size vid inläsning av ett skyddat kalkylblad. 
## **Lösning**
Lösningen är faktiskt mycket enkel som detaljeras nedan.

1. Ladda ner Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files.
1. Packa upp JAR-filerna från den nedladdade arkivet och placera dem i ${java.home}/jre/lib/security/ katalogen.
1. Kör programmet igen.
## **Nedladdningslänkar**
Var god använd nedladdningslänken som motsvarar din JDK/JRE-version.

- [Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 6](https://www.oracle.com/java/technologies/jce-6-download.html)
- [Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 7](https://www.oracle.com/java/technologies/jce-7-download.html)
- [Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 8](https://www.oracle.com/java/technologies/javase-jce8-downloads.html)
{{< app/cells/assistant language="java" >}}
