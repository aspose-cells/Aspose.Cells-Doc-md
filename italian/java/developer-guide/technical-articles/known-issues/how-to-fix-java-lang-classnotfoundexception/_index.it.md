---
title: Come risolvere l'eccezione java.lang.ClassNotFoundException
type: docs
weight: 30
url: /it/java/how-to-fix-java-lang-classnotfoundexception/ 
description: Scopri come risolvere java.lang.ClassNotFoundException in Aspose.Cells for Java.
keywords: How to fix BouncyCastleProvider ClassNotFoundException in Java, Solve BouncyCastleProvider exception using Java, Java solve ClassNotFoundException BouncyCastleProvider.
---
Aspose.Cells for Java API dipende da alcune librerie aggiuntive, se mancano, potrebbe essere generata un'eccezione come "java.lang.ClassNotFoundException".
Questo articolo elenca questo tipo di eccezioni e spiega quali librerie sono installate per risolverle.

##  Come risolvere ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider
###  **Riepilogo**
Aspose.Cells for Java API dipende da Bouncy Castle per le funzionalità di crittografia e decrittografia, ovvero, se il programma deve caricare o salvare fogli di calcolo crittografati, è necessario aggiungere il riferimento di bcprov-jdk16-146.jar nel percorso classe del progetto.
###  **Sintomi**
 Potresti ottenere la java.lang.ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider.
###  **Soluzione**
La soluzione è in realtà molto semplice, come spiegato di seguito.

1.  Scarica qualsiasi versione principale di[Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. Estrai l'archivio scaricato e vai alla directory \JDK 1.6\aspose-cells-xx0-java\lib.
1. Fare riferimento a bcprov-jdk16-146.jar nel percorso classe del progetto.

In alternativa, puoi aggiungere la dipendenza nel pom.xml e lasciare che il progetto risolva la dipendenza tramite maven.

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

