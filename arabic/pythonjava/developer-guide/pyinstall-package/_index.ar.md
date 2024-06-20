---
title: استخدام PyInstaller لتوزيع تطبيقات Python بسهولة
linktitle: استخدام حزمة بواسطة PyInstaller
type: docs
weight: 10
url: /ar/python-java/pyinstaller-python/
description: تعبئة كود Python لملف تنفيذ exe عبر PyInstaller.
---

## **ما هو استخدام PyInstaller؟**
يقرأ PyInstaller سيناريو Python مكتوب من قبلك. يحلل الكود الخاص بك لاكتشاف كل وحدة أخرى ومكتبة تحتاج إليها لتنفيذ السيناريو. ثم يجمع نسخًا من جميع تلك الملفات - بما في ذلك مفسر Python النشط!

## **لماذا استخدام Pyinstaller لتعبئة Python؟**
يُستخدم PyInstaller لتعبئة كود Python في تطبيقات تنفيذية مستقلة لأنظمة التشغيل المختلفة. يأخذ سيناريو Python ويولد ملف تنفيذي واحد يحتوي على جميع التبعيات اللازمة ويمكن تشغيله على الكمبيوترات التي لا تحتوي على Python مثبت. يسمح هذا بتوزيع ونشر تطبيقات Python بسهولة، حيث لا يحتاج المستخدم إلى تثبيت Python وأي وحدات مطلوبة على نظامه لتشغيل التطبيق. بالإضافة إلى ذلك، يمكن استخدام PyInstaller أيضًا لإنشاء ملفات تنفيذية من نوع واحد، وهي ملفات تنفيذية واحدة تحتوي على جميع التبعيات اللازمة للتطبيق. يمكن أن يجعل هذا الأمر التوزيع التطبيق أسهل، حيث يحتاج المستخدم فقط إلى تنزيل ملف واحد.

## **كيفية تثبيت PyInstaller**
يتوفر PyInstaller كحزمة Python عادية. تتوفر الأرشيفات الأصلية للإصدارات المفرج عنها من [PyPi](https://pypi.org/project/pyinstaller/)، ولكن من الأسهل تثبيت آخر إصدار باستخدام [pip](https://pip.pypa.io/en/stable/):
{{< highlight java >}}

C:\> pip install pyinstaller

{{< /highlight >}}

لترقية تثبيت PyInstaller الحالي إلى آخر إصدار، استخدم:
{{< highlight java >}}

C:\> pip install --upgrade pyinstaller

{{< /highlight >}}
لتثبيت الإصدار التطويري الحالي، استخدم:
{{< highlight java >}}

C:\> pip install https://github.com/pyinstaller/pyinstaller/tarball/

{{< /highlight >}}

## **كيف يمكنني إنشاء ملف exe باستخدام PyInstaller**
سنأخذ ملف Python واحدًا كمثال لشرح خطوات التعبئة بالتفصيل.تأخذ Python 3.11.0 كمثال بعد تثبيت [aspose.cells](https://pypi.org/project/aspose-cells/).

1. قم بإنشاء ملف Python عيني يسمى [example.py](example.py).
{{< highlight java >}}

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
1. قم بإنشاء مجلدًا باسم c:\app، وانسخ example.py المرفق إلى c:\app.
1. افتح موجه الأوامر الخاصة بك وقم بتشغيل أمر pyinstaller example.py.
{{< highlight java >}}

C:\app> pyinstaller example.py

{{< /highlight >}}
1. انسخ الملفات التنفيذية (aspose-cells-xxx.jar, bcprov-jdk15on-160.jar, bcpkix-jdk15on-1.60.jar, JavaClassBridge.jar. يوجد في مجلد C:\Python311\Lib\site-packages\asposecells\lib) إلى c:\app.
1. عدل الملف باسم اللاحقة spec لإضافة قسم البيانات مثل [example.spec](example.spec).
![todo:image_alt_text](example.png)
1. قم بتشغيل pyinstaller example.spec في نافذة موجه الأوامر.
{{< highlight java >}}

C:\app> pyinstaller example.spec

{{< /highlight >}}
1. انتقل إلى الدليل C:\app\dist\example، وستجد ملف example.exe.
