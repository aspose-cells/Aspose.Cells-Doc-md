---
title: التركيب
type: docs
weight: 20
url: /ar/java/installation/
---
## **تركيب Aspose.Cells for Java من مستودع Maven**

يستضيف Aspose جميع واجهات برمجة تطبيقات Java[مستودع Maven](https://releases.aspose.com/java/repo/) . يمكنك بسهولة استخدام ملفات[Aspose.Cells for Java API](https://releases.aspose.com/cells/java/) مباشرة في مشاريعك Maven ذات التكوينات البسيطة.

أولاً ، تحتاج إلى تحديد تكوين / موقع المستودع Aspose Maven في Maven pom.xml على النحو التالي:

{{< highlight "java" >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>https://releases.aspose.com/java/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

ثم حدد تبعية Aspose.Cells for Java API في ملف pom.xml الخاص بك على النحو التالي (سيشمل ذلك كل شيء ، مثل ملف jar الرئيسي و Java Docs والمكتبات الأخرى وفقًا لذلك):

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

تهانينا! لقد نجحت في تحديد التبعية Aspose.Cells for Java Maven في مشروعك Maven.

## **الدعم**

يرجى التحقق مما يلي للحصول على دعم فني سريع

[Aspose.Cells - المنتديات](https://forum.aspose.com/c/cells/9)
