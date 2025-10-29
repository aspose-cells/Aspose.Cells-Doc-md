---
title: Получить диапазон с внешними ссылками
type: docs
weight: 120
url: /ru/python-net/get-range-with-external-links/
description: Эта статья показывает, как получить диапазон с внешними ссылками с помощью Aspose.Cells для Python via .NET API.
keywords: Python Excel Library, Python Get Range with External Links.
---

## **Получить диапазон с внешними ссылками**

Много раз файлы Excel имеют доступ к данным из других файлов Excel с использованием внешних ссылок. Aspose.Cells для Python via .NET предоставляет возможность извлекать эти внешние ссылки, используя метод [**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool). Метод [**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool) возвращает массив типа [**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea). Класс [**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea) предоставляет свойство [**external_file_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/external_file_name/), которое возвращает имя внешнего файла. Класс [**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea) предоставляет следующие члены.

- [**end_column**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/end_column/): Конечный столбец области
- [**end_row**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/end_row/): Конечная строка области
- [**external_file_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/external_file_name/): Получить имя внешнего файла, если это внешняя ссылка
- [**is_area**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/is_area/): Указывает, является ли это областью
- [**is_external_link**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/is_external_link/): Указывает, является ли это внешней ссылкой
- [**sheet_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/sheet_name/): Указывает, в каком листе находится эта ссылка
- [**start_column**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/start_column): Начальный столбец области
- [**start_row**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/start_row): Начальная строка области

Приведенный ниже пример кода демонстрирует использование метода [**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool) для получения диапазонов с внешними ссылками.

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Worksheets-GetRangeWithExternalLinks-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
