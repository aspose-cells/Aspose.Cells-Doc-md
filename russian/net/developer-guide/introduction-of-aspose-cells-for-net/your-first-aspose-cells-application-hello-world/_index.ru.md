---
title: Ваше первое заявление на номер Aspose.Cells — Hello World
type: docs
weight: 30
url: /ru/net/your-first-aspose-cells-application-hello-world/
description: Создайте, отредактируйте и сохраните свой первый файл Excel в любом поддерживаемом формате, используя Aspose.Cells for .NET, чтобы ощутить его простоту и мощь в C#.
keywords: C# Hello World, Aspose.Cells for .NET Hello World, The first application using Aspose.Cells for .NET, The first program via Aspose.Cells for .NET.
---
{{% alert color="primary" %}}

В этом руководстве показано, как создать самое первое приложение (Hello World), используя простой Aspose.Cells' API. Это простое приложение создает файл Excel Microsoft с текстом 'Hello World' в указанной ячейке листа.

{{% /alert %}}

##  **Как создать приложение Hello World**

Следующие шаги создают приложение Hello World с использованием Aspose.Cells API:

1.  Создайте экземпляр[Рабочая тетрадь](https://reference.aspose.com/cells/net/aspose.cells/workbook) сорт.
1.  Если у вас есть лицензия, то[применить это](/cells/ru/net/licensing/).
 Если вы используете ознакомительную версию, пропустите строки кода, связанные с лицензией.
1. Создайте новый файл Excel или откройте существующий файл Excel.
1. Получите доступ к любой желаемой ячейке листа в файле Excel.
1.  Вставьте слова**Hello World!** в ячейку, к которой осуществляется доступ.
1. Создайте измененный файл Excel Microsoft.

Реализация вышеописанных шагов продемонстрирована на примерах ниже.

###  **Как создать новую книгу**

В следующем примере создается новая книга с нуля, пишется Hello World! в ячейку A1 на первом листе и сохраняет файл Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

###  **Как открыть существующий файл**

В следующем примере открывается существующий файл шаблона Excel Microsoft с именем «Sample.xlsx», вводятся «Hello World!» текст в ячейку A1 на первом листе и сохраняет книгу.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
