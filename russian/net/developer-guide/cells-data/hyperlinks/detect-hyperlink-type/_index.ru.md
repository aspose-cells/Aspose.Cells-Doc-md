---
title: Определить тип гиперссылки
type: docs
weight: 160
url: /ru/net/detect-hyperlink-type/
description: Узнайте, как определить тип гиперссылки с помощью Aspose.Cells for .NET API.
keywords: Detect hyperlink type, Detect the type of hyperlink, Get the type of hyperlink
---
##  **Определить тип гиперссылки**

 Файл Excel может иметь различные типы гиперссылок, например внешние, ссылку на ячейку, путь к файлу и т. д. Aspose.Cells поддерживает функцию определения типа гиперссылки. Типы гиперссылок представлены[**Таргетмодетипе**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)Перечисление.[**Таргетмодетипе**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)Перечисление имеет следующие члены.

- Внешний: Внешняя ссылка
- FilePath: локальный и полный путь к файлам\папкам.
- Электронная почта: Электронная почта
- CellReference: ссылка на ячейку или именованный диапазон.

 Чтобы проверить тип гиперссылки,[**Гиперссылка**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) класс обеспечивает[**Тип ссылки**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype) свойство с возвращаемым типом[**Таргетмодетипе**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype). Следующий фрагмент кода демонстрирует использование[**Тип ссылки**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype)свойство, используя это[исходный файл Excel](94896195.xlsx).

###  Исходный код

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-DetectLinkTypes-1.cs" >}}

Ниже приведен вывод, сгенерированный фрагментом кода, приведенным выше.

###  Консольный вывод
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
