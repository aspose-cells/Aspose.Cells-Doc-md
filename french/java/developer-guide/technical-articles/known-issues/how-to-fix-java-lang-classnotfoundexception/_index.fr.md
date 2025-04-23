---
title: Comment résoudre java.lang.ClassNotFoundException
type: docs
weight: 30
url: /fr/java/how-to-fix-java-lang-classnotfoundexception/ 
description: Découvrez comment résoudre java.lang.ClassNotFoundException dans le Aspose.Cells for Java.
keywords: Comment résoudre BouncyCastleProvider ClassNotFoundException en Java, Résoudre l exception BouncyCastleProvider en utilisant Java, Java résout ClassNotFoundException BouncyCastleProvider.
---

API Aspose.Cells for Java dépend de certaines bibliothèques supplémentaires, si elles sont manquantes, une exception peut être déclenchée sous la forme de "java.lang.ClassNotFoundException".
Cet article répertorie ce type d'exceptions et explique quelles bibliothèques sont installées pour les résoudre.

## Comment résoudre ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider
### **Résumé**
L'API Aspose.Cells for Java dépend de Bouncy Castle pour les fonctionnalités de chiffrement et de déchiffrement, c'est-à-dire que si le programme doit charger ou enregistrer des feuilles de calcul chiffrées, il est nécessaire d'ajouter une référence à bcprov-jdk16-146.jar dans le chemin de classe du projet.
### **Symptômes**
Vous pouvez rencontrer java.lang.ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider. 
### **Solution**
La solution est en fait très simple comme indiqué ci-dessous.

1. Téléchargez une version majeure de [Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. Extrayez l'archive téléchargée et accédez au répertoire \JDK 1.6\aspose-cells-x.x.0-java\lib.
1. Faites référence à bcprov-jdk16-146.jar dans le chemin de classe du projet.

Alternativement, vous pouvez ajouter la dépendance dans le fichier pom.xml et laisser le projet résoudre la dépendance via maven.

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
