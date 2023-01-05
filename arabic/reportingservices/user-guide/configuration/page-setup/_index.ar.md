---
title: اعداد الصفحة
type: docs
weight: 80
url: /ar/reportingservices/page-setup/
---
يتضمن التكوين قسمين و 8 أنواع من خصائص إعداد الصفحة. تتضمن هذه الخصائص الاسم والفهرس و FitToPagesTall و FitToPagesWide و TopMargin و FooterMargin و HeaderMargin و BottomMargin و LeftMargin و RightMargin.

- **اسم** يمثل اسم التقرير ، فهو يمثل التقرير بأكمله عندما يكون الاسم فارغًا.
- **فهرس** يمثل فهرس ورقة العمل لملف Excel الذي تم تصديره.
- **FitToPagesTall** يمثل عدد الصفحات الطويلة التي سيتم تغيير حجم ورقة العمل إليها عند طباعتها.
- **FitToPagesWide** يمثل عدد الصفحات التي سيتم تغيير حجم ورقة العمل إليها عند طباعتها.
- **التذييل** يمثل المسافة من أسفل الصفحة إلى تذييلها ، بوحدة السنتيمترات.
- **HeaderMargin** يمثل المسافة من أعلى الصفحة إلى رأس الصفحة ، بوحدة السنتيمترات.
- **الهامش الأيسر** يمثل حجم الهامش الأيسر بوحدة السنتيمترات.
- **الهامش الأيمن** يمثل حجم الهامش الأيمن بوحدة السنتيمترات.
- **الهامش العلوي** يمثل حجم الهامش العلوي بوحدة السنتيمترات.
- **الهامش السفلي**يمثل حجم الهامش السفلي بوحدة السنتيمترات.

مثال على تكوين إعداد الصفحة:

{{code  lang="xml" }}
<PageSetup>
<Report name=”report name” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”>
<Sheet index=”0” FitToPagesTall=”1” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
<Sheet index=”1” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
</Report>
</PageSetup>

{{code}}
