---
title: DeviceInfo في ملف rsreportserver.config
type: docs
weight: 70
url: /ar/reportingservices/deviceinfo-in-rsreportserver-config-file/
---
 قسم DeviceInfo بتنسيق**rsreportserver.config** يأخذ المعلمات التالية التي تؤثر على سلوك Aspose.Cells ':

- **امتداد الملف** : عندما تكون القيمة**لا شيء**، ملحق ملف التقرير الذي تم تصديره هو القيمة الافتراضية. عندما لا تكون القيمة خالية ، يتم تعيين امتداد التقرير على القيمة.
- **SimplePageHeaders** : عندما تكون القيمة**حقيقي** ، يتم تقديم عنصر رأس التقرير كرأس صفحة Excel Microsoft. النظام الأساسي**خاطئة**.
- **SimplePageFooters** : متى**حقيقي** ، يتم تقديم عنصر تذييل التقرير كتذييل صفحة Excel Microsoft. النظام الأساسي**حقيقي**.
- **رأس البوت** : متى**حقيقي** (افتراضيًا) ، يتم تصدير عنصر رأس التقرير. متي**خاطئة**، لا يتم تصدير عنصر رأس التقرير. يدعم فقط ملحق Excel 2007 XLSX (بيانات فقط).
- **بوتوتفوتر** : متى**حقيقي** (افتراضيًا) ، يتم تصدير عنصر تذييل التقرير. متي**خاطئة**، ليس. يدعم فقط ملحق Excel 2007 XLSX (بيانات فقط).
- **FillTableGroupHeaderForSimpleOutPut**: **خاطئة** بشكل افتراضي. تدعم القيمة فقط ملحق Excel 2007 XLSX (بيانات فقط).
- **NoOutPutTotalForSimpleOutPut**: **خاطئة** بشكل افتراضي. تدعم القيمة فقط ملحق Excel 2007 XLSX (بيانات فقط).
- **NoOutPutGroupForSimpleOutPut**: **خاطئة** بشكل افتراضي. تدعم القيمة فقط ملحق Excel 2007 XLSX (بيانات فقط).
- **NoDoGroupPageForSimpleOutPut**: **حقيقي** بشكل افتراضي. تدعم القيمة فقط ملحق Excel 2007 XLSX (بيانات فقط).
- **NoDoPageForSimpleOutPut**: **حقيقي** بشكل افتراضي. تدعم القيمة فقط ملحق Excel 2007 XLSX (بيانات فقط).
- **محدد المجال**: تعيين محددات المجال. تدعم القيمة امتدادات CSV و TXT.
