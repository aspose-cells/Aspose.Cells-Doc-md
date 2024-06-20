---
title: Изменения в общедоступном API в Aspose.Cells 8.7.2
type: docs
weight: 250
url: /ru/net/public-api-changes-in-aspose-cells-8-7-2/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.7.1 до 8.7.2, которые могут быть интересны разработчикам модулей/приложений. Он включает не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но также описание любых изменений в поведении внутри Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Расширен стандартный расчетный механизм**
API Aspose.Cells имеет мощный расчетный механизм, который может вычислять практически все функции Microsoft Excel. Более того, API Aspose.Cells теперь позволяет расширять стандартный расчетный механизм для удовлетворения индивидуальных потребностей расчета любого приложения.

Следующие API были добавлены с выпуском Aspose.Cells for .NET 8.7.2.

1. Класс AbstractCalculationEngine
1. Класс CalculationData
1. Свойство CalculationOptions.CustomEngine

{{% alert color="primary" %}} 

Упомянутые выше API позволяют реализовать пользовательский расчетный движок для всех функций (включая собственные функции Excel) с большей гибкостью.

{{% /alert %}} {{% alert color="primary" %}} 

Для получения дополнительной информации об этой функции ознакомьтесь со подробной статьей по [Реализация пользовательского расчетного механизма](/cells/ru/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

 public class MyEngine : AbstractCalculationEngine

{

    public override void Calculate(CalculationData data)

    {

        string funcName = data.FunctionName.ToUpper();

        if ("MYFUNC".Equals(funcName))

        {

            //do calculation for MYFUNC here

            int count = data.ParamCount;

            object res = null;

            for (int i = 0; i < count; i++)

            {

                object pv = data.GetParamValue(i);

                if (pv is ReferredArea)

                {

                    ReferredArea ra = (ReferredArea)pv;

                    pv = ra.GetValue(0, 0);

                }

                //process the parameter here

                //res = ...;

            }

            data.CalculatedValue = res;

        }

    }

}

{{< /highlight >}}


### **Добавлен перегруженный индексатор для коллекции TextBox**
Aspose.Cells for .NET 8.7.2 добавил перегруженный индекс для класса TextBoxCollection для доступа к экземпляру TextBox по его имени в виде строки.

{{% alert color="primary" %}} 

Для получения дополнительной информации об этой функции ознакомьтесь со подробной статьей по [Доступ к текстовому полю по его имени](/cells/ru/net/access-the-text-box-by-the-name/)

{{% /alert %}} 

Простой сценарий использования выглядит следующим образом.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook workbook = new Workbook();

//Access the first Worksheet from the collection

Worksheet sheet = workbook.Worksheets[0];

//Add a TextBox to the collection

int idx = sheet.TextBoxes.Add(10, 10, 10, 10);

//Access the TextBox using its index

TextBox box = sheet.TextBoxes[idx];

//Set the name for the TextBox

box.Name = "MyTextBox";

//Access the same TextBox via its name

box = sheet.TextBoxes["MyTextBox"];

{{< /highlight >}}


### **Добавлено событие OnAfterColumnFilter для GridWeb**
Aspose.Cells.GridWeb для .NET 8.7.2 добавил событие OnAfterColumnFilter, которое служит в качестве обратного вызова для механизма фильтрации, выполненной через пользовательский интерфейс Aspose.Cells.GridWeb. Как следует из названия, событие срабатывает после применения фильтрации столбца и может использоваться для получения информации о фильтрации, такой как индекс столбца, на котором был применен фильтр, и выбранное значение фильтра.

Простой сценарий использования выглядит следующим образом.

**C#**

{{< highlight csharp >}}

 protected void GridWeb1_AfterColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Do not forget to register the event to GridWeb control <acw:gridweb OnAfterColumnFilter="GridWeb1_AfterColumnFilter"/>

{{% /alert %}}
