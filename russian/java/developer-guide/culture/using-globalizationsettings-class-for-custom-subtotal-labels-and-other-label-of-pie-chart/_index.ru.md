---
title: Использование класса GlobalizationSettings для пользовательских меток промежуточных итогов и других меток круговой диаграммы
type: docs
weight: 50
url: /ru/java/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---
## **Возможные сценарии использования**
 Aspose.Cells API-интерфейсы раскрыли[Настройки глобализации](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) класс, чтобы иметь дело со сценариями, когда пользователь хочет использовать настраиваемые метки для промежуточных итогов в электронной таблице. Более того,[Настройки глобализации](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) класс также может быть использован для изменения**Другой** метка для круговой диаграммы при отображении рабочего листа или диаграммы.
## **Введение в класс GlobalizationSettings**
[Настройки глобализации](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) класс в настоящее время предлагает следующие 3 метода, которые можно переопределить в пользовательском классе, чтобы получить желаемые метки для промежуточных итогов или отобразить пользовательский текст для**Другой** метка круговой диаграммы.

1. [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName\(int\)): получает полное имя функции.
1. [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName\(int\)): получает общее имя функции.
1. [GlobalizationSettings.getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)): получает имя метки «Другое» для круговых диаграмм.
### **Пользовательские метки для промежуточных итогов**
[Настройки глобализации](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)можно использовать для настройки меток промежуточных итогов путем переопределения[GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName\(int\)) & [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName\(int\)) методы, как показано выше.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


 Чтобы внедрить пользовательские метки, необходимо назначить[WorkbookSettings.GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) свойство экземпляра*Пользовательские настройки*класс, определенный выше, прежде чем добавлять промежуточные итоги на лист.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomLabelsforSubtotals-CustomLabelsforSubtotals.java" >}}

{{% alert color="primary" %}} 

[Настройки глобализации](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)класс работает только для добавления новых промежуточных итогов. Если электронная таблица уже содержит промежуточные итоги, их метки нельзя изменить.

{{% /alert %}} 
### **Пользовательский текст для других меток круговой диаграммы**
[Настройки глобализации](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) класс предлагает[getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\) ), который полезен для присвоения метке «Другое» круговых диаграмм пользовательского значения. Следующий фрагмент определяет пользовательский класс и переопределяет[getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)) для получения пользовательской метки на основе языка, установленного по умолчанию для JVM.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


 Следующий фрагмент загружает существующую электронную таблицу, содержащую круговую диаграмму, и визуализирует диаграмму в изображение, используя*Пользовательские настройки*класс, созданный выше.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomTextforOtherLabelofPieChart-CustomTextforOtherLabelofPieChart.java" >}}


Ниже приведено результирующее изображение, когда языковой стандарт машины установлен на Францию. Как вы можете видеть, метка «Другое» была переведена на «Autre», как определено в*Пользовательские настройки*учебный класс.

![дело:изображение_альтернативный_текст](using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart_1.png)
