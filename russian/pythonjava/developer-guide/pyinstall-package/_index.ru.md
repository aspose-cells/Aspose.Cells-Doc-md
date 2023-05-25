---
title: Использование PyInstaller для простого распространения приложений Python
linktitle: Пакет с использованием Pyinstaller
type: docs
weight: 10
url: /ru/python-java/pyinstaller-python/
description: Упакуйте код Python в exe через pyinstaller.
---
##  **Для чего используется PyInstaller?**
PyInstaller читает написанный вами скрипт Python. Он анализирует ваш код, чтобы обнаружить все остальные модули и библиотеки, необходимые вашему сценарию для выполнения. Затем он собирает копии всех этих файлов, включая активный интерпретатор Python!

##  **Зачем использовать Pyinstaller для пакета Python?**
PyInstaller используется для упаковки кода Python в автономные исполняемые приложения для различных операционных систем. Он берет сценарий Python и генерирует один исполняемый файл, который содержит все необходимые зависимости и может быть запущен на компьютерах, на которых не установлен Python. Это позволяет легко распространять и развертывать приложения Python, поскольку пользователю не нужно устанавливать Python и любые необходимые модули в своей системе для запуска приложения. Кроме того, PyInstaller также можно использовать для создания однофайловых исполняемых файлов, которые представляют собой отдельные исполняемые файлы, содержащие все необходимые зависимости для приложения. Это может еще больше упростить распространение приложения, поскольку пользователю нужно загрузить только один файл.

##  **Как установить PyInstaller**
 PyInstaller доступен как обычный пакет Python. Исходные архивы выпущенных версий доступны по адресу[ПиПи](https://pypi.org/project/pyinstaller/) , но проще установить последнюю версию с помощью[точка](https://pip.pypa.io/en/stable/):
{{< highlight "java" >}}

C:\> pip install pyinstaller

{{< /highlight >}}

Чтобы обновить существующую установку PyInstaller до последней версии, используйте:
{{< highlight "java" >}}

C:\> pip install --upgrade pyinstaller

{{< /highlight >}}
Чтобы установить текущую версию разработки, используйте:
{{< highlight "java" >}}

C:\> pip install https://github.com/pyinstaller/pyinstaller/tarball/

{{< /highlight >}}

##  **Как создать EXE с помощью PyInstaller**
 Мы возьмем один файл Python в качестве примера, чтобы подробно объяснить шаги упаковки. Возьмем Python 3.11.0 в качестве примера после установки.[aspose.cells](https://pypi.org/project/aspose-cells/).

1.  Создайте файл примера Python с именем[пример.py](example.py).
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
1. Создайте папку как c:\app и скопируйте example.py(прилагается) в c:\app.
1. Откройте командную строку и запустите команду pyinstaller example.py.
{{< highlight "java" >}}

C:\app> pyinstaller example.py

{{< /highlight >}}
1. Скопируйте файлы jar(aspose-cells-xxx.jar, bcprov-jdk15on-160.jar, bcpkix-jdk15on-1.60.jar, JavaClassBridge.jar. Они находятся в папке C:\Python311\Lib\site-packages\asposecells\lib ) в c:\app.
1.  Отредактируйте файл с суффиксом спецификации, чтобы добавить раздел данных, например[пример.spec](example.spec).
![дело:image_alt_text](example.png)
1. Запустите pyinstaller example.spec в окне командной строки.
{{< highlight "java" >}}

C:\app> pyinstaller example.spec

{{< /highlight >}}
1. Перейдите в каталог C:\app\dist\example, и вы найдете файл example.exe.
