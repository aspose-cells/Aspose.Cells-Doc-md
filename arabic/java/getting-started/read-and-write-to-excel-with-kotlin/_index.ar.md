---
title: قراءة وكتابة إلى إكسل مع كوتلين
type: docs
weight: 189
url: /ar/java/read-and-write-to-excel-with-kotlin/
description: تعلم القراءة والكتابة وتنسيق ملفات إكسل في كوتلين باستخدام Aspose.Cells for Java. يتضمن أمثلة على الصيغ والتنسيقات.
keywords: كوتلين إكسل، Aspose.Cells كوتلين، قراءة إكسل كوتلين، كتابة إكسل كوتلين، صيغ إكسل كوتلين، تنسيق خلية إكسل، إعداد Aspose.Cells.
---

Aspose.Cells for Java هي مكتبة قوية تتيح للمطورين التلاعب بملفات إكسل برمجيًا. على الرغم من أنها مصممة لجاوا، إلا أنها تتكامل بسلاسة مع كوتلين، بفضل التوافق الكامل لكوتلين مع جاوا. يوفر هذا المستند دليلًا خطوة بخطوة للقراءة من وكتابة ملفات إكسل باستخدام كوتلين وAspose.Cells for Java.

## متطلبات قبلية
- تثبيت كوتلين وJDK.
- أداة بناء (Maven أو Gradle) مهيأة لإدارة الاعتمادات.

## إعداد Aspose.Cells في مشروع كوتلين

أضف تبعية Aspose.Cells إلى مشروعك:

### ل Maven (`pom.xml`):
```xml
<repositories>
    <repository>
        <id>AsposeJavaAPI</id>
        <name>Aspose Java API</name>
        <url>https://releases.aspose.com/java/repo/</url>
    </repository>
</repositories>

<dependencies>
    <!-- Aspose.Cells for Java -->
    <dependency>
        <groupId>com.aspose</groupId>
        <artifactId>aspose-cells</artifactId>
        <version>25.2</version>
    </dependency>

    <!-- Mandatory Bouncy Castle Libraries -->
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
```
### ل Gradle (`build.gradle.kts`):
```kotlin
repositories {
    maven { url = uri("https://releases.aspose.com/java/repo/") }
}

dependencies {
    // Aspose.Cells for Java
    implementation("com.aspose:aspose-cells:25.2")

    // Mandatory Bouncy Castle Libraries
    implementation("org.bouncycastle:bcprov-jdk15on:1.68")
    implementation("org.bouncycastle:bcpkix-jdk15on:1.68")
}
```
## الكتابة إلى إكسل

يوضح هذا المثال كيفية إنشاء مصنف إكسل جديد، ملء الخلايا بالبيانات، وحفظ الملف على القرص.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-WriteToExcel.kt" >}}

## القراءة من إكسل

يرى هذا المثال كيف يتم تحميل ملف إكسل موجود، قراءة قيم الخلايا، وطباعة النتائج.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-ReadFromExcel.kt" >}}

## عمليات متقدمة

### التعامل مع الصيغ

يضيف هذا المثال صيغة (`SUM`) إلى خلية، يعيد حساب المصنف، ويطبع النتيجة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-HandleFormulas.kt" >}}

### تنسيق الخلايا

يطبق هذا المثال تنسيقًا (نص غامق، لون أحمر، ومحاذاة في الوسط) على خلية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-FormatCells.kt" >}}

{{< app/cells/assistant language="java" >}}
