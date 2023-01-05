---
title: Скопируйте рабочий лист
type: docs
weight: 50
url: /ru/net/copy-a-worksheet/
---
{{% alert color="primary" %}} 

[Добавить рабочие листы](/cells/ru/net/add-worksheets/) описывает, как добавлять новые рабочие листы в Aspose.Cells.GridWeb. Также можно добавить копию (или реплику) другого рабочего листа в элемент управления Aspose.Cells.GridWeb. Эта функция может быть полезна, когда идентичные или похожие данные на одном листе требуются и на другом листе. В этом случае проще скопировать существующий рабочий лист и добавить его в Aspose.Cells.GridWeb в качестве нового рабочего листа, чем создавать его с нуля.

{{% /alert %}} 
## **Копирование рабочего листа**
### **Использование индекса листа**
В приведенном ниже примере кода показано, как добавить копию рабочего листа в элемент управления GridWeb, указав индекс рабочего листа в методе AddCopy GridWorksheetCollection.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingIndex.cs" >}}
### **Использование имени листа**
В приведенном ниже примере кода показано, как добавить копию рабочего листа в элемент управления GridWeb, указав имя рабочего листа в методе AddCopy GridWorksheetCollection.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingName.cs" >}}

{{% alert color="primary" %}} 

 Метод AddCopy возвращает индекс недавно добавленного рабочего листа, который можно использовать для доступа к экземпляру рабочего листа. Подробнее о том, как получить доступ к рабочим листам, см.[Доступ к рабочим листам](/cells/ru/net/access-worksheets/).

{{% /alert %}}
