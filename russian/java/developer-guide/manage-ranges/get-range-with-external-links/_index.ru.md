---
title: Получить диапазон с внешними ссылками
type: docs
weight: 140
url: /ru/java/get-range-with-external-links/
---
## **Получить диапазон с внешними ссылками**

Файлы Excel часто обращаются к данным из других файлов Excel с помощью внешних ссылок. Aspose.Cells предоставляет возможность получить эти внешние ссылки с помощью[**Имя.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) метод.[**Имя.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) возвращает массив типа[**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea).[**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea)класс предоставляет[**ИмяВнешнегоФайла**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName)свойство, которое возвращает имя внешнего файла.[**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea)класс предоставляет следующие члены.

- [**Конечная колонка**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndColumn): Конечный столбец области
- [**Конечная строка**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndRow): Конечная строка области
- [**ИмяВнешнегоФайла**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName): получить имя внешнего файла, если это внешняя ссылка
- [**IsArea**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsArea): Указывает, является ли это областью
- [**Исэкстерналлинк**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsExternalLink): указывает, является ли это внешней ссылкой
- [**имя листа**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#SheetName): Указывает, на каком листе находится эта ссылка.
- [**СтартКолонка**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartColumn): Начальный столбец области
- [**StartRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartRow): Начальный ряд области

Пример кода, приведенный ниже, демонстрирует использование[**Имя.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) метод получения диапазонов с внешними ссылками.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetRangeWithExternalLinks-1.java" >}}
