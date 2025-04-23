---
title: Как исправить java.lang.ClassNotFoundException
type: docs
weight: 30
url: /ru/java/how-to-fix-java-lang-classnotfoundexception/ 
description: Узнайте, как исправить java.lang.ClassNotFoundException в Aspose.Cells for Java.
keywords: Как исправить ошибку ClassNotFoundException BouncyCastleProvider в Java, Решение исключения BouncyCastleProvider с помощью Java, Решение ClassNotFoundException BouncyCastleProvider в Java.
---

API Aspose.Cells for Java зависит от дополнительных библиотек, и если они отсутствуют, может возникнуть исключение "java.lang.ClassNotFoundException".
Эта статья перечисляет такие виды исключений и объясняет, какие библиотеки установлены для их устранения.

## Как исправить ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider
### **Сводка**
API Aspose.Cells for Java зависит от Bouncy Castle для функций шифрования и дешифрования, то есть, если программа требуется загрузить или сохранить зашифрованные электронные таблицы, необходимо добавить ссылку на bcprov-jdk16-146.jar в путь класса проекта.
### **Симптомы**
Вы можете получить java.lang.ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider. 
### **Решение**
Решение очень простое и описано ниже.

1. Скачайте любую основную версию [Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. Извлеките скачанный архив и перейдите в каталог \JDK 1.6\aspose-cells-x.x.0-java\lib.
1. Добавьте ссылку на bcprov-jdk16-146.jar в путь класса проекта.

Кроме того, вы можете добавить зависимость в pom.xml и позволить проекту разрешить зависимость через maven.

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
