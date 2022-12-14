---
title: Проверьте, содержит ли рабочая книга скрытые внешние ссылки
type: docs
weight: 950
url: /ru/java/check-if-workbook-contains-hidden-external-links/
---
## **Возможные сценарии использования**
Иногда рабочая книга содержит внешние ссылки, которые скрыты и не могут быть просмотрены в Microsoft Excel. Aspose.Cells извлекает все внешние ссылки, видимые они или скрытые. Тем не менее, вы можете проверить[ExternalLink.IsVisible](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsVisible)свойство, чтобы проверить, видна ли внешняя ссылка или нет
## **Проверьте, содержит ли рабочая книга скрытые внешние ссылки**
 Следующий пример кода загружает[исходный файл excel](5472525.xlsx) который содержит скрытые внешние ссылки. Эти ссылки нельзя просмотреть в Microsoft Excel, но они присутствуют внутри рабочей книги. После печати[ВнешняяСсылка.DataSource](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#DataSource) а также[ExternalLink.IsReferred](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsReferred) свойство, он печатает[ExternalLink.IsVisible](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsVisible)имущество. В приведенном ниже выводе консоли вы видите, что все его внешние ссылки не видны.
## **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckWorkbookContainsHiddenExternalLinks-CheckWorkbookContainsHiddenExternalLinks.java" >}}
## **Консольный вывод**
 Вот вывод консоли приведенного выше примера кода при выполнении с заданным[образец эксель файла](5472525.xlsx).



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
