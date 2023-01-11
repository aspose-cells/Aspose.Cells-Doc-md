﻿---
title: تحويل ورقة العمل إلى CSV
type: docs
weight: 30
url: /ar/java/convert-worksheet-to-csv/
---
## **Aspose.Cells - تحويل ورقة العمل إلى CSV**
إذا احتاج المطورون إلى حفظ ملفاتهم في بعض مواقع التخزين ، فيمكنهم ببساطة تحديد اسم الملف (بمسار التخزين الكامل) وتنسيق الملف المطلوب (باستخدام**نوع الملف**تعداد) أثناء استدعاء**حفظ**طريقة**دفتر العمل**موضوع.

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook with Excel file path

Workbook workbook = new Workbook(dataPath + "workbook.xls");

//Save the document in PDF format

workbook.save(dataPath + "AsposeWorkbookCSV.csv", SaveFormat.CSV);

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - تحويل ورقة العمل إلى CSV**
يوضح الكود أدناه كيف يمكن تحويل ورقة العمل إلى CSV باستخدام Apache POI HSSF و XSSF API مقارنة بـ Aspose.Cells Java API.

**Java**

{{< highlight "java" >}}

 /**

\ * معالج بدائي XLSX -> CSV مصمم على طراز

\ * برنامج عينة POI XLS2CSVmra بواسطة Nick Burch من

\ * package org.apache.poi.hssf.eventusermodel.examples.

* على عكس إصدار HSSF ، يتجاهل هذا الإصدار تمامًا

\ * صفوف مفقودة.

\ * <p />

\ * تتم قراءة أوراق البيانات باستخدام محلل SAX للاحتفاظ بملحق

\ * مساحة الذاكرة صغيرة نسبيًا ، لذا يجب أن يكون هذا

\ * قادر على قراءة مصنفات هائلة. جدول الأنماط و

\ * يجب الاحتفاظ بجدول السلسلة المشتركة في الذاكرة. ال

\ * يتم استخدام فئة جدول أنماط POI القياسية ، ولكنها مخصصة

يتم استخدام فئة \ * (للقراءة فقط) لجدول السلسلة المشتركة

\ * لأن POI SharedStringsTable القياسي ينمو بشكل كبير

\ * بسرعة مع عدد السلاسل الفريدة.

\ * <p />

\ * شكرا لإريك سميث على التصحيح الذي يصلح مشكلة

\ * يتم تشغيلها بواسطة خلايا بها عناصر "t" متعددة ، وهي

\ * كيف يمثل Excel تنسيقات مختلفة (على سبيل المثال ، كلمة واحدة

\ * عادي وكلمة واحدة جريئة).

\*

\ * @ المؤلف كريس لوت

*/

فئة عامة ApacheXLSX2CSV {