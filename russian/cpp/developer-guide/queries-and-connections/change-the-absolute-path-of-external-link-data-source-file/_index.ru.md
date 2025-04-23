---
title: Изменить абсолютный путь внешнего источника данных с помощью C++
linktitle: Изменение абсолютного пути источника данных внешней ссылки
type: docs
weight: 290
url: /ru/cpp/change-the-absolute-path-of-external-link-data-source-file/
description: Изменить абсолютный путь внешнего источника данных в Aspose.Cells с помощью C++.
---

## Возможные сценарии использования

Если вы хотите изменить абсолютный путь внешнего источника данных, используйте метод [**GetAbsolutePath()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getabsolutepath/). Изначально это свойство устанавливается в путь, из которого был загружен файл Excel. Но вы можете установить его в пустую строку или указать путь к локальной папке или удаленной сети. При изменении этого свойства изменится также путь внешнего источника данных.

## Изменение абсолютного пути файла источника данных внешней ссылки

Следующий пример кода загружает [образец файла Excel](5115146.xlsx), содержащий внешнюю ссылку. Он сначала выводит источник данных внешней ссылки, который показывает удаленный путь, затем удаляет его и снова выводит, теперь показывая источник данных с локальным путем. Затем он меняет [**GetAbsolutePath()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getabsolutepath/) на локальный и удалённый путь и снова выводит источник данных, отражая изменения в консоли.

Вот вывод консоли или отладки после выполнения вышеприведенного образца кода с [образцовым файлом Excel](5115146.xlsx).

{{< highlight cpp >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
