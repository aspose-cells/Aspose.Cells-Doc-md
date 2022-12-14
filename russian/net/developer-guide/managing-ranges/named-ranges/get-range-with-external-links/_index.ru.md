---
title: Получить диапазон с внешними ссылками
type: docs
weight: 120
url: /ru/net/get-range-with-external-links/
---
## **Получить диапазон с внешними ссылками**

Файлы Excel часто обращаются к данным из других файлов Excel с помощью внешних ссылок. Aspose.Cells предоставляет возможность получить эти внешние ссылки с помощью[**Имя.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)метод.[**Имя.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)метод возвращает массив типа[**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea).[**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea) класс предоставляет[**ИмяВнешнегоФайла**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename)свойство, которое возвращает имя внешнего файла.[**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea)класс предоставляет следующие члены.

- [**Конечная колонка**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endcolumn): Конечный столбец области
- [**Конечная строка**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endrow): Конечная строка области
- [**ИмяВнешнегоФайла**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename): получить имя внешнего файла, если это внешняя ссылка
- [**IsArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isarea): Указывает, является ли это областью
- [**Исэкстерналлинк**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isexternallink): указывает, является ли это внешней ссылкой
- [**имя листа**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/sheetname): Указывает, на каком листе находится эта ссылка.
- [**СтартКолонка**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startcolumn): Начальный столбец области
- [**StartRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startrow): Начальный ряд области

 Пример кода, приведенный ниже, демонстрирует использование[**Имя.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)способ получить диапазоны с внешними ссылками.

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-GetRangeWithExternalLinks-1.cs" >}}
