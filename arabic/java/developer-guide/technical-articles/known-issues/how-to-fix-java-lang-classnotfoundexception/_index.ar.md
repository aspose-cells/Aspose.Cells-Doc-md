---
title: كيفية إصلاح java.lang.ClassNotFoundException
type: docs
weight: 30
url: /ar/java/how-to-fix-java-lang-classnotfoundexception/ 
---
Aspose.Cells for Java API يعتمد على بعض المكتبات الإضافية ، إذا كانت مفقودة ، فقد يتم طرح استثناء باسم "java.lang.ClassNotFoundException".
تسرد هذه المقالة هذا النوع من الاستثناءات وتوضح المكتبات المثبتة لحلها.

## كيفية إصلاح ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider
### **ملخص**
Aspose.Cells for Java API يعتمد على Bouncy Castle لميزات التشفير وفك التشفير ، أي إذا كان البرنامج مطلوبًا لتحميل أو حفظ جداول البيانات المشفرة ، فيجب إضافة مرجع bcprov-jdk16-146.jar في مسار فئة المشروع.
### **أعراض**
 يمكنك الحصول على java.lang.ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider.
### **المحلول**
الحل في الواقع بسيط للغاية كما هو مفصل أدناه.

1. قم بتنزيل أي إصدار رئيسي من[Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. قم باستخراج الأرشيف الذي تم تنزيله واستعرض وصولاً إلى دليل \ JDK 1.6 \ aspose-cells-xx0-java \ lib.
1. ارجع إلى bcprov-jdk16-146.jar في مسار الفصل الدراسي للمشروع.

بدلاً من ذلك ، يمكنك إضافة التبعية في ملف pom.xml والسماح للمشروع بحل التبعية عبر maven.

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

