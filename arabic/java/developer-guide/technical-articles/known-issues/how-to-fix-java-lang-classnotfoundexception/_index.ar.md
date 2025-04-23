---
title: كيفية إصلاح java.lang.ClassNotFoundException
type: docs
weight: 30
url: /ar/java/how-to-fix-java-lang-classnotfoundexception/ 
description: تعلم كيفية إصلاح java.lang.ClassNotFoundException في Aspose.Cells for Java.
keywords: كيفية إصلاح فئة الاستثناء BouncyCastleProvider ClassNotFoundException في جافا، حل مشكلة BouncyCastleProvider باستخدام جافا، جافا حل ClassNotFoundException BouncyCastleProvider.
---

Aspose.Cells for Java API تعتمد على بعض المكتبات الإضافية، إذا كانت مفقودة، فقد يتم طرح استثناء مثل "java.lang.ClassNotFoundException".
يعرض هذا المقال مثل هذا النوع من الاستثناءات ويشرح الفئات التي يتم تثبيتها لحلها.

## كيفية إصلاح ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider
### **ملخص**
Aspose.Cells for Java API يعتمد على Bouncy Castle لميزات التشفير والفك التشفير، أي أنه إذا كان من الضروري للبرنامج تحميل أو حفظ جداول بيانات مشفرة، فيجب إضافة إشارة لـ bcprov-jdk16-146.jar في مسار الفئات للمشروع.
### **الأعراض**
قد تحصل على java.lang.ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider. 
### **الحل**
الحل في الواقع بسيط جدًا كما هو موضح أدناه.

1. قم بتنزيل أي إصدار رئيسي من [Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. استخرج الأرشيف المُنزَّل وتصفح إلى مجلد \JDK 1.6\aspose-cells-x.x.0-java\lib.
1. قم بإضافة مرجع bcprov-jdk16-146.jar في مسار الفئات للمشروع.

بدلاً من ذلك، يمكنك إضافة التبعية في ملف pom.xml والسماح للمشروع بحل التبعية عبر maven.

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
