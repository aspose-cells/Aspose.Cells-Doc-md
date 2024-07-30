---
title: Установка
type: docs
weight: 20
url: /ru/java/installation/
---

## **Установка Aspose.Cells for Java из репозитория Maven**

Aspose размещает все Java API на [репозитории Maven](https://releases.aspose.com/java/repo/). Вы можете легко использовать [Aspose.Cells for Java API](https://releases.aspose.com/cells/java/) непосредственно в ваших проектах Maven с помощью простых конфигураций.

Сначала вам необходимо указать конфигурацию/местоположение репозитория Aspose Maven в своем файле pom.xml Maven, как показано ниже:

{{< highlight java >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>https://releases.aspose.com/java/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

для Gradle в вашем скрипте build.gradle, как показано ниже:
{{< highlight java >}}
//Add Aspose maven repository
repositories {
    mavenCentral()
    maven {
        url "https://releases.aspose.com/java/repo/"
    }
}
{{< /highlight >}}

Затем определите зависимость API Aspose.Cells for Java в вашем файле pom.xml, как показано ниже (Это включит все, например основной файл jar, Java Docs и другие библиотеки соответственно):

{{< highlight java >}}

     <dependencies>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>24.7</version>

        </dependency>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>24.7</version>

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

Поздравляем! Вы успешно определили зависимость Maven Aspose.Cells for Java в своем проекте Maven.

## **Загрузка изображений в формате WebP**

WebP - современный формат изображений, разработанный для создания файлов меньшего размера при сохранении высокого качества изображения.

В настоящее время в Microsoft Excel нельзя напрямую вставлять изображения в формате WebP. Однако существуют случаи, когда изображения в формате WebP могут быть вставлены в исходные файлы Excel непосредственно с использованием некоторых библиотек от сторонних разработчиков.

В общем, для загрузки растровых изображений Aspose.Cells for Java использует Java's ImageIO, но на данный момент сам JDK не поддерживает загрузку изображений в формате WebP. Для загрузки изображений в формате WebP с использованием Java's ImageIO требуются дополнительные плагины или расширения (например, плагин [imageio-webp](https://mvnrepository.com/artifact/com.twelvemonkeys.imageio/imageio-webp)).

## **Поддержка**

Пожалуйста, проверьте следующее, чтобы получить быструю техническую поддержку

[Aspose.Cells - Форумы](https://forum.aspose.com/c/cells/9)
