---
title: Проверка, содержит ли рабочая книга скрытые внешние ссылки
type: docs
weight: 950
url: /ru/java/check-if-workbook-contains-hidden-external-links/
---

## **Возможные сценарии использования**
Иногда в рабочей книге содержатся внешние ссылки, которые скрыты и не могут быть просмотрены в Microsoft Excel. Aspose.Cells извлекает все внешние ссылки, независимо от того, видимы они или скрыты. Однако вы можете проверить свойство [ExternalLink.IsVisible](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsVisible) чтобы проверить, является ли внешняя ссылка видимой или нет
## **Проверка, содержит ли рабочая книга скрытые внешние ссылки**
Следующий образец кода загружает [исходный файл Excel](5472525.xlsx), который содержит скрытые внешние ссылки. Эти ссылки не могут быть просмотрены в Microsoft Excel, но они присутствуют внутри книги. После печати [ExternalLink.DataSource](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#DataSource) и свойства [ExternalLink.IsReferred](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsReferred) он печатает свойство [ExternalLink.IsVisible](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsVisible). В выводе консоли ниже вы видите, что все его внешние ссылки не видимы.
## **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckWorkbookContainsHiddenExternalLinks-CheckWorkbookContainsHiddenExternalLinks.java" >}}
## **Вывод в консоль**
Вот вывод консоли вышеуказанного образца кода при выполнении с заданным [образцом файла Excel](5472525.xlsx).



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
