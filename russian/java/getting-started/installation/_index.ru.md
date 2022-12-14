---
title: Монтаж
type: docs
weight: 20
url: /ru/java/installation/
---
## **Установка Aspose.Cells for Java из репозитория Maven**

Aspose размещает все Java API на[Maven репозиторий](https://releases.aspose.com/java/repo/) . Вы можете легко использовать[Aspose.Cells for Java API](https://releases.aspose.com/cells/java/) непосредственно в ваших проектах Maven с простыми конфигурациями.

Во-первых, вам нужно указать конфигурацию/местоположение репозитория Aspose Maven в вашем Maven pom.xml, как показано ниже:

{{< highlight "java" >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>https://releases.aspose.com/java/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

Затем определите зависимость Aspose.Cells for Java API в вашем pom.xml следующим образом (это будет включать все, например, основной файл jar, документы Java и другие библиотеки соответственно):

{{< highlight "java" >}}

     <dependencies>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>22.12</version>

        </dependency>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>22.12</version>

            <classifier>javadoc</classifier>

        </dependency>

        <dependency>

            <groupId>org.bouncycastle</groupId>

            <artifactId>bcprov-jdk15on</artifactId>

            <version>1.60</version>

        </dependency>        

        <dependency>

            <groupId>org.bouncycastle</groupId>

            <artifactId>bcpkix-jdk15on</artifactId>

            <version>1.60</version>

        </dependency>        

    </dependencies>

{{< /highlight >}}

Поздравляем! Вы успешно определили зависимость Aspose.Cells for Java Maven в своем проекте Maven.

## **Поддерживать**

Пожалуйста, проверьте следующее, чтобы получить быструю техническую поддержку

[Aspose.Cells - Форумы](https://forum.aspose.com/c/cells/9)
