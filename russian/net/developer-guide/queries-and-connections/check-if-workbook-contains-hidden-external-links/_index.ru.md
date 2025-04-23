---
title: Проверка, содержит ли рабочая книга скрытые внешние ссылки
type: docs
weight: 230
url: /ru/net/check-if-workbook-contains-hidden-external-links/
---

## **Возможные сценарии использования**
Иногда в рабочей книге могут содержаться скрытые внешние ссылки, которые нельзя просмотреть в Microsoft Excel. Aspose.Cells извлекает все внешние ссылки, независимо от того, видимы они или скрыты. Однако вы можете проверить свойство [ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible), чтобы проверить, видима ли внешняя ссылка или нет.
## **Проверка, содержит ли рабочая книга скрытые внешние ссылки**
Следующий образец кода загружает [исходный файл Excel](5115413.xlsx), который содержит скрытые внешние ссылки. Эти ссылки нельзя просмотреть в Microsoft Excel, но они присутствуют внутри рабочей книги. После печати [ExternalLink.DataSource](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/datasource) и [ExternalLink.IsReferred](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isreferred), он выводит свойство [ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible). На выводе консоли ниже вы видите, что все его внешние ссылки не видны.
### **Образец кода**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckHiddenExternalLinks-CheckHiddenExternalLinks.cs" >}}
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
{{< app/cells/assistant language="csharp" >}}
