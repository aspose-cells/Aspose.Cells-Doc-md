---
title: Использование функции ICustomFunction
type: docs
weight: 890
url: /ru/java/using-icustomfunction-feature/
---
{{% alert color="primary" %}} 

В этой статье подробно рассказывается, как использовать функцию ICustomFunction для реализации пользовательских функций с помощью API Aspose.Cells.

Интерфейс ICustomFunction позволяет добавлять пользовательские функции расчета формулы для расширения основного механизма расчета Aspose.Cells для удовлетворения определенных требований. Эта функция полезна для определения пользовательских (определяемых пользователем) функций в файле шаблона или в коде, где пользовательскую функцию можно реализовать и оценить с помощью Aspose.Cells API, как и любую другую функцию Excel по умолчанию Microsoft.

 Обратите внимание, этот интерфейс был заменен на[АннотацияРасчетДвигатель](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) и будут удалены в будущем. Некоторые технические статьи/примеры по новому номеру API:[здесь](/cells/ru/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) а также[здесь](/cells/ru/java/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} {{% alert color="primary" %}} 

 Если вы новичок в API Aspose.Cells for Java, проверьте[это](https://docs.aspose.com/cells/java/installation/) статью, чтобы узнать, как вы можете получить и сослаться на Aspose.Cells for Java в своем проекте.

{{% /alert %}} 
## **Создание и оценка пользовательской функции**
В этой статье демонстрируется реализация интерфейса ICustomFunction для написания пользовательской функции и использования ее в электронной таблице для получения результатов. Мы определим пользовательскую функцию по имени**MyFunc** который будет принимать 2 параметра со следующими деталями.

- 1-й параметр относится к одной ячейке
- 2-й параметр относится к диапазону ячеек

Пользовательская функция добавит все значения из диапазона ячеек, указанного в качестве второго параметра, и разделит результат на значение в первом параметре.

Вот как мы реализовали метод calculateCustomFunction.

**Java**

{{< highlight "csharp" >}}

 public class CustomFunction implements ICustomFunction

{

    @Override

    public Object calculateCustomFunction(String functionName, java.util.ArrayList paramsList, java.util.ArrayList contextObjects)

    {

        double result = 0f;

        double sum = 0;

        //Get the value of 1st parameter

        Object firstParamB1 = paramsList.get(0);

        if (firstParamB1 instanceof ReferredArea)

        {

            ReferredArea ra = (ReferredArea)firstParamB1;

            firstParamB1 = ra.getValue(0, 0);

        }

        //Get values of 2nd parameter

        Object secondParamC1C5 = paramsList.get(1);

        if (secondParamC1C5 instanceof ReferredArea)

        {

            ReferredArea ra = (ReferredArea)secondParamC1C5;

            for (int i = ra.getStartRow(); i <= ra.getEndRow(); i++)

            {

                //Add all values

                sum += (double)ra.getValue(i, 0);

            }

        }

        result = sum / (double)firstParamB1;

        // Return result of the function

        return result;

    }

}

{{< /highlight >}}

Вот как использовать вновь определенную функцию в электронной таблице

**Java**

{{< highlight "csharp" >}}

 //Open the workbook

Workbook workbook = new Workbook();

//Obtaining the reference of the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Adding a sample value to "A1" cell

worksheet.getCells().get("B1").putValue(5);

//Adding a sample value to "A2" cell

worksheet.getCells().get("C1").putValue(100);

//Adding a sample value to "A3" cell

worksheet.getCells().get("C2").putValue(150);

//Adding a sample value to "B1" cell

worksheet.getCells().get("C3").putValue(60);

//Adding a sample value to "B2" cell

worksheet.getCells().get("C4").putValue(32);

//Adding a sample value to "B2" cell

worksheet.getCells().get("C5").putValue(62);

//Adding custom formula to Cell A1

worksheet.getCells().get("A1").setFormula("=MyFunc(B1,C1:C5)");

//Calcualating Formulas

workbook.calculateFormula(false, new CustomFunction());

//Assign resultant value to Cell A1

worksheet.getCells().get("A1").putValue(worksheet.getCells().get("A1").getValue());

//Save the file

workbook.save(dir + "UsingICustomFunction.xls");

{{< /highlight >}}
## **Обзор**
API Aspose.Cells просто помещают объект ReferredArea в «paramsList», когда соответствующий параметр является ссылкой или его вычисленный результат является ссылкой. Если вам нужна сама ссылка, вы можете напрямую использовать ReferredArea. Если вам нужно получить значение одной ячейки из ссылки, соответствующей положению формулы, вы можете использовать метод ReferredArea.getValue(rowOffset, int colOffset). Если вам нужен массив значений ячеек для всей области, вы можете использовать метод ReferredArea.getValues.

Поскольку API-интерфейсы Aspose.Cells предоставляют ReferredArea в «paramsList», ReferredAreaCollection в «contextObjects» больше не понадобится (в старых версиях он не мог всегда давать однозначное сопоставление с параметрами пользовательской функции), поэтому он был удален из "contextObjects".

{{< highlight "java" >}}

 public Object calculateCustomFunction(String functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    Object o = paramsList.get(i);

    if(o is ReferredArea) //fetch data from reference

    {

        ReferredArea ra = (ReferredArea)o;

        if(ra.isArea())

        {

            o = ra.getValues();

        }

        else

        {

            o = ra.getValue(0, 0);

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
