---
title: Изменение абсолютного пути источника данных внешней ссылки
type: docs
weight: 1020
url: /ru/java/change-the-absolute-path-of-external-link-data-source-file/
---

## **Возможные сценарии использования**
Если вы хотите изменить абсолютный путь источника данных внешней ссылки, то, пожалуйста, используйте свойство [Workbook.AbsolutePath](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath). Изначально это свойство будет установлено на путь, откуда был загружен excel-файл. Но вы можете установить его на пустую строку или на локальный путь к папке или удаленный сетевой путь. Когда вы измените это свойство, также изменится путь источника данных внешней ссылки.
## **Измените абсолютный путь внешнего источника данных ссылки**
Следующий образец кода загружает [образец файла Excel](5472589.xlsx), который содержит внешнюю ссылку. Сначала он выводит источник данных внешней ссылки, который печатает удаленный путь. Затем он удаляет удаленный путь и снова печатает, на этот раз печатает источник данных внешней ссылки с локальным путем. Затем он изменяет свойство [Workbook.AbsolutePath](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath) на локальный и удаленный путь и снова печатает источник данных внешней ссылки, и изменения отображаются на выводе консоли.
## **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAbsolutePathofExternalLink-ChangeAbsolutePathofExternalLink.java" >}}
## **Вывод в консоль**
Вот вывод консоли или отладки после выполнения вышеуказанного образца кода с [образцом файла Excel](5472589.xlsx).

{{< highlight java >}}

 External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
