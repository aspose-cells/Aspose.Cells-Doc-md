---
title: تحميل ملف Excel المصدر بدون رسوم بيانية
type: docs
weight: 750
url: /ar/java/load-source-excel-file-without-charts/
---

{{% alert color="primary" %}} 

تتيح لك Aspose.Cells تحميل ملف Excel الخاص بك بدون رسوم بيانية. يرجى استخدام خاصية LoadOptions.LoadFilter لهذا الغرض.

{{% /alert %}} 
## **تحميل ملف Excel المصدر بدون رسوم بيانية**
تحمل عينة الشفرة التالية ملف Excel العينات دون الرسوم البيانية وتقوم بحفظه بتنسيق PDF الناتج.





{{< highlight java >}}

 //Specify the load options and filter the data

//We do not want to load charts

LoadOptions options = new LoadOptions();

options.setLoadFilter(new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.CHART));

//Load the workbook with specified load options

Workbook workbook = new Workbook("sample.xlsx", options);

//Save the workbook in output format

workbook.save("LoadExcelFileWithoutChart_out.pdf", SaveFormat.PDF);

{{< /highlight >}}






