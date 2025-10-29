---
title: Обнаружение типа гиперссылки
type: docs
weight: 160
url: /ru/python-net/detect-hyperlink-type/
description: Узнайте, как определять тип гиперссылки через API Aspose.Cells для Python via .NET.
keywords: Библиотека Python для Excel, определение типа гиперссылки в Python, определение типа гиперссылки в Python, получение типа гиперссылки в Python.
---

## **Обнаружение типа гиперссылки**

Файл Excel может содержать различные типы гиперссылок, такие как внешние, ссылки на ячейки, пути к файлам и т. д. Aspose.Cells для Python via .NET поддерживает функцию определения типа гиперссылки. Типы гиперссылок представлены перечислением {0}. Перечисление {1} имеет следующие члены: {2}.

- ВНЕШНИЙ: внешняя ссылка
- ПУТЬ_К_ФАЙЛУ: локальный и полный путь к файлам/папкам.
- EMAIL: адрес электронной почты
- ССЫЛКА_НА_ЯЧЕЙКУ: ссылка на ячейку или именованный диапазон.

Для проверки типа гиперссылки, класс [**Hyperlink**](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink) предоставляет свойство [**link_type**](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink/link_type/) с возвращаемым типом [**TargetModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/targetmodetype). В следующем фрагменте кода демонстрируется использование свойства [**link_type**](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink/link_type/), используя этот [исходный файл Excel](94896195.xlsx).

### Исходный код

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DetectLinkTypes-1.py" >}}

Ниже приведен вывод, сгенерированный указанным выше фрагментом кода.

### Вывод в консоли
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
{{< app/cells/assistant language="python-net" >}}
