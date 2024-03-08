---
title: Начиная
linktitle: Начиная
type: docs
weight: 4
url: /ru/python-net/getting-started/
description: Узнайте, как установить Aspose.Cells for Python via .NET и создать приложение Hello World.
keywords: How to install Aspose.Cells for Python via .NET in Windows Linux and MacOS, installation guidelines for Aspose.Cells for Python via .NET, Python Via .NET Hello World program. 
---
##  **Системные Требования**
 Aspose.Cells for Python via .NET не зависит от платформы API и может использоваться на любой платформе (Windows и Linux), где[Python](https://www.python.org/downloads/) установлен.

##  **Python Версия**
- Python 3.6 или выше

##  **Монтаж**
###  **Windows:**
 Вы можете легко использовать Aspose.Cells for Python via .NET из[пипи](https://pypi.org/project/aspose-cells-python/) с помощью следующей команды.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

###  **Линукс:**
 Вы можете легко использовать Aspose.Cells for Python via .NET из[пипи](https://pypi.org/project/aspose-cells-python/) с помощью следующей команды.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Примечание. Перед установкой необходимо выполнить следующую команду.
{{< highlight "NET" >}}
For Ubuntu/Debian: apt-get install libgdiplus 
For CentOS/RHEL/Fedora: yum install libgdiplus 
{{< /highlight >}}

###  **МакОС:**
 Вы можете легко использовать Aspose.Cells for Python via .NET из[пипи](https://pypi.org/project/aspose-cells-python/) с помощью следующей команды.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Примечание. Если ваш Python — Python3.7 (возьмите, например, Python3.7 здесь), после установки aspose-cells-python могут возникнуть следующие ошибки.
 Запрос «/usr/local/lib/libpython3.7m.dylib» (нет такого файла), «/usr/lib/libpython3.7m.dylib» (нет такого файла).
 В такой ситуации добавьте следующую команду в свой bash_profile (сначала найдите, где находится libpython3.7m.dylib, возьмите /Library/Frameworks/Python.framework/Versions/3.7/lib
 например здесь)
{{< highlight "NET" >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}

- Примечание. Поскольку мы полагаемся на графическую библиотеку SkiaSharp, если вы столкнулись со следующей ошибкой:
**System.DllNotFoundException: невозможно загрузить общую библиотеку libSkiaSharp или одну из ее зависимостей.** пожалуйста, установите SkiaSharp.
{{< highlight "NET" >}}
brew  install nuget
nuget install SkiaSharp.NativeAssets.macOS -Version 2.88.3
{{< /highlight >}}
 После установки выполните следующую команду
{{< highlight "NET" >}}
cp ./SkiaSharp.NativeAssets.macOS.2.88.3/runtimes/osx/native/libSkiaSharp.dylib /usr/local/lib/.
{{< /highlight >}}

 Конечно, если вы хотите проще, вы также можете скачать[libSkiaSharp.dylib](libSkiaSharp.dylib) а потом**копировать** это к**/usr/локальный/библиотека** каталог.

##  **Как создать приложение Hello World, используя Aspose.Cells for Python via .NET**

-  Создайте файл с именем**СозданиеHelloWorldFile.py** и используйте следующий пример кода:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- Теперь сохраните приведенный выше код в «CreatingHelloWorldFile.py» и запустите «python MakingHelloWorldFile.py» в командной строке.

##  **Python via .NET Пример github**
-  Пожалуйста, посетите[Aspose.Cells for Python via .NET Пример](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET) github, чтобы просмотреть больше примеров кода.


