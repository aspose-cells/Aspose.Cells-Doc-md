---
title: كيفية تشغيل Aspose.Cells for Java في Docker
type: docs
description: "تشغيل Aspose.Cells for Java في حاوية Docker لنظام Linux."
weight: 139
url: /ar/java/how-to-run-aspose-cells-in-docker/
---

تجعل الخدمات الصغيرة، بالتزامن مع تحتوين الحاويات، من الممكن الجمع بسهولة بين التقنيات. يتيح لك Docker دمج وظائف Aspose.Cells بسهولة في تطبيقك، بغض النظر عن التقنية المستخدمة في مكدس التطوير الخاص بك.

في حالة استهدافك للخدمات الصغيرة المتنقلة، أو إذا كانت التكنولوجيا الرئيسية في ستاك البرمجيات الخاص بك ليست .NET أو C++ أو Java، لكنك بحاجة إلى وظائف Aspose.Cells، أو إذا كنت تستخدم بالفعل Docker في ستاك برمجياتك، فقد تكون مهتمًا بالاستفادة من Aspose.Cells for Java في حاوية Docker.

## متطلبات قبلية

- يجب تثبيت Docker على نظامك. 

## إنشاء تطبيق Java

في هذا المثال، ستقوم بإنشاء تطبيق Java ينشئ ملف xlsx بسيط، يحفظه ويقرأه. يمكن بناء التطبيق ثم تشغيله في Docker.

### إنشاء تطبيق الجافا

قم بإنشاء تطبيق الجافا في Eclipse باستخدام الكود التالي. في هذا المثال، نستخدم Aspose.Cells for Java لإنشاء ورقة عمل xlsx جديدة وتعيين اسم الورقة وقيم الخلية الخاصة بها، ثم قراءتها وطباعتها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "TestDocker.java" >}}

### تحويل تطبيق الجافا إلى ملف jar

تظهر الشكل التالي وسيلة لتحويل تطبيق jar باستخدام قائمة "Export" في Eclipse.

**![إنشاء ملف Jar باستخدام Eclipse](MakeJar.png)**

الآن بعد أن قمنا بكتابة برنامج Java باستخدام Aspose.Cells for Java، حصلنا على ملف jar. الخطوة التالية هي إنشاء ملف dockerfile.

### تكوين ملف Dockerfile

الخطوة التالية هي إنشاء وتكوين ملف Dockerfile.

1. قم بإنشاء ملف Dockerfile وضعه بجوار ملف الـ jar. احتفظ باسم هذا الملف بدون امتداد (الافتراضي).
2. في ملف Dockerfile، حدد:

{{< highlight plain >}}
   FROM williamyeh/java8:latest

   VOLUME /tmp

   ADD TestDocker.jar app.jar

   ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]
{{< /highlight >}}

### بناء وتشغيل التطبيق في Docker

الآن يمكن بناء التطبيق وتشغيله في Docker. افتح موجه الأوامر المفضلة لديك، غير الدليل إلى المجلد الذي يحتوي على ملف Dockerfile وقم بتشغيل الأمر التالي:

{{< highlight plain >}}
docker build -t java-app .
{{< /highlight >}}

بعد تنفيذ الأمر أعلاه، ستحصل على نتيجة ورقة العمل XLSX ونتيجة سطر الأوامر. في هذه النقطة، تم تشغيل برنامج Java بنجاح في Docker على نظام Linux.
