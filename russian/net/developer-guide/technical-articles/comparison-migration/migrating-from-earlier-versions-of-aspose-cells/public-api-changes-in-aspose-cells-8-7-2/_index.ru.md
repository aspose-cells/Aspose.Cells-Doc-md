---
title: Общедоступный API Изменения в Aspose.Cells 8.7.2
type: docs
weight: 250
url: /ru/net/public-api-changes-in-aspose-cells-8-7-2/
---
{{% alert color="primary" %}} 

Этот документ описывает изменения в Aspose.Cells API с версии 8.7.1 до 8.7.2, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Расширен механизм расчета по умолчанию**
Aspose.Cells API-интерфейсы имеют мощный вычислительный механизм, который может вычислять почти все Microsoft функции Excel. Более того, API-интерфейсы Aspose.Cells теперь позволяют расширить механизм вычислений по умолчанию, чтобы он соответствовал требованиям к вычислениям для любого приложения.

Следующие API были добавлены с выпуском Aspose.Cells for .NET 8.7.2.

1. Класс AbstractCalculationEngine
1. Класс CalculationData
1. CalculationOptions.CustomEngine Свойство

{{% alert color="primary" %}} 

Вышеупомянутые API-интерфейсы позволяют реализовать настраиваемый механизм расчета для всех функций (включая собственные функции Excel) с большей гибкостью.

{{% /alert %}} {{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Внедрение пользовательского механизма расчета](/cells/ru/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

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


### **Добавлен перегруженный индексатор для TextBoxCollection**
Aspose.Cells for .NET 8.7.2 предоставил перегруженный индекс для класса TextBoxCollection, чтобы получить доступ к экземпляру TextBox, используя его имя в виде строки.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Доступ к TextBox через его имя](/cells/ru/net/access-the-text-box-by-the-name/)

{{% /alert %}} 

Простой сценарий использования выглядит следующим образом.

**C#**

{{< highlight "csharp" >}}

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


### **Добавлено событие OnAfterColumnFilter для GridWeb.**
Aspose.Cells.GridWeb for .NET 8.7.2 предоставляет событие OnAfterColumnFilter, которое служит обратным вызовом для механизма фильтрации, выполняемого через пользовательский интерфейс Aspose.Cells.GridWeb. Как следует из названия, событие запускается после применения фильтрации столбца и может использоваться для получения информации о фильтрации, такой как индекс столбца, к которому был применен фильтр, и выбранное значение фильтра.

Простой сценарий использования выглядит следующим образом.

**C#**

{{< highlight "csharp" >}}

 protected void GridWeb1_AfterColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Не забудьте зарегистрировать событие в элементе управления GridWeb.<acw:gridweb OnAfterColumnFilter="GridWeb1_AfterColumnFilter"/>

{{% /alert %}}
