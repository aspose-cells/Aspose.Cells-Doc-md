---
title: Изменить абсолютный путь к файлу источника данных внешней ссылки
type: docs
weight: 1020
url: /ru/java/change-the-absolute-path-of-external-link-data-source-file/
---
## **Возможные сценарии использования**
 Если вы хотите изменить абсолютный путь к файлу источника данных внешней ссылки, используйте[Рабочая книга.Абсолютный путь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath)имущество. Первоначально для этого свойства будет задан путь, по которому был загружен файл Excel. Но вы можете установить для него пустую строку или указать путь к какой-либо локальной папке или удаленному сетевому пути. Всякий раз, когда вы изменяете это свойство, путь к файлу источника данных внешней ссылки также будет изменен.
## **Изменить абсолютный путь к файлу источника данных внешней ссылки**
 Следующий пример кода загружает[образец эксель файла](5472589.xlsx) который содержит внешнюю ссылку. Сначала он печатает источник данных внешней ссылки, который печатает удаленный путь. Затем он удаляет удаленный путь и снова печатает, на этот раз он печатает источник данных внешней ссылки с локальным путем. Затем он изменяет[Рабочая книга.Абсолютный путь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath)свойство на локальный и удаленный путь и снова печатает источник данных внешней ссылки, и изменения отражаются в выводе консоли.
## **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAbsolutePathofExternalLink-ChangeAbsolutePathofExternalLink.java" >}}
## **Консольный вывод**
Вот вывод консоли или отладки после выполнения приведенного выше примера кода с[образец эксель файла](5472589.xlsx).

{{< highlight "java" >}}

 External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
