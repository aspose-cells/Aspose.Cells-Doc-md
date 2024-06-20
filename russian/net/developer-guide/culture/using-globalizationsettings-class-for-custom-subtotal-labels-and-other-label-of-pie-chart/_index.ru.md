---
title: Использование класса GlobalizationSettings для пользовательских подписей и других меток в круговой диаграмме
type: docs
weight: 70
url: /ru/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---

## **Возможные сценарии использования**

API Aspose.Cells предоставляет класс [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) для работы со сценариями, где пользователь хочет использовать пользовательские метки для итогов в электронной таблице. Кроме того, класс [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) также можно использовать для изменения метки **Другие** для круговой диаграммы при отображении листа или диаграммы.

## **Введение в класс GlobalizationSettings**

Класс [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) в настоящее время предлагает следующие 3 метода, которые могут быть переопределены в пользовательском классе для получения нужных меток для итогов или для вывода пользовательского текста для метки **Другие** круговой диаграммы.

1. [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname): Получает полное имя функции.
1. [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname): Получает полное имя итоговой функции.
1. [**GlobalizationSettings.GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername): Получает имя меток "Другие" для круговых диаграмм.

### **Пользовательские метки для итогов**

Класс [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) можно использовать для настройки меток итогов путем переопределения методов [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname) и [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname), как показано далее.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-GlobalizationSettings.cs" >}}

Чтобы добавить пользовательские метки, требуется назначить свойство [**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) экземпляру класса **CustomSettings**, определенного выше, перед добавлением итогов в сводную таблицу.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-UsingGlobalizationSettings.cs" >}}

{{% alert color="primary" %}}

Класс [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) работает только для добавления новых итогов. Если электронная таблица уже содержит итоги, их метки не могут быть изменены.

{{% /alert %}}

### **Пользовательский текст для метки "Другие" круговой диаграммы**

Класс [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) предлагает метод [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername), который полезен для задания пользовательского значения метки "Другие" для круговых диаграмм. В следующем фрагменте определяется пользовательский класс и переопределяется метод [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername), чтобы получить пользовательскую метку на основе идентификатора культуры системы.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-GlobalizationSettings.cs" >}}

В следующем фрагменте загружается существующая электронная таблица с круговой диаграммой и отображается диаграмма в виде изображения с использованием созданного выше класса **CustomSettings**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-UsingGlobalizationSettings.cs" >}}
