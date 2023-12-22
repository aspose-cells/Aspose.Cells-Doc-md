---
title: Comment corriger l'exception java.lang.ClassNotFoundException
type: docs
weight: 30
url: /fr/java/how-to-fix-java-lang-classnotfoundexception/ 
description: Découvrez comment corriger java.lang.ClassNotFoundException dans le Aspose.Cells for Java.
keywords: How to fix BouncyCastleProvider ClassNotFoundException in Java, Solve BouncyCastleProvider exception using Java, Java solve ClassNotFoundException BouncyCastleProvider.
---
Aspose.Cells for Java API dépend de certaines bibliothèques supplémentaires, si elles sont manquantes, une exception peut être levée sous la forme "java.lang.ClassNotFoundException".
Cet article répertorie ce type d'exceptions et explique quelles bibliothèques sont installées pour les résoudre.

##  Comment réparer ClassNotFoundException : org.bouncycastle.jce.provider.BouncyCastleProvider
###  **Résumé**
Aspose.Cells for Java API dépend de Bouncy Castle pour les fonctionnalités de cryptage et de décryptage, c'est-à-dire que si le programme doit charger ou enregistrer des feuilles de calcul cryptées, il est nécessaire d'ajouter la référence bcprov-jdk16-146.jar dans le chemin de classe du projet.
###  **Symptômes**
 Vous pouvez obtenir l'exception java.lang.ClassNotFoundException : org.bouncycastle.jce.provider.BouncyCastleProvider.
###  **Solution**
La solution est en fait très simple comme détaillée ci-dessous.

1.  Téléchargez n'importe quelle version majeure de[Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. Extrayez l'archive téléchargée et accédez au répertoire \JDK 1.6\aspose-cells-xx0-java\lib.
1. Référencez le bcprov-jdk16-146.jar dans le chemin de classe du projet.

Alternativement, vous pouvez ajouter la dépendance dans le pom.xml et laisser le projet résoudre la dépendance via maven.

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

