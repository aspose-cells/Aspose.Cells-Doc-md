---
title: java.security.InvalidKeyException
type: docs
weight: 10
url: /de/java/java-security-invalidkeyexception/
---

## **Zusammenfassung**
Standardmäßig unterstützt AES einen 128-Bit-Schlüssel. Wenn Sie einen 192-Bit- oder 256-Bit-Schlüssel verwenden möchten, wirft der Java-Compiler eine Ausnahme für ungültige Schlüsselgröße. Dies liegt nicht an einem Fehler der Aspose.Cells API, sondern an den eingeschränkten Funktionen des JDK/JRE selbst. Die Standardrichtliniendateien des JDK/JRE sind aufgrund von Importbeschränkungen in einigen Ländern eingeschränkt. Benutzer müssen die Richtliniendateien für "Unbegrenzte Stärke" erhalten und in ihr JRE installieren, um erweiterte kryptografische Funktionen für Verschlüsselung/Entschlüsselung zu verwenden.
## **Symptome**
Sie können die java.security.InvalidKeyException: Ungültige Schlüsselgröße oder Standardparameter oder java.security.InvalidKeyException: Ungültige Schlüsselgröße beim Laden einer geschützten Tabellekalkulation erhalten. 
## **Lösung**
Die Lösung ist tatsächlich sehr einfach, wie unten detailliert beschrieben.

1. Laden Sie die Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files herunter.
1. Entpacken Sie die JAR-Dateien aus dem heruntergeladenen Archiv und platzieren Sie sie im Verzeichnis ${java.home}/jre/lib/security/.
1. Führen Sie das Programm erneut aus.
## **Download-Links**
Verwenden Sie bitte den Download-Link, der Ihrer JDK/JRE-Version entspricht.

- [Unbeschränkte Stärke der Richtlinien für die kryptografische Erweiterung (JCE) in Java 6](https://www.oracle.com/java/technologies/jce-6-download.html)
- [Unbeschränkte Stärke der Richtlinien für die kryptografische Erweiterung (JCE) in Java 7](https://www.oracle.com/java/technologies/jce-7-download.html)
- [Unbeschränkte Stärke der Richtlinien für die kryptografische Erweiterung (JCE) in Java 8](https://www.oracle.com/java/technologies/javase-jce8-downloads.html)
