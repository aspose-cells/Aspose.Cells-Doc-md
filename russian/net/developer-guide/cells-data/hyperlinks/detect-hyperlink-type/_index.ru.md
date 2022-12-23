---
title: Определить тип гиперссылки
type: docs
weight: 160
url: /ru/net/detect-hyperlink-type/
---
## **Определить тип гиперссылки**

 Файл Excel может иметь различные типы гиперссылок, такие как внешние ссылки, ссылки на ячейки, пути к файлам и т. д. Aspose.Cells поддерживает функцию определения типа гиперссылок. Типы гиперссылок представлены[**Тип таргетмоде**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)Перечисление.[**Тип таргетмоде**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)Перечисление имеет следующие члены.

- Внешний: внешняя ссылка
- FilePath: Локальный и полный путь к файлам\папкам.
- Электронная почта: Электронная почта
- CellReference: ссылка на ячейку или именованный диапазон.

Чтобы проверить тип гиперссылки,[**Гиперссылка**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) класс предоставляет[**Тип ссылки**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype) свойство с возвращаемым типом[**Тип таргетмоде**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype). Следующий фрагмент кода демонстрирует использование[**Тип ссылки**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype)свойство с помощью этого[исходный файл excel](94896195.xlsx).

### Исходный код

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-DetectLinkTypes-1.cs" >}}

Ниже приведен вывод, созданный фрагментом кода, приведенным выше.

### Консольный вывод
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
