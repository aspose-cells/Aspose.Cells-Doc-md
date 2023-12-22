---
title: Как исправить java.lang.ClassNotFoundException
type: docs
weight: 30
url: /ru/java/how-to-fix-java-lang-classnotfoundexception/ 
description: Узнайте, как исправить исключение java.lang.ClassNotFoundException в Aspose.Cells for Java.
keywords: How to fix BouncyCastleProvider ClassNotFoundException in Java, Solve BouncyCastleProvider exception using Java, Java solve ClassNotFoundException BouncyCastleProvider.
---
Aspose.Cells for Java API зависит от некоторых дополнительных библиотек, если они отсутствуют, может быть выдано исключение "java.lang.ClassNotFoundException".
В этой статье перечислены такие исключения и объяснено, какие библиотеки установлены для их устранения.

##  Как исправить ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider
###  **Краткое содержание**
Aspose.Cells for Java API зависит от функций шифрования и дешифрования Bouncy Castle, то есть, если программе требуется загружать или сохранять зашифрованные электронные таблицы, необходимо добавить ссылку на bcprov-jdk16-146.jar в путь к классам проекта.
###  **Симптомы**
 Вы можете получить исключение java.lang.ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider.
###  **Решение**
Решение на самом деле очень простое, как описано ниже.

1.  Загрузите любую крупную версию[Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. Распакуйте загруженный архив и перейдите в каталог \JDK 1.6\aspose-cells-xx0-java\lib.
1. Создайте ссылку на bcprov-jdk16-146.jar в пути к классам проекта.

Альтернативно вы можете добавить зависимость в pom.xml и позволить проекту разрешить зависимость через maven.

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

