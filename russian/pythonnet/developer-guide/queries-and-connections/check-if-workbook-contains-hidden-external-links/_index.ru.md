---
title: Проверка, содержит ли рабочая книга скрытые внешние ссылки
type: docs
weight: 230
url: /ru/python-net/check-if-workbook-contains-hidden-external-links/
---

## **Возможные сценарии использования**
Иногда рабочая книга содержит внешние ссылки, которые скрыты и не могут быть просмотрены в Microsoft Excel. Aspose.Cells for Python via .NET извлекает все внешние ссылки, независимо от того, видимы они или скрыты. Однако, вы можете проверить свойство [ExternalLink.is_visible](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_visible), чтобы узнать, видимы ли внешние ссылки или нет.

## **Проверка, содержит ли рабочая книга скрытые внешние ссылки**
Следующий пример кода загружает исходный Excel-файл [source excel file](5115413.xlsx), содержащий скрытые внешние ссылки. Эти ссылки нельзя просмотреть в Microsoft Excel, но они присутствуют внутри рабочей книги. После вывода свойств [ExternalLink.data_source](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/data_source) и [ExternalLink.is_referred](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_referred), выводится свойство [ExternalLink.is_visible](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_visible). В приведённом ниже выводе в консоли видно, что все внешние ссылки не видимы.

### **Образец кода**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-CheckHiddenExternalLinks.py" >}}

### **Вывод в консоль**
Вот вывод консоли вышеприведенного образца кода при выполнении с заданным [образцовым файлом Excel](5115413.xlsx).



{{< highlight java >}}

 Data Source: C:\International\DDB\FAS 133\Swap Rates\GS_1M_3M_1_2_5_¥$_(B)IRSwaps_0400.xls

Is Referred: True

Is Visible: False

Data Source: C:\DIST DAY\MAY TEMPLATES\030601t.xls

Is Referred: True

Is Visible: False

Data Source: C:\AREVIEW\2002 Controllable\Autobrct.xls

Is Referred: True

Is Visible: False

Data Source: C:\CARDSFO\Main Files\Rate Forecast\FY 11\IFR 11 01 (New Model REPORTS 11.08.07).xls

Is Referred: True

Is Visible: False

{{< /highlight >}}

