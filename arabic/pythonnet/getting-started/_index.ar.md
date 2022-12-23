---
title: ابدء
linktitle: ابدء
type: docs
weight: 4
url: /ar/python-net/getting-started/ 
keywords: python, excel, instal
description: إعداد Aspose.Cells for Python via .NET وإرشادات التثبيت.
---
## **متطلبات النظام**
 Aspose.Cells for Python via .NET مستقل عن النظام الأساسي API ويمكن استخدامه على أي منصة (Windows و Linux) حيث[Python](https://www.python.org/downloads/) تم تنصيبه.

## **إصدار Python**
- Python 3.6 أو أعلى

## **التركيب**
### **Windows:**
 يمكنك بسهولة استخدام Aspose.Cells for Python via .NET من[بايبي](https://pypi.org/project/aspose-cells-python/) بالأمر التالي.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

### **لينكس:**
 يمكنك بسهولة استخدام Aspose.Cells for Python via .NET من[بايبي](https://pypi.org/project/aspose-cells-python/) بالأمر التالي.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

### **نظام التشغيل MacOS:**
 يمكنك بسهولة استخدام Aspose.Cells for Python via .NET من[بايبي](https://pypi.org/project/aspose-cells-python/) بالأمر التالي.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- ملاحظة: إذا كان python الخاص بك هو Python3.7 (خذ python3.7 ، على سبيل المثال ، هنا) ، بعد تثبيت aspose-cells-python ، قد تكون هناك الأخطاء التالية
 موجه "/usr/local/lib/libpython3.7m.dylib" (لا يوجد مثل هذا الملف) ، موجه "/usr/lib/libpython3.7m.dylib" (لا يوجد مثل هذا الملف).
 في مثل هذه الحالة ، يرجى إضافة الأمر التالي إلى ملفك bash_profile (ابحث عن مكان libpython3.7m.dylib أولاً ، خذ /Library/Frameworks/Python.framework/Versions/3.7/lib
 على سبيل المثال هنا)
{{< highlight "NET" >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}
## **إنشاء تطبيق Hello World**

-  قم بإنشاء ملف باسم**إنشاءHelloWorldFile.py** واستخدم نموذج التعليمات البرمجية التالي:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- الآن احفظ الكود أعلاه في "CreatingHelloWorldFile.py" وقم بتشغيل "python CreatingHelloWorldFile.py"command موجه.

