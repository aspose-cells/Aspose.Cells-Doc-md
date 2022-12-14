---
title: قم بتنزيل وتهيئة Aspose.Cells في Ruby
type: docs
weight: 10
url: /ar/java/download-and-configure-aspose-cells-in-ruby/
---
## **تحميل المكتبات المطلوبة**
تحميل المكتبات المطلوبة المذكورة أدناه. هذه هي المطلوبة لتنفيذ Aspose.Cells Java لأمثلة روبي.

- [Aspose.Cell for Java مكون](https://downloads.aspose.com/cells/java/)
## **تنزيل أمثلة من مواقع الترميز الاجتماعي**
الإصدارات التالية من الأمثلة قيد التشغيل متاحة للتنزيل على مواقع الترميز الاجتماعي المذكورة أدناه:

**جيثب**

- [Aspose.Cells Java لروبي](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)
## **التثبيت**
إنه بسيط للغاية وسهل التثبيت Aspose.cells Java لجوهرة روبي ، يرجى اتباع هذه الخطوات البسيطة:

1.  أضف هذا السطر إلى ملف Gemfile الخاص بتطبيقك.

{{< highlight "java" >}}

 gem 'aspose-cellsjava'

{{< /highlight >}}

1.  ثم نفذ

{{< highlight "java" >}}

 $ bundle

{{< /highlight >}}

**أو**

1.  قم بتشغيل الأمر التالي.

{{< highlight "java" >}}

 $ gem install aspose-cellsjava

{{< /highlight >}}
## **استخدام**
قم بتضمين الملفات المطلوبة للعمل مع مثال helloworld.

{{< highlight "java" >}}

 require require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-cellsjava'

include Asposecellsjava

include Asposecellsjava::HelloWorld

initialize_aspose_cells

{{< /highlight >}}

دعونا نفهم الكود أعلاه.

1. يتأكد السطر الأول من تحميل خلايا الغرض وإتاحتها.
1. قم بتضمين الملفات المطلوبة للوصول إلى خلايا الغرض.
1. تهيئة المكتبات. يتم تحميل فئات aspose JAVA من المسار المتوفر في ملف aspose.yml /
