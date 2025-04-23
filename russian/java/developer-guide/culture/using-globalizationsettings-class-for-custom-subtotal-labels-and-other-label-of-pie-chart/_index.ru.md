---
title: Использование класса GlobalizationSettings для пользовательских подписей и других меток в круговой диаграмме
type: docs
weight: 50
url: /ru/java/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---

## **Возможные сценарии использования**
API Aspose.Cells предоставляет класс [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) для работы со сценариями, где пользователь хочет использовать настраиваемые метки для подытогов в электронной таблице. Более того, класс [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) можно использовать для изменения метки **Другой** для круговой диаграммы при рендеринге листа или диаграммы.
## **Введение в класс GlobalizationSettings**
Класс [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) в настоящее время предлагает следующие 3 метода, которые могут быть переопределены в пользовательском классе для получения желаемых меток для подытогов или для визуализации пользовательского текста для метки **Другие** на круговой диаграмме.

1. [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName-int-): Получает название общего итога функции.
1. [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName-int-): Получает название общего итогового значения функции.
1. [GlobalizationSettings.getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName--): Получает название ярлыка "Другие" для круговых диаграмм.
### **Пользовательские метки для итогов**
Класс [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) можно использовать для настройки меток подытогов, переопределяя методы [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName-int-) и [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName-int-), как показано ниже.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


Для вставки пользовательских меток необходимо назначить свойство [WorkbookSettings.GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) экземпляру класса *CustomSettings* до добавления подитогов в лист.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomLabelsforSubtotals-CustomLabelsforSubtotals.java" >}}

{{% alert color="primary" %}} 

Класс [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) работает только при добавлении новых подитогов. Если электронная таблица уже содержит подитоги, их метки не могут быть изменены.

{{% /alert %}} 
### **Пользовательский текст для метки "Другие" круговой диаграммы**
Класс [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) предлагает метод [getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName--) , который полезен для назначения пользовательского значения для ярлыка "Другие" круговых диаграмм. Следующий код определяет пользовательский класс и переопределяет метод [getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName--) для получения пользовательской метки в зависимости от настроенного языка системы JVM.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


Приведенный ниже фрагмент загружает существующую электронную таблицу, содержащую круговую диаграмму, и рендерит диаграмму в изображение с использованием созданного выше класса *CustomSettings*.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomTextforOtherLabelofPieChart-CustomTextforOtherLabelofPieChart.java" >}}


Ниже приведено полученное изображение в случае, когда локализация компьютера установлена на Францию. Как видите, метка "Другие" была переведена как "Autre", как определено в классе *CustomSettings*.

![todo:image_alt_text](using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart_1.png)
{{< app/cells/assistant language="java" >}}
