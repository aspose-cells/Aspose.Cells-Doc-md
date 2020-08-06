---
title: java.security.InvalidKeyException
type: docs
weight: 10
url: /java/java-security-invalidkeyexception/
---

### **Summary**
By default, the AES supports a 128 bit key, if you plan to use 192 bit or 256 bit key, java compiler will throw Illegal key size exception. This is not due to some bug of Aspose.Cells API rather due to the limited feature for JDK/JRE itself. The default policy files of JDK/JRE is crippled due to import restrictions in some countries. Users have to get the "Unlimited Strength" policy files and install them in their JRE to use advanced cryptography functionality for encryption/decryption.
### **Symptoms**
You may get the java.security.InvalidKeyException: Illegal key size or default parameters or java.security.InvalidKeyException: Illegal key size while loading a protected spreadsheet. 
### **Solution**
The solution is actually very simple as detailed below.

1. Download the Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files.
1. Extract the JAR files from the downloaded archive and place them in ${java.home}/jre/lib/security/ directory.
1. Rerun the program.
#### **Download Links**
Please use the download link that corresponds to your JDK/JRE version.

- [Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 6](http://www.oracle.com/technetwork/java/javase/downloads/jce-6-download-429243.html)
- [Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 7](http://www.oracle.com/technetwork/java/javase/downloads/jce-7-download-432124.html)
- [Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 8](http://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html)
