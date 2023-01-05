---
title: Внедрение меток промежуточных или общих итогов на других языках
type: docs
weight: 50
url: /ru/net/implement-subtotal-or-grand-total-labels-in-other-languages/
---
## **Возможные сценарии использования**

Иногда вам нужно отобразить метки промежуточных и общих итогов на языках, отличных от английского, таких как китайский, японский, арабский, хинди и т. д. Aspose.Cells позволяет вам сделать это с помощью[**Настройки глобализации**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)класс и[**Workbook.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) имущество. Пожалуйста, ознакомьтесь с этой статьей о том, как использовать[**Настройки глобализации**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)учебный класс

- [Использование класса GlobalizationSettings для пользовательских меток промежуточных итогов и других меток круговой диаграммы](/cells/ru/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## **Внедрение меток промежуточных или общих итогов на других языках**

 Следующий пример кода загружает[образец эксель файла](5115151.xlsx) и реализует промежуточные и общие названия на китайском языке. Пожалуйста, проверьте[выходной файл Excel](5115152.xlsx) сгенерированный этим кодом для справки. Сначала мы создаем класс[**Настройки глобализации**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)а затем использовать его в нашем коде.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-GlobalizationSettings.cs" >}}

Теперь используйте созданный выше класс в коде, как показано ниже:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-UsingGlobalizationSettings.cs" >}}
