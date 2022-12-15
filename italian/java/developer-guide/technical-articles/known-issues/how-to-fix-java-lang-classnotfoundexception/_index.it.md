---
title: Come correggere java.lang.ClassNotFoundException
type: docs
weight: 30
url: /it/java/how-to-fix-java-lang-classnotfoundexception/ 
---
Aspose.Cells for Java L'API dipende da alcune librerie aggiuntive, se mancano, può essere generata un'eccezione come "java.lang.ClassNotFoundException".
Questo articolo elenca questo tipo di eccezioni e spiega quali librerie sono installate per risolverle.

## Come correggere ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider
### **Riepilogo**
Aspose.Cells for Java L'API dipende da Bouncy Castle per le funzionalità di crittografia e decrittografia, ovvero, se il programma deve caricare o salvare fogli di calcolo crittografati, è necessario aggiungere il riferimento a bcprov-jdk16-146.jar nel percorso di classe del progetto.
### **Sintomi**
 Potresti ottenere java.lang.ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider.
### **Soluzione**
La soluzione è in realtà molto semplice come descritto di seguito.

1.  Scarica qualsiasi versione principale di[Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. Estrarre l'archivio scaricato e accedere alla directory \JDK 1.6\aspose-cells-xx0-java\lib.
1. Fare riferimento a bcprov-jdk16-146.jar nel percorso classi del progetto.

In alternativa, puoi aggiungere la dipendenza in pom.xml e lasciare che il progetto risolva la dipendenza tramite maven.

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

