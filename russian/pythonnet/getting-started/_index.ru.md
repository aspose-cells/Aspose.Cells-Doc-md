---
title: Начиная
linktitle: Начиная
type: docs
weight: 4
url: /ru/python-net/getting-started/ 
keywords: python, excel, instal
description: Установка Aspose.Cells for Python via .NET и инструкции по установке.
---
## **Системные Требования**
 Aspose.Cells for Python via .NET не зависит от платформы API и может использоваться на любой платформе (Windows и Linux), где[Python](https://www.python.org/downloads/) установлен.

## **Python Версия**
- Python 3.6 или выше

## **Монтаж**
### **Windows:**
 Вы можете легко использовать Aspose.Cells for Python via .NET от[пипи](https://pypi.org/project/aspose-cells-python/) с помощью следующей команды.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

### **Линукс:**
 Вы можете легко использовать Aspose.Cells for Python via .NET от[пипи](https://pypi.org/project/aspose-cells-python/) с помощью следующей команды.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

### **MacOS:**
 Вы можете легко использовать Aspose.Cells for Python via .NET от[пипи](https://pypi.org/project/aspose-cells-python/) с помощью следующей команды.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Примечание: Если ваш python Python3.7(взять python3.7, например здесь), после установки aspose-cells-python могут быть следующие ошибки
 '/usr/local/lib/libpython3.7m.dylib' (нет такого файла), '/usr/lib/libpython3.7m.dylib' (нет такого файла).
 В такой ситуации добавьте следующую команду в свой профиль bash (сначала найдите, где находится libpython3.7m.dylib, возьмите /Library/Frameworks/Python.framework/Versions/3.7/lib
 например здесь)
{{< highlight "NET" >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}
## **Создание приложения Hello World**

-  Создайте файл с именем**СозданиеHelloWorldFile.py** и используйте следующий пример кода:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- Теперь сохраните приведенный выше код в «CreatingHelloWorldFile.py» и запустите командную строку «python MakingHelloWorldFile.py» @.

