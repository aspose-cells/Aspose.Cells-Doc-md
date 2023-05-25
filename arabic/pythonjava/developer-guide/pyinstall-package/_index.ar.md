---
title: استخدام PyInstaller لتوزيع تطبيقات Python بسهولة
linktitle: الحزمة باستخدام Pyinstaller
type: docs
weight: 10
url: /ar/python-java/pyinstaller-python/
description: حزمة كود python إلى exe عبر pyinstaller.
---
##  **ما هو استخدام PyInstaller؟**
يقرأ PyInstaller Python نصًا كتبته أنت. يقوم بتحليل التعليمات البرمجية الخاصة بك لاكتشاف كل وحدة ومكتبة أخرى يحتاجها البرنامج النصي الخاص بك من أجل التنفيذ. ثم يقوم بجمع نسخ من كل هذه الملفات - بما في ذلك مترجم Python النشط!

##  **لماذا تستخدم Pyinstaller لحزمة Python؟**
يستخدم PyInstaller لحزم Python كود في تطبيقات مستقلة قابلة للتنفيذ لأنظمة تشغيل مختلفة. يأخذ Python سكربت وينشئ ملف تنفيذي واحد يحتوي على جميع التبعيات الضرورية ويمكن تشغيله على أجهزة الكمبيوتر التي لم يتم تثبيت Python عليها. وهذا يسمح بسهولة توزيع ونشر Python تطبيقات ، حيث لا يحتاج المستخدم إلى Python وأي وحدات نمطية مطلوبة مثبتة على نظامهم من أجل تشغيل التطبيق. بالإضافة إلى ذلك ، يمكن أيضًا استخدام PyInstaller لإنشاء ملفات تنفيذية ذات ملف واحد ، وهي ملفات فردية قابلة للتنفيذ تحتوي على جميع التبعيات المطلوبة للتطبيق. يمكن أن يسهل هذا توزيع التطبيق ، حيث يحتاج المستخدم فقط إلى تنزيل ملف واحد.

##  **كيفية تثبيت PyInstaller**
 يتوفر PyInstaller كحزمة Python عادية. أرشيفات المصدر للإصدارات التي تم إصدارها متوفرة من[PyPi](https://pypi.org/project/pyinstaller/) ، ولكن من الأسهل تثبيت أحدث إصدار باستخدام[نقطة](https://pip.pypa.io/en/stable/):
{{< highlight "java" >}}

C:\> pip install pyinstaller

{{< /highlight >}}

لترقية تثبيت PyInstaller الحالي إلى أحدث إصدار ، استخدم:
{{< highlight "java" >}}

C:\> pip install --upgrade pyinstaller

{{< /highlight >}}
لتثبيت إصدار التطوير الحالي ، استخدم:
{{< highlight "java" >}}

C:\> pip install https://github.com/pyinstaller/pyinstaller/tarball/

{{< /highlight >}}

##  **كيف أقوم بإنشاء EXE باستخدام PyInstaller**
 سنأخذ ملف python واحد كمثال لشرح خطوات التغليف بالتفصيل ، خذ Python 3.11.0 كمثال بعد التثبيت[aspose.cells](https://pypi.org/project/aspose-cells/).

1.  قم بإنشاء ملف عينة Python باسم[example.py](example.py).
{{< highlight "java" >}}

import os
from jpype import *

__cells_jar_dir__ = os.path.dirname(__file__)
addClassPath(os.path.join(__cells_jar_dir__, "aspose-cells-23.1.jar"))
addClassPath(os.path.join(__cells_jar_dir__, "bcprov-jdk15on-160.jar"))
addClassPath(os.path.join(__cells_jar_dir__, "bcpkix-jdk15on-1.60.jar"))
addClassPath(os.path.join(__cells_jar_dir__, "JavaClassBridge.jar"))

import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, FileFormatType, CellsHelper

print(CellsHelper.getVersion())
workbook = Workbook(FileFormatType.XLSX)
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Hello World")
workbook.save("output.xlsx")

jpype.shutdownJVM()

{{< /highlight >}}
1. أنشئ مجلدًا باسم c: \ app ، وانسخ example.py (مرفق) إلى c: \ app.
1. افتح موجه الأوامر الخاص بك وقم بتشغيل الأمر pyinstaller example.py.
{{< highlight "java" >}}

C:\app> pyinstaller example.py

{{< /highlight >}}
1. انسخ البرطمانات (aspose-cells-xxx.jar، bcprov-jdk15on-160.jar، bcpkix-jdk15on-1.60.jar، JavaClassBridge.jar. وهي موجودة في المجلد C: \ Python311 \ Lib \ site -pack \ asposecells \ lib ) إلى c: \ app.
1.  قم بتحرير الملف بلاحقة المواصفات لإضافة قسم البيانات مثل[example.spec](example.spec).
![ما يجب القيام به: image_alt_text](example.png)
1. قم بتشغيل pyinstaller example.spec في نافذة موجه الأوامر.
{{< highlight "java" >}}

C:\app> pyinstaller example.spec

{{< /highlight >}}
1. قم بتبديل الدليل إلى C: \ app \ dist \ example ، وستجد ملف example.exe.
