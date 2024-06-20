---
title: Изменение абсолютного пути источника данных внешней ссылки
type: docs
weight: 290
url: /ru/net/change-the-absolute-path-of-external-link-data-source-file/
---

## Возможные сценарии использования

Если вы хотите изменить абсолютный путь файла источника данных внешней ссылки, используйте свойство [**Workbook.AbsolutePath**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/absolutepath). Изначально это свойство будет установлено на путь, откуда был загружен файл Excel. Но вы можете установить его в пустую строку или указать путь к локальной или удаленной сетевой папке. При изменении этого свойства изменится и путь источника данных внешней ссылки.

## Изменение абсолютного пути файла источника данных внешней ссылки

Следующий образец кода загружает [образец файла Excel](5115146.xlsx), который содержит внешнюю ссылку. Сначала он выводит источник данных внешней ссылки и печатает удаленный путь. Затем он удаляет удаленный путь и снова печатает, на этот раз выводя источник данных внешней ссылки с локальным путем. Затем он изменяет свойство [**Workbook.AbsolutePath**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/absolutepath) на локальный и удаленный путь и снова выводит источник данных внешней ссылки, и изменения отражены в выводе консоли.

Вот вывод консоли или отладки после выполнения вышеприведенного образца кода с [образцовым файлом Excel](5115146.xlsx).

{{< highlight java >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
