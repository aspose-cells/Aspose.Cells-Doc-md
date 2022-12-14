---
title: java.security.InvalidKeyException
type: docs
weight: 10
url: /de/java/java-security-invalidkeyexception/
---
## **Zusammenfassung**
Standardmäßig unterstützt AES einen 128-Bit-Schlüssel. Wenn Sie 192-Bit- oder 256-Bit-Schlüssel verwenden möchten, löst der Java-Compiler eine Ausnahme wegen illegaler Schlüsselgröße aus. Dies liegt nicht an einem Fehler von Aspose.Cells API, sondern an der eingeschränkten Funktion für JDK/JRE selbst. Die Standardrichtliniendateien von JDK/JRE sind aufgrund von Importbeschränkungen in einigen Ländern lahmgelegt. Benutzer müssen die „Unlimited Strength“-Richtliniendateien abrufen und sie in ihrer JRE installieren, um erweiterte Kryptografiefunktionen für die Verschlüsselung/Entschlüsselung zu verwenden.
## **Symptome**
 Möglicherweise erhalten Sie die java.security.InvalidKeyException: Illegal key size or default parameters oder java.security.InvalidKeyException: Illegal key size while loading a protected Spreadsheet.
## **Lösung**
Die Lösung ist eigentlich sehr einfach, wie unten beschrieben.

1. Laden Sie die Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files herunter.
1. Extrahieren Sie die JAR-Dateien aus dem heruntergeladenen Archiv und legen Sie sie im Verzeichnis ${java.home}/jre/lib/security/ ab.
1. Führen Sie das Programm erneut aus.
## **Download links**
Bitte verwenden Sie den Download-Link, der Ihrer JDK/JRE-Version entspricht.

- [Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 6](https://www.oracle.com/java/technologies/jce-6-download.html)
- [Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 7](https://www.oracle.com/java/technologies/jce-7-download.html)
- [Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 8](https://www.oracle.com/java/technologies/javase-jce8-downloads.html)
