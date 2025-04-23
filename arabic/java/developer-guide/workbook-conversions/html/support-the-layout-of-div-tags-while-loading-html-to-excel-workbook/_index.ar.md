---
title: دعم تخطيط علامات DIV أثناء تحميل ملف HTML في دفتر عمل إكسل
type: docs
weight: 770
url: /ar/java/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/
---

{{% alert color="primary" %}} 

عادةً، يتم تجاهل تخطيط علامات div أثناء تحميل HTML إلى كائن دفتر العمل في Excel. ومع ذلك، إذا كنت ترغب في عدم تجاهل تخطيط علامات div، يرجى ضبط الخاصية [HtmlLoadOptions.SupportDivTag](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#SupportDivTag) على **true**. القيمة الافتراضية لهذه الخاصية هي **false**.

{{% /alert %}} 
## **دعم تخطيط علامات DIV أثناء تحميل HTML إلى دفتر عمل Excel**
الكود العيني التالي يوضح استخدام الخاصية [HtmlLoadOptions.SupportDivTag](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#SupportDivTag). يرجى تنزيل [شعار Aspose](5473442.png) المستخدم داخل ملف HTML الدخل و [ملف Excel الناتج](5473439.xlsx) الذي تم إنشاؤه بواسطة الكود.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-SupportthelayoutofDIVtags-1.java" >}}
{{< app/cells/assistant language="java" >}}
