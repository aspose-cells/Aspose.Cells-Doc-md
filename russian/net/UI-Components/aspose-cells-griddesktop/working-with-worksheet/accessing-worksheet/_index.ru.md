---
title: Доступ к рабочему листу
type: docs
weight: 10
url: /ru/net/accessing-worksheet/
---
{{% alert color="primary" %}} 

Рабочий лист является неотъемлемой частью файла Excel. Фактически файл Excel состоит из одного или нескольких рабочих листов. Каждый рабочий лист может состоять только из 65 536 строк и 256 столбцов. Это рабочий лист, который содержит данные в файле Excel.

Aspose.Cells.GridDesktop может создавать и управлять существующими и новыми файлами Excel, поэтому, конечно же, есть способ доступа к рабочим листам с помощью Aspose.Cells.GridDesktop. В этой теме обсуждается как.

{{% /alert %}} 
## **Использование указателя рабочего листа**
Разработчики могут получить доступ к экземпляру любого рабочего листа, используя индекс рабочего листа любого желаемого рабочего листа, как показано ниже в примере. Этот подход удобен для перебора нескольких рабочих листов в файле Excel.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithIndex.cs" >}}
## **Использование имени рабочего листа**
Если имя рабочего листа известно, можно получить доступ к рабочему листу, используя его имя, как показано ниже.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithName.cs" >}}
## **Доступ к активному рабочему листу**
Возможно, файл Excel будет иметь более одного рабочего листа. Тот лист, над которым работает пользователь, называется активным рабочим листом. Доступ к активному листу возможен.

Для доступа к активному рабочему листу Aspose.Cells.GridDesktop предлагает два подхода:
### **Использование свойства AcriveSheetIndex**
Один из способов получить доступ к активному рабочему листу с помощью элемента управления Aspose.Cells.GridDesktop — использовать свойство ActiveSheetIndex элемента управления GridDesktop. Используя это свойство, можно получить индекс активного рабочего листа в элементе управления Aspose.Cells.GridDesktop. Затем этот индекс можно использовать для доступа к рабочему листу традиционным способом, как показано ниже.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithActiveWorksheet.cs" >}}
### **Использование метода GetActiveWorksheet**
Другой подход заключается в вызове метода GetActiveWorksheet элемента управления GridDesktop. Этот метод предоставляет ссылку на рабочий лист, который в данный момент активен в элементе управления Aspose.Cells.GridDesktop, как показано ниже.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithGetActiveWorksheet.cs" >}}
