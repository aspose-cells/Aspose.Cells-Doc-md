---
title: Så här fixar du java.lang.ClassNotFoundException
type: docs
weight: 30
url: /sv/java/how-to-fix-java-lang-classnotfoundexception/ 
---
Aspose.Cells för Java API beror på några ytterligare bibliotek, om de saknas kan ett undantag kastas som "java.lang.ClassNotFoundException".
Den här artikeln listar sådana typer av undantag och förklarar vilka bibliotek som är installerade för att lösa dem.

## Så här fixar du ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider
### **Sammanfattning**
Aspose.Cells för Java API beror på Bouncy Castle för krypterings- och dekrypteringsfunktioner, det vill säga om programmet krävs för att ladda eller spara krypterade kalkylblad, krävs det att man lägger till referens för bcprov-jdk16-146.jar i projektets klasssökväg.
### **Symtom**
 Du kan få java.lang.ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider.
### **Lösning**
Lösningen är faktiskt väldigt enkel som beskrivs nedan.

1.  Ladda ner alla större utgåvor av[Aspose.Cells för Java](https://downloads.aspose.com/cells/java).
1. Extrahera det nedladdade arkivet och bläddra till katalogen \JDK 1.6\aspose-cells-xx0-java\lib.
1. Referera till bcprov-jdk16-146.jar i projektets klasssökväg.

Alternativt kan du lägga till beroendet i pom.xml och låta projektet lösa beroendet via maven.

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

