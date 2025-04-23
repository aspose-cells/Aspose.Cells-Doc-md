---
title: Получить диапазон с внешними ссылками
type: docs
weight: 140
url: /ru/java/get-range-with-external-links/
---

## **Получить диапазон с внешними ссылками**

Многократно файлы Excel получают доступ к данным из других файлов Excel с использованием внешних ссылок. Aspose.Cells предоставляет возможность получить эти внешние ссылки, используя метод [**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas-boolean-). Метод [**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas-boolean-) возвращает массив типа [**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea). Класс [**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea) предоставляет свойство [**ExternalFileName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName), которое возвращает имя внешнего файла. Класс [**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea) выдает следующие члены.

- [**EndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndColumn): Конечный столбец области
- [**EndRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndRow): Конечная строка области
- [**ExternalFileName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName): Получить имя внешнего файла, если это внешняя ссылка
- [**IsArea**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsArea): Указывает, является ли это областью
- [**IsExternalLink**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsExternalLink): Указывает, является ли это внешней ссылкой
- [**SheetName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#SheetName): Указывает, в каком листе находится эта ссылка
- [**StartColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartColumn): Начальный столбец области
- [**StartRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartRow): Начальная строка области

Приведенный ниже образец кода демонстрирует использование метода [**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas-boolean-) для получения диапазонов с внешними ссылками.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetRangeWithExternalLinks-1.java" >}}
{{< app/cells/assistant language="java" >}}
