---
title: دعم تخطيط علامات DIV أثناء تحميل ملف HTML في دفتر عمل إكسل
type: docs
weight: 50
url: /ar/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/
---

{{% alert color="primary" %}} 

عادةً، يتم تجاهل تخطيط وسم div أثناء تحميل HTML في كائن دفتر العمل في Excel. ومع ذلك، إذا كنت ترغب في عدم تجاهل تخطيط وسم div، يرجى ضبط خاصية [HTMLLoadOptions.SupportDivTag](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/supportdivtag) على **true**. القيمة الافتراضية لهذه الخاصية هي **false**.

{{% /alert %}} 

الكود النموذجي التالي يوضح استخدام خاصية [HTMLLoadOptions.SupportDivTag](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/supportdivtag). يرجى تنزيل [شعار Aspose](5115218.png) المستخدم داخل HTML المدخل والملف [مصنوع من الكود](5115220.xlsx) الذي أنشئه.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DivTagsLayout-1.cs" >}}
