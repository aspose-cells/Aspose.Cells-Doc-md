---
title: Прямое вычисление пользовательской функции без её записи в лист с Golang через C++
linktitle: Прямое вычисление пользовательской функции
description: Эта статья представляет, как использовать библиотеку Aspose.Cells для прямого расчета пользовательских функций в Microsoft Excel без записи функции в рабочем листе. Загружая существующий файл Excel или создавая новый файл Excel, мы можем использовать методы, предоставленные Aspose.Cells, для расчета пользовательской функции и получения результата. Наконец, мы сохраняем измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, пользовательские функции, прямые расчеты, нет необходимости в написании, рабочие листы
type: docs
weight: 90
url: /ru/go-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Прямое вычисление пользовательской функции без её записи в лист**

Эта тема объясняет, как напрямую вычислить ваши пользовательские функции, не записывая их предварительно в лист. Пожалуйста, используйте метод [**Worksheet::CalculateFormula(System::String formula, CalculationOptions opts)**](https://reference.aspose.com/cells/go-cpp/worksheet/calculateformula_string/) для этой цели.

Посмотрите следующий пример кода, иллюстрирующий использование этого метода. Мы использовали пользовательскую функцию с именем MyCompany::CustomFunction() и самостоятельно вычисляем её значение как "Aspose.Cells." Тогда это значение автоматически конкатенируется с значением ячейки A1, которое равно "Welcome to " с помощью движка расчетов, и итоговое вычисленное значение возвращается как "Welcome to Aspose.Cells.". Как видно из кода, мы не записывали нашу пользовательскую функцию нигде в листе, и она вычисляется напрямую нашим собственным логикой.

### **Пример программирования**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DirectCalculationOfCustomFunctionWithoutWritingItInAWorksheet.go" >}}
### **Вывод в консоль**

Ниже приведен вывод консоли приведенного выше образца кода.

{{< highlight java >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Связанная статья**

{{% alert color="primary" %}}

[Реализация пользовательского движка расчетов для расширения стандартного движка Aspose.Cells](/cells/ru/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
