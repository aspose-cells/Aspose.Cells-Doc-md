---
title: Получить диапазон с внешними ссылками
type: docs
weight: 120
url: /ru/net/get-range-with-external-links/
---

## **Получить диапазон с внешними ссылками**

Часто файлы Excel получают доступ к данным из других файлов Excel с использованием внешних ссылок. Aspose.Cells предоставляет возможность извлечь эти внешние ссылки, используя метод [**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas). Метод [**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas) возвращает массив типа [**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea). Класс [**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea) предоставляет свойство [**ExternalFileName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename), которое возвращает название внешнего файла. Класс [**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea) предоставляет следующие члены.

- [**EndColumn**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endcolumn): Конечный столбец области
- [**EndRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endrow): Конечная строка области
- [**ExternalFileName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename): Получить имя внешнего файла, если это внешняя ссылка
- [**IsArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isarea): Указывает, является ли это областью
- [**IsExternalLink**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isexternallink): Указывает, является ли это внешней ссылкой
- [**SheetName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/sheetname): Указывает, в каком листе находится эта ссылка
- [**StartColumn**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startcolumn): Начальный столбец области
- [**StartRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startrow): Начальная строка области

Приведенный ниже пример кода демонстрирует использование метода [**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas) для получения диапазонов с внешними ссылками.

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-GetRangeWithExternalLinks-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
