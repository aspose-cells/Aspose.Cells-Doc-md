---
title: Настройка страницы
type: docs
weight: 80
url: /ru/reportingservices/page-setup/
---
Конфигурация включает в себя два раздела и 8 видов свойств страницы. Эти свойства включают имя, индекс, FitToPagesTall, FitToPagesWide, TopMargin, FooterMargin, HeaderMargin, BottomMargin, LeftMargin и RightMargin.

- **имя** представляет имя отчета, представляет весь отчет, если имя не указано.
- **индекс** представляет индекс рабочего листа экспортированного файла Excel.
- **FitToPagesTall** представляет количество страниц в высоту, до которых рабочий лист будет масштабирован при печати.
- **FitToPagesWide** представляет количество страниц в ширину, до которых рабочий лист будет масштабирован при печати.
- **Нижний колонтитул**представляет собой расстояние от нижней части страницы до нижнего колонтитула в сантиметрах.
- **ЗаголовокМаргин** представляет собой расстояние от верха страницы до заголовка в сантиметрах.
- **Левое поле** представляет размер левого поля в сантиметрах.
- **Правое поле** представляет размер правого поля в сантиметрах.
- **Верхнее поле** представляет размер верхнего поля в сантиметрах.
- **Нижнее поле** представляет размер нижнего поля в сантиметрах.

Пример конфигурации PageSetup:

{{code  lang="xml" }}
<PageSetup>
<Report name=”report name” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”>
<Sheet index=”0” FitToPagesTall=”1” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
<Sheet index=”1” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
</Report>
</PageSetup>

{{code}}
