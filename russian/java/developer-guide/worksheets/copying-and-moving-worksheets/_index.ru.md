﻿---
title: Копирование и перемещение рабочих листов
type: docs
weight: 20
url: /ru/java/copying-and-moving-worksheets/
---
{{% alert color="primary" %}}

Иногда вам нужно несколько рабочих листов с общим форматированием и данными. Например, если вы работаете с квартальными бюджетами, вы можете создать рабочую книгу с листами, содержащими одинаковые заголовки столбцов, заголовки строк и формулы. Есть способ сделать это: создать один лист, а затем скопировать его.

Aspose.Cells поддерживает копирование и перемещение рабочих листов внутри или между книгами. Рабочий лист с данными, форматированием, таблицами, матрицами, диаграммами, изображениями и другими объектами копируется с высочайшей степенью точности.

{{% /alert %}}

## **Перемещение или копирование листов с помощью Microsoft Excel**

Ниже приведены шаги, необходимые для копирования и перемещения рабочих листов внутри или между книгами.

1. Чтобы переместить или скопировать листы в другую книгу, откройте книгу, которая получит листы.
1. Переключитесь на книгу, содержащую листы, которые вы хотите переместить или скопировать, а затем выберите листы.
1.  На**Редактировать** меню, нажмите**Переместить или скопировать лист**.
1. В поле В книгу щелкните книгу, чтобы получить листы.
1.  Чтобы переместить или скопировать выбранные листы в новую книгу, щелкните**новая книга**.
1.  в**Перед листом** щелкните лист, перед которым вы хотите вставить перемещенные или скопированные листы.
1.  Чтобы копировать листы, а не перемещать их, выберите значок**Создать копию** флажок.

## **Копировать рабочие листы в рабочую книгу**

 Aspose.Cells предоставляет перегруженный метод,[**WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#addCopy(int)), который используется для добавления листа в коллекцию и копирования данных из существующего листа. Одна версия метода принимает в качестве параметра индекс исходного листа. Другая версия берет имя исходного рабочего листа.

В следующем примере показано, как скопировать существующий рабочий лист в рабочую книгу.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWithinWorkbook-CopyWithinWorkbook.java" >}}

## **Копировать рабочие листы между рабочими книгами**

 Aspose.Cells предоставляет метод,[**Рабочий лист.копировать()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)), используемый для копирования данных и форматирования с исходного рабочего листа на другой рабочий лист внутри или между рабочими книгами. Метод принимает исходный объект рабочего листа в качестве параметра.

В следующем примере показано, как скопировать лист из одной книги в другую книгу.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetsBetweenWorkbooks-CopyWorksheetsBetweenWorkbooks.java" >}}

В следующем примере показано, как скопировать лист из одной книги в другую.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetFromWorkbookToOther-CopyWorksheetFromWorkbookToOther.java" >}}

## **Перемещение рабочих листов в рабочей книге**

 Aspose.Cells предоставляет метод,[**Рабочий лист.moveTo()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#moveTo(int)), используемый для перемещения рабочего листа в другое место в той же электронной таблице.

В следующем примере показано, как переместить лист в другое место в книге.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-MoveWorksheet-MoveWorksheet.java" >}}
