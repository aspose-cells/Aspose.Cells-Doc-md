---
title: Доступ к рабочим листам
type: docs
weight: 10
url: /ru/net/access-worksheets/
---
{{% alert color="primary" %}} 

В этом разделе обсуждается доступ к листам в элементе управления Aspose.Cells.GridWeb. Мы будем называть их «веб-листами», поскольку они принадлежат Aspose.Cells.GridWeb и используются в веб-приложениях.

{{% /alert %}} 
## **Доступ к рабочему листу**
Все рабочие листы, содержащиеся в Aspose.Cells.GridWeb, хранятся в коллекции GridWorksheetCollection элемента управления GridWeb. Существует два способа доступа к рабочему листу: по индексу листа или по имени листа.
### **Использование указателя листов**
В приведенном ниже фрагменте кода показано, как получить доступ к определенному веб-листу из коллекции GridWorksheetCollection элемента управления GridWeb с помощью индекса листа.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AccessWorksheets.aspx-AccessWorksheetUsingIndex.cs" >}}
### **Использование имени листа**
В приведенном ниже фрагменте кода показано, как получить доступ к веб-листу из коллекции GridWorksheetCollection элемента управления GridWeb, используя имя листа.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AccessWorksheets.aspx-AccessWorksheetUsingName.cs" >}}
