---
title: التثبيت
type: docs
weight: 20
url: /ar/java/installation/
---

## **تثبيت Aspose.Cells for Java من مستودع Maven**

تستضيف Aspose جميع واجهات برمجة تطبيقات Java على [مستودع Maven](https://releases.aspose.com/java/repo/). يمكنك استخدام [Aspose.Cells for Java API](https://releases.aspose.com/cells/java/) مباشرة في مشاريعك Maven بتكوينات بسيطة.

أولاً، يجب عليك تحديد موقع تكوين / مستودع Aspose Maven في Maven pom.xml الخاص بك كما يلي:

{{< highlight java >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>https://releases.aspose.com/java/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

لـ Gradle في نص build.gradle الخاص بك كما يلي:
{{< highlight java >}}
//Add Aspose maven repository
repositories {
    mavenCentral()
    maven {
        url "https://releases.aspose.com/java/repo/"
    }
}
{{< /highlight >}}

ثم حدد تبعية Aspose.Cells for Java API في pom.xml الخاص بك على النحو التالي (سيتم ذلك بما في ذلك كل شيء، على سبيل المثال، الملف الرئيسي القابل للتطبيق، وثنائيات JavaDocs وغيرها من المكتبات وفقًا لذلك):

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

تهانينا! لقد قمت بتحديد تبعية Aspose.Cells for Java Maven بنجاح في مشروعك Maven.

## **تحميل صورة WebP**

WebP هو تنسيق صور حديث. تم تصميمه لإنتاج أحجام ملفات أصغر، مع الحفاظ على جودة الصورة البصرية العالية.

حالياً، في Microsoft Excel، لا يُسمح بإدراج صور WebP مباشرة. ومع ذلك، هناك حالات يتم فيها إدراج صور WebP في ملفات مصدر Excel مباشرة عن طريق بعض مكتبات الطرف الثالث.

عموماً، يستخدم Aspose.Cells for Java ImageIO لجافا لتحميل الصور النقطية، وحالياً لا يدعم JDK نفسه تحميل صور WebP. يتطلب الأمر بعض الإضافات أو الامتدادات الإضافية (مثل [إضافة imageio-webp](https://mvnrepository.com/artifact/com.twelvemonkeys.imageio/imageio-webp)) لـ ImageIO لجافا لتحميل الصور WebP.

## **الدعم**

يرجى التحقق من ما يلي للحصول على دعم فني سريع

[منتديات Aspose.Cells](https://forum.aspose.com/c/cells/9)
