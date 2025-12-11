---
title: java.security.InvalidKeyException
type: docs
weight: 10
url: /java/java-security-invalidkeyexception/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Summary**
By default, AES supports a 128‑bit key. If you plan to use a 192‑bit or 256‑bit key, the Java compiler will throw an *Illegal key size* exception. This is not due to a bug in the Aspose.Cells API, but rather due to the limited features of the JDK/JRE itself. The default policy files of the JDK/JRE are crippled because of import restrictions in some countries. Users have to obtain the **Unlimited Strength** policy files and install them in their JRE to use advanced cryptography functionality for encryption/decryption.

## **Symptoms**
You may get `java.security.InvalidKeyException: Illegal key size` (or default parameters) while loading a protected spreadsheet.

## **Solution**
The solution is actually very simple, as detailed below.

1. Download the Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files.  
2. Extract the JAR files from the downloaded archive and place them in the `${java.home}/jre/lib/security/` directory.  
3. Rerun the program.

## **Download Links**
Please use the download link that corresponds to your JDK/JRE version.

- [Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 6](https://www.oracle.com/java/technologies/jce-6-download.html)
- [Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 7](https://www.oracle.com/java/technologies/jce-7-download.html)
- [Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 8](https://www.oracle.com/java/technologies/javase-jce8-downloads.html)

{{< app/cells/assistant language="java" >}}
