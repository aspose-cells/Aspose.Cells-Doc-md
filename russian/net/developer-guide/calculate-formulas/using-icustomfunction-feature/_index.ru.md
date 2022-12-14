---
title: Использование функции ICustomFunction
type: docs
weight: 30
url: /ru/net/using-icustomfunction-feature/
---
{{% alert color="primary" %}} 

В этой статье подробно рассказывается, как использовать функцию ICustomFunction для реализации пользовательских функций с помощью API Aspose.Cells.

Интерфейс ICustomFunction позволяет добавлять пользовательские функции расчета формулы для расширения основного механизма расчета Aspose.Cells для удовлетворения определенных требований. Эта функция полезна для определения пользовательских (определяемых пользователем) функций в файле шаблона или в коде, где пользовательскую функцию можно реализовать и оценить с помощью Aspose.Cells API, как и любую другую функцию Excel по умолчанию Microsoft.

{{% /alert %}} 
## **Создание и оценка пользовательской функции**
В этой статье демонстрируется реализация интерфейса ICustomFunction для написания пользовательской функции и использования ее в электронной таблице для получения результатов. Мы определим пользовательскую функцию по имени**MyFunc** который будет принимать 2 параметра со следующими деталями.

- 1-й параметр относится к одной ячейке
- 2-й параметр относится к диапазону ячеек

Пользовательская функция добавит все значения из диапазона ячеек, указанного в качестве второго параметра, и разделит результат на значение в первом параметре.

Вот как мы реализовали метод CalculateCustomFunction.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


Вот как использовать вновь определенную функцию в электронной таблице



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
## **Обзор**
API Aspose.Cells просто помещают объект ReferredArea в «paramsList», когда соответствующий параметр является ссылкой или его вычисленный результат является ссылкой. Если вам нужна сама ссылка, вы можете напрямую использовать ReferredArea. Если вам нужно получить значение одной ячейки из ссылки, соответствующей позиции формулы, вы можете использовать метод ReferredArea.GetValue(rowOffset, int colOffset). Если вам нужен массив значений ячеек для всей области, вы можете использовать метод ReferredArea.GetValues.

Поскольку API-интерфейсы Aspose.Cells предоставляют ReferredArea в «paramsList», ReferredAreaCollection в «contextObjects» больше не понадобится (в старых версиях он не мог всегда давать однозначное сопоставление с параметрами пользовательской функции), поэтому он был удален из "contextObjects".

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
