---
title: Installation
type: docs
weight: 20
url: /ar/java/installation/
---
##  **تثبيت Aspose.Cells for Java من مستودع Maven**

Aspose يستضيف جميع واجهات برمجة التطبيقات Java[مستودع Maven](https://releases.aspose.com/java/repo/) . يمكنك استخدامها بسهولة[Aspose.Cells for Java API](https://releases.aspose.com/cells/java/) مباشرة في مشاريعك Maven بتكوينات بسيطة.

أولاً، تحتاج إلى تحديد Aspose Maven تكوين/موقع المستودع في Maven pom.xml الخاص بك على النحو التالي:

{{< highlight "java" >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>https://releases.aspose.com/java/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

لـ Gradle في البرنامج النصي build.gradle الخاص بك على النحو التالي:
{{< highlight "java" >}}
//Add Aspose maven repository
repositories {
    mavenCentral()
    maven {
        url "https://releases.aspose.com/java/repo/"
    }
}
{{< /highlight >}}

ثم قم بتعريف التبعية Aspose.Cells for Java API في pom.xml الخاص بك على النحو التالي (سيشمل هذا كل شيء، على سبيل المثال ملف jar الرئيسي، Java Docs، والمكتبات الأخرى وفقًا لذلك):

{{< highlight "java" >}}

     <dependencies>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>23.12</version>

        </dependency>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>23.12</version>

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

تهانينا! لقد نجحت في تحديد التبعية Aspose.Cells for Java Maven في مشروعك Maven.

##  **يدعم**

يرجى التحقق مما يلي للحصول على الدعم الفني السريع

[Aspose.Cells - المنتديات](https://forum.aspose.com/c/cells/9)
