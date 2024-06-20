---
title: Начало работы
linktitle: Начало работы
type: docs
weight: 4
url: /ru/python-net/getting-started/
description: Узнайте, как установить Aspose.Cells для Python via .NET и создать приложение Hello World.
keywords: Как установить Aspose.Cells для Python via .NET в Windows Linux и MacOS, руководство по установке Aspose.Cells для Python via .NET, Hello World программа Python через .NET. 
---

## **Системные требования**
Aspose.Cells для Python via .NET - это кроссплатформенное API и может использоваться на любой платформе (Windows и Linux), где установлен [Python](https://www.python.org/downloads/). 

## **Версия Python**
- Python 3.6 или выше

## **Установка**
### **Windows:**
Вы легко можете использовать Aspose.Cells для Python via .NET из [pypi](https://pypi.org/project/aspose-cells-python/) с помощью следующей команды.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

### **Linux:**
Вы легко можете использовать Aspose.Cells для Python via .NET из [pypi](https://pypi.org/project/aspose-cells-python/) с помощью следующей команды.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Примечание: перед установкой вам необходимо выполнить следующую команду
{{< highlight NET >}}
For Ubuntu/Debian: apt-get install libgdiplus 
For CentOS/RHEL/Fedora: yum install libgdiplus 
{{< /highlight >}}

### **MacOS:**
Вы легко можете использовать Aspose.Cells для Python via .NET из [pypi](https://pypi.org/project/aspose-cells-python/) с помощью следующей команды.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Примечание: Если ваш Python - Python3.7 (возьмем, например, python3.7 здесь), после установки aspose-cells-python могут возникнуть следующие ошибки
  '/usr/local/lib/libpython3.7m.dylib' (файл отсутствует), '/usr/lib/libpython3.7m.dylib' (файл отсутствует) - информирует.
  В такой ситуации добавьте следующую команду в свой bash_profile (сначала найдите, где находится libpython3.7m.dylib, возьмем /Library/Frameworks/Python.framework/Versions/3.7/lib, например, здесь).
  - Примечание: Из-за нашей зависимости от графической библиотеки SkiaSharp, если вы столкнетесь с следующей ошибкой:
{{< highlight NET >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}

**System.DllNotFoundException: Невозможно загрузить общую библиотеку 'libSkiaSharp' или одну из ее зависимостей.** пожалуйста, установите SkiaSharp.
После установки выполните следующую команду
{{< highlight NET >}}
brew  install nuget
nuget install SkiaSharp.NativeAssets.macOS -Version 2.88.3
{{< /highlight >}}
Конечно же, если вы хотите упростить, вы также можете скачать [libSkiaSharp.dylib](libSkiaSharp.dylib) и затем **скопировать** его в каталог **/usr/local/lib**. 
{{< highlight NET >}}
cp ./SkiaSharp.NativeAssets.macOS.2.88.3/runtimes/osx/native/libSkiaSharp.dylib /usr/local/lib/.
{{< /highlight >}}

Конечно, если вы хотите упростить процесс, вы также можете скачать [libSkiaSharp.dylib](libSkiaSharp.dylib) и затем **скопировать** его в каталог **/usr/local/lib**.

## **Как создать пример приложения Hello World с использованием Aspose.Cells для Python via .NET**

- Создайте файл с именем **CreatingHelloWorldFile.py** и используйте следующий образец кода:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- Теперь сохраните код выше в "CreatingHelloWorldFile.py" и выполните "python CreatingHelloWorldFile.py" на командной строке.

## **Пример Python via .NET github**
- Пожалуйста, посетите [пример Aspose.Cells для Python via .NET](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET) на github, чтобы посмотреть больше образцов кода.


