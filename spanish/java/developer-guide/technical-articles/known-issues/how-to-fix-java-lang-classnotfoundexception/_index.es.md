---
title: Cómo solucionar java.lang.ClassNotFoundException
type: docs
weight: 30
url: /es/java/how-to-fix-java-lang-classnotfoundexception/ 
description: Aprende cómo solucionar java.lang.ClassNotFoundException en el Aspose.Cells for Java.
keywords: Cómo solucionar ClassNotFoundException de BouncyCastleProvider en Java, Solucionar la excepción de BouncyCastleProvider usando Java, Resolver ClassNotFoundException de BouncyCastleProvider en Java.
---

Aspose.Cells for Java API depende de algunas bibliotecas adicionales, si faltan, puede producirse una excepción como "java.lang.ClassNotFoundException".
Este artículo enumera ese tipo de excepciones y explica qué bibliotecas se instalan para resolverlas.

## Cómo solucionar ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider
### **Resumen**
La API Aspose.Cells for Java depende de Bouncy Castle para funciones de cifrado y descifrado, es decir, si el programa necesita cargar o guardar hojas de cálculo cifradas, es necesario agregar una referencia de bcprov-jdk16-146.jar en la ruta de clases del proyecto.
### **Síntomas**
Puede obtener la java.lang.ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider. 
### **Solución**
La solución es en realidad muy simple como se detalla a continuación.

1. Descargue cualquier versión importante de [Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. Extraiga el archivo descargado y vaya al directorio \JDK 1.6\aspose-cells-x.x.0-java\lib.
1. Referencie el bcprov-jdk16-146.jar en la ruta de clases del proyecto.

Alternativamente, puede agregar la dependencia en el pom.xml y permitir que el proyecto resuelva la dependencia a través de maven.

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
