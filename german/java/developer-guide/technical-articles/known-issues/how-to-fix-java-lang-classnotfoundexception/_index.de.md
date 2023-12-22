---
title: So beheben Sie die Ausnahme java.lang.ClassNotFoundException
type: docs
weight: 30
url: /de/java/how-to-fix-java-lang-classnotfoundexception/ 
description: Erfahren Sie, wie Sie die Ausnahme java.lang.ClassNotFoundException in Aspose.Cells for Java beheben.
keywords: How to fix BouncyCastleProvider ClassNotFoundException in Java, Solve BouncyCastleProvider exception using Java, Java solve ClassNotFoundException BouncyCastleProvider.
---
Aspose.Cells for Java API hängt von einigen zusätzlichen Bibliotheken ab. Wenn diese fehlen, wird möglicherweise eine Ausnahme als „java.lang.ClassNotFoundException“ ausgelöst.
In diesem Artikel werden solche Ausnahmen aufgeführt und erläutert, welche Bibliotheken installiert werden, um sie zu beheben.

##  So beheben Sie ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider
###  **Zusammenfassung**
Aspose.Cells for Java API ist für die Verschlüsselungs- und Entschlüsselungsfunktionen von Bouncy Castle abhängig. Wenn das Programm also verschlüsselte Tabellen laden oder speichern muss, muss im Klassenpfad des Projekts ein Verweis auf bcprov-jdk16-146.jar hinzugefügt werden.
###  **Symptome**
 Möglicherweise erhalten Sie die java.lang.ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider.
###  **Lösung**
Die Lösung ist eigentlich sehr einfach, wie unten beschrieben.

1.  Laden Sie eine beliebige Hauptversion von herunter[Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. Extrahieren Sie das heruntergeladene Archiv und navigieren Sie zum Verzeichnis \JDK 1.6\aspose-cells-xx0-java\lib.
1. Verweisen Sie auf bcprov-jdk16-146.jar im Klassenpfad des Projekts.

Alternativ können Sie die Abhängigkeit in pom.xml hinzufügen und das Projekt die Abhängigkeit über maven auflösen lassen.

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

