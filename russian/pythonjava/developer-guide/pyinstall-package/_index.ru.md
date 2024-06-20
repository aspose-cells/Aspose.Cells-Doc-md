---
title: Использование PyInstaller для удобного распространения приложений на Python
linktitle: Упаковка с помощью Pyinstaller
type: docs
weight: 10
url: /ru/python-java/pyinstaller-python/
description: Упаковать код Python в exe с помощью pyinstaller.
---

## **Для чего используется PyInstaller?**
PyInstaller читает Python-скрипт, написанный вами. Он анализирует ваш код для определения всех других модулей и библиотек, необходимых для выполнения вашего скрипта. Затем он собирает копии всех этих файлов - включая активный интерпретатор Python!

## **Зачем использовать Pyinstaller для упаковки Python?**
PyInstaller используется для упаковки кода Python в автономные исполняемые приложения для различных операционных систем. Он берет скрипт Python и создает одиночный исполняемый файл, который содержит все необходимые зависимости и может быть запущен на компьютерах, на которых не установлен Python. Это облегчает распространение и развертывание приложений на Python, поскольку пользователю не нужно устанавливать Python и необходимые модули на своей системе для запуска приложения. Кроме того, PyInstaller также может использоваться для создания однофайловых исполняемых файлов, которые представляют собой единый исполняемый файл, содержащий все необходимые зависимости для приложения. Это может сделать распространение приложения еще проще, поскольку пользователю нужно лишь загрузить один файл.

## **Как установить PyInstaller**
PyInstaller доступен как обычный пакет Python. Исходные архивы для выпущенных версий доступны на [PyPi](https://pypi.org/project/pyinstaller/), но установить последнюю версию легче с помощью [pip](https://pip.pypa.io/en/stable/):
{{< highlight java >}}

C:\> pip install pyinstaller

{{< /highlight >}}

Чтобы обновить существующую установку PyInstaller до последней версии, используйте:
{{< highlight java >}}

C:\> pip install --upgrade pyinstaller

{{< /highlight >}}
Чтобы установить текущую версию разработки, используйте:
{{< highlight java >}}

C:\> pip install https://github.com/pyinstaller/pyinstaller/tarball/

{{< /highlight >}}

## **Как создать EXE с помощью PyInstaller**
Мы возьмем один файл Python в качестве примера, чтобы подробно объяснить шаги по упаковке. Возьмем Python 3.11.0 в качестве примера после установки [aspose.cells](https://pypi.org/project/aspose-cells/).

1. Создайте образец файла Python с именем [example.py](example.py).
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
1. Создайте папку под названием c:\app и скопируйте файл example.py (прикрепленный) в c:\app.
1. Откройте командную строку и выполните команду pyinstaller example.py.
{{< highlight java >}}

C:\app> pyinstaller example.py

{{< /highlight >}}
1. Скопируйте файлы-заготовки (aspose-cells-xxx.jar, bcprov-jdk15on-160.jar, bcpkix-jdk15on-1.60.jar, JavaClassBridge.jar. Они находятся в папке C:\Python311\Lib\site-packages\asposecells\lib) в c:\app.
1. Отредактируйте файл с суффиксом spec, чтобы добавить секцию данных, пример под названием [example.spec](example.spec).
![todo:image_alt_text](example.png)
1. Выполните pyinstaller example.spec в окне командной строки.
{{< highlight java >}}

C:\app> pyinstaller example.spec

{{< /highlight >}}
1. Перейдите в каталог C:\app\dist\example, и вы найдете файл example.exe.
