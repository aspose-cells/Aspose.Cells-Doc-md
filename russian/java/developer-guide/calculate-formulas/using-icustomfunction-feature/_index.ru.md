---
title: Использование функции ICustomFunction
type: docs
weight: 890
url: /ru/java/using-icustomfunction-feature/
---

{{% alert color="primary" %}} 

Эта статья предоставляет подробное понимание того, как использовать функцию ICustomFunction для реализации пользовательских функций с помощью API Aspose.Cells.

Интерфейс ICustomFunction позволяет добавлять пользовательские функции расчета формул для расширения основного расчетного движка Aspose.Cells с целью удовлетворения определенных требований. Эта функция полезна для определения пользовательских функций в шаблонном файле или в коде, где пользовательская функция может быть реализована и оценена с использованием API Aspose.Cells, как любая другая функция Microsoft Excel по умолчанию.

Обратите внимание, что этот интерфейс был заменен [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) и будет удален в будущем. Некоторые технические статьи/примеры о новом API: [здесь](/cells/ru/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) и [здесь](/cells/ru/java/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} {{% alert color="primary" %}} 

Если вы новичок в Aspose.Cells for Java API, пожалуйста, проверьте [эту](https://docs.aspose.com/cells/java/installation/) статью, чтобы узнать, как вы можете получить и ссылаться на Aspose.Cells for Java в своем проекте.

{{% /alert %}} 
## **Создание и оценка пользовательской функции**
Эта статья демонстрирует реализацию интерфейса ICustomFunction для написания пользовательской функции и использования ее в электронной таблице для получения результатов. Мы определим пользовательскую функцию с именем **MyFunc**, которая принимает 2 параметра со следующими деталями.

- 1-й параметр относится к одной ячейке
- 2-й параметр относится к диапазону ячеек

Пользовательская функция добавит все значения из указанного диапазона ячеек и разделит результат на значение в 1-м параметре.

Вот как мы реализовали метод CalculateCustomFunction.

**Java**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

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
API Aspose.Cells просто помещает объект ReferredArea в «paramsList», когда соответствующий параметр является ссылкой или его вычисленный результат является ссылкой. Если вам нужна сама ссылка, то вы можете использовать ReferredArea напрямую. Если вам нужно получить значение одной ячейки из соответствующего с формулой положения, вы можете использовать метод ReferredArea.getValue(rowOffset, int colOffset). Если вам нужен массив значений ячеек для всей области, то вы можете использовать метод ReferredArea.getValues.

Поскольку API Aspose.Cells предоставляют ReferredArea в "paramsList", коллекция ReferredArea в "contextObjects" больше не понадобится (в старых версиях не всегда удавалось обеспечить однозначное соответствие параметрам пользовательской функции), поэтому она была удалена из "contextObjects".

{{< highlight java >}}

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
