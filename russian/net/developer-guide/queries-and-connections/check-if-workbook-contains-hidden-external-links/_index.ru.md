---
title: Проверьте, содержит ли рабочая книга скрытые внешние ссылки
type: docs
weight: 230
url: /ru/net/check-if-workbook-contains-hidden-external-links/
---
## **Возможные сценарии использования**
Иногда рабочая книга содержит внешние ссылки, которые скрыты и не могут быть просмотрены в Microsoft Excel. Aspose.Cells извлекает все внешние ссылки, видимые они или скрытые. Тем не менее, вы можете проверить[ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible)свойство, чтобы проверить, видна ли внешняя ссылка или нет
## **Проверьте, содержит ли рабочая книга скрытые внешние ссылки**
 Следующий пример кода загружает[исходный файл excel](5115413.xlsx) который содержит скрытые внешние ссылки. Эти ссылки нельзя просмотреть в Microsoft Excel, но они присутствуют внутри рабочей книги. После печати[ВнешняяСсылка.DataSource](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/datasource) а также[ExternalLink.IsReferred](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isreferred) свойство, он печатает[ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible)имущество. В приведенном ниже выводе консоли вы видите, что все его внешние ссылки не видны.
### **Образец кода**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckHiddenExternalLinks-CheckHiddenExternalLinks.cs" >}}
### **Консольный вывод**
 Вот вывод консоли приведенного выше примера кода при выполнении с заданным[образец эксель файла](5115413.xlsx).



{{< highlight "java" >}}

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
