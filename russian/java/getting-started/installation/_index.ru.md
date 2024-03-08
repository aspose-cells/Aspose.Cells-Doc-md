---
title: Installation
type: docs
weight: 20
url: /ru/java/installation/
---
##  **Установка Aspose.Cells for Java из репозитория Maven**

Aspose содержит все API Java.[Maven хранилище](https://releases.aspose.com/java/repo/) . Вы можете легко использовать[Aspose.Cells for Java API](https://releases.aspose.com/cells/java/) прямо в ваших проектах Maven с простыми конфигурациями.

Сначала вам нужно указать конфигурацию/расположение репозитория Aspose Maven в вашем pom.xml Maven, как показано ниже:

{{< highlight "java" >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>https://releases.aspose.com/java/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

для Gradle в вашем скрипте build.gradle следующим образом:
{{< highlight "java" >}}
//Add Aspose maven repository
repositories {
    mavenCentral()
    maven {
        url "https://releases.aspose.com/java/repo/"
    }
}
{{< /highlight >}}

Затем определите зависимость Aspose.Cells for Java API в вашем pom.xml следующим образом (это будет включать в себя все, например, основной файл jar, Java Docs и другие библиотеки соответственно):

{{< highlight "java" >}}

     <dependencies>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>24.2</version>

        </dependency>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>24.2</version>

            <classifier>javadoc</classifier>

        </dependency>

        <dependency>

            <groupId>org.bouncycastle</groupId>

            <artifactId>bcprov-jdk15on</artifactId>

            <version>1.68</version>

        </dependency>        

        <dependency>

            <groupId>org.bouncycastle</groupId>

            <artifactId>bcpkix-jdk15on</artifactId>

            <version>1.68</version>

        </dependency>        

    </dependencies>

{{< /highlight >}}

Поздравляем! Вы успешно определили зависимость Aspose.Cells for Java Maven в своем проекте Maven.

##  **Поддерживать**

Пожалуйста, проверьте следующее, чтобы получить быструю техническую поддержку

[Aspose.Cells - Форумы](https://forum.aspose.com/c/cells/9)
