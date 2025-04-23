---
title: Wie man java.lang.ClassNotFoundException behebt
type: docs
weight: 30
url: /de/java/how-to-fix-java-lang-classnotfoundexception/ 
description: Erfahren Sie, wie man java.lang.ClassNotFoundException in der Aspose.Cells for Java behebt.
keywords: Wie man BouncyCastleProvider ClassNotFoundException in Java behebt, BouncyCastleProvider Ausnahme mit Java lösen, ClassNotFoundException BouncyCastleProvider mit Java lösen, Java ClassNotFoundException BouncyCastleProvider lösen.
---

Aspose.Cells for Java API ist von einigen zusätzlichen Bibliotheken abhängig. Wenn sie fehlen, kann eine Ausnahme als "java.lang.ClassNotFoundException" ausgelöst werden.
Dieser Artikel listet solche Ausnahmen auf und erläutert, welche Bibliotheken installiert sind, um sie zu beheben.

Wie man ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider behebt
### **Zusammenfassung**
Die Aspose.Cells for Java API ist auf Bouncy Castle für Verschlüsselungs- und Entschlüsselungsfunktionen angewiesen. D. h. wenn das Programm erforderlich ist, verschlüsselte Tabellen zu laden oder zu speichern, ist es erforderlich, eine Referenz von bcprov-jdk16-146.jar im Klassenpfad des Projekts hinzuzufügen.
### **Symptome**
Es kann sein, dass Sie die java.lang.ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider erhalten. 
### **Lösung**
Die Lösung ist tatsächlich sehr einfach, wie unten detailliert beschrieben.

1. Laden Sie eine beliebige Hauptversion von [Aspose.Cells for Java](https://downloads.aspose.com/cells/java) herunter.
1. Entpacken Sie das heruntergeladene Archiv und navigieren Sie zum Verzeichnis \JDK 1.6\aspose-cells-x.x.0-java\lib.
1. Verweisen Sie auf die bcprov-jdk16-146.jar im Klassenpfad des Projekts.

Alternativ können Sie die Abhängigkeit in der pom.xml hinzufügen und das Projekt die Abhängigkeit über Maven auflösen lassen.

{{< highlight java >}}

 <dependencies>

	<dependency>

		<groupId>org.bouncycastle</groupId>

		<artifactId>bcprov-jdk16</artifactId>

		<version>1.46</version>

		<type>jar</type>

	</dependency>

</dependencies>

{{< /highlight >}}

{{< app/cells/assistant language="java" >}}
