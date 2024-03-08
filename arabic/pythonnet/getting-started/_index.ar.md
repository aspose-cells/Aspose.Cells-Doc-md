---
title: ابدء
linktitle: ابدء
type: docs
weight: 4
url: /ar/python-net/getting-started/
description: تعرف على كيفية تثبيت Aspose.Cells for Python via .NET وإنشاء تطبيق Hello World.
keywords: How to install Aspose.Cells for Python via .NET in Windows Linux and MacOS, installation guidelines for Aspose.Cells for Python via .NET, Python Via .NET Hello World program. 
---
##  **متطلبات النظام**
 Aspose.Cells for Python via .NET مستقل عن النظام الأساسي API ويمكن استخدامه على أي نظام أساسي (Windows وLinux) حيث[Python](https://www.python.org/downloads/) تم تنصيبه.

##  **نسخة Python**
- Python 3.6 أو أعلى

##  **تثبيت**
###  **Windows:**
 يمكنك بسهولة استخدام Aspose.Cells for Python via .NET من[pypi](https://pypi.org/project/aspose-cells-python/) مع الأمر التالي.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

###  **لينكس:**
 يمكنك بسهولة استخدام Aspose.Cells for Python via .NET من[pypi](https://pypi.org/project/aspose-cells-python/) مع الأمر التالي.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- ملاحظة: تحتاج إلى تشغيل الأمر التالي قبل التثبيت
{{< highlight "NET" >}}
For Ubuntu/Debian: apt-get install libgdiplus 
For CentOS/RHEL/Fedora: yum install libgdiplus 
{{< /highlight >}}

###  **ماك:**
 يمكنك بسهولة استخدام Aspose.Cells for Python via .NET من[pypi](https://pypi.org/project/aspose-cells-python/) مع الأمر التالي.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- ملاحظة: إذا كان بايثون الخاص بك هو Python3.7 (خذ python3.7، على سبيل المثال، هنا)، بعد تثبيت aspose-cells-python، قد تكون هناك الأخطاء التالية
 موجه "/usr/local/lib/libpython3.7m.dylib" (لا يوجد مثل هذا الملف)، "/usr/lib/libpython3.7m.dylib" (لا يوجد مثل هذا الملف).
 في مثل هذه الحالة، يرجى إضافة الأمر التالي إلى ملف bash_profile الخاص بك (ابحث عن مكان libpython3.7m.dylib أولاً، خذ /Library/Frameworks/Python.framework/Versions/3.7/lib
 مثلا هنا)
{{< highlight "NET" >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}

- ملحوظة:نظرًا لاعتمادنا على مكتبة الرسومات SkiaSharp، إذا واجهت الخطأ التالي:
**System.DllNotFoundException: غير قادر على تحميل المكتبة المشتركة 'libSkiaSharp' أو أحد تبعياتها.** الرجاء تثبيت SkiaSharp.
{{< highlight "NET" >}}
brew  install nuget
nuget install SkiaSharp.NativeAssets.macOS -Version 2.88.3
{{< /highlight >}}
 بعد التثبيت، الرجاء تشغيل الأمر التالي
{{< highlight "NET" >}}
cp ./SkiaSharp.NativeAssets.macOS.2.88.3/runtimes/osx/native/libSkiaSharp.dylib /usr/local/lib/.
{{< /highlight >}}

 وبطبيعة الحال، إذا كنت تريد أن يكون الأمر أكثر بساطة، يمكنك أيضا تحميله[libSkiaSharp.dylib](libSkiaSharp.dylib) وثم**ينسخ** ذلك إلى**/usr/local/lib** الدليل.

##  **كيفية إنشاء تطبيق Hello World باستخدام Aspose.Cells for Python via .NET**

-  قم بإنشاء ملف باسم**إنشاءHelloWorldFile.py** واستخدم نموذج التعليمات البرمجية التالي:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- الآن احفظ الكود أعلاه في "CreatingHelloWorldFile.py" وقم بتشغيل "python CreateHelloWorldFile.py" @command موجه.

##  **Python via .NET مثال جيثب**
-  يرجى زيارة[Aspose.Cells for Python via .NET مثال](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET) جيثب لعرض المزيد من نماذج الرموز.


