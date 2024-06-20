---
title: Настройка страницы
type: docs
weight: 80
url: /ru/reportingservices/page-setup/
---

Конфигурация включает два раздела и 8 видов свойств настройки страницы. Эти свойства включают имя, индекс, FitToPagesTall, FitToPagesWide, TopMargin, FooterMargin, HeaderMargin, BottomMargin, LeftMargin и RightMargin.

- **name** представляет имя отчета, оно представляет весь отчет, когда имя пустое.
- **index** представляет индекс листа книги Excel, экспортированной в файл.
- **FitToPagesTall** представляет количество страниц по вертикали, на которые будет масштабирован лист при его печати.
- **FitToPagesWide** представляет количество страниц по горизонтали, на которые будет масштабирован лист при его печати.
- **FooterMargin** представляет расстояние от нижней части страницы до нижнего колонтитула, в сантиметрах.
- **HeaderMargin** представляет расстояние от верхней части страницы до верхнего колонтитула, в сантиметрах.
- **LeftMargin** представляет размер левого поля, в сантиметрах.
- **RightMargin** представляет размер правого поля, в сантиметрах.
- **TopMargin** представляет размер верхнего поля, в сантиметрах.
- **BottomMargin** представляет размер нижнего поля, в сантиметрах.

Пример настройки PageSetup:

{{code  lang="xml" }}
<PageSetup>
<Report name=”report name” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”>
<Sheet index=”0” FitToPagesTall=”1” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
<Sheet index=”1” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
</Report>
</PageSetup>

{{code}}
