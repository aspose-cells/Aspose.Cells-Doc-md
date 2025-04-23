---
title: Измените абсолютный путь внешнего источника данных с помощью Node.js через C++
linktitle: Изменение абсолютного пути источника данных внешней ссылки
type: docs
weight: 290
url: /ru/nodejs-cpp/change-the-absolute-path-of-external-link-data-source-file/
description: Узнайте, как изменить абсолютный путь внешнего источника данных с помощью Aspose.Cells for Node.js via C++. 
---

## Возможные сценарии использования

Если вы хотите изменить абсолютный путь файла внешней ссылки, используйте свойство [**Workbook.getAbsolutePath()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getAbsolutePath--). Изначально это свойство установлено в путь, откуда был загружен файл Excel. Но вы можете установить его в пустую строку, или указать локальную папку или удаленную сетевую папку. При каждом изменении этого свойства также изменится путь внешнего источника данных.

## Изменение абсолютного пути файла источника данных внешней ссылки

Следующий пример загружает [пример файла Excel](5115146.xlsx), содержащий внешнюю ссылку. Он сначала выводит источник данных внешней ссылки — удаленный путь, затем удаляет его и выводит локальный путь, затем меняет свойство [**Workbook.getAbsolutePath()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getAbsolutePath--) на локальный и удаленный пути и снова выводит источник данных, показывая, что изменения отражены в консоли.

Вот вывод в консоль или отладчике после выполнения вышеуказанного примера с [примером файла Excel](5115146.xlsx).

{{< highlight javascript >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
