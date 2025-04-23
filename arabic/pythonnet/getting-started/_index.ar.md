---
title: البدء
linktitle: البدء
type: docs
weight: 4
url: /ar/python-net/getting-started/
description: تعلم كيفية تثبيت Aspose.Cells for Python via .NET وإنشاء تطبيق Hello World.
keywords: كيفية تثبيت Aspose.Cells for Python via .NET في Windows Linux و MacOS، إرشادات التثبيت لـ Aspose.Cells for Python via .NET، برنامج Hello World باستخدام Python Via .NET. 
---

## **متطلبات النظام**
Aspose.Cells for Python via .NET API غير متوقف عن النظام ويمكن استخدامه على أي نظام (Windows و Linux) حيث يتم تثبيت [Python](https://www.python.org/downloads/). 

## **إصدار Python**
- Python 3.6 أو أحدث

## **التثبيت**
### **Windows:**
يمكنك استخدام Aspose.Cells for Python via .NET بسهولة من [pypi](https://pypi.org/project/aspose-cells-python/) بالأمر التالي.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

### **Linux:**
يمكنك استخدام Aspose.Cells for Python via .NET بسهولة من [pypi](https://pypi.org/project/aspose-cells-python/) بالأمر التالي.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- ملاحظة: يجب عليك تشغيل الأمر التالي قبل التثبيت
{{< highlight NET >}}
For Ubuntu/Debian: apt-get install libgdiplus 
For CentOS/RHEL/Fedora: yum install libgdiplus 
{{< /highlight >}}

### **MacOS:**
يمكنك استخدام Aspose.Cells for Python via .NET بسهولة من [pypi](https://pypi.org/project/aspose-cells-python/) بالأمر التالي.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- ملاحظة: إذا كان Python الخاص بك هو Python3.7 (خذ Python3.7 على سبيل المثال، هنا)، بعد تثبيت aspose-cells-python، قد تظهر الأخطاء التالية
  '/usr/local/lib/libpython3.7m.dylib' (ملف غير موجود), '/usr/lib/libpython3.7m.dylib' (ملف غير موجود) prompt.
  في مثل هذا الوضع، الرجاء إضافة الأمر التالي إلى ملف الـ bash_profile الخاص بك (العثور على مكان ملف libpython3.7m.dylib أولاً، واستخراج /Library/Frameworks/Python.framework/Versions/3.7/lib،
  على سبيل المثال هنا)
{{< highlight NET >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}

- ملاحظة: بسبب اعتمادنا على مكتبة الرسومات SkiaSharp، إذا واجهت الخطأ التالي:
**System.DllNotFoundException: غير قادر على تحميل مكتبة مشتركة 'libSkiaSharp' أو أحد تبعياتها.** يرجى تثبيت SkiaSharp.
{{< highlight NET >}}
brew  install nuget
nuget install SkiaSharp.NativeAssets.macOS -Version 2.88.6
{{< /highlight >}}
بعد التثبيت، يرجى تشغيل الأمر التالي 
{{< highlight NET >}}
cp ./SkiaSharp.NativeAssets.macOS.2.88.6/runtimes/osx/native/libSkiaSharp.dylib /usr/local/lib/.
{{< /highlight >}}

بالطبع، إذا كنت ترغب في ذلك بشكل أبسط، يمكنك أيضًا تنزيل [libSkiaSharp.dylib](libSkiaSharp.dylib) ثم **نسخها** إلى دليل **/usr/local/lib**.

## **كيفية إنشاء تطبيق Hello World باستخدام Aspose.Cells لـ Python via .NET**

- أنشئ ملفًا بإسم **CreatingHelloWorldFile.py** واستخدم الكود المثال التالي:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- الآن قم بحفظ الكود أعلاه في "CreatingHelloWorldFile.py" وقم بتشغيل "python CreatingHelloWorldFile.py" @command prompt.

## **مثال Python via .NET github**
- يرجى زيارة [مثال Aspose.Cells لـ Python via .NET](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET) على github لعرض مزيد من أكواد العينات.


