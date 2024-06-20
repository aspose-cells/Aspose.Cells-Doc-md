---
title: Доступ к рабочему листу
type: docs
weight: 10
url: /ru/net/aspose-cells-griddesktop/access-worksheet/
keywords: GridDesktop,worksheet
description: Эта статья представляет, как работать с листом в GridDesktop.
---

{{% alert color="primary" %}} 

Рабочий лист - неотъемлемая часть файла Excel. Фактически, файл Excel состоит из одного или нескольких рабочих листов. Каждый рабочий лист может состоять только из до 65 536 строк и 256 столбцов. Именно рабочий лист хранит данные в файле Excel.

Aspose.Cells.GridDesktop может создавать и управлять существующими и новыми файлами Excel, поэтому, конечно, существует способ доступа к рабочим листам с помощью Aspose.Cells.GridDesktop. В этой теме рассматривается, как это сделать.

{{% /alert %}} 
## **Использование индекса листа**
Разработчики могут получить доступ к экземпляру любого рабочего листа, используя индекс рабочего листа в соответствии с желаемым рабочим листом, как показано ниже в примере. Этот подход хорош для итерации через несколько рабочих листов в файле Excel.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithIndex.cs" >}}
## **Использование имени листа**
Если известно имя рабочего листа, можно получить доступ к нему по его имени, как показано ниже.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithName.cs" >}}
## **Доступ к активному рабочему листу**
Возможно, что в файле Excel будет более одного рабочего листа. Тот, над которым работает пользователь, называется активным рабочим листом. Есть возможность получить доступ к активному листу.

Для доступа к активному рабочему листу Aspose.Cells.GridDesktop предлагает два подхода:
### **Использование свойства AcriveSheetIndex**
Один из способов получить доступ к активному рабочему листу с использованием элемента управления Aspose.Cells.GridDesktop - это использовать свойство ActiveSheetIndex элемента управления GridDesktop. Используя это свойство, можно получить индекс активного рабочего листа в элементе управления Aspose.Cells.GridDesktop, после чего этот индекс можно использовать для доступа к рабочему листу в традиционном порядке, как показано ниже.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithActiveWorksheet.cs" >}}
### **Использование метода GetActiveWorksheet**
Другой подход - вызвать метод GetActiveWorksheet элемента управления GridDesktop. Этот метод предоставляет ссылку на рабочий лист, который в данный момент активен в элементе управления Aspose.Cells.GridDesktop, как показано ниже.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithGetActiveWorksheet.cs" >}}
