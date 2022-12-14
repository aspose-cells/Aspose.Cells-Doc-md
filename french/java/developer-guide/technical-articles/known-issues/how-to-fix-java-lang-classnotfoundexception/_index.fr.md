---
title: Comment réparer java.lang.ClassNotFoundException
type: docs
weight: 30
url: /fr/java/how-to-fix-java-lang-classnotfoundexception/ 
---
Aspose.Cells for Java API dépend de certaines bibliothèques supplémentaires, si elles sont manquantes, une exception peut être levée comme "java.lang.ClassNotFoundException".
Cet article répertorie ce type d'exceptions et explique quelles bibliothèques sont installées pour les résoudre.

## Comment réparer ClassNotFoundException : org.bouncycastle.jce.provider.BouncyCastleProvider
### **Sommaire**
Aspose.Cells for Java API dépend de Bouncy Castle pour les fonctionnalités de chiffrement et de déchiffrement, c'est-à-dire que si le programme doit charger ou enregistrer des feuilles de calcul chiffrées, il est nécessaire d'ajouter la référence de bcprov-jdk16-146.jar dans le chemin de classe du projet.
### **Les symptômes**
 Vous pouvez obtenir l'exception java.lang.ClassNotFoundException : org.bouncycastle.jce.provider.BouncyCastleProvider.
### **La solution**
La solution est en fait très simple comme détaillé ci-dessous.

1. Téléchargez n'importe quelle version majeure de[Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. Extrayez l'archive téléchargée et accédez au répertoire \JDK 1.6\aspose-cells-xx0-java\lib.
1. Référencez le fichier bcprov-jdk16-146.jar dans le chemin d'accès aux classes du projet.

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

