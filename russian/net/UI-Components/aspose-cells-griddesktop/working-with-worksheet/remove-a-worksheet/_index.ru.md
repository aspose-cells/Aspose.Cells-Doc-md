---
title: Удалить лист
type: docs
weight: 30
url: /ru/net/aspose-cells-griddesktop/remove-a-worksheet/
keywords: GridDesktop,удалить,лист
description: Эта статья представляет, как удалить лист в GridDesktop.
---

{{% alert color="primary" %}} 

Эта тема обсуждает удаление листов с использованием элемента управления Aspose.Cells.GridDesktop. Есть несколько простых подходов к выполнению этой базовой задачи.

{{% /alert %}} 
## **Удаление листа**
Чтобы удалить лист с помощью элемента управления Aspose.Cells.GridDesktop, выполните следующие действия:

1. Добавьте элемент управления Aspose.Cells.GridDesktop на форму.
1. Вызовите метод Remove коллекции Worksheets в элементе управления GridDesktop.
### **Использование индекса листа**
В этом подходе просто передайте индекс листа (в коллекции листов таблицы) листа, который нужно удалить.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingIndex.cs" >}}
### **Использование имени листа**
Если известно имя листа, можно удалить конкретный лист, указав его имя.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingName.cs" >}}

{{% alert color="primary" %}} 

Remove - это метод. Используйте его для удаления листа по его индексу (в коллекции листов) или используйте метод RemoveAt для удаления листа по его индексу/имени.

{{% /alert %}}
