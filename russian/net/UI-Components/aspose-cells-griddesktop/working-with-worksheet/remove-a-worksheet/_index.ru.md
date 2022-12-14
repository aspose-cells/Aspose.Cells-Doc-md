---
title: Удалить рабочий лист
type: docs
weight: 30
url: /ru/net/remove-a-worksheet/
---
{{% alert color="primary" %}} 

В этом разделе обсуждается удаление листов с помощью элемента управления Aspose.Cells.GridDesktop. Есть несколько простых подходов к выполнению этой основной задачи.

{{% /alert %}} 
## **Удаление рабочего листа**
Чтобы удалить рабочий лист с помощью элемента управления Aspose.Cells.GridDesktop, выполните следующие действия:

1. Добавьте в форму элемент управления Aspose.Cells.GridDesktop.
1. Вызовите метод Remove коллекции Worksheets в элементе управления GridDesktop.
### **Использование указателя рабочего листа**
В этом подходе просто передайте индекс рабочего листа (в коллекции рабочих листов сетки) рабочего листа, который нужно удалить.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingIndex.cs" >}}
### **Использование имени рабочего листа**
Если имя рабочего листа известно, можно удалить конкретный рабочий лист, указав его имя.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingName.cs" >}}

{{% alert color="primary" %}} 

Удалить — это метод. Используйте его, чтобы удалить рабочий лист, используя его индекс (в коллекции рабочих листов), или используйте метод RemoveAt, чтобы удалить рабочий лист, используя его индекс/имя.

{{% /alert %}}
