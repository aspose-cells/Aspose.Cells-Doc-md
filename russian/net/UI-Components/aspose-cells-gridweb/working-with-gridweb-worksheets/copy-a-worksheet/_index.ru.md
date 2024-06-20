---
title: Скопируйте лист
type: docs
weight: 50
url: /ru/net/aspose-cells-gridweb/copy-a-worksheet/
keywords: GridWeb, копирование, GridWorksheet
description: Эта статья представляет, как скопировать лист (GridWorksheet) в GridWeb.
---

{{% alert color="primary" %}} 

[Добавление листов](/cells/ru/net/aspose-cells-gridweb/add-worksheets/) описывает, как добавить новые листы в Aspose.Cells.GridWeb. Также возможно добавить копию (или реплику) другого листа в элемент управления Aspose.Cells.GridWeb. Эта функция может быть полезна, когда идентичные или похожие данные на одном листе также требуются на другом листе. В таком случае проще скопировать существующий лист и добавить его в Aspose.Cells.GridWeb как новый лист, а не создавать его с нуля.

{{% /alert %}} 
## **Копирование листа**
### **Используя индекс листа**
Приведенный ниже пример кода показывает, как добавить копию листа в элемент управления GridWeb, указав индекс листа в методе AddCopy коллекции GridWorksheetCollection.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingIndex.cs" >}}
### **Использование имени листа**
Приведенный ниже пример кода показывает, как добавить копию листа в элемент управления GridWeb, указав имя листа в методе AddCopy коллекции GridWorksheetCollection.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingName.cs" >}}

{{% alert color="primary" %}} 

Метод AddCopy возвращает индекс вновь добавленного листа, который может быть использован для доступа к экземпляру листа. Для получения более подробной информации о доступе к листам, прочтите [Доступ к листам](/cells/ru/net/aspose-cells-gridweb/access-worksheets/).

{{% /alert %}}
