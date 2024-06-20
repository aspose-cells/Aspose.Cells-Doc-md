---
title: DeviceInfo в файле  rsreportserver.config 
type: docs
weight: 70
url: /ru/reportingservices/deviceinfo-in-rsreportserver-config-file/
---

Раздел DeviceInfo в **rsreportserver.config** содержит следующие параметры, влияющие на поведение Aspose.Cells:

- **FileExtension**: когда значение **null**, расширение экспортированного файла отчета устанавливается в значение по умолчанию. Когда значение не равно null, расширение отчета устанавливается в это значение.
- **SimplePageHeaders**: когда значение **true**, элемент заголовка отчета отображается как заголовок страницы Microsoft Excel. Значение по умолчанию - **false**.
- **SimplePageFooters**: когда **true**, элемент нижнего колонтитула отчета отображается как нижний колонтитул страницы Microsoft Excel. Значение по умолчанию - **true**.
- **PutoutHeader**: когда **true** (по умолчанию), элемент заголовка отчета экспортируется. Когда **false**, элемент заголовка отчета не экспортируется. Поддерживается только расширение Excel 2007 XLSX (только данные).
- **PutoutFooter**: когда **true** (по умолчанию), элемент нижнего колонтитула отчета экспортируется. Когда **false**, он не экспортируется. Поддерживается только расширение Excel 2007 XLSX (только данные).
- **FillTableGroupHeaderForSimpleOutPut**: **false** по умолчанию. Значение поддерживается только для расширения Excel 2007 XLSX (только данные).
- **NoOutPutTotalForSimpleOutPut**: **false** по умолчанию. Значение поддерживается только расширением Excel 2007 XLSX (только данные).
- **NoOutPutGroupForSimpleOutPut**: **false** по умолчанию. Значение поддерживается только расширением Excel 2007 XLSX (только данные).
- **NoDoGroupPageForSimpleOutPut**: **true** по умолчанию. Значение поддерживается только расширением Excel 2007 XLSX (только данные).
- **NoDoPageForSimpleOutPut**: **true** по умолчанию. Значение поддерживается только расширением Excel 2007 XLSX (только данные).
- **FieldDelimiter**: устанавливает разделители полей. Значение поддерживает расширения CSV и TXT.
