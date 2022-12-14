---
title: Использование класса GlobalizationSettings для пользовательских меток промежуточных итогов и других меток круговой диаграммы
type: docs
weight: 70
url: /ru/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---
## **Возможные сценарии использования**

 Aspose.Cells API-интерфейсы раскрыли[**Настройки глобализации**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)класс, чтобы иметь дело со сценариями, когда пользователь хочет использовать настраиваемые метки для промежуточных итогов в электронной таблице. Более того,[**Настройки глобализации**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)класс также может быть использован для изменения**Другой** метка для круговой диаграммы при отображении рабочего листа или диаграммы.

## **Введение в класс GlobalizationSettings**

[**Настройки глобализации**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) класс в настоящее время предлагает следующие 3 метода, которые можно переопределить в пользовательском классе, чтобы получить желаемые метки для промежуточных итогов или отобразить пользовательский текст для**Другой** метка круговой диаграммы.

1. [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname): получает полное имя функции.
1. [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname): получает общее имя функции.
1. [**GlobalizationSettings.GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername): получает имя метки «Другое» для круговых диаграмм.

### **Пользовательские метки для промежуточных итогов**

[**Настройки глобализации**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) можно использовать для настройки меток промежуточных итогов путем переопределения[**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname) & [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname)методы, как показано выше.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-GlobalizationSettings.cs" >}}

 Чтобы внедрить пользовательские метки, необходимо назначить[**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) свойство экземпляра**Пользовательские настройки**класс, определенный выше, прежде чем добавлять промежуточные итоги на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-UsingGlobalizationSettings.cs" >}}

{{% alert color="primary" %}}

[**Настройки глобализации**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)класс работает только для добавления новых промежуточных итогов. Если электронная таблица уже содержит промежуточные итоги, их метки нельзя изменить.

{{% /alert %}}

### **Пользовательский текст для других меток круговой диаграммы**

[**Настройки глобализации**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) предложения класса[**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername)метод, который полезен для присвоения метке «Другое» круговых диаграмм пользовательского значения. Следующий фрагмент определяет пользовательский класс и переопределяет[**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername)метод для получения пользовательской метки на основе идентификатора культуры системы.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-GlobalizationSettings.cs" >}}

 Следующий фрагмент загружает существующую электронную таблицу, содержащую круговую диаграмму, и визуализирует диаграмму в изображение, используя**Пользовательские настройки**класс, созданный выше.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-UsingGlobalizationSettings.cs" >}}
