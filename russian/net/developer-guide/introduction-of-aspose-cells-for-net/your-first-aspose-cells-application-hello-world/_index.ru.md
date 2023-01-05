---
title: Ваша первая заявка Aspose.Cells - Hello World
type: docs
weight: 30
url: /ru/net/your-first-aspose-cells-application-hello-world/
---
{{% alert color="primary" %}}

В этом руководстве показано, как создать самое первое приложение (Hello World) с помощью простого Aspose.Cells API. Это простое приложение создает файл Excel Microsoft с текстом 'Hello World' в указанной ячейке рабочего листа.

{{% /alert %}}

## **Создание приложения Hello World**

Следующие шаги создают приложение Hello World, используя Aspose.Cells API:

1.  Создайте экземпляр[Рабочая тетрадь](https://reference.aspose.com/cells/net/aspose.cells/workbook) учебный класс.
1.  Если у вас есть лицензия, то[применить это](/cells/ru/net/licensing/).
 Если вы используете ознакомительную версию, пропустите строки кода, связанные с лицензией.
1. Создайте новый файл Excel или откройте существующий файл Excel.
1. Получите доступ к любой нужной ячейке рабочего листа в файле Excel.
1.  Вставьте слова**Hello World!** в ячейку, к которой осуществляется доступ.
1. Создайте измененный файл Excel Microsoft.

Реализация вышеуказанных шагов продемонстрирована на примерах ниже.

### **Пример кода: создание новой книги**

В следующем примере создается новая книга с нуля, пишет Hello World! в ячейку A1 на первом листе и сохраняет файл Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **Пример кода: открытие существующего файла**

В следующем примере открывается существующий файл шаблона Excel Microsoft с именем «Sample.xlsx», вводится «Hello World!» текст в ячейку A1 на первом листе и сохраняет книгу.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
