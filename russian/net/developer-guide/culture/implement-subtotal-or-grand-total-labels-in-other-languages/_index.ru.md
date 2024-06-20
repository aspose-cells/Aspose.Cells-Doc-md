---
title: Реализация меток промежуточных и итоговых итогов на других языках
type: docs
weight: 50
url: /ru/net/implement-subtotal-or-grand-total-labels-in-other-languages/
---

## **Возможные сценарии использования**

Иногда вы хотите показать метки итоговых и итоговых итогов на не-английских языках, таких как китайский, японский, арабский, хинди и пр. Aspose.Cells позволяет сделать это с помощью класса [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) и свойства [**Workbook.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings). Пожалуйста, ознакомьтесь с этой статьей о том, как использовать класс [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings).

- [Использование класса GlobalizationSettings для пользовательских меток итогов и других меток круговой диаграммы](/cells/ru/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## **Реализация меток промежуточных и итоговых итогов на других языках**

Приведенный ниже образец кода загружает [образец файла Excel](5115151.xlsx) и реализует названия промежуточных и итоговых итогов на китайском языке. Пожалуйста, проверьте [выходной Excel-файл](5115152.xlsx), созданный этим кодом для справки. Сначала мы создаем класс [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings), а затем используем его в нашем коде.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-GlobalizationSettings.cs" >}}

Теперь используйте созданный выше класс в коде, как показано ниже:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-UsingGlobalizationSettings.cs" >}}
