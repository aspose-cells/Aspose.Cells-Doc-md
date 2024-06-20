---
title: Изменения в общедоступном API в Aspose.Cells 8.7.2
type: docs
weight: 260
url: /ru/java/public-api-changes-in-aspose-cells-8-7-2/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.7.1 до 8.7.2, которые могут быть интересны разработчикам модулей/приложений. Он включает не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но также описание любых изменений в поведении внутри Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Расширен стандартный расчетный механизм**
API Aspose.Cells имеет мощный расчетный механизм, который может вычислять практически все функции Microsoft Excel. Более того, API Aspose.Cells теперь позволяет расширять стандартный расчетный механизм для удовлетворения индивидуальных потребностей расчета любого приложения.

Следующие API были добавлены с выпуском Aspose.Cells for Java 8.7.2.

1. Класс AbstractCalculationEngine
1. Класс CalculationData
1. Свойство CalculationOptions.CustomEngine

{{% alert color="primary" %}} 

Упомянутые выше API позволяют реализовать пользовательский расчетный движок для всех функций (включая собственные функции Excel) с большей гибкостью.

{{% /alert %}} {{% alert color="primary" %}} 

Для получения дополнительной информации об этой функции, ознакомьтесь со статьей [Реализация Пользовательского Расчетного Движка](/cells/ru/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

Вот простой сценарий использования.

**Java**

{{< highlight csharp >}}

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
### **Добавлен перегруженный индексатор для коллекции TextBox**
Aspose.Cells for Java 8.7.2 добавил перегруженный индексатор для класса TextBoxCollection для доступа к экземпляру TextBox по его имени в виде строки.

{{% alert color="primary" %}} 

Для получения дополнительной информации об этой функции, ознакомьтесь со статьей [Доступ к TextBox по его имени](/cells/ru/java/access-the-text-box-by-the-name/)

{{% /alert %}} 

Простой сценарий использования выглядит следующим образом. 

**Java**

{{< highlight csharp >}}

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
