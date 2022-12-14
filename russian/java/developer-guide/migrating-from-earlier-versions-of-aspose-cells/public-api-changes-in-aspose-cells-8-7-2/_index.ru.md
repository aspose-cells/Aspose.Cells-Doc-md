---
title: Общедоступный API Изменения в Aspose.Cells 8.7.2
type: docs
weight: 260
url: /ru/java/public-api-changes-in-aspose-cells-8-7-2/
---
{{% alert color="primary" %}} 

Этот документ описывает изменения в Aspose.Cells API с версии 8.7.1 до 8.7.2, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Расширен механизм расчета по умолчанию**
Aspose.Cells API-интерфейсы имеют мощный вычислительный механизм, который может вычислять почти все Microsoft функции Excel. Более того, API-интерфейсы Aspose.Cells теперь позволяют расширить механизм вычислений по умолчанию, чтобы он соответствовал требованиям к вычислениям для любого приложения.

Следующие API были добавлены с выпуском Aspose.Cells for Java 8.7.2.

1. Класс AbstractCalculationEngine
1. Класс CalculationData
1. CalculationOptions.CustomEngine Свойство

{{% alert color="primary" %}} 

Вышеупомянутые API-интерфейсы позволяют реализовать настраиваемый механизм расчета для всех функций (включая собственные функции Excel) с большей гибкостью.

{{% /alert %}} {{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Внедрение пользовательского механизма расчета](/cells/ru/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

Ниже приведен простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

 public class CustomEngine extends AbstractCalculationEngine

{

	public void calculate(CalculationData data)

        {

		if(data.getFunctionName().toUpperCase().equals("SUM")==true)

                {

                    double val = (double)data.getCalculatedValue();

                    val = val + 30;

                    data.setCalculatedValue(val);

                }

        }

}

{{< /highlight >}}
### **Добавлен перегруженный индексатор для TextBoxCollection**
Aspose.Cells for Java 8.7.2 предоставил перегруженный индексатор для класса TextBoxCollection, чтобы получить доступ к экземпляру TextBox, используя его имя как String.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Доступ к TextBox через его имя](/cells/ru/java/access-the-text-box-by-the-name/)

{{% /alert %}} 

 Простой сценарий использования выглядит следующим образом.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook workbook = new Workbook();

//Access the first Worksheet from the collection

Worksheet sheet = workbook.getWorksheets().get(0);

//Add a TextBox to the collection

int idx = sheet.getTextBoxes().add(10, 10, 10, 10);

//Access the TextBox using its index

TextBox box = sheet.getTextBoxes().get(idx);

//Set the name for the TextBox

box.setName("MyTextBox");

//Access the same TextBox via its name

box = sheet.getTextBoxes().get("MyTextBox");

{{< /highlight >}}
