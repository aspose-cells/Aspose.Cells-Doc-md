---
title: Hur man åtgärdar java.lang.ClassNotFoundException
type: docs
weight: 30
url: /sv/java/how-to-fix-java-lang-classnotfoundexception/ 
description: Lär dig hur man åtgärdar java.lang.ClassNotFoundException i Aspose.Cells for Java.
keywords: Hur man åtgärdar BouncyCastleProvider ClassNotFoundException i Java, Lös BouncyCastleProvider undantag med Java, Java löser ClassNotFoundException BouncyCastleProvider.
---

Aspose.Cells for Java API är beroende av några ytterligare bibliotek, om de saknas kan ett undantag kastas som "java.lang.ClassNotFoundException".
Den här artikeln listar sådana typer av undantag och förklarar vilka bibliotek som är installerade för att lösa dem.

## Hur man åtgärdar ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider
### **Sammanfattning**
Aspose.Cells for Java API är beroende av Bouncy Castle för krypterings- och dekrypteringsfunktioner, det vill säga om programmet måste ladda eller spara krypterade kalkylblad är det nödvändigt att lägga till referens för bcprov-jdk16-146.jar i projektets classpath.
### **Symptom**
Du kan få java.lang.ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider. 
### **Lösning**
Lösningen är faktiskt mycket enkel som detaljeras nedan.

1. Ladda ner en huvudversion av [Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. Packa upp den nerladdade arkivet och bläddra till \JDK 1.6\aspose-cells-x.x.0-java\lib-mappen.
1. Ange bcprov-jdk16-146.jar i projektets classpath.

Alternativt kan du lägga till beroendet i pom.xml och låta projektet lösa beroendet via maven.

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

