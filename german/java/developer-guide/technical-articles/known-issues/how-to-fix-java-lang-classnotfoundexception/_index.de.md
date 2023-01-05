---
title: So beheben Sie java.lang.ClassNotFoundException
type: docs
weight: 30
url: /de/java/how-to-fix-java-lang-classnotfoundexception/ 
---
Aspose.Cells for Java API hängt von einigen zusätzlichen Bibliotheken ab, wenn sie fehlen, kann eine Ausnahme als "java.lang.ClassNotFoundException" ausgelöst werden.
Dieser Artikel listet solche Ausnahmen auf und erklärt, welche Bibliotheken installiert werden, um sie zu beheben.

## So beheben Sie ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider
### **Zusammenfassung**
Aspose.Cells for Java API hängt von Bouncy Castle für Verschlüsselungs- und Entschlüsselungsfunktionen ab, d. h. wenn das Programm verschlüsselte Tabellenkalkulationen laden oder speichern muss, muss der Verweis auf bcprov-jdk16-146.jar im Klassenpfad des Projekts hinzugefügt werden.
### **Symptome**
 Möglicherweise erhalten Sie die java.lang.ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider.
### **Lösung**
Die Lösung ist eigentlich sehr einfach, wie unten beschrieben.

1. Laden Sie eine beliebige Hauptversion von herunter[Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. Extrahieren Sie das heruntergeladene Archiv und navigieren Sie zum Verzeichnis \JDK 1.6\aspose-cells-xx0-java\lib.
1. Verweisen Sie im Klassenpfad des Projekts auf bcprov-jdk16-146.jar.

Alternativ können Sie die Abhängigkeit in der pom.xml hinzufügen und das Projekt die Abhängigkeit über maven auflösen lassen.

{{< highlight "java" >}}

 <dependencies>

	<dependency>

		<groupId>org.bouncycastle</groupId>

		<artifactId>bcprov-jdk16</artifactId>

		<version>1.46</version>

		<type>jar</type>

	</dependency>

</dependencies>

{{< /highlight >}}

