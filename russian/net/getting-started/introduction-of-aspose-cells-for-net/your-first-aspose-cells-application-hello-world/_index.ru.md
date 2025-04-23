---
title: Ваше первое веб приложение Aspose.Cells  Привет, мир
type: docs
weight: 30
url: /ru/net/your-first-aspose-cells-application-hello-world/
description: Создайте, отредактируйте и сохраните свой первый файл Excel в любых поддерживаемых форматах с помощью Aspose.Cells for .NET, чтобы ощутить его простоту и мощь на C#.
keywords: C# Hello World, Aspose.Cells for .NET Hello World, Первое приложение с использованием Aspose.Cells for .NET, Первая программа через Aspose.Cells for .NET.
---

{{% alert color="primary" %}}

В этом учебнике показано, как создать первое приложение (Hello World) с использованием простого API Aspose.Cells. Это простое приложение создает файл Microsoft Excel с текстом 'Hello World' в указанной ячейке листа.

{{% /alert %}}

## **Как создать приложение Hello World**

Нижеприведенные шаги создают приложение Hello World с использованием API Aspose.Cells:

1. Создайте экземпляр класса [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Если у вас есть лицензия, то [примените ее](/cells/ru/net/licensing/).
   Если вы используете пробную версию, пропустите строки кода, связанные с лицензией.
1. Создайте новый файл Excel или откройте существующий файл Excel.
1. Получите доступ к любой желаемой ячейке листа Excel в файле Excel.
1. Вставьте слова **Привет, мир!** в ячейку для доступа.
1. Сгенерируйте модифицированный файл Microsoft Excel.

Реализация вышеуказанных шагов продемонстрирована в примерах ниже.

### **Как создать новую книгу**

В следующем примере создается новая книга с нуля, записывается Hello World! в ячейку A1 на первом листе и сохраняется файл Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **Как открыть существующий файл**

В следующем примере открывается существующий файл шаблона Microsoft Excel с именем "Sample.xlsx", вводится текст "Hello World!" в ячейку A1 первого листа и сохраняется книга.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
