---
title: تحميل ملف اكسل المصدر بدون الرسوم البيانية
type: docs
weight: 750
url: /ar/java/load-source-excel-file-without-charts/
---
{{% alert color="primary" %}} 

Aspose.Cells يسمح لك بتحميل ملف excel الخاص بك بدون رسوم بيانية. الرجاء استخدام خاصية LoadOptions.LoadFilter لهذا الغرض.

{{% /alert %}} 
## **تحميل ملف اكسل المصدر بدون الرسوم البيانية**
يقوم نموذج التعليمات البرمجية التالي بتحميل نموذج ملف Excel بدون مخططات وحفظه بتنسيق PDF الناتج.





{{< highlight "java" >}}

 //Specify the load options and filter the data

//We do not want to load charts

LoadOptions options = new LoadOptions();

options.setLoadFilter(new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.CHART));

//Load the workbook with specified load options

Workbook workbook = new Workbook("sample.xlsx", options);

//Save the workbook in output format

workbook.save("LoadExcelFileWithoutChart_out.pdf", SaveFormat.PDF);

{{< /highlight >}}






