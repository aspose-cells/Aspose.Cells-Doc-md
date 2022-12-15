---
title: Как исправить исключение java.lang.ClassNotFoundException
type: docs
weight: 30
url: /ru/java/how-to-fix-java-lang-classnotfoundexception/ 
---
Aspose.Cells for Java API зависит от некоторых дополнительных библиотек, если они отсутствуют, может быть выдано исключение в виде "java.lang.ClassNotFoundException".
В этой статье перечислены такие исключения и объясняется, какие библиотеки установлены для их устранения.

## Как исправить ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider
### **Резюме**
Aspose.Cells for Java API зависит от Bouncy Castle для функций шифрования и дешифрования, то есть, если программе требуется загружать или сохранять зашифрованные электронные таблицы, необходимо добавить ссылку bcprov-jdk16-146.jar в путь к классам проекта.
### **Симптомы**
 Вы можете получить исключение java.lang.ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider.
### **Решение**
Решение на самом деле очень простое, как описано ниже.

1. Загрузите любой основной выпуск[Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. Извлеките загруженный архив и перейдите в каталог \JDK 1.6\aspose-cells-xx0-java\lib.
1. Ссылка на bcprov-jdk16-146.jar в пути к классам проекта.

В качестве альтернативы вы можете добавить зависимость в pom.xml и позволить проекту разрешить зависимость через maven.

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

