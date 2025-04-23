---
title: Come risolvere java.lang.ClassNotFoundException
type: docs
weight: 30
url: /it/java/how-to-fix-java-lang-classnotfoundexception/ 
description: Scopri come risolvere java.lang.ClassNotFoundException nell Aspose.Cells for Java
keywords: Come risolvere BouncyCastleProvider ClassNotFoundException in Java, Risolvi l eccezione BouncyCastleProvider usando Java, Risolvi ClassNotFoundException BouncyCastleProvider in Java
---

L'API Aspose.Cells for Java dipende da alcune librerie aggiuntive, se mancano, potrebbe essere generata un'eccezione come "java.lang.ClassNotFoundException"
Questo articolo elenca tali tipi di eccezioni e spiega quali librerie devono essere installate per risolverle

## Come risolvere ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider
### **Sommario**
L'API Aspose.Cells for Java dipende da Bouncy Castle per funzionalità di crittografia e decrittografia, ovvero, se il programma deve caricare o salvare fogli di calcolo criptati, è necessario aggiungere il riferimento a bcprov-jdk16-146.jar nel percorso delle classi del progetto
### **Sintomi**
Potresti ottenere java.lang.ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider 
### **Soluzione**
La soluzione è molto semplice come dettagliato di seguito.

1. Scarica una qualsiasi release principale di [Aspose.Cells for Java](https://downloads.aspose.com/cells/java)
1. Estrai l'archivio scaricato e passa alla cartella \JDK 1.6\aspose-cells-x.x.0-java\lib
1. Fai riferimento a bcprov-jdk16-146.jar nel percorso delle classi del progetto

In alternativa, puoi aggiungere la dipendenza nel pom.xml e far risolvere la dipendenza tramite maven.

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
