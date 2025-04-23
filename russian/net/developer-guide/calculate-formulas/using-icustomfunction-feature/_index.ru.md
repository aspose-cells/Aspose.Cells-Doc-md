---
title: Использование функции ICustomFunction
description: Эта статья описывает, как создать пользовательскую функцию в Microsoft Excel с использованием функции ICustomFunction в библиотеке Aspose.Cells. Загрузив существующий файл Excel или создав новый файл Excel, мы можем использовать методы, предоставленные Aspose.Cells, для определения и регистрации пользовательских функций и получения результатов. Наконец, мы сохраняем измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, функцииICustomFunction, пользовательские функции, как вычислить пользовательские функции.
type: docs
weight: 30
url: /ru/net/how-to-calculate-custom-fuctions/
---

{{% alert color="primary" %}} 

Эта статья предоставляет подробное понимание того, как использовать функцию ICustomFunction для реализации пользовательских функций с помощью API Aspose.Cells.

Интерфейс ICustomFunction позволяет добавлять пользовательские функции расчета формул для расширения основного расчетного движка Aspose.Cells с целью удовлетворения определенных требований. Эта функция полезна для определения пользовательских функций в шаблонном файле или в коде, где пользовательская функция может быть реализована и оценена с использованием API Aspose.Cells, как любая другая функция Microsoft Excel по умолчанию.

Обратите внимание, что этот интерфейс был заменен на [AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/) и будет удален в будущем. Некоторые технические статьи/примеры о новом API: [здесь](/cells/ru/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) и [здесь](/cells/ru/net/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} 
## **Создание и оценка пользовательской функции**
Эта статья демонстрирует реализацию интерфейса ICustomFunction для написания пользовательской функции и использования ее в электронной таблице для получения результатов. Мы определим пользовательскую функцию с именем **MyFunc**, которая принимает 2 параметра со следующими деталями.

- 1-й параметр относится к одной ячейке
- 2-й параметр относится к диапазону ячеек

Пользовательская функция добавит все значения из указанного диапазона ячеек и разделит результат на значение в 1-м параметре.

Вот как мы реализовали метод CalculateCustomFunction.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


Вот как использовать вновь определенную функцию в электронной таблице



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
## **Обзор**
API Aspose.Cells просто помещают объект ReferredArea в "paramsList", когда соответствующий параметр является ссылкой или его рассчитанный результат является ссылкой. Если вам нужна сама ссылка, то вы можете использовать ReferredArea напрямую. Если вам нужно получить значение одной ячейки из соответствующей ссылки с позицией формулы, вы можете использовать метод ReferredArea.GetValue(rowOffset, int colOffset). Если вам нужен массив значений ячеек для всей области, то вы можете использовать метод ReferredArea.GetValues.

Поскольку API Aspose.Cells предоставляют ReferredArea в "paramsList", коллекция ReferredArea в "contextObjects" больше не понадобится (в старых версиях не всегда удавалось обеспечить однозначное соответствие параметрам пользовательской функции), поэтому она была удалена из "contextObjects".

{{< highlight java >}}

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
{{< app/cells/assistant language="csharp" >}}
