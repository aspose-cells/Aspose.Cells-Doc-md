---
title: Использование функции ICustomFunction
description: В этой статье описывается, как создать пользовательскую функцию в Excel Microsoft с помощью функции ICustomFunction в библиотеке Aspose.Cells. Загрузив существующий файл Excel или создав новый файл Excel, мы можем использовать методы, предоставленные Aspose.Cells, для определения и регистрации пользовательских функций и получения результатов. Наконец, мы сохраняем измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, ICustomFunction features, custom functions
type: docs
weight: 30
url: /ru/net/using-icustomfunction-feature/
---
{{% alert color="primary" %}} 

В этой статье представлено подробное описание того, как использовать функцию ICustomFunction для реализации пользовательских функций с помощью API Aspose.Cells.

Интерфейс ICustomFunction позволяет добавлять пользовательские функции расчета формул для расширения основного механизма вычислений Aspose.Cells' и удовлетворения определенных требований. Эта функция полезна для определения пользовательских (определяемых пользователем) функций в файле шаблона или в коде, где пользовательская функция может быть реализована и оценена с использованием API-интерфейсов Aspose.Cells, как и любая другая функция Excel по умолчанию Microsoft.

 Обратите внимание: этот интерфейс был заменен на[АннотацияРасчетДвигатель](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/) и будет удален в будущем. Некоторые технические статьи/примеры о новом API:[здесь](/cells/ru/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) и[здесь](/cells/ru/net/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} 
##  **Создание и оценка пользовательской функции**
 В этой статье демонстрируется реализация интерфейса ICustomFunction для написания пользовательской функции и использования ее в электронной таблице для получения результатов. Мы определим пользовательскую функцию по имени**МояФунк** который будет принимать 2 параметра со следующими деталями.

- Первый параметр относится к одной ячейке
- Второй параметр относится к диапазону ячеек

Пользовательская функция сложит все значения из диапазона ячеек, указанного в качестве второго параметра, и разделит результат на значение в первом параметре.

Вот как мы реализовали метод CalculateCustomFunction.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


Вот как использовать недавно определенную функцию в электронной таблице.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
##  **Обзор**
API Aspose.Cells просто помещают объект ReferredArea в «paramsList», когда соответствующий параметр является ссылкой или его вычисленный результат является ссылкой. Если вам нужна сама ссылка, вы можете использовать ReferredArea напрямую. Если вам нужно получить значение одной ячейки из ссылки, соответствующей позиции формулы, вы можете использовать метод ReferredArea.GetValue(rowOffset, int colOffset). Если вам нужен массив значений ячеек для всей области, вы можете использовать метод ReferredArea.GetValues.

Поскольку API Aspose.Cells предоставляют ReferredArea в «paramsList», ReferredAreaCollection в «contextObjects» больше не понадобится (в старых версиях он не мог всегда давать однозначное сопоставление параметрам пользовательской функции), поэтому он был удален из «contextObjects».

{{< highlight "java" >}}

 public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    object o = paramsList[i];

    if(o is ReferredArea) //fetch data from reference

    {

        ReferredArea ra = (ReferredArea)o;

        if(ra.IsArea)

        {

            o = ra.GetValues();

        }

        else

        {

            o = ra.GetValue(0, 0);

        }

    }

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}
