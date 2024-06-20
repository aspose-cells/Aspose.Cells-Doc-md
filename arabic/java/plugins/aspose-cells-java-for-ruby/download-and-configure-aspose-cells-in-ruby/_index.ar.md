---
title: تنزيل وتكوين Aspose.Cells في Ruby
type: docs
weight: 10
url: /ar/java/download-and-configure-aspose-cells-in-ruby/
---

## **تحميل المكتبات المطلوبة**
قم بتنزيل المكتبات المطلوبة المذكورة أدناه. هذه المكتبات مطلوبة لتنفيذ أمثلة Aspose.Cells Java لـ Ruby.

- [مكون Aspose.Cell لجافا](https://downloads.aspose.com/cells/java/)
## **تحميل الأمثلة من مواقع الترميز الاجتماعي**
الإصدارات التالية لأمثلة تشغيل متوفرة للتنزيل على المواقع التالية المذكورة أدناه:

**GitHub**

- [Aspose.Cells Java for Ruby](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)
## **التثبيت**
من السهل جداً وبسيط تثبيت Aspose.cells Java لـ Ruby gem، يرجى اتباع هذه الخطوات البسيطة:

1. قم بإضافة هذا السطر إلى ملف Gemfile لتطبيقك. 

{{< highlight java >}}

 gem 'aspose-cellsjava'

{{< /highlight >}}

1. ثم قم بتنفيذ 

{{< highlight java >}}

 $ bundle

{{< /highlight >}}

**أو**

1. قم بتشغيل الأمر التالي. 

{{< highlight java >}}

 $ gem install aspose-cellsjava

{{< /highlight >}}
## **استخدام**
يجب تضمين الملفات المطلوبة للعمل مع مثال helloworld.

{{< highlight java >}}

 require require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-cellsjava'

include Asposecellsjava

include Asposecellsjava::HelloWorld

initialize_aspose_cells

{{< /highlight >}}

دعونا نفهم الشيفرة أعلاه.

1. السطر الأول يتأكد من أن مكتبة aspose cells محملة ومتوفرة.
1. قم بتضمين الملفات المطلوبة للوصول إلى aspose cells.
1. قم بتهيئة المكتبات. تتم تحميل فئات aspose JAVA من المسار المُقدم في ملف aspose.yml.
